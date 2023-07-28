
# Introduction

We will introduce the reductions of “wanna”, “gonna”, “gotta”, explain their reasons and provide a  in several AmE dialects. Our inspiration for choosing this topic is from our watching television programs. Thus we will first show several pieces of video clips to get you familiar about our topic.

An interesting fact of this phenomenon: It is focused in bias analysis in hate speech detection task. A reduced form is 20%~30% more likely to be classified as hate speech as it is considered more related to African American English. [9]

# Video Clip Examples⭐

# Theory

In the following section, we will give a theoretical analysis of the phenomenon we found.

### Relevant Studies

[1]**Patterns of Function Words Reduction**

- The reduction of function words is showed as following changes:
    - Vowel quality
    - Coda consonant deletion
    - Word speech rate
- In the context of a higher rate of speech, the function word is significantly more likely to reduce.
- Significantly less reduction is found when the following word begins with a vowel than when it begins with a consonant.
- High-frequency words are likely to have weakened pronunciation.
- Collocational effects also contribute to the distribution of function word reduction.

[2]**Wanna Contraction and prosodic boundary**⭐

- Abstract
    - Wanna-contraction is a phonological process that involves the shortening or weakening of the words "want to" to "wanna", "going to" to "gonna".
    - by nature: phonological weakening or shortening of the function word “to”
    - sensitive to: lengthening of the syllables at the prosodic boundary
    - no more reducing arises when the function word is stressed or lengthened. Lengthening blocks the contraction
- Method: Case study
    - sentense-final postion: strong form.
        
        ```
        a. I want to (wanna) dance//with somebody.5 
        b. I don‘t want to (*wanna)//.
        ```
        
    - “wanna” contraction to be one way of disambiguating the sentence
    - no “wanna” contraction takes place with the lengthening of the final word
    - 这篇里下面的结论大致讲的是在wanna/gonna/gotta+verb做谓语的情况下会reduction，加名词或作为其它句子成分的时候不会。我需要再去细分一下

[3]**Multiple Spell-Out and Contraction at the Syntax-Phonology Interface**

- Abstract
    - “wanna” contraction is possible in the subject-control case (Who do you wanna marry?) but blocked in the DP+infinitival case (Who do you wanna marry you?)

[4]**Frequency and Category Factors in the Reduction and Assimilation of Function Words: EPG and Acoustic Measures**

- Abstract
    - to confirm whether syntactically defined function words are indeed phonologically and phonetically reduced or assimilated.

[5]**Reduction of English Function Words in Switchboard**

- Abstract
    - Corpus analysis: 10 frequent English function words, 8458 occurrence, 4-hour example from Switchboard corpus
    - Method: linear and logistic regression models
    - Features: word length, form of vowel (basic, full, reduced), final obstruent deletion.
    - Effect factors: speaking rate, predictability, the form of the following word, planning problem disfluencies
- Rate of speech
    - affects all measures of reduction
    - compare: fast rate of 7.5 syllables/sec and slow rate of 2.5 syllables/sec, the estimated increase in the odds(=#full/#reduced, 一个文本里自己定义的公式) of full vowel is 2.2 times
    - Most strongly affected words: a, the, to, and, I.
- Planning problems, disfluency
    - 这段的意思应该是说话人想不起来了停顿的时候（例如说the that），停顿之前的说的那个词不会reduce
    - “Fox Tree and Clark suggested that such planning problems are likely to cause words in immediately preceding speech to have less reduced pronunciations.”
- Following consonant/vowel
    - more reduced forms before a consonant than before a vowel.
    - “to” is greatly affected
- Predictability and frequency
    - higher-frequency words are more likely to have weakened pronunciations in the previous several words.
    - Jespersen: might be misleading
- Collocations

[6]**From Reduction to Emancipation: Is “gonna” A Word?**⭐

P.133

[Corpus Perspectives on Patterns of Lexis](https://books.google.co.jp/books?hl=zh-CN&lr=&id=S0PPD0OnChUC&oi=fnd&pg=PA133&dq=gonna+wanna+reduction+in+dialects&ots=5OeV1rJL9B&sig=Nw_T2eeQ9xqsv8tVNFNOptRf3f4&redir_esc=y#v=onepage&q&f=false)

[7]**Communicative efficiency and the Principle of No Synonymy: predictability effects and the variation of want to and wanna**

Variables:

- structural variables: expression, infinitive, neg_part, question, subject
- socialinguistic variables: speaker, sex, ageGroup
- variables related to style, register, text type: textType, settingID, speechRate, formal-informal, informative-aesthetic
- predictability: (=[5]里的planning problem)

[8]**Some Informal Contractions in American English**

写得不是很好

[9]**Exploring the Role of Grammar and Word Choice in Bias Toward African American English (AAE) in Hate Speech Classification, Diyi Yang**

- Abstract
    - AAE is more likely to be misclassified as hate speech.

### Our Conclusion⭐

- involves syntax-phonology interface
- 

# Corpus Analysis

In this section, a corpus analysis is carried out to confirm the theories in the literature.

怎么听：用第三个international dialect这个库。里面可以选择African, North American, South American，其中每一个又有地域之分。里面都有transcription，直接搜索有没有这三个词组，有就定位听一下。

可能不能找齐所有变量，我自己听的时候觉得是很少的，能找到多少算多少好了。

### Relevant Corpus Resources

- Common Voice
    
    [Iterating Dataset Access on Common Voice](https://foundation.mozilla.org/en/blog/iterating-dataset-access-on-common-voice/)
    
- People’s Speech⭐
    
    [MLCommons/peoples_speech · Datasets at Hugging Face](https://huggingface.co/datasets/MLCommons/peoples_speech)
    
- International Dialects⭐
    
    [Accents and Dialects of England | IDEA: International Dialects of English Archive](https://www.dialectsarchive.com/england)
    
- (a dataset in Kaggle)
- openSLR
    
    [openslr.org](http://openslr.org/resources.php)
    
- Stanford CS22S
    
    [CS224S: Spoken Language Processing](https://web.stanford.edu/class/cs224s/)
    

### Corpus Analysis

每个记录一个比值：#reduction/#听了的句子。每个变量10～15条即可，这3个短语出现一次算一条，不是一人算一条

- General Pattern⭐
    
    去听五种情况
    
    - 在verb前，一起做谓语（期望reduction多）
    - 在noun前（期望fully pronounced多）
    - 在句尾（期望fully pronounced多）
    - 句子里有两个wanna/gonna+verb，其中一个的verb为避免重复被省略了（期望fully pronounced多）
    - want/got/go因为语义，被强调了（期望fully pronounced多）
- Dialect⭐
    - 分成美国西、南、中、北去听，期望#reduction in 西、北>中、南
    - 重点听：以加州为例的、以波士顿为例的、以德州为例的
- Race⭐
    
    African的在库里比较少
    
    - African American English
    - Whiter
- Gender
    
    分成男女去听，期望#reduction in 男>女