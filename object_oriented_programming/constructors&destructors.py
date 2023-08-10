# constructors are functions that are called when an object of a class is created
# the `__init__` function is used as a constructor

class ClassSchedule:
    def __init__(self, course):  
        self.course = course

# the `self` parameter refers to the current instance
# the instance variable `course` allows for input to assign a value

first = ClassSchedule('Chemistry')
print(first.course)

# destructors are called to delete an object
# the `__del__()` method is commonly used as the destructor

class ClassSchedule:
    def __init__(self, course):  
        self.course = course

    def __del__(self):
        print('you successfully deleted your schedule') 

sched = ClassSchedule('Chemistry')
del sched