import mysql.connector as mysql

# Establishing database connection
db = mysql.connect(host="localhost", user="root", password="", database="college")
ch = db.cursor()

def display_menu():
    print("WELCOME TO SUBHAS BOSE INSTITUTE OF TECHNOLOGY")
    print("1. Admission page")
    print("2. Fee Structure")
    print("3. Highest packages and average packages")
    print("4. Exit")

def admission_page():
    print("Codes for the subjects are :-")
    print("Computer science: cse")
    print("Information Technology: it")
    print("Electrical and communication: ece")
    print("Mechanical: mec")
    print("Civil: civ")
    print("Textile: txt")
    print()
    f = input("Enter your first name: ")
    f = f.capitalize()
    l = input("Enter your last name: ")
    l = l.capitalize()
    r = int(input("Enter your jee rank: "))
    p = int(input("Enter your board percentage: "))
    s = input("Enter your stream: ")
    s = s.upper()
    re = input("Enter your reservation: ")
    re = re.upper()
    cn = int(input("Enter your contact number: "))
    bm = str(cn)
    if len(bm) > 10 or len(bm) > 10:
        cn = int(input("Enter your valid contact number: "))
    else:
        pass
    ei = input("Enter your Email ID: ")
    c = ch.execute(
        "INSERT INTO `admission`(`First Name`, `Last Name`, `JEE Rank`, `Board Percentage`, `Stream`, `Reservation`,`Phone No.`,`Email ID`) VALUES ('{}','{}',{},{},'{}','{}',{},'{}')".format(
            f, l, r, p, s, re, cn, ei))
    db.commit()
    c = db.cursor()
    c.execute("SELECT * FROM admission")
    r = c.fetchall()
    print(r[-1])
    print("Thank you for filling up the admission form, You will be notified within 5 business days ")
    pass

def fee_structure():
    print("Welcome to the fee page")
    print("the fee structures for the streams are given below:-")
    print('Computer science:-', '200000')
    print('Information And Technology:-', '180000')
    print('Electrical And Communication:-', '150000')
    print('Mechanical:-', '120000')
    print('Civil:-', '100000')
    print('Textile:-', '90000')
    print('Hostel Fees for single room:- 2000 per month')
    print('Hostel Fees for shared room:- 1000 per month')
    pass

def highest_packages():
    print("Highest package for 2017-18:- 2cr", 'average package:- 27 lpa')
    print("Highest package for 2018-19:- 1.5cr", 'average package:- 21 lpa')
    print("Highest package for 2019-20:- 2.5cr", 'average package:- 25 lpa')
    print("Highest package for 2020-21:- 3cr", 'average package:- 30 lpa')
    print("Highest package for 2021-22:- 1.25cr", 'average package:- 19 lpa')
    print("Highest package for 2022-23:- 2.75cr", 'average package:- 26.5 lpa')
    pass

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            admission_page()
        elif choice == '2':
            fee_structure()
        elif choice == '3':
            highest_packages()
        elif choice == '4':
            print("Thank you for using the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()

