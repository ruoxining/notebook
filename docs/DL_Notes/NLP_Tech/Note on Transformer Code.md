## Introduction
This note only focuses on the classes and eliminates all other packages or data processing lines.

To implement a Transformer model, the following classes need to be implemented.
- embeddings: positional encoding, token embedding, transformer embedding
- layers: layer norm, multi-head attention, position-wise feed forward, scale dot product attention
- blocks: encoder-layer, decoder-layer
- model: encoder, decoder, Transformer
## Utils
```Python
import torch
from torch import nn

```

## Positional embedding
```Python
class PositionalEncoding(nn.Module):
    """
    compute sinusoid encoding.
    """
    def __init__(self, d_model, max_len, device):
        """
        constructor of sinusoid encoding class

        :param d_model: dimension of model
        :param max_len: max sequence length
        :param device: hardware device setting
        """
        super(PositionalEncoding, self).__init__()

        # same size with input matrix (for adding with input matrix)
        self.encoding = torch.zeros(max_len, d_model, device=device)
        self.encoding.requires_grad = False  # we don't need to compute gradient

        pos = torch.arange(0, max_len, device=device)
        pos = pos.float().unsqueeze(dim=1)
        # 1D => 2D unsqueeze to represent word's position

        _2i = torch.arange(0, d_model, step=2, device=device).float()
        # 'i' means index of d_model (e.g. embedding size = 50, 'i' = [0,50])
        # "step=2" means 'i' multiplied with two (same with 2 * i)

        self.encoding[:, 0::2] = torch.sin(pos / (10000 ** (_2i / d_model)))
        self.encoding[:, 1::2] = torch.cos(pos / (10000 ** (_2i / d_model)))
        # compute positional encoding to consider positional information of words

    def forward(self, x):
        # self.encoding
        # [max_len = 512, d_model = 512]

        batch_size, seq_len = x.size()
        # [batch_size = 128, seq_len = 30]

        return self.encoding[:seq_len, :]
        # [seq_len = 30, d_model = 512]
        # it will add with tok_emb : [128, 30, 512]

```

## Token Embedding
```Python
class TokenEmbedding(nn.Embedding):
    """
    Token Embedding using torch.nn
    they will dense representation of word using weighted matrix
    """

    def __init__(self, vocab_size, d_model):
        """
        class for token embedding that included positional information

        :param vocab_size: size of vocabulary
        :param d_model: dimensions of model
        """
        super(TokenEmbedding, self).__init__(vocab_size, d_model, padding_idx=1)
```

## Transformer Embedding
Transformer adopts an embedding which is a summation of the token embedding and the positional embedding.
```Python
class TransformerEmbedding(nn.Module):
    """
    token embedding + positional encoding (sinusoid)
    positional encoding can give positional information to network
    """

    def __init__(self, vocab_size, d_model, max_len, drop_prob, device):
        """
        class for word embedding that included positional information

        :param vocab_size: size of vocabulary
        :param d_model: dimensions of model
        """
        super(TransformerEmbedding, self).__init__()
        self.tok_emb = TokenEmbedding(vocab_size, d_model)
        self.pos_emb = PositionalEncoding(d_model, max_len, device)
        self.drop_out = nn.Dropout(p=drop_prob)

    def forward(self, x):
        tok_emb = self.tok_emb(x)
        pos_emb = self.pos_emb(x)
        return self.drop_out(tok_emb + pos_emb)

```

## Scale dot product attention
```Python
class ScaleDotProductAttention(nn.Module):
    """
    compute scale dot product attention
    Query : given sentence that we focused on (decoder)
    Key : every sentence to check relationship with Qeury(encoder)
    Value : every sentence same with Key (encoder)
    """
    def __init__(self):
        super(ScaleDotProductAttention, self).__init__()
        self.softmax = nn.Softmax(dim=-1)

    def forward(self, q, k, v, mask=None, e=1e-12):
        # input is 4 dimension tensor
        # [batch_size, head, length, d_tensor]
        batch_size, head, length, d_tensor = k.size()

        # 1. dot product Query with Key^T to compute similarity
        k_t = k.transpose(2, 3)  # transpose
        score = (q @ k_t) / math.sqrt(d_tensor)  # scaled dot product
		
        # 2. apply masking (opt)
        if mask is not None:
            score = score.masked_fill(mask == 0, -10000)

        # 3. pass them softmax to make [0, 1] range
        score = self.softmax(score)

        # 4. multiply with Value
        v = score @ v
        return v, score

```


