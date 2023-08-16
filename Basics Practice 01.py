print("Hello")
print('"This is Srija"')
#Printing in differnt ways

a = "Welcome to my World"
print(a)
#Assigning string to variable and printing it

a = """Hope you are doin good!!,
Hello from Srija."""
print(a)
#Printing by using three double quotes

a = "Hello, Srija!"
print(a[8])
#Getting a charecter by postion

for x in "\nWelcome":
  print(x)
#Looping charecters

a = "Hello, Srija!"
print(len(a))
#Returning Length of a string

txt = "The best things in life are free!"
print("free" in txt)
#Checking free is present in following text

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
#Printing if the txt is present

txt = "The best things in life are free!"
print("expensive" not in txt)
#Checking the string and returning boolean output

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
#Checking and printing the statement 

b = "Hello, Srija!"
print(b[2:5])
#Getting charecters from particular position

b = "Hello, Srija"
print(b[:5])
#Getting charecters from start index to particular position

b = "Hello, Srija!"
print(b[2:])
#Getting charecters from particular position to end

b = "Hello, Srija!"
print(b[-5:-2])
#Negative indexing
#Getting charecters from end of the string

a = "Srija!"
print(a.upper())
#Converting existing string to upper case

a = "Srija!"
print(a.lower())
#Converting existing string to lower case

a = " Hello, Srija! "
print(a.strip()) # returns "Hello, World!"
#Removes spaces at the beginning and or at end of the string

a = "Hello, Srija!"
print(a.replace("H", "J"))
#Replaces charecter in a particular string

a = "Hello, Srija!"
b = a.split(",")
print(b)
#Splitting into substrings

a = "Hello"
b = "Srija"
c = a + b
print(c)
#Merging variables by concatenating

a = "Hello"
b = "Srija"
c = a + " " + b
print(c)
#Adding space by using Concatenation

age = 26
txt = "My name is Srija, and I am {}"
print(txt.format(age))
#Format method for inserting numbers into strings with the help of placeholder

quantity = 6
itemno = 356
price = 84.29
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
#Format method adding number of arguments with the help of placeholders

quantity = 6
itemno = 356
price = 84.29
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
#Format method adding arguments by using index and making sure that it is placed in correct placeholders

txt = "We are the so-called \"Vikings\" from the north."
#Escape charecter that helps to use double quotes

txt = 'It\'s alright.'
print(txt)
#Escape charecter that helps to use single quotes

txt = "This will insert one \\ (backslash)."
print(txt)
#Escape charecter that helps to use backslash

txt = "Hello\nWorld!"
print(txt)
#Escape charecter that helps enter in a newline

txt = "Hello\tWorld!"
print(txt)
#Escape charecter that helps enter tab space

txt = "Hello \bWorld!"
print(txt)
#Escape charecter that helps backspacing

txt = "\110\145\154\154\157"
print(txt)
#converting octal value into string

txt = "\x45\x55\x5c\x5c\x5f"
print(txt)
#converting hexal value intring

txt = "hello, and welcome to my world."
x = txt.capitalize()
print (x)
#Converts the first character to upper case

txt = "Hello, And Welcome To My World!"
x = txt.casefold()
print(x)
#Converts the first character to lower case

txt = "banana"
x = txt.center(50)
print(x)
#Returns a centered string

txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)
#Returns the number of times a specified value occurs in a string

txt = "My name is Bråndon"
x = txt.encode()
print(x)
#Returns encoded version of string

txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(x)
#Returns true if the string ends with the specified value

txt = "H\te\tl\tl\to"
x =  txt.expandtabs(2)
print(x)
#Sets the tab size of the string

txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)
#Searches the string for a specified value and returns the position of where it was found

txt = "For only {price:.2f} dollars!"
print(txt.format(price = 55))
#Formats specified values in a string

#format_map()	

txt = "Hello, welcome to my world."
x = txt.index("welcome")
print(x)
#Searches the string for a specified value and returns the position of where it was found

xt = "Company12"
x = txt.isalnum()
print(x)
#Returns True if all characters in the string are alphanumeric

txt = "CompanyX"
x = txt.isalpha()
print(x)
#Returns True if all characters in the string are in the alphabet

txt = "Company123"
x = txt.isascii()
print(x)
#Returns True if all characters in the string are ascii characters

txt = "1234"
x = txt.isdecimal()
print(x)
#doubt

txt = "50800"
x = txt.isdigit()
print(x)
#Returns True if all characters in the string are digits

txt = "Demo"
x = txt.isidentifier()
print(x)
#Returns True if the string is an identifier

txt = "hello world!"
x = txt.islower()
print(x)
#Returns True if all characters in the string are lower case

txt = "565543"
x = txt.isnumeric()
print(x)
#Returns True if all characters in the string are numeric

txt = "Hello! Are you #1?"
x = txt.isprintable()
print(x)
#Returns True if all characters in the string are printable

txt = "   "
x = txt.isspace()
print(x)
#Returns True if all characters in the string are whitespaces

txt = "Hello, And Welcome To My World!"
x = txt.istitle()
print(x)
#Returns True if the string follows the rules of a title

txt = "THIS IS NOW!"
x = txt.isupper()
print(x)
#Returns True if all characters in the string are upper case

myTuple = ("John", "Peter", "Ram")
x = "".join(myTuple)
print(x)
#Joins the elements of an iterable to the end of the string

txt = "banana"
x = txt.ljust(20)
print(x, "is my favorite fruit.")
#Returns a left justified version of the string

txt = "Hello my FRIENDS"
x = txt.lower()
print(x)
#Converts a string into lower case

txt = "     banana     "
x = txt.lstrip()
print("of all fruits", x, "is my favorite")
#Returns a left trim version of the string

