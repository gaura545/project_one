  
import user
import students
import mysql.connector
connection = mysql.connector.connect(user='root',password='gaurav',host='localhost',database='quiz')
mycursor = connection.cursor()

def question():

    level = input("Enter the dificulty level")
    topic = input("Enter the topic name: ")
    ques = input("Enter the question: ")
    opa = input("Enter option a: ")
    opb = input("Enter option b: ")
    opc = input("Enter option c: ")
    opd = input("Enter option d: ")
    correct = input("Correct option: ")
    mycursor.execute("insert into questions values('%s','%s','%s','%s','%s','%s','%s') ;" % (
        ques, opa, opb, opc, opd, correct, topic, level))
    connection.commit()
    
def remove_question(self,delQ):
        sql = "DELETE question = %s"
        val = (delQ,)
        mycursor.execute(sql,val)
        mydb.commit()

def student_marks():
    mycursor.execute("select * from details ;")
    print('MARKS:\nName\t\tTopic\t\tMarks\t\tDate')
    for i in mycursor.fetchall():
        print(i[0], i[1], i[2], i[3], sep='\t\t')
    connection.commit()

def main():
    n = ''
    while n != 'q':
        print('Enter the choice')
        print('1:Add user\n2:Add Question\n3:View student Marks\nq:quit')
        n = input()
        if n == '1':
            mycursor.execute("insert into user values('%s','%s')" %
                      (input('Enter new username: '), input('Enter password: ')))
            connection.commit()

        elif n == '2':
            question()
            connection.commit()

        elif n == '3':
            student_marks()
            connection.commit()
