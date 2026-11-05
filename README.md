# AI漫剧制作
Python入门练习项目｜漫剧AI绘图Prompt生成器

## 📌 项目说明
脚本名称：day7.py
内置10名角色：南宫问天、东方燕、南宫问雅、南宫颖、北冥雪、西门晴、南宫清鸢、李长河、南宫玄、赵德柱
一共13组分镜，使用for循环自动拼接角色人设+镜头画面描述，批量输出AI绘图提示词。

## 📅 学习复盘 Day1 ~ Day7
- Day1：搭建Python+VS Code环境，安装插件；学习print、变量、字符串、数字类型。练习打印漫剧角色人设、分镜文本。
- Day2：运算符、注释、input输入输出。练习控制台输入提示词，自动拼接成完整prompt。
- Day3：if/else条件判断。练习检测提示词长度，文字过长给出截断提醒。
- Day4：for / while 循环。练习循环批量生成多条分镜提示词列表。
- Day5：列表、字典。重点学习字典存储角色信息：发型、服装、画风，搭建角色库。
- Day6：练习字典查询，读取角色设定组合生成画面提示词。
- Day7：本周复盘整理，编写综合脚本；完成第一次GitHub代码提交。

## ▶ 运行方法
1. VS Code打开 day7.py，安装Code Runner插件
2. 运行代码，控制台自动输出13组分镜prompt

## Week2 学习复盘（Day8~Day14）
学习内容：异常捕获、pip第三方库、文件读写、requests GET/POST、json解析
综合脚本功能：
1. 读取本地剧本txt分镜
2. 自动拼接漫剧画风提示词prompt
3. POST请求调用AI绘图API，连通测试
4. 捕获文件、网络、JSON解析异常
5. 输出全部记录保存到文本

文件清单：
- day8.py  异常捕获练习
- day9.py  pip模块练习
- day10.py 文件读写
- day11.py requests GET
- day12.py requests POST
- day13.py json解析返回
- day14.py 本周综合复盘脚本
- script.txt 剧本源文件
- week2_result.txt 输出结果
