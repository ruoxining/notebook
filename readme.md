# Readme
## 简介

我的BLOG，主要语言是中文，主要内容有笔记 + 一些瞎话。在线部署在[MiniBabelLibrary](https://ruoxining.github.io/OBvault/)。

如果想查找ZJU课程资料，可以配合仓库[ZJU_COURSE_MATERIALS](https://github.com/ruoxining/ZJU_COURSE_MATERIALS)食用。本BLOG的定位是掺杂自己观点的笔记 + 心得，上述仓库的定位是客观通用的一个工具箱。暂时这样分工。


## 撰写规则

部署命令

```
conda activate MKdocs
mkdocs gh-deploy --clean
```

工程文件夹结构

- 只需要操作 `mkdocs.yml` 和 `docs/`。
- 每一个文件夹都应该有一个 `index.md`。

文件命名规则

- 不允许出现中文路径
- 文件路径不准出现多个单词，最多用驼峰，文件夹名只能用单个单词大写；文件名用全小写蛇形命名。

### MKdocs Materials 语法备忘

[Reference Document](https://squidfunk.github.io/mkdocs-material/)

普通文本

- 同一行文字之间中英文混排，应当在交界处空格。
- 不同行文本之间需要空行，才能显示为换行。
  
外链

- 图片语法 `![标题](相对路径)` 必须要用加.的相对路径
- html图片语法 `<img src="相对路径" alt="标题" width="宽度" height="高度">`
- md链接语法 `[标题](链接)` 链接也要用部署后的链接，不要用文件名因为找不到
- html链接语法 `<a href="链接"> 标题 </a>`

