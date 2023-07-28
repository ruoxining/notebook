
## install
(MacOS, conda, no GPU or CUDA)
```bash
conda install pytorch torchvision torchaudio -c pytorch
```

## 2022/01/12 cannot import name ‘Field’ from ‘torchtext’

新版torchtext把field类删了，’.legacy’也检测不到，用版本回退
```Terminal
pip --default-timeout=100 install torchtext==0.10.0
```

