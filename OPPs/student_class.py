class Student:
    def __init__(self,enrID,subject,hobby):
        #def __init__(self,enrID  ,subject = "Maths" ,hobby = "cricket"): is the by default value of it 
        self.enrID = enrID
        self.subject = subject
        self.hobby = hobby

student_data = Student(123,"Mathematics","Playing Cricket")
print(student_data.enrID,student_data.subject,student_data.hobby)

student_data = Student(123,"Science","Cricket")
print(student_data.enrID,student_data.subject,student_data.hobby)
