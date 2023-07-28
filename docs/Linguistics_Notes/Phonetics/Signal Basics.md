
## 浊音与清音

当声带处于收紧状态，流经的气流使声带振动，这时产生的音是浊音（voiced sound）；当声带处于放松状态，不伴有声带振动的音，称为清音（unvoiced sound）。

## 激励源与滤波器

气流与声门是激励源，声道是滤波器。

## 共振峰

声门的质量决定基音频率，基频的高低也与性别和年龄相关。男性大约在60～200hz。女性和儿童大约在200～450hz。

人的发声器官（声道和口腔）肌肉较软，阻尼较大，会对较多的频率产生共鸣。把声道当作一个发音的谐振腔体来看，当发音的激励频率等于声道的谐振频率时，即两个频率相等，声道就会以最大的振幅来回震荡，也就是共鸣。共鸣引起了谐振腔振动，接着声道就放大了某些频率成分，并衰减其它频率成分，从而产生某些谐振频率，在频率特性上被放大的谐振频率就会陆续峰起，一般把这些共振频率称为共振频率，峰称为formant。

关于共振频率的大小，因为口腔和声道可以组合成各种形状和尺寸，所以声道有不同的共振频率。

关于共振频率的语义，由于浊音和元音是声带振动产生的，所以一般认为共振峰与浊音和元音密切相关。
![](Linguistics_Notes/asset/Untitled.png)


理想声道模型
![](Untitled%201.png)


下面图是主要元音和第一二共振峰的频率对应图。

![](Linguistics_Notes/asset/Untitled%202.png)

三个元音和共振峰的对应关系如下。一个音素可以用三个共振峰表示，每个共振峰的频谱特性都可以用一个GMM来建模拟合，也就是说三个GMM可以建模拟合一个音素，这也就是为什么HMM需要三个状态。而一般实际中我们用五个HMM状态，因为清音（非文本因素）比较复杂，需要五个共振峰才能较好表示。

事实中的问题没有这么简单，如果考虑变时，当形成一个词语时，每个音素总会与前后的音素关联，称为协同发音。由于协同发音的作用，前后两个共振峰可能会重叠或者靠近，或者相互作用，此时很难说三个共振峰表示一个独立的元音，这三个共振峰可能会带有别的前后音素频谱特性在其中。

![](Linguistics_Notes/asset/Untitled%203.png)

## 语谱图(spectrogram, spectral waterfall, voice-print)

语谱图有三个维度：x轴时间，y轴频率，z轴辐值。
![](Linguistics_Notes/asset/Untitled%204.png)

![](Linguistics_Notes/asset/Untitled%205.png)


# 元音和辅音的语/频谱图特征

元音的语谱图差异

- 开口度越大，f1越高
- 舌位越靠前，f2越高
- 不圆唇元音的f3比圆唇元音高

![Untitled](Linguistics_Notes/asset/Untitled%206.png)

f3最明显的体现是在辅音/r/中，f3明显低

辅音的语谱图差异
![](consonant_spectrogram.png)
区分voiced和voiceless

- voice周期波，voiceless非周期波
- voice二维频谱图上有基频和谐波结构，voiceless二维频谱上杂乱无章
- voice语谱图上面有代表声带振动的浊音杠，voiceless无浊音杠，有冲直条或乱纹

## Acoustic Aspects of Consonants

### English plosives: /p/ /b/ /t/ /d/ /k/ /g/

- /p//b/ are produced with the constriction at the lips
- /t//d/ are produced with the constriction of the blade of tongue
- /k//g/ are produced with the constriction of the back of the tongue

four acoustic properties of plosives

- duration of stop gap: silent period in the closure phase
- voicing bar: a dark bar that is shown at the low frequencies and its usually below 200Hz
- release burst: a strong vertical spike
- aspiration: a short frication noise before vowel formants begin and it is usually in 30ms
![](spectrogram1.png)
![](spectrogram2.png)


[第四章元辅音的声学知识辨析.ppt](https://max.book118.com/html/2017/0618/116388050.shtm)

[Music lab](https://musiclab.chromeexperiments.com/Spectrogram/)
[https://esp.mit.edu/download/a29f71f1fddf4f6470eb50726aa98de4/L7357_Phonetics_2hrs_Splash2013.pdf](https://esp.mit.edu/download/a29f71f1fddf4f6470eb50726aa98de4/L7357_Phonetics_2hrs_Splash2013.pdf)

[https://www.mq.edu.au/__data/assets/pdf_file/0009/911646/vowels.pdf](https://www.mq.edu.au/__data/assets/pdf_file/0009/911646/vowels.pdf)

[Acoustic structure of consonants](http://www.phon.ox.ac.uk/jcoleman/consonant_acoustics.htm)

[Human Voices and the Wah Pedal](http://www.geofex.com/Article_Folders/wahpedl/voicewah.htm)

[3.2. Acoustic Aspects of Consonants](https://corpus.eduhk.hk/english_pronunciation/index.php/3-2-acoustic-aspects-of-consonants/)

# 常用音频特征

[音频特征提取——常用音频特征 - LeeLIn。 - 博客园](https://www.cnblogs.com/xingshansi/p/6815217.html)

[开源项目audioFlux: 针对音频领域的深度学习工具库 - audioFluxLab - 博客园](https://www.cnblogs.com/audioflux/p/17302316.html)
