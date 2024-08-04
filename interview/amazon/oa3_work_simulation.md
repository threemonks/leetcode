https://www.1point3acres.com/bbs/interview/amazon-software-engineer-562078.html

Module1:
制定deliver route plan 需要满足1.enable 80 deliveries per day 2.should not exceed 200 miles
有两个备选方案，第一个每天够了80但是mile数超了好多，第二个mile数没超但送货数量不够
Q1 问你选哪个 五个statement按effective级别排序
Q2 问你如果可以request additional info 哪个更重要 （我选了BC）
A 会影响efficiency的future trends data B mile数和delivery数哪个重要 C 过去100天的data D 城市地图 E 过去3天的performance data
Q3 给了你过去3天和100天的traffic data 问你planA和B哪个好
我真的不知道哪个好啊！！！最后犹豫半天选了第一个 因为送货数量pattern比较符合traffic，也不知道对不对
  -
  
Module2:
同组的两个人说你的code不错，一个人说不行要重做
Q1问你怎么办
选项大致就是 A 有人approve了所以就按我的来 B 你说不对就按你的来吧 C meeting决定
应该是选和这个人单独offline meeting那个选项 因为接下来就和他讨论了
Q2 讨论到了下班，你还是很confused, 但记了好多笔记 问你怎么办 排序
A 明天再full time meeting B 新方法太难了还是用旧的 C 回家过一遍笔记把能写的都写出来 不能写的记下来明天接着meeting D do as much as you can E找那两个说你做的不错的同事帮你 F 和这人再meet三十分钟（这是要把他累死啊）

Module3:
给你两个要implement的feature


Q1 选出4个feature1的优点
Q2 选出2个feature2的优点
两个都不难 比gre阅读简单
Q3只能implement一个 你选哪个 应该是排序 我选了feature1 应该是对的 因为最后决定做1了
Q4 有个senior engineer说我们要implement feature 2 问这时候你怎么做
A 和他还有high level decision makers开会 B 坚持做feature1因为已经讨论过pros and cons了 C 和这人还有external team开会 D 全组投票 E 因为他比你有经验所以听他的 F 问manager
Q5 manager过来说我们要做feature1，而且要在social media C D E上实现，但是ddl很紧张，问你怎么做 排序
A 直接跟manager说做不了 需要更多resource B 因为ddl紧张所以不test了 C 排序这三个social media的重要性 先做重要的 把不重要的留到ddl之后 D 先做着 过几周再找manager说你做不完了 需要additional resource（这个不太好吧） E 自己找team member寻求帮助 F 直接驳回 建议只work on 1-2 social medias G 自己work overtime

Module4:
亚麻的product page出问题了，有customer无法查看product info，你manager让你解决
Q1 What additional info would be helpful? 排序
A customer region B URL C Screenshot of error page D session ID E Browser versions
Q2 你怎么fix this bug？ 排序
A search the logs B look at metrics(latency, error counts, # of requests....) C 手动去看code然后debug（好猛） D 分析有可能会fail的request的log E 跟technician说这是偶然现象 自己会fix F 只分析failed request不看valid request G 因为太urgent了所以立刻去向大佬请教
Q3 给了log data 让你分析到底哪出错了
这题应该选unequal number of rate and review

Module5: 这个module好好笑
你要debug一个东西，manager跟你说大概需要三天，但PM让你今天就交因为他觉得是个小bug 可以不用test
Q1 你怎么办 排序
A 跟senior eng讨论一下risk再决定 B 还是先test过后再release C 跟PM manager开会再决定 D 都有理所以重新问问你manager E 相信PM 不test了
Q2 一周以后你同事也遇到了相同情况，他想push without test，你怎么办 排序
这道题选项记不太清了 大致就以下几种： A 把你上次情况跟他说，劝他别这样 B 不关我事 C 建议他找senior eng讨论下 D 找他manager告状（当时看到这个选项笑得停不下来）
Q3 马上下班时候收到同事msg，他没听你的，直接push code了，结果翻车了（哈哈哈哈哈哈哈哈哈哈）你怎么办 排序
A 早跟你说了你不听 B ask for more info about the issue C 帮助他revert code change D 帮助他push另一个code把问题立刻解决（这真的能做到吗。。） E 找senior eng求救 F ignore the message and sign off（这个也好好笑）
Q4 manager给你发邮件说让你come up with a plan to make sure this doesn't happen again 而且希望你把这个任务prioritize 你怎么搞 单选
A 跟他说我做完手头的再去做（作死啊） B write up document详细描述 C set ‍‌‍‌‌‌‌‌‍‌‍‌‍‌‌‌‌‌‌‍up automations来预防 D 规定以后每个code change都必须有至少一个peer review  E 和manager，PM再好好探讨下不test的风险（打PM脸啊这是）F 让之前翻车的同事跟你一起弄