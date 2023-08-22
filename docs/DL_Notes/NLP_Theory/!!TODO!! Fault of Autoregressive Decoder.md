This note collects papers that demonstrates the shortcomings of autoregressive decoders. Two main common concerns about the autoregressive decoders are that they are lacking the generalizability and the efficiency with respect to the amount of training data, due to the limitation of its structure.





## Limitation in generalizability
Information theory based: compositionality
climbing towards NLU: only learning the surface structure of language

In this paper, we 

#### Towards Revealing the Mystery behind Chain of Thought: A Theoretical Perspective (2023)
This paper points out the reason why the CoT success in prompting LLMs. 
增加模型的有效深度


#### Deep Encoder, Shallow Decoder: Reevaluating the Speed-Quality Tradeoff in Machine Translation
In section *Deep Encoder, Shallow Decoder*, this paper discusses the 

(Edunov et al., 2018; Pinnis et al., 2018; Ng et al., 2019).




## Limitation in error accumulation
GSM8k uses a verifier to correct the mistakes in reasoning paths, which is a worthy attempt. However, more efficient verification and correction in the early reasoning stage should also be explored.
GSM8k and scaling relationship also indicates the log linear-hood has not been reached by the autoregressive decoders.

