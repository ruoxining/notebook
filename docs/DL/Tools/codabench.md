# Codabench 配置教程

## 简介

[Codabench](https://www.codabench.org/) 是一个为数据科学和机器学习比赛设计的低代码模型测试平台。平台提供 CPU，允许比赛创办者通过上传脚本和数据的方式创办比赛，并允许其它用户使用平台 CPU 来运行代码得到结果。前序工作是 [CodaLab](https://codalab.org/)，2023 年 Codabench 团队仿照 CodaLab 改进出了 Codabench。

## 运作

比赛创办者通过上传比赛配置后，每当有用户加入并提交一个运行请求，平台将在 CPU 上为每个提交创建一个 Docker，包含比赛创办者提供的比赛配置和该用户提交的数据，在 Docker 中运行指定路径的代码，并将结果显示在平台展示的 terminal 上。

## 配置

在 Codabench 官网注册登陆后，点击右上角 Benchmark -> Management，可以选择 Create 或 Upload 来创建比赛。

- Create 是使用平台 UI 创建比赛
- Upload 是在本地写好配置文件，直接上传后被解析为一个比赛

更推荐用 Upload 来创建，因为 UI 的用户提示比较欠缺。

### 上传创建

bundle 指比赛创建者上传的压缩文件。里面含有：

- competition.yaml 是比赛的 metadata
- scoring program 是平台所运行的评测脚本
- reference data 是评测脚本所读的 gold answer 数据

需要期待用户上传：

- result data 用户上传的答案数据
- ingestion program 是指用户提交的代码，如果希望用户将方法/模型上传，需要在 scoring program 中留出给 ingestion program 的接口


分别介绍：

1. competition.yaml 不能改名，且必须位于 .zip 中最顶层的文件夹（即多选 competition.yaml 和其它文件夹后创建 .zip，而非把含有 competition.yaml 和其它文件夹的上层文件夹创建为 .zip）。支持的字段有：

```yaml
title: # 比赛名
version: # 1 指是 CodaLab bundle，2 指 CodaBench bundle，区别是有些 competition.yaml 字段不兼容
description: # 比赛描述
image: # 比赛 logo.png
registration_auto_approve: True  # do not require approval from organizers to join
docker_image: codalab/codalab-legacy:py39 # the Docker image in which submissions are run，用此 default 即可
enable_detailed_results: True # 不明，可以 default

# Documentation web pages
terms: pages/terms.md # 必须有一个 terms
pages:  # 可任意加页面
  - title: Overview
    file: pages/overview.md

# Definition of the tasks
tasks:
- index: 0
  name: Development Task
  description: 'Development phase: create models and submit them to obtain feedback.'
  is_public: true
  input_data: feedback_phase/input_data         # 此处及下列路径需要填写所上传 bundle 里的路径，而非所生成 Docker 中的
  reference_data: feedback_phase/reference_data
  scoring_program: scoring_program
  ingestion_program: ingestion_program
solutions: []   # 不明

# Sample code submission
solutions:      # 不明，似乎在比赛中无处显示
  - index: 0
    tasks:
    - 0
    - 1
    path: solution/

phases:
- index: 0
  name: Development
  description: 'Development phase: create models and submit them to obtain feedback.
      You can make 5 submissions per day and 100 submissions in total.'
  start: 1-1-2023 # Month/Day/Year
  end: 1-30-2024
  max_submissions_per_day: 5
  max_submissions: 100
  execution_time_limit: 600
  tasks:
  - 0
  solutions: []
  starting_kit: starting_kit
  public_data: feedback_phase/input_data

# Fact sheets to add more information in the leaderboard
fact_sheet: {
    "method_name": {
        "key": "method_name",
        "type": "text",
        "title": "Method name",
        "selection": "",
        "is_required": "false",
        "is_on_leaderboard": "true"
    }
}

# Leaderboard
leaderboards:
- index: 0
  title: Results
  key: Results
  submission_rule: "Force_Last"     # 可以去掉，默认似乎是允许展示多个结果
  columns:
      - title: Average Accuracy     # 在 output.json 中，读取该 json 的哪个 key
        key: avg_accuracy           
        index: 0
        sorting: desc
        computation: avg
        computation_indexes:
          - 1
```

2. scoring program

奇异的是，比赛运行时所创建的 Docker 中文件结构并不是 bundle 的结构，或者示例 competition.yml 中指示的路径，而是会把各种资源结构打乱放在不同的位置。对我们影响就是，如果 scoring program 需要读其它文件（多代码文件 / gold answer 等），就需要按创建好的 Docker 中的新文件路径读取。

比如，在我的测试中，Docker 的实际文件夹结构如下：

```
.
- app
    - codalab           // 不明
    - data              // 不明
    - input
        - res           // 用户结果
        - ref           // gold anwser
    - shared            // 不明
    - program           // 所上传脚本
        - score.py
        - metadata.yaml
    - output            // 脚本输出，用于 leaderboard 读取
        - output.json
```

如果上述路径在你的测试中不 work，可以先上传一个含有 competition.yaml / scoring program / reference data / result data / ingestion program 等所有资源的测试 bundle，要求 scoring program 输出 Docker 的文件夹结构树，在 terminal 中依次记下资源的路径。

可供参考：

- [codalab/competition-examples/codabench](https://github.com/codalab/competition-examples/tree/master/codabench)

### UI 创建

TODO

## 修改

只支持通过 UI 修改。不能重新上传 bundle，每次重新上传 bundle 就视为创建一个新的比赛。

进入 Codabench 首页 -> 右上角 Benchmark -> Management -> 选择一个已有的比赛右侧 Edit 按钮。

顶层有 Details / Participation / Pages / Phases / Leaderboard / Administrators 六个页面，其它较易懂，Phases 和 Leaderboard 的设置比较复杂。

### Phases

Phases 构成比赛主体。一个比赛可以有一个或多个 phase，这样设计可能是有些比赛分成在多个数据集上测试；一个 phase 又可以包含多个 tasks，可能是为了支持有些比赛每个 phase 又有多个数据集。phase 之间不共享资源/Docker 环境，同一个 phase 的不同 task 之间共享资源/环境。

最简单的方式可以只定义一个 phase。区分数据集甚至可以只通过 scoring program 来实现。

在 phase 的 edit 界面最下方，可以通过 Manage tasks 按钮打开 task 的 edit 界面，该界面中 Submission / Datasets and programs / Bundles 三个页面都可以忽视，只需要使用 Tasks 这个页面。

task 的本质意义是 scoring program 和 reference data / ingestion program / result data 的关联方式。

（TODO：资源文件夹名和资源别名的关系，哪些资源必须添加，如何删除资源）

### Leaderboard

（TODO；scoring program 和这里设置的关联方式）

## 使用

1. 提交：TODO（如果卡住）
2. 查看结果：TODO terminal 的每个页面
3. Leaderboard：结果不会自动更新到 Leaderboard，需要用户同意。

## 参考资料

- [Codabench: Flexible, Easy-to-Use and Reproducible Benchmarking Platform](https://arxiv.org/abs/2110.05802)
- [Codabench Repo Wiki](https://github.com/codalab/codabench/wiki)
- [Codabench Repo Issue](https://github.com/codalab/codabench/issues)

现有参考资料都不太全面，不能覆盖各种常见错误，一些创建步骤和行为需要通过猜测得知。