# kaggle-leaderboard-scraper

可以爬取全部kaggle比赛的leaderboard数据，已结束的比赛可以获取其public或private榜，正在进行的比赛只有public榜，可以通过传入的参数决定爬取哪个榜单数据。

只需确定比赛的唯一名字，在比赛的链接中可以找到，如著名的titanic比赛链接为：

https://www.kaggle.com/c/titanic

它的唯一名字为"titanic"，只需在命令行执行：

```
python main.py titanic private
```

或

```
python main.py titanic public
```

