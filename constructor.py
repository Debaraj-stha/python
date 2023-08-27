class student:
    office_name = 'xyz private compony limited'
    def __init__(self,name,grade,section):
        self.name = name
        self.grade = grade
        self.section = section
    def show_details(self):
        print(f" office name:{self.office_name} \nname:{self.name} \n grade:{self.grade} \nsection:{self.section}\n")
        


s=student("Ram",10,"A")
s2=student("Sita",12,"B")
s3=student("Sina",13,"C")
s.show_details()
s2.show_details()
s3.show_details()