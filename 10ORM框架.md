# 引提：学完pymysql后大家已经可以写学生管理系统的MySQL数据库版本了，类似sqlite版本
步骤： 1>设计数据库     2>数据库图形工具中或py脚本中创建数据库表      3>开发    开发缺点：1>纸上、或画ER图，写SQL，图形工具中运行SQL创建表  2>数据取出来之后需要声明一些变量来接收。这些变量与student类类似。重复 3>如果要修改表结构添加字段，首先要在SQL console运行SQL添加字段，然后再回到后端项目取新增加字段、修改业务逻辑。不断在数据库datagrip和pycharm切换。    4>如果项目需要切换sqlite到MySQL，配置服务器，后端调整   5>有的人擅长python但不擅长SQL语法

## orm
ORM:object relational mapping   对象关系映射。类映射数据库表。类似wtform从后端类生成前端html代码，orm框架会从类生成SQL并执行。查询时不需要SQL直接通过类对象知名的orm框架：sqlAlechemy(),django,peewee(轻量)
优点：提高开发效率，代码风格统一为后端
缺点：由于封装，一旦出错不好修改，如果SQL基础不牢，一旦出错不易修改。
