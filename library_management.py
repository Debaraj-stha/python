class student:
    name=""
    department=""
    section=""
    books=[]
    number_of_books=0
    def  take_user_details(self):
        self.name=input("Please enter name").lower()
        self.department=input("Please enter department").lower()
        self.section=input("Please enter section").lower()
    
    def take_book(self):
        while True:
            number_of_books=input("Please enter number of books")
            if(int(number_of_books)>5 or int(number_of_books)<0):
                print("number of books must be less tha or equal to 5 and greater than 0")
            else:
                break
        for i in range(1,int(number_of_books)+1):
            user_input=input("Please enter name of book")
            self.books.append(user_input)
    def show_details(self):
        print(f"Name:{self.name} \nsection:{self.section} \ndepartment:{self.department} \nnumber of books:{len(self.books)}\n")
        print("name of books")
        for book in self.books:
            print(book)


s = []
for i in range(1, 2):
    si = student()
    si.take_user_details()
    si.take_book()
    si.show_details()