## Multi-head Attention
A multi-head attention is a self-attention running in parallel. 
The multi-head attention module output an attention output and an attention weight matrix with the scaled-dot product module.
```Python
class MultiHeadAttention(nn.Module):
	"""
	q, k, v: with dimension of d_model to d_model. Each is a weight matrix.
	"""
    def __init__(self, d_model, n_head):
        super(MultiHeadAttention, self).__init__()
        self.n_head = n_head
        self.attention = ScaleDotProductAttention()
        self.w_q = nn.Linear(d_model, d_model)
        self.w_k = nn.Linear(d_model, d_model)
        self.w_v = nn.Linear(d_model, d_model)
        self.w_concat = nn.Linear(d_model, d_model)
        
    def forward(self, q, k, v, mask=None):
		"""
		query = [batch size, query len, hid dim]
		key = [batch size, key len, hid dim]
		value = [batch size, value len, hid dim]
		"""
        # 1. dot product with weight matrices
        q, k, v = self.w_q(q), self.w_k(k), self.w_v(v)
        # 2. split tensor by number of heads
        q, k, v = self.split(q), self.split(k), self.split(v)
        # 3. do scale dot product to compute similarity
        out, attention = self.attention(q, k, v, mask=mask)
        # 4. concat and pass to linear layer
        out = self.concat(out)
        out = self.w_concat(out)
        return out

    def split(self, tensor):
        """
        split tensor by number of head
        :param tensor: [batch_size, length, d_model]
        :return: [batch_size, head, length, d_tensor]
        """
        batch_size, length, d_model = tensor.size()
        # head dimension = hidden dimension // number of heads
        d_tensor = d_model // self.n_head
        tensor = tensor.view(batch_size, length, self.n_head, d_tensor).transpose(1, 2)
        # it is similar with group convolution (split by number of heads)
        return tensor

    def concat(self, tensor):
        """
        inverse function of self.split(tensor : torch.Tensor)
        :param tensor: [batch_size, head, length, d_tensor]
        :return: [batch_size, length, d_model]
        """
        batch_size, head, length, d_tensor = tensor.size()
        d_model = head * d_tensor
        tensor = tensor.transpose(1, 2).contiguous().view(batch_size, length, d_model)
        return tensor
        
```

## Position-wise Feed Forward Layer
Another main block inside the encoder is the positionwise ffd. The input is transformed from hid_dim to pf_dim, where pf_dim is usually much larger than the hid_dim. The original transformer has a hid_dim of 512 while a pf_dim of 2048.
The purpose of this block is not explained in the Transformer paper.
```Python
class PositionwiseFeedForward(nn.Module):
    def __init__(self, d_model, hidden, drop_prob=0.1):
        super(PositionwiseFeedForward, self).__init__()
        self.linear1 = nn.Linear(d_model, hidden)
        self.linear2 = nn.Linear(hidden, d_model)
        self.relu = nn.ReLU()
        self.dropout = nn.Dropout(p=drop_prob)
    def forward(self, x):
        x = self.linear1(x)
        x = self.relu(x)
        x = self.dropout(x)
        x = self.linear2(x)
        return x
```

## Layer Norm
```Python
class LayerNorm(nn.Module):
    def __init__(self, d_model, eps=1e-12):
        super(LayerNorm, self).__init__()
        self.gamma = nn.Parameter(torch.ones(d_model))
        self.beta = nn.Parameter(torch.zeros(d_model))
        self.eps = eps

    def forward(self, x):
        mean = x.mean(-1, keepdim=True)
        var = x.var(-1, unbiased=False, keepdim=True)
        # '-1' means last dimension. 

        out = (x - mean) / torch.sqrt(var + self.eps)
        out = self.gamma * out + self.beta
        return out

```

