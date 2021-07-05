# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import random
import mysql.connector

def info_database():

    mydb = mysql.connector.connect(
          host="localhost",
          user="root",
          passwd="",
          database="python_first_database"
    )

    mycursor = mydb.cursor()
    mycursor.execute("CREATE TABLE users (name VARCHAR(255), surname VARCHAR(255), email VARCHAR(255),address VARCHAR(255))")
    mycursor.execute("SHOW TABLES")

    #mycursor.execute("INSERT INTO customers (name, address) VALUES ('John', 'Highway 21')")
    #mydb.commit() # Use this command after insert or update


#Collection data
# There are four collection data types in the Python programming language:

# -List is a collection which is ordered and changeable. Allows duplicate members.
# -Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# -Set is a collection which is unordered and unindexed. No duplicate members.
# -Dictionary is a collection which is unordered and changeable. No duplicate members.


# Set up a secret number between 0 and 99
secret_number = random.randint(0, 100)  # return a random int between [0, 100]


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print('Python '+ (name))  # Press Ctrl+F8 to toggle the breakpoint.


def print_sum(result):

    # first = 10
    # second = 20

    # first = 10
    # second = 20
    # print  "First number is %(first)d and second number is %(second)d" % {"first": first, "second": second}


    print("The sum of the elements list  is  %(result)d " % {"result": result})

    #print('The sum of the elements list  is: %d' % result)  # Formatted output (old style)
    #another print way
    #print('The sum of the elements list  is: {:d}'.format(result))  # Formatted output (new style)


def my_min(list):

    min = list[0]

    for item in list:
        if(item < min):
            min=item

    return min


def my_sum(list):
    sum=0

    for item in list:
        sum = item + sum
    return sum

def my_average(list):
    return my_sum(list)/len(list)   #return a float


def guess_number():
    print_hi('3.7 Guess_number ')
    done = False
    trial_number = 0  # number of trials

    while not (done):

        trial_number += 1
        entered_number = (int)(input('Enter your number '))

        if (entered_number == secret_number):
            print('Congratulations you won ')
            print('You got it in {} trials.'.format(trial_number))  # Formatted printing
            done = True

        elif (entered_number > secret_number):
            print('Try lower ')
        else:
            print('Try higher ')

def info_lists():

    print('3.7 Lists ')
    my_list=['apple','oranges','pears','kiwi','grapes']
    print(my_list[1:2])
    print(my_list[:2])
    print(my_list[2:])
    my_list[1]='banana' #substitute the  oranges element with banana
    print(my_list)
    my_list.insert(2,'watermelon')  #insert watermelon as the third element
    print(my_list)
    # the updated list is  = ['apple', 'banana','watermelon','pears','kiwi','grapes']
    my_list.insert(6, 'orange')
    print(my_list)
    # the updated list is  = ['apple', 'banana','watermelon','pears','kiwi','grapes' ,'orange']
    my_list.append('cherry')
    print(my_list)
    # the updated list is  = ['apple', 'banana','watermelon','pears','kiwi','grapes' ,'orange','cherry']

    #Add the elements of the second_list to my_list:
    second_list = ["mango", "pineapple", "papaya"]
    my_list.extend(second_list)
    print(my_list)
    # the updated list is  = ['pears', 'kiwi', 'grapes', 'orange', 'cherry', 'mango', 'pineapple', 'papaya']
    #also not only lists but set can be extended
    set=('kumbulla','mandarina')
    my_list.extend(set)
    print(my_list)
    #the updated list is = ['apple', 'banana', 'watermelon', 'pears', 'kiwi', 'grapes', 'orange', 'cherry', 'mango', 'pineapple', 'papaya',
    # 'kumbulla', 'mandarina']

    #remove specified index
    my_list.pop(1)  #remove banana
    print(my_list)

    #The del keyword also removes the specified index:
    del my_list[0]
    print(my_list)
    #The clear() method empties the list.
    #my_list.clear()


    my_list.insert(0,'apple')
    #updated list =[apple, watermelon ,pears , kiwi , grapes ,  orange , cherry , mango ,  pineapple ,  papaya ,  kumbulla ,   mandarina]

    # loop list

    for index in range(len(my_list)):
        print(my_list[index])

    #list comphrension
    #Based on a list of fruits, you want a new list,containing only the fruits with the letter "o" in the name.
    new_list=[]
    for item in my_list:
        if ("o" in item):
             new_list.append(item)

    print(new_list)

    #With list comprehension you can do all that with only one line of code:
    new_list = [item for item in my_list if "o" in item]
    print(new_list)

    #newlist = [expression for item in iterable if condition == True]
    #The return value is a  new list, leaving the old list unchanged.

    new_list = [ item for item in my_list if item != 'apple' ]
    print(new_list)

    #The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome:
    new_list = [item if item != "banana" else "orange" for item in my_list] #substitute the banana with orange
    print(new_list)

    my_list.sort() #sort the list alphabetically .
    print(my_list)
    my_list.sort(reverse=True) # sort in the inverse mode
    print(my_list)


    #my_list.reverse()  #reverse the list elements
    #print(my_list)

    #Copy lists
    #if we did  list2 = my_list the changes made in my_list will automatically also be made in list2.
    #so we have to use copy()
    list2=[]
    list2=my_list.copy()
    print(list2)

    #Join 2 lists
    list3=[1,2,3]
    print(my_list + list3)
    return 0


