from datetime import datetime, timedelta
books = [
    {
        "semester": "1",
        "books": ["Digital logic", "Math", "Physics", "IIT", "C programming"]
    },
    {
        "semester": "2",
        "books": ["OOP", "Math", "Statistics", "Discrete", "Microprocessor"]
    },
    {
        "semester": "3",
        "books": ["Graphics", "Statistics-ii", "Data structure", "Architecture", "Numerical method"]
    },
    {
        "semester": "4",
        "books": ["OS", "CN", "AI", "DBMS", "TOC"]
    },
    {
        "semester": "5",
        "books": ["Digital logic", "Math", "Physics", "IIT", "C programming"]
    },
    {
        "semester": "6",
        "books": ["Digital logic", "Math", "Physics", "IIT", "C programming"]
    },
    {
        "semester": "7",
        "books": ["OOP", "Math", "Statistics", "Discrete", "Microprocessor"]
    },
    {
        "semester": "8",
        "books": ["Graphics", "Statistics-ii", "Data structure", "Architecture", "Numerical method"]
    },
]


class Person:
    name = ""
    phone = ""
    role = ""

    def get_details(self):
        self.name = input("Enter name--").lower()
        self.phone = input("Enter phone--").lower()

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Phone: {self.phone}")
        print(f"Role: {self.role}")


class Librarian(Person):

    def get_details(self):
        Person.role = "admin"
        Person.get_details(self)
        print()

    def view_Books(self):
        for book in books:
            print("--------------------------------")
            print(f"semester:{book['semester']}")
            for a in book['books']:
                print(f"{a}")


class student(Person):
    batch = ""
    section = ""
    Person.role = "student"

    def get_details(self):
        Person.get_details(self)
        self.section = input("Enter section--").lower()
        self.batch = input("Enter batch--").lower()

    def show_details(self):
        Person.show_details(self)
        print(f"section: {self.section.upper()}")
        print(f"batch: {self.batch}")


class Book:
    name = ""
    ISBN = ""
    books=[]
    def get_details(self):
        self.name = input("ENter book name--")
        self.ISBN = int(input("Enter book ISBN number--"))
        self.books.append({"name":self.name,"ISBN":self.ISBN})
    def borrow_book(self, s1):
        while True:
            user_input = int(input(
            "Enter  number of books to borrow--"))
            if(user_input>5 or user_input<=0):
                print("number of books must be less tha or equal to 5 and greater than 0")
            else:
                break

        books = []
        for i in range(1, user_input + 1):
                book = Book()
                book.get_details()
                books.append(book)
        print()
        s1.show_details()
        print()     

    def return_book(self, s1):
        user_input = input(
            "Enter  number of books to return--")

        if user_input > 0:
            books = []
            for i in range(1, int(user_input) + 1):
                book = Book()
                book.get_details()
                books.append(book)
            print()
            s1.show_details()
            print("Books you returned are:")
            print("=================================")
            print("Name\t\t\t ISBN\n")
        else:
            print("invalid number")

    def show_details(self,type):
        if(type=="borrow"):
            print("Books you borrowed are:")
        else:
            print("Books you returned are:")
        print("==========================")
        print("Name\t\t\t ISBN")
        for book in books:
            book.show_details()
        date = datetime.now().date()
        if(type=="borrow"):
            print(f"borrowed date:{date}")
            print(f"yow have to return book in {date+timedelta(days=5)}")
        else:
            print(f"returned date:{date}")
        for book in self.books:
            if(len(book['name'])>=15):
                print(f"{book['name'][:15]} ...\t {book['ISBN']}")
            else:
                print(f"{book['name']}\t {book['ISBN']}")
students=[]
books=[]
i=0
while True:
    si = student()
    si.get_details()
    students.append(si)
    bi = Book()
    user_input = input("enter b for borrow and r for return book--").lower()
    if (user_input == "b"):
        bi.borrow_book(si)
        bi.show_details()
    if(user_input == "r"):
        bi.return_book(si)
        books.append(bi)
    else:
        print("invalid choice!!")
        exit(1)
    print()
    user_input=input("add more student[y/n]:").lower()
    if(user_input == "y"):
        i+=1
    else:
        break