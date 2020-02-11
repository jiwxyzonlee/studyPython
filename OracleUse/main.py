
import cx_Oracle
import sys
try:
    dsnStr = cx_Oracle.makedsn('211.183.7.81/24', '1521', 'xe')
    con = cx_Oracle.connect(user = 'scott', password = 'tiger', dsn = dsnStr)
    print(con)
except:
    print('exception', sys.exc_info())
finally:
    con.close()