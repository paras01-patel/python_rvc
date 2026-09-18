class Student:

    course = "BCA"

    def info(self, name, age):
        self.name = name
        self.age = age
        print("Name:", self.name, "Age:", self.age)


s1 = Student()
s1.info("Paras", 21)

s2 = Student()
s2.info("Rahul", 20)

s3 = Student()
s3.info("Aman", 22)

s4 = Student()
s4.info("Rohit", 19)

s5 = Student()
s5.info("Vikas", 23)