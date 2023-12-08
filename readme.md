# Readme
## 给大家看的
我的BLOG，主要语言是中文，主要内容有笔记 + 一些瞎话。在线部署在[MiniBabelLibrary](https://ruoxining.github.io/OBvault/)

如果想查找ZJU课程资料，可以配合仓库[ZJU_COURSE_MATERIALS](https://github.com/ruoxining/ZJU_COURSE_MATERIALS)食用

- 本BLOG的定位是掺杂自己观点的笔记 + 心得
- 上述仓库的定位是客观通用的一个工具箱

暂时这样分工

## 给我看的
之后的部署命令

```
mkdocs gh-deploy --clean
```

工程文件夹结构
- 我只需要操作 `mkdocs.yml` 和 `docs/`，别的不要动
- TODO: 每一个文件夹都去给我好好建一个 `index.md`

文件命名规则

- 不要被obsidian骗了，文件名不一定等于文件一级标题，文件名也不会显示在部署后的网页上，所以不准出现中文路径！！
- 文件路径不准出现多个单词，最多最多万不得已要用驼峰，文件夹名只能用单个单词大写；文件名用全小写蛇形命名，因为我看着舒服
- 图片名之后整理一下找不到的
- 其它TODO

书写规则:
- TODO

写给自己的mkdocs语法备忘录

- 正常文本如果想要换行记得要空一行🙁️
- md图片语法 `![标题](相对路径)` 必须要用相对路径！加.的那种！不要只放图片名字因为mkdocs找不到
- html图片语法 `<img src="相对路径" alt="标题" width="宽度" height="高度">`
- md链接语法 `[标题](链接)` 链接也要用部署后的链接，不要用文件名因为找不到
- html链接语法 `<a href="链接"> 标题 </a>`