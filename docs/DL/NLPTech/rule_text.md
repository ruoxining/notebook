# 规则提取文本格式总结

## 任务1
需要在四本格式不一样的词典中提取出相同格式的词源信息，词源一共有9大类+一种"Other"，文本中有数个词源信息，需要找到最初的那个词源信息，归到9大类中并记录下来具体是哪一类。
需要的格式
```Json
[{
	"word": "",
	"etymology": [
		{
			"origin": "",
			"source": "",
			"excerpt": ""
		},
        {
			"origin": "",
			"source": "",
			"excerpt": ""
		}
    ]
}]
```

### 方法
1. 纯规则
	是指人工看出词源的分类规则，需要找到数据集里都有哪些格式，写个跟自己组别的格式对应
2. 用ChatGPT
	写prompt，让ChatGPT返回分类
	我的prompt写法 介绍+类别+示范
	```Plain
	"An ultimate origin of a word is the language where a word comes from at the very beginning, or the language where it appears at the earliest time. For the given word %s, please find its ultimate origin of this word from the following passage: %s. You should only answer one word from Anglo, Arabic, Asian, Celtic, English, French, Germanic, Greek, Latin, Spanish, or Other, without outputing anything else. If the origin not provided, just output Other. Origin: %s" % ("a", "prefix meaning \"not,\" from Latin. a-, short for ab \"away from\" (cf. avert), or its cognate, Greek. a-, short for apo \"away from, from,\" both cognate with Skt. apa \"away from,\" Goth. af, Old.English. of. ", "Latin")
	```
	这里可以看到，为了防止ChatGPT将English理解成Other而非Anglo，特意将English添加在了备选项中，之后再对返回的English类别做一个规则处理。
3. 用阅读理解模型
	因为ChatGPT比较贵，尝试用一些预训练的阅读理解模型来做。
	一开始找到的是RoBERTa，具体是huggingface上的RoBERTa-based-QA，但是发现该预训练模型对人类指令的支持很不好，比如prompt中写明了”如果提供的信息中不含任何词源，请返回Other“，但是模型仍然不会按格式返回，而是会输出一大段文字以解释为什么提供的信息中的词源不属于任何一类。说明这些模型few-shot能力还是并不好，也没有根据人类指令微调过。


## 任务2
需要将一个文本库中的文本分词后词形还原
1. nltk
	优点：调用简单，快
	缺点：预训练模型下载不稳定，往往需要手动下载后放在本地的nltk文件夹中，准确率低一些
2. spaCy
	优点：准确率更高
	缺点：调用慢，预训练模型下载不稳定
3. stanza
	优点：准确率更高
	缺点：预训练模型下载不稳定

三个包的推荐程度排序
stanza = spaCy > nltk