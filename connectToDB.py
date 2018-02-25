import pymysql

connection = pymysql.connect(host="127.0.0.1", user="root", password="root", db="world")
statement = connection.cursor()
rowcount = statement.execute("select * from countrylanguage limit 2")
description = statement.description

print('Number of records = ', rowcount)

fieldNames = [i[0] for i in description]
print('Description : ', fieldNames)

# for a in range(rowcount):
#     data = statement.fetchone()
#     print(data)

data = statement.fetchall()
print('Printing all the data', data)

for row in data:
    print(row[0], '\t', row[1], '\t', row[2], '\t', row[3])
    # print(row)

connection.close()
