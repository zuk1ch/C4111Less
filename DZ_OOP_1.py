class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0

    def __str__(self):
        return self.name


class StudentGroup:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def best_student(self):
        if not self.students:
            return "Група студентів порожня"

        best_student = None
        best_average = 0

        for student in self.students:
            average = student.average_grade()
            if average > best_average:
                best_average = average
                best_student = student

        if best_student:
            return f"Найкращий студент: {best_student.name} із середньою оцінкою: {best_average}"
        else:
            return "Не вдалося визначити найкращого студента."


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hi(self):
        print(f"Привіт, мене звати {self.name}!")

    def __len__(self):
        return self.age





class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Внесено: {amount}. Новий баланс: {self.balance}")
        else:
            print("Сума для внесення повинна бути більше нуля.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Знято: {amount}. Новий баланс: {self.balance}")
        else:
            print("Недостатньо коштів або неправильна сума.")

    def get_balance(self):
        return self.balance




student_1 = Student("Іван", [90, 80, 85])
student_2 = Student("Марія", [95, 85, 90])
print (f"Студент {student_1} має середню оцінку: {student_1.average_grade()}")
print (f"Студент {student_2} має середню оцінку: {student_2.average_grade()}")

print ("================================================================")

group = StudentGroup()
group.add_student(student_1)
group.add_student(student_2)
print(group.best_student())

print ("================================================================")

person = Person("Олександр", 30)
person.say_hi()
print(len(person))


print ("================================================================")

account = BankAccount("123456789", 1000)
account.deposit(500)
account.withdraw(200)
print(f"Поточний баланс: {account.get_balance()}")
