import pyodbc
server = 'KEERTHANA\MSSQLSERVER01'  # replace with your server name or IP address
database = 'datasci'  # replace with your database name
username = 'sa'  # replace with your username
password = 'Sachin$00'  # replace with your password
connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                            f'SERVER={server};'
                            f'DATABASE={database};'
                            f'UID={username};'
                            f'PWD={password}')
cursor = connection.cursor()
    # id=int(input('enter a number'))
    # name=input('enter a name')
    # mark1=int(input('enter a mark'))
    # mark2=int(input('enter a mark2'))
    # mark3=int(input('enter a mark3'))
    # total=mark1+mark2+mark3
    # avg=total/3
    # if total>=290:
    #     grade='A'
    # elif total<290 and total>=275:
    #     grade='B'
    # elif total<275 and total>=250:
    #     grade='C'
    # elif total<250 and total>=200:
    #     grade='D'
    # else:
    #     grade='E'
    # print(id,name,mark1,mark2,mark3,total,avg,grade)
def insertstudent(id,name,mark1,mark2,mark3,total,avg,grade):
    query = f"INSERT INTO student_python VALUES ({id}, '{name}', {mark1}, {mark2}, {mark3}, {total}, {avg}, '{grade}')"
    cursor.execute(query)
    connection.commit()
    # cursor.close()

#insertstudent(2,'shabie',45,56,45,136,34.5,'A')
