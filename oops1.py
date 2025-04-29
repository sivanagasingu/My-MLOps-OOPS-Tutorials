# initiate a calss
class employee:
    # special method/magic method/dunder method - constructor
    def __init__(self):
        print("Started executing attributes/data")
        self.id = 123
        self.salary = 50000
        self.designation = "SDE"
        print("attributes/data have been initiated")

    def travel(self, destination):
        print("This travel function was called manually")
        print(f"Employee is now travelling to {destination}")    
        

# create an object/instance of the class
emp_1 = employee()

# printing attributes
print(emp_1.salary)
print(emp_1.designation)

# Calling a method
emp_1.travel("Kerala")

print(type(emp_1))
