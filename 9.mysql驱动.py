# 引提：已经学习了SQL语法，sqlite驱动操作sqlite数据库，datagrip的jdbc java驱动操作MySQL。所以我们要找python操作MySQL驱动
"""
1. MYSQLDB。已经有C驱动MySQL的成熟包。MYSQL包python对这个C驱动包封装。优点效率高。py2环境和众多项目中使用。缺点Windows下pip安装包错(因为pip中没有这个包），可以去网上找对应平台编译后的.whl安装（也可能出错）最终解决去MySQL官网下载对应平台的connector.msi安装
2. pymysql。纯python写的。缺点效率低。优点安装方便，完全兼容，MySQLdb的语法，市场占有率越来越高


"""

import pymysql.cursors
connection = pymysql.connect(host='127.0.0.1',
                             port=3306,
                             user='root',
                             password='111111',     #安全风险，未来会从环境变量中读取
                             db='test',
                             # charset='utf-8mb4',
                             cursorclass=pymysql.cursors.DictCursor   #返回字典格式的结果集，不写返回默认元组格式
                            )
try:
    with connection.cursor() as cursor:
        sql = """SELECT * FROM shirt;"""
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
        for rows in result:
            print('小红有一件{}色的{}'.format(rows['collor'], rows['style']))
            print('-'*50)
    with connection.cursor()as cursor:
        sql ="""INSERT INTO shirt value (%s,%s,%s,%s)"""
        affected_rows = cursor.execute(sql, (None, '裙子', '绿', 2))
        print(affected_rows)
    connection.commit()
except Exception as e:
    print(e)
finally:
    connection.close()


# 扁平写法
# cursor = connection.cursor()
# cursor.exe()
# cursor.fetchone()
# cursor.close()
# connection.close()