txt = "Hello Sam!"
mytable = str.maketrans("S", "P")
print(txt.translate(mytable))
#Returns a translation table to be used in translations

txt = "I could eat bananas all day"
x = txt.partition("bananas")
print(x)
#Returns a tuple where the string is parted into three parts

txt = "I like bananas"
x = txt.replace("bananas", "apples")
print(x)
#Returns a string where a specified value is replaced with a specified value

txt = "Mi casa, su casa."
x = txt.rfind("casa")
print(x)
#Searches the string for a specified value and returns the last position of where it was found

txt = "Mi casa, su casa."
x = txt.rindex("casa")
print(x)
#Searches the string for a specified value and returns the last position of where it was found

txt = "banana"
x = txt.rjust(20)
print(x, "is my favorite fruit.")
#Returns a right justified version of the string

txt = "I could eat bananas all day, bananas are my favorite fruit"
x = txt.rpartition("bananas")
print(x)
#Returns a tuple where the string is parted into three parts

txt = "apple, banana, cherry"
x = txt.rsplit(", ")
print(x)
#Splits the string at the specified separator, and returns a list

txt = "     banana     "
x = txt.rstrip()
print("of all fruits", x, "is my favorite")
#Returns a right trim version of the string

txt = "welcome to the jungle"
x = txt.split()
print(x)
#Splits the string at the specified separator, and returns a list

txt = "Thank you for the music\nWelcome to the jungle"
x = txt.splitlines()
print(x)
#Splits the string at line breaks and returns a list

txt = "Hello, welcome to my world."
x = txt.startswith("Hello")
print(x)
#Returns true if the string starts with the specified value

txt = "     banana     "
x = txt.strip()
print("of all fruits", x, "is my favorite")
#Returns a trimmed version of the string

txt = "Hello My Name Is PETER"
x = txt.swapcase()
print(x)
#Swaps cases, lower case becomes upper case and vice versa

txt = "Welcome to my world"
x = txt.title()
print(x)
#Converts the first character of each word to upper case

mydict = {83:  80}
txt = "Hello Sam!"
print(txt.translate(mydict))
#Returns a translated string(ascii codes)

txt = "Hello my friends"
x = txt.upper()
print(x)
#Converts a string into upper case

txt = "50"
x = txt.zfill(10)
print(x)
#Fills the string with a specified number of 0 values at the beginning

thislist = ["Volvo", "Bmw", "Lamborgini",]
print(thislist)
#Printing Lists

thislist = ["Volvo", "Bmw", "Lamborgini","Volvo"]
print(thislist)
#List allows duplicates
print(len(thislist))
#Printing number of items in list

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
print(list1)
print(list2)
print(list3)
#List can store different types of datatypes

list1 = ["abc", 34, True, 40, "male"]
print(list1)
#Can store different datatypes in a single list

mylist = ["apple", "banana", "cherry"]
print(type(mylist))
#Type of datatype of a list

thislist = list(("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")) # note the double round-brackets
print(thislist)
#Using list constructor
print(thislist[1])
#Printing items in the list by index values
print(thislist[-1])
#Printing items in the list by index values(negative index which starts from right to left)
print(thislist[2:5])
#Printing range of items
print(thislist[:4])
#Printing range of items
print(thislist[2:])
#Printing range of items
print(thislist[-4:-1])
#Printing range of items
if "apple" in thislist:
 print("Yes, 'apple' is in the fruits list")
#Checking whether the item is there in the list or not

thislist[1] = "blackcurrant"
print(thislist)
#Replacing an item in the list

thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
#Replacing range of items in the list

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)
#changing values by replacing with new values

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
#Inserting values to the list  with the help of index

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
#Append adds the value to the list at the end

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
#Combining two lists

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
#removing items in the list 

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
#Removes last element in the list

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
#Removes element in the list with reference of index

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
#Removes first element in the list

thislist = ["apple", "banana", "cherry"]
del thislist
#del keyword can also delete the list completely

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
#Clears the list content

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
#Printing items one by one  

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
#Printing items with reference to index number

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
#Printing using while loop

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
#shorthand for printing

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)
#checking whether that charecter is there in the string
newlist = [x for x in fruits if x != "apple"]
print(newlist)
#Only accepts items that are not "apple"

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits]
print(newlist)
#No if statement

newlist = [x for x in range(10)]
print(newlist)
#Printing number for the range of 9

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]
print(newlist)
#Converting list of items into uppercase

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = ['hello' for x in fruits]
print(newlist)
#Set all values in the new list to 'hello'

newlist = [x if x != "banana" else "orange" for x in fruits]
#set all values in the new list to 'hello'

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)
#Replacing banana with orange

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
#Sorting list in order

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
#Sorting lists numerically

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)
#sorting and printing in reverse order

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)
#sorting and printing in reverse order

def myfunc(n):
  return abs(n - 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)
#Sort the list based on how close the number is to 50

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)
#Case sensitivity sorting

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)
#Converting the list of strings into lower case

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)
#Prints the List in reverse order

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()  #mylist = list(thislist) #alternative
print(mylist)
#Copying the list

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)
#Joining lists

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
print(list1)
#Joining lists

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)
#Joining lists

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)
#Altering in tuple

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
#Another way of altering tuple

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)
#Create a new tuple with the value "orange", and add that tuple:

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
#Removing item in tuple

# thistuple = ("apple", "banana", "cherry")
# del thistuple
# print(thistuple) #this will raise an error because the tuple no longer exists
# #deletion of tuple

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)
#Unpacking tuples

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
#Looping tuples

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])
#Printing all with respect to index

thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1
#Printing all using while loop

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)
#Join two tuples

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)
#Multiplying tuples

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(5)
print(x)
#Return the number of times the value 5 appears in the tuple

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.index(8)
print(x)
#getting index of element in tuple





