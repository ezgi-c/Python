# public access modifier
    #  no modification, class members can be accessed from any part of the program

# protected access modifier
    # protected members denoted with prefix `_` , can only be accessed from outside of class from a subclass

# private access modifier
    # private members denoted with prefix `__` , accessible within the class only


class ClassSchedule:
    def __init__(self, course, instructor):
        self.__course = course  # private
        self.__instructor = instructor  # private

    def display_course(self):  # public

        print(f'Course: {self.__course}, Instructor: {self.__instructor}')

sched = ClassSchedule('Biology', 'Ms. Smith')

# the following will throw an Attribute Error because we're trying to access a private member
#sched.__course 

# this line won't throw an Attribute Error because this method is public
sched.display_course() 