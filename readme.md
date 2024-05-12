# Readme
## 给大家看的

我的BLOG，主要语言是中文，主要内容有笔记 + 一些瞎话。在线部署在[MiniBabelLibrary](https://ruoxining.github.io/OBvault/)。

如果想查找ZJU课程资料，可以配合仓库[ZJU_COURSE_MATERIALS](https://github.com/ruoxining/ZJU_COURSE_MATERIALS)食用。本BLOG的定位是掺杂自己观点的笔记 + 心得，上述仓库的定位是客观通用的一个工具箱。暂时这样分工。


## 给我看的

部署命令

```
mkdocs gh-deploy --clean
```

工程文件夹结构

- 我只需要操作 `mkdocs.yml` 和 `docs/`，别的不要动。
- 每一个文件夹都应该有一个 `index.md`。

文件命名规则

- 不准出现中文路径！
- 文件路径不准出现多个单词，最多最多万不得已要用驼峰，文件夹名只能用单个单词大写；文件名用全小写蛇形命名。

mkdocs 语法备忘录

- 正常文本如果想要换行记得要空一行🙁️
- md图片语法 `![标题](相对路径)` 必须要用相对路径！加.的那种！不要只放图片名字因为mkdocs找不到
- html图片语法 `<img src="相对路径" alt="标题" width="宽度" height="高度">`
- md链接语法 `[标题](链接)` 链接也要用部署后的链接，不要用文件名因为找不到
- html链接语法 `<a href="链接"> 标题 </a>`

TODO list

- 你好 我服了 评论不会配
  snippet 生成出来是这样的

    ```html
    <script src="https://giscus.app/client.js"
            data-repo="ruoxining/OBvault"
            data-repo-id="R_kgDOKAxP-Q"
            data-category="Announcements"
            data-category-id="DIC_kwDOKAxP-c4Cd9bq"
            data-mapping="pathname"
            data-strict="0"
            data-reactions-enabled="1"
            data-emit-metadata="0"
            data-input-position="bottom"
            data-theme="light"
            data-lang="zh-CN"
            data-loading="lazy"
            crossorigin="anonymous"
            async>
    </script>
    ```
    后续参照[这个帖子](https://squidfunk.github.io/mkdocs-material/setup/adding-a-comment-system/)

- 实现一下网站访问统计：[MkDocs实现网站访问统计(不蒜子)及添加评论系统模块(livere来必应)实现](https://blog.csdn.net/arnolan/article/details/105026738)

- 实现一下渲染 mermaid：[HTML - 在网页上显示mermaid流程图（使用纯js在网页上显示mermaid流程图）](https://blog.csdn.net/Tisfy/article/details/131464925)