## Encoder
First we build an encoder layer.
```Python
class EncoderLayer(nn.Module):

    def __init__(self, d_model, ffn_hidden, n_head, drop_prob):
        super(EncoderLayer, self).__init__()
        self.attention = MultiHeadAttention(d_model=d_model, n_head=n_head)
        self.norm1 = LayerNorm(d_model=d_model)
        self.dropout1 = nn.Dropout(p=drop_prob)

        self.ffn = PositionwiseFeedForward(d_model=d_model, hidden=ffn_hidden, drop_prob=drop_prob)
        self.norm2 = LayerNorm(d_model=d_model)
        self.dropout2 = nn.Dropout(p=drop_prob)

    def forward(self, x, src_mask):
        # 1. compute self attention
        _x = x
        x = self.attention(q=x, k=x, v=x, mask=src_mask)
        # 2. add and norm
        x = self.dropout1(x)
        x = self.norm1(x + _x)
        # 3. positionwise feed forward network
        _x = x
        x = self.ffn(x)
        # 4. add and norm
        x = self.dropout2(x)
        x = self.norm2(x + _x)
        return x

```
And then the whole encoder.
```Python
class Encoder(nn.Module):
	"""
	enc_voc_size: dictionary size
	max_len: max input length
	n_layers: defines #encoder_layers to stack in the encoder
	"""
	def __init__(self, enc_voc_size, max_len, d_model, ffn_hidden, n_head, n_layers, drop_prob, device):
	super().__init__()
	self.emb = TransformerEmbedding(d_model = d_model, max_len = max_len, 
						voacb_size = enc_voc_size, drop_prob = drop_prob, device = device)
	# a stacked encoder
	self.layers = nn.ModuleList([EncoderLayer(d_model = d_model, ffn_hidden = ffn_hidden, 
								n_head = n_head, drop_prob = drop_prob)
								for _ in range(n_layers)])
								
	def forward(self, x, src_mask):  # src_mask: during Transformer's training, a forward mask
		x = self.emb(x)
		for layer in self.layers:
			x = layer(x, src_mask)
		return x

```

## Decoder
First we build a decoder layer.
```Python
class DecoderLayer(nn.Module):
    def __init__(self, d_model, ffn_hidden, n_head, drop_prob):
        super(DecoderLayer, self).__init__()
        self.self_attention = MultiHeadAttention(d_model=d_model, n_head=n_head)
        self.norm1 = LayerNorm(d_model=d_model)
        self.dropout1 = nn.Dropout(p=drop_prob)

        self.enc_dec_attention = MultiHeadAttention(d_model=d_model, n_head=n_head)
        self.norm2 = LayerNorm(d_model=d_model)
        self.dropout2 = nn.Dropout(p=drop_prob)

        self.ffn = PositionwiseFeedForward(d_model=d_model, hidden=ffn_hidden, drop_prob=drop_prob)
        self.norm3 = LayerNorm(d_model=d_model)
        self.dropout3 = nn.Dropout(p=drop_prob)

    def forward(self, dec, enc, trg_mask, src_mask):
        # 1. compute self attention
        _x = dec   # ideal target
        x = self.self_attention(q=dec, k=dec, v=dec, mask=trg_mask)   # predicted target
        # 2. add and norm
        x = self.dropout1(x)
        x = self.norm1(x + _x)
        if enc is not None:
            # 3. compute encoder - decoder attention
            _x = x
            x = self.enc_dec_attention(q=x, k=enc, v=enc, mask=src_mask)
            # 4. add and norm
            x = self.dropout2(x)
            x = self.norm2(x + _x)
        # 5. positionwise feed forward network
        _x = x
        x = self.ffn(x)
        # 6. add and norm
        x = self.dropout3(x)
        x = self.norm3(x + _x)
        return x
```
And then the whole decoder.
```Python
class Decoder(nn.Module):
	def __init__(self, dec_voc_size, max_len, d_model, ffn_hidden, n_head, n_layers, drop_prob, device):
		super().__init__()
		self.emb = TransformerEmbedding(d_model = d_model, drop_prob = drop_prob, 
						max_len = max_len, vocab_size = dec_voc_size, device = devoce)
		# a stacked decoder layer
		self.layers = nn.ModuleList([DecoderLayer(d_model = d_model, ffn_hidden = ffn_hidden, 
									n_head = n_head, drop_prob = drop_prob)
									for _ in range(n_layers)])
		self.linear = nn.Linear(d_model, dec_voc_size)
	"""
	trg = [batch size, trg len]
	enc_src = [batchsize, src len, hid dim]
	trg_mask = [batch size, 1, trg len, trg len]
	src_mask = [batch size, 1, 1, src len] 
	"""
	def forward(self, trg, enc_src, trg_mask, src_mask):
		trg = self.emb(trg)
		for layer in self.layers:
			trg = layer(trg, enc_src, trg_mask, src_mask)
		# pass to LM head
		output = self.linear(trg)
		return output
```