def guess_number():

        done = False
        trial_number = 0  # number of trials

        while not (done):

            trial_number += 1
            entered_number = (int)(input('Enter your number '))

            if (entered_number == secret_number):
                print('congratulations you won ')
                print('You got it in {} trials.'.format(trial_number))  # Formatted printing
                done = True

            elif (entered_number > secret_number):
                print('Try lower ')
            else:
                print('Try higher ')


def fill_list():

    # Create an initial empty list for grades to receive from input
    grade_list = []

    grade = int(input('Enter a valid grade between 0 and 100 (or -1 to end )'))

    while (grade != -1):

        if (0 <= grade <= 100):
            grade_list.append(grade)
        else:
            print('invalid grade , try again ')
        grade = int(input('Enter a valid grade between 0 and 100 (or -1 to end )'))

    if len(grade_list):
        result = my_sum(grade_list)
        print_sum(result)
        print('The average  of the elements list  is: %.2f' % my_average(grade_list))  # Formatted output (old style)
        # another printing  way
        # print('The average  of the elements list  is: {:.2f}'.format(my_average(grade_list)))  # Formatted output (new style)

    return


def info_tuples():
    print_hi('3.7 Touples ')
    my_tuple = ("Apple", "Banana", "Cherry")

    #Tuples  are ordered, it means that the items have a defined order, and that order will not change.
    #Tuples are unchangeable, meaning that we cannot  change, add or remove items after  the tuple has  been created.
    #Touples allow dublicate values

    print(my_tuple)
    # It's possible to specify a range of indexes by specifying where to start and where to end the range.
    print(my_tuple[1:2])
    print(my_tuple[:2])
    print(my_tuple[2:])

    #To determine if a specified  item is present in a tuple use the in keyword:
    if "Apple" in my_tuple:
       print ("item is present ")

    #Due to the fact the touple is unchangeable and immutable It's possible to convert a touple in list and also a list in touple
    #in this way we can add or change elements and then convert it again in touple
    converted_list=list(my_tuple)
    converted_list.insert(3,"kiwi")
    my_tuple = tuple(converted_list)
    print(converted_list)
    print(my_tuple)

    #Idem for  removing an item from the tuple Tuples are unchangeable, so it's not possible to remove items from it
    #convert the touple in list and then again convert in tuple
    converted_list.remove("kiwi")
    print(converted_list)
    my_tuple = tuple(converted_list)
    print(my_tuple)
    #The del keyword can delete the tuple completely
    #del my_touple

    #It's  allowed to extract the values back into variables. This is called "unpacking":

    (variable1, variable2, variable3) = my_tuple

    print(variable1)  #variable1 =Apple
    print(variable2)  #variable2 =Banana
    print(variable3)  #variable3 =Cherry

    #If the number of variables is less than the number of values,you can
    #add an * to the variable name and the values will be assigned to the
    #variable as a list:

    fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
    (variable1, variable2, *variable3) = fruits

    print(variable1)  # variable1 =apple
    print(variable2)  # variable2 =banana
    print(variable3)  # variable3 = ["cherry", "strawberry", "raspberry"]

    #If the asterix is added to another variable name than the last, python will assign  values to
    #the variable until the  number  of  values  left matches  the  number  of variables left.

    fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
    (variable1, *variable2, variable3) = fruits

    print(variable1)  # variable1 = apple
    print(variable2)  # variable2 = ["banana", "cherry", "strawberry"]
    print(variable3)  # variable3 = raspberry

    #To join one or more tuples is used the + operator
    tuple1 = ("a", "b", "c")
    tuple2 = (1, 2, 3)
    tuple3 = tuple1 + tuple2
    print(tuple3)
    #It's possible to multiply the tuple by a number of times using the  * operator
    tuple1 = ("a", "b", "c")
    print(tuple1 * 2)
    tuple4 = tuple3 * 2
    #The methoud count() return the number of times the specific value appears in the tuple:
    print(tuple4.count("b"))

    #Index method
    #Search for the first occurrence of the value "b"  and return its position:
    print(tuple4.index("b"))
    return 0


