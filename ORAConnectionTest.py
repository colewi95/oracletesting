import os
import cx_Oracle

print(os.environ['ORACLE_HOME'])

try:
 connection = cx_Oracle.connect("LDCS_SEYMOUR_DEV","SOUR+Dev_Pwd_123!!","//10.13.31.174/orclcdb")
 cursor = connection.cursor()
 rs = cursor.execute("SELECT * FROM ACCESSION_66 WHERE ROWNUM <10")

 for row in rs: 
     print(row)
    
except cx_Oracle.DatabaseError as exc:
  err, = exc.args
  print("Oracle-Error-Code:", err.code)
  print("Oracle-Error-Message:", err.message)
finally:
  cursor.close()
  connection.close()