## Transformer Model
The model use forward's src and trg to receive the input and output during both training and testing procedures. During training, the trgs are as references of calculating training loss, while during testing, the testing loss. In the DecoderLayer class, the ideal target and predicted target are compared.
```Python
class Transformer(nn.Module):
	"""
	src_pad_idx: A matrix indicating <pad> positions in the input. <pad>s are not paid attention
	trg_pad_idx: A matrix indicating <pad> positions in the output. <pad>s are not paid attention
	trg_sos_idx: A matrix indicating <sos> positions in the output. Sentence initial.
	enc_voc_size: input encoding size
	dec_voc_size: output encoding size
	d_model: Usually an emphirical value of \sqrt[4]{#classes}. Originally 512
	n_head: number of heads. Originally 8.
	max_len: limit on the input length
	ffn_hidden: number of hidden layers in the ffn
	n_layers: #layers in stacked encoder and decoder. Originally 6.
	drop_prob: drop out probability
	device: cpu or gpu
	"""
    def __init__(self, src_pad_idx, trg_pad_idx, trg_sos_idx, enc_voc_size, dec_voc_size, d_model, n_head, max_len, ffn_hidden, n_layers, drop_prob, device):
        super().__init__()
        self.src_pad_idx = src_pad_idx
        self.trg_pad_idx = trg_pad_idx
        self.trg_sos_idx = trg_sos_idx
        self.device = device
        self.encoder = Encoder(d_model=d_model,
                               n_head=n_head,
                               max_len=max_len,
                               ffn_hidden=ffn_hidden,
                               enc_voc_size=enc_voc_size,
                               drop_prob=drop_prob,
                               n_layers=n_layers,
                               device=device)
        self.decoder = Decoder(d_model=d_model,
                               n_head=n_head,
                               max_len=max_len,
                               ffn_hidden=ffn_hidden,
                               dec_voc_size=dec_voc_size,
                               drop_prob=drop_prob,
                               n_layers=n_layers,
                               device=device)

    def forward(self, src, trg):
        src_mask = self.make_src_mask(src)
        trg_mask = self.make_trg_mask(trg)
        enc_src = self.encoder(src, src_mask)
        output = self.decoder(trg, enc_src, trg_mask, src_mask)
        return output

    def make_src_mask(self, src):
        src_mask = (src != self.src_pad_idx).unsqueeze(1).unsqueeze(2)
        return src_mask

    def make_trg_mask(self, trg):
        trg_pad_mask = (trg != self.trg_pad_idx).unsqueeze(1).unsqueeze(3)
        trg_len = trg.shape[1]
        trg_sub_mask = torch.tril(torch.ones(trg_len, trg_len)).type(torch.ByteTensor).to(self.device)
        trg_mask = trg_pad_mask & trg_sub_mask
        return trg_mask

```

Let's finally see the default configs.
```Python
# GPU device setting
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

# model parameter setting
batch_size = 128
max_len = 256
d_model = 512
n_layers = 6
n_heads = 8
ffn_hidden = 2048
drop_prob = 0.1

# optimizer parameter setting
init_lr = 1e-5
factor = 0.9
adam_eps = 5e-9
patience = 10
warmup = 100
epoch = 1000
clip = 1.0
weight_decay = 5e-4
inf = float('inf')
```

## References
Vaswani et al. Attention is all you need. 2017
[hyunwoongko/transformer: PyTorch Implementation of "Attention Is All You Need" (github.com)](https://github.com/hyunwoongko/transformer/tree/master)
[6 - Attention is All You Need.ipynb - Colaboratory (google.com)](https://colab.research.google.com/github/bentrevett/pytorch-seq2seq/blob/master/6%20-%20Attention%20is%20All%20You%20Need.ipynb#scrollTo=JFKHiCa6Q5ZT)