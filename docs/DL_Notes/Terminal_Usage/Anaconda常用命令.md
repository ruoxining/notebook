
## 创建环境
```bash
conda create --name [ENV_NAME] python==3.9
```

## 删除环境
```bash
 conda remove -n [ENV_NAME] --all
```

## 查看现存虚拟环境
```bash
conda env list
```

## 查看目前环境已安装包
```bash
conda list
```

## 打开环境
```bash
 conda activate [ENV_NAME]
```

## 关闭环境
```bash
conda deactivate
```

## 删除环境中的某个包
```bash
conda remove --name [ENV_NAME] [PACK_NAME]
```

1. Update specific package:
```
conda update [PACK_NAME]
```

2. Update all packages in the current environment:
```
conda update --all
```

3. Update all packages in the current environment:
```
conda update -n myenv --all
```

4. Update Python:
```
conda update python
```

5. Update conda itself:
```
conda update conda
```