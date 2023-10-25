
class Person:
    def _init_(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")

# Create an object
person1 = Person("Alice", 30)

# Access object attributes and methods
print(person1.name)
person1.introduce()
Inheritance:
python
Copy code
class Student(Person):
    def _init_(self, name, age, student_id):
        super()._init_(name, age)
        self.student_id = student_id

    def study(self):
        print(f"{self.name} is studying.")

# Create a student object
student1 = Student("Bob", 20, "S12345")

# Access inherited attributes and methods
print(student1.name)
student1.introduce()
student1.study()



class BankAccount:
    def _init_(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds.")

    def get_balance(self):
        return self.__balance

# Create a bank account object
account = BankAccount(1000)

# Access balance using public method
print("Balance:", account.get_balance())