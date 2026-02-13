# ELMo

ELMo (embeddings from language model) is a word embedding method for representing a sequence of words as a corresponding sequence of vectors. Its essence is a bidirectional LSTM which takes character-level as inputs and produces word-level embeddings.

According to its original paper (?), it requires training on a corpus of about 30 million sentences and a billion words.

Contributions: 

- An early example of pretraining-finetuning paradigm: after the ELMo model is pretrained, its parameters are frozen, except for the projection matrix which can be fine-tuned to minimize the loss on specific language.

- Contextualized word representation: 
    - The first forward LSTM of ELMo would process each input token in the context of all previous token
    - The first backward LSTM would process each token in the context of all subsequent tokens. 
    - The second forward LSTM would process each token in the context of all subsequent tokens, and then incorporate those to further contextualize each token.

e.g., for sentence 

```
She went to the bank to withdraw money.
```

- the first forward LSTM processes 'bank' in the context of 'She went to'.
- the first backward LSTM processes 'bank' in the context of 'to withdraw money'.
- the second forward LSTM processes 'bank' with the representation vector provided by the first backward LSTM. 


References

[Wikipedia ELMo](https://en.wikipedia.org/wiki/ELMo)