def info_sets():
    #Sets are  used to store multiple  items in a single  variable.
    #Duplicate values will be ignored:
    #Set items are unordered, unchangeable, and do not allow duplicate values.
    #Once a set is created,you cannot change its items, but you can add new items.
    #It's not possible to access items in a set by referring  to an  index or a  key.

    my_set = {"apple", "banana", "cherry"}
    for x in my_set:
        print(x)

    #Check if "banana" is present in the set:
    print('banana' in my_set)

    #Once a set is created, it's not possible to change its items,but we can add new items.
    my_set.add("kiwi")
    print(my_set)

    #To add items from another set into the current set,use the update() method.

    my_set1 = {"apple", "banana", "cherry"}
    my_set2 = {"pineapple", "mango", "papaya"}

    my_set1.update(my_set2)
    print(my_set1)

    #The object in the update() method does not have to be only a set but
    #it can be any iterable object(tuples,lists,dictionaries et,).

    mylist = ["kiwi", "orange"]

    my_set1.update(mylist)
    print(my_set1)

    #To remove an item in a set,use the remove(), or the discard() method.
    my_set1.remove('kiwi')
    print(my_set1)

    #The clear() method empty the set .
    #The del() method delete the set

    #You can use the union() method  that returns a  new  set containing all items from both sets, or the
    #update()  method  that  inserts  all  the items from one set into another:

    set1 = {"a", "b", "c"}
    set2 = {1, 2, 3}

    set3 = set1.union(set2)
    print(set3)

    set1.update(set2)
    print(set1)

    #The intersection_update()  method will keep only the  items  that are  present in both sets
    x = {"apple", "banana", "cherry"}
    y = {"google", "microsoft", "apple"}
    x.intersection_update(y)
    print(x)

    #The symmetric_difference_update() method will  keep only the elements that are NOT present in both sets .

    x = {"apple", "banana", "cherry"}
    y = {"google", "microsoft", "apple"}
    #x.symmetric_difference_update(y)
    #print(x)
    #The symmetric_difference() method will return a new set,that contains only the elements
    #that are NOT present in both sets.

    z=x.symmetric_difference(y)
    print(z)

    #difference() method
    #Return a set that contains the items that only exist in set x, and not in set y:

    x = { 1, 2, 3, 4}
    y = { 5, 6, 3, 8}
    #z = x.difference(y)
    #print(z) # 1,2,4

    #symmetric_difference() method
    #Return a set that contains all items from both sets, except items that are present in both sets:

    #z = x.symmetric_difference(y)

    #print(z)  # 1,2,4 ,5,6,8

    #Remove the items that exist in both sets:
    #x.difference_update(y)
    #print(x)

    #issubset() method
    #Return True if all items set x are present in set y:
    x = {"a", "b", "c"}
    y = {"f", "e", "d", "c", "b", "a"}
    z = x.issubset(y)
    print(z)

    return 0

def info_dictionaries():
    #Dictionaries are used to store data values in key:value pairs.
    #A dictionary is a collection which is ordered, changeable and does not allow duplicates.

    my_dictionary={
                     "gender": "male",
                     "city" :"Milano",
                     "matricola":"458796",
                     "electric": False,
                     "year": 1964,
                     "colors": ["red", "white", "blue"]
                  }
    print(my_dictionary)
    #Dictionaries are defined as objects with the data type 'dict':
    print(type(my_dictionary))  # <class 'dict'>
    #Can access the items of a dictionary by referring to its key name, inside square brackets:
    #A method called get() will give the same result:
    print(my_dictionary['gender'])
    #print(my_dictionary.get('gender'))

    #The keys() method will return a list of all the keys in the dictionary.
    print(my_dictionary.keys())
    #Add new item
    my_dictionary['country'] = 'Italia'
    print(my_dictionary)
    #Change the value of a specific item by referring to its key name:
    #my_dictionary.update({'country' : 'Germania'})
    #print(my_dictionary)

    #my_dictionary['country'] = 'Germania'
    #print(my_dictionary)
    #The pop() method removes the item with the specified key name:

    #my_dictionary.pop('country')
    #print(my_dictionary)

    my_dictionary['country'] = 'Germania'
    print(my_dictionary)

    #The clear() method empties the dictionary:

    #Loop dictionaries
    # print all keys
    # It is possible to use the keys() method to return the keys of a dictionary:
    for x in my_dictionary:
        print(x)
    for x in my_dictionary.keys():
        print(x)

    # print all values
    for x in my_dictionary:
        print(my_dictionary[x])

    #It is also possible to  use the values() method to return values of a dictionary:
    for x in my_dictionary.values():
        print(x)

   #Loop through both keys and values, by using the items() method:
    for x, y in my_dictionary.items():
        print(x, y)

    #Make a copy of a dictionary with the copy() method:
    mydict2 = my_dictionary.copy()
    print(mydict2)

    #A dictionary can contain dictionaries, this is called nested dictionaries.

    myfamily = {
        "child1": {
            "name": "Emil",
            "year": 2004
        },
        "child2": {
            "name": "Tobias",
            "year": 2007
        },
        "child3": {
            "operating_system": "Linux",
            "year": 2011
        }
    }

    print(myfamily['child3'])
    print(myfamily['child3']['year'])

    #From keys return a dictionary with the specified keys and values
    x = ('country')
    my_dict = my_dictionary.fromkeys(x)
    print(my_dict)
    print(my_dictionary)

    return 0


