import mysql.connector as sql
mycon=sql.Connect(host="localhost",user='root',password='root',database='miniprojects')

cursor=mycon.cursor()
tablename='todolist'

query1=f'Create table todolist(SrNo int, Todolist varchar)'
cursor.execute(query1)
mycon.commit()
cursor.close()

'''
for index, row in f.iterrows():
    query = f"INSERT INTO {tablename} (Sr No.,Tasks) VALUES (%d, %s)"
    values = tuple(row)  # Convert the row values to a tuple
    cursor.execute(query, values)
mycon.commit()
cursor.close()
'''
'''

todolist=[]
def createTodo():
    srno=len(todolist)+1
    task=input("{}.".format(srno))
    #taking todo
    todolist.append(task)
def readTodo():
    for index,todo in enumerate(todolist):
        print("{}. {}".format(index+1,todo))
def updateTodo():
    try:
        taskindex=int(input("Enter the Todo you want to update :"))
        task=input("{}.".format(taskindex))
        todolist.pop(taskindex-1)
        todolist.insert(taskindex-1,task)
    except ValueError:
        updateTodo()
def doneTask():
    try:
        done=int(input("Enter the Todo :"))
        print(todolist)
    except Exception:
        doneTask()
def deleteTodo():
    try:
        deltask=int(input("Enter the Todo which you want to delete :"))
        todolist.pop(deltask-1)
    except ValueError :
        deleteTodo()
createTodo()
createTodo()
createTodo()
updateTodo()
readTodo()
'''