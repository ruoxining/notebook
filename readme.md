# Readme
## Introduction 简介

Notebook on computer science, linguistics, deep learnin, opinions, and life. Making it bilingual (en/zh).

Link: [🔗 Mini-Babel Library](https://ruoxining.github.io/notebook/).

如需 ZJU 课程资料，可以配合仓库 [ZJUCourse](https://github.com/ruoxining/ZJUCourse)食用。本 BLOG 的定位是掺杂自己观点的笔记 + 心得，上述仓库的定位是客观通用的一个工具箱。暂时这样分工。

## Style Guide 撰写规则

## 工程文件夹结构

- 只需要操作 `mkdocs.yml` 和 `docs/`。
- 每一个文件夹都应该有一个 `index.md`。

## 文件命名规则

- No Chinese paths or folders.
- No uppercases.
- Use `-` between words instead of `_`.

## Titles

- Make each title and sub-title bilingual.
- Use congruent emojis along each section.
- Use emojis to indicate the degree of completeness for each sub-section and article.  
  - 🌕: For completed notes, worthy opening and reading.
  - 🌗: For incomplete notes, but still worthy opening and reading.
  - 🌑: For incomplete notes. Only open it when you have time or you dont want to lose any resources on that topic.

## MKdocs Materials Grammar Memo 语法备忘

[Reference Document](https://squidfunk.github.io/mkdocs-material/)

### 普通文本

- 同一行文字之间中英文混排，应当在交界处空格。
- 不同行文本之间需要空行，才能显示为换行。
  
### 外链

- 图片语法 `![标题](相对路径)` 必须要用加.的相对路径
- html图片语法 `<img src="相对路径" alt="标题" width="宽度" height="高度">`
- md链接语法 `[标题](链接){target="_blank"}` 链接也要用部署后的链接，不要用文件名因为找不到
- html链接语法 `<a href="链接"> 标题 </a>`