def info_loops():

    #break statement can stop the loop before it has looped through all teh item

    fruits=["apple","orange","kiwi","grapes"]
    for item in fruits:
        if item=="kiwi":
           break
        print(item)

    #Exit the loop when the cycle reached the desired kiwi
    for item in fruits:
        print(item)
        if item=="kiwi":
           break
    #continue, we can stop the current iteration and then continue to the next
    for item in fruits:
        if item=="kiwi":
           continue
        print(item)

    #The range() function returns a sequence of numbers,
    #starting from 0 by default, and increments by 1 (by default), and ends at a specified number.

    for x in range(2,6):
        print(x)

    for x in range(6):
        if x == 3: break
        print(x)
    else:
        print("Finally finished!")

    #The range() function defaults to increment the sequence by 1, however it is possible to specify the
    #increment value by adding a third parameter: range(2, 30, 3):
    for x in range(2,30,3):
        print(x)

    #A nested loop is a loop inside a loop.
    #The "inner loop" will be executed one time for each iteration of the "outer loop":

    adj = ["red", "big", "tasty"]
    fruits = ["apple", "banana", "cherry"]

    for x in adj:
        for y in fruits:
            print(x,y)

    #for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass
    #statement to avoid getting an error.

    for x in [0,1,2]:
        pass

    #Arbitrary arguments , *args


    return 0

def info_functions():
    #If it is not knowed how many arguments that will be passed into your function,
    #we can add a * before the parameter name in the function definition.
    #This way the function will receive a tuple of arguments, and can access the items accordingly:

    def my_function(*kids):
            print("The youngest child is " + kids[2])

    def my_function2(*kids):
        for item in range(len(kids)):
            print (kids[item])

    my_function("Emil", "Tobias", "Linus")
    my_function2("Emil", "Tobias", "Linus")

    # If It is not knowed how many keyword arguments  will be passed into
    # the function, add two asterisk: ** before the parameter name in the function definition.
    # This way the function will receive a dictionary of arguments, and can access the items accordingly:

    def my_function3(**kids):
            print("the last name is "  + kids["lname"])

    my_function3(name="pluto",lname="pippo")

    #default argument
    def my_function4(country="Germania"):
            print("I came from " + country)

    my_function4('ITALIA')
    my_function4()

    #Pass stamement .Used in case for some reasons we have a functions without a content
    def my_function5():
            pass

    #recursive function

    def tri_recursion(k):
        if (k > 0):
            result = k + tri_recursion(k - 1)
            print(result)
        else:
            result = 0
        return result

    print("\n\nRecursion Example Results")
    tri_recursion(6)

    def function1():  # outer function
        print("Hello from outer function")

        def function2():  # inner function
            print("Hello from inner function")

        function2()

    function1()

    #Note if we are calling the method first_child without the parentheses. Recall in this way means that the
    #returning is a  reference to the function first_child.
    #If the  first_child() is called with   parentheses then it refers to the result of evaluating the function.
    #This can be seen in the following example:


    def parent(num):

        def first_child():
            return "Hi, I am Emma"

        def second_child():
            return "Call me Liam"

        if num == 1:
            return first_child
        else:
            return second_child

    first = parent(1)
    first()

    print("\n")


    #decorators
    def my_decorator(func):
        def wrapper():
            print("Something is happening before the function is called.")
            func()
            print("Something is happening after the function is called.")

        return wrapper

    @my_decorator
    def say_whee():
        print("Whee!")

    output_here = my_decorator(say_whee)
    output_here()

    print("\n")

    def my_decorator(func):
        def wrapper():
            print("Something is happening before the function is called.")
            func()
            print("Something is happening after the function is called.")

        return wrapper

    @my_decorator
    def say_whee():
        print("Whee!")

    say_whee()


