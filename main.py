class Student:
    group = "C2011"
    education = "STEP"

    def __init__(self, name, age):
        self.name = name
        self.age = age


print(Student.group, Student.education)
st = Student(name="Oleg", age=15)
print(f"ST = {st.group} ")
st1 = Student(name="Anna", age=16)
print(f"ST1 = {st1.group} ")
st2 = Student(name="Sacha", age=14)
print(f"ST2 = {st2.group}")
print(f"Name st {st.name} {st.age}")
print(f"Name st1 {st1.name} {st1.age}")
temp = f"Name st2 {st2.name}{st2.age}"
print(temp)
print("Name st2", st2.name,st2.age)
