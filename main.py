import mysql.connector as mysql
db=mysql.connect(host="localhost",user="root", password="",database="college")
ch=db.cursor()
i='y'
while i=="Y" or i=='y':
    print("WELCOME TO SUBHAS BOSE INSTITUTE OF TECHNOLOGY")
    print("press 1 for the Admission page")
    print('Press 2 for the Fee Structure')
    print("Press 3 for the highest packages and average packages")
    n = int(input("Enter your response:- "))
    if n!=1 or n!=2 or n!=3:
        print("Please enter a valid response")
    while n==1:
        print("Codes for the subjects are :-")
        print("Computer science: cse")
        print("Information Technology: it")
        print("Electrical and communication: ece")
        print("Mechanical: mec")
        print("Civil: civ")
        print("Textile: txt")
        print()
        f=input("Enter your first name: ")
        l=input("Enter your last name: ")
        r=int(input("Enter your jee rank: "))
        p=int(input("Enter your board percentage: "))
        s=input("Enter your stream: ")
        re=input("Enter your reservation: ")
        cn=int(input("Enter your contact number: "))
        ei=input("Enter your Email ID: ")
        c=ch.execute("INSERT INTO `admission`(`First Name`, `Last Name`, `JEE Rank`, `Board Percentage`, `Stream`, `Reservation`,`Phone No.`,`Email ID`) VALUES ('{}','{}',{},{},'{}','{}',{},'{}')".format(f,l,r,p,s,re,cn,ei))
        db.commit()
        c=db.cursor()
        c.execute("SELECT * FROM admission")
        r=c.fetchall()
        print(r[-1])
        print("Thank you for filling up the admission form, You will be notified within 5 business days ")
        print("Do you want to continue??")
        i = input("Y or N:- ")
        break

    while n==2:
        print("Welcome to the fee page")
        print("the fee structures for the streams are given below:-")
        print('Computer science:-','200000')
        print('Information And Technology:-','180000')
        print('Electrical And Communication:-', '150000')
        print('Mechanical:-', '120000')
        print('Civil:-', '100000')
        print('Textile:-', '90000')
        print('Hostel Fees for single room:- 2000 per month')
        print('Hostel Fees for shared room:- 1000 per month')
        print("Do you want to continue??")
        i = input("Y or N:- ")
        break



    while n==3:
        print("Highest package for 2017-18:- 2cr",'average package:- 27 lpa')
        print("Highest package for 2018-19:- 1.5cr",'average package:- 21 lpa')
        print("Highest package for 2019-20:- 2.5cr",'average package:- 25 lpa')
        print("Highest package for 2020-21:- 3cr",'average package:- 30 lpa')
        print("Highest package for 2021-22:- 1.25cr",'average package:- 19 lpa')
        print("Highest package for 2022-23:- 2.75cr",'average package:- 26.5 lpa')
        print("Do you want to continue??")
        i = input("Y or N:- ")
        break
if i=='n' or i=='N':
    print('Thank You')
    exit()
#completed
