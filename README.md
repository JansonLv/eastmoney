`2017年8月01日`

项目开始


`2017年8月02日`

wap页面分析,获取数据

Q:正文获取,正则匹配

J:正则匹配,反向思路,找共同点

`2017年8月6日`

Q:数据库添加错误

J:最好加在一行


`2017年8月10日`

Q:内存损耗大大增加

J:更改过滤器,将爬取的网站的urlhas+bloom加密存储,然后再判断

`2017年8月12日`
Q:多任务启动
J:暂时没必要,不如多终端zho启动爬虫


'2017年8月20日'
Q:基于布隆的优化,大概有1/20的重复率,过高

**可能性**:
确定是url问题
算法问题
中间暂停导致的问题

**测试**
1.增加url属性
2.夜间不间断测试
3.分别测试haslib和bloom

**`假设算法问题`**
1.优化布隆

**`_暂停问题_`**
1.单机redis