#Classes
#The self parameter is a reference to the current instance of the class, and is used to access variables
#that belongs to the class.
#It does not have to be named self , you can call it whatever you like,
#but it has to be the first parameter of any function in the class:

class Person:

    def __init__(self, name, surname):
        self.first_name=name
        self.last_name=surname

    def printName(self):
        print("The name is " + self.first_name)

    def printSurname(self):
        print("The name is " + self.last_name)

    def welcome(self):
        print("Welcome", self.first_name, self.last_name)


#Inheritances
#Create a class called Student, which will inherit the properties and methods from the Person class:

#class Student(Person):
#    def __init__(self, fname, lname):
#        self.first_name = fname
#        self.last_name = lname


#class Student(Person):
#    def __init__(self, name, surname):
#        Person.__init__(self, name, surname)

#Or by super() method we can inherit  al the methods nd proprieties of the father
#By using the super() function it's  not neccessary to use the name of the parent element,
#it will automatically inherit the methods and properties from its parent.

class Student(Person):
  def __init__(self, fname,lname,year):
    super().__init__(fname, lname)
    self.graduation_year = year

  def welcome(self):
      print("Welcome", self.first_name, self.last_name, "to the class of", self.graduation_year)


#Also it's possible to add a new variable in the student in the above ex called year
#If It's added a new  method in the child class with the same name as a
#function in the parent class, the inheritance of the parent method will be overridden just as happens for the welcome
#method above

#Iterators

class MyRange:
    def __init__(self,start,end):
        self.value=start
        self.end=end

    def __iter__(self):
        return self

    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current=self.value
        self.value += 1
        return current

def main():

    #fill_list()
    #guess_number()
    #info_lists()
    #info_tuples()
    #info_sets()
    #info_dictionaries()
    #info_loops()
    #info_database()

    info_functions()

    person1=Person('Person_Leonard','37')
    person1.printName()
    person1.welcome()

    student1 = Student('Student_Olsi','39',1983)
    student1.printName()
    student1.welcome()
    range=MyRange(1,6)

    print(next(range))
    print(next(range))

    print(range.__next__())
    print(range.__next__())

    #The lists , dictionaries, touples are all iterable objects
    #All these are iterable objects. They are iterable containers which we  can get an iterator from them
    my_tuple = ("apple", "banana", "cherry")
    my_list = ['apple', 'oranges', 'pears', 'kiwi', 'grapes']
    my_dictionary = {
        "gender": "male",
        "city": "Milano",
        "matricola": "458796",
        "electric": False,
        "year": 1964,
        "colors": ["red", "white", "blue"]
    }

    my_iterator_tuple = iter(my_tuple)

    my_iterator_list  = iter(my_list)
    my_iterator_list = my_list.__iter__()

    #my_iterator_dictionary = iter(my_dictionary)
    my_iterator_dictionary = my_dictionary.__iter__()

    print(next(my_iterator_tuple))
    print(next(my_iterator_tuple))
    print(next(my_iterator_tuple))

    print(next(my_iterator_list))
    print(next(my_iterator_list))
    print(next(my_iterator_list))

    print(next(my_iterator_dictionary))
    print(next(my_iterator_dictionary))
    print(next(my_iterator_dictionary))

    class MyNumbers:
        def __iter__(self):
            self.a = 1
            return self

        def __next__(self):
            x = self.a
            self.a += 1
            return x

    myclass = MyNumbers()
    myiter = iter(myclass)
    #myiter = myclass.__iter__()

    print(next(myiter))
    print(next(myiter))
    print(next(myiter))
    print(next(myiter))
    print(next(myiter))
    #To prevent the iteration to go on forever, we can use the StopIteration statement.
    #stop after 20 iterations

    class MyNumbers:
        def __iter__(self):
            self.a = 1
            return self

        def __next__(self):
            if self.a <= 20:
                x = self.a
                self.a += 1
                return x
            else:
                raise StopIteration

    myclass = MyNumbers()
    myiter = iter(myclass)

    for x in myiter:
        print(x)




# Run the main function .
if __name__ == '__main__':
    main()


