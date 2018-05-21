#INDENTIONS AND PRINTS ARE COMMENTED OUT, UNCOMMENT TO TEST ANY SNIPPET

##BASICS

###############VARIABLES/STRINGS#######################
print("hello world!")

msg = "hello world!"
#print(msg)

firstName = 'Ben'
lastName = 'Mercer'
fullName = firstName + " " + lastName
#print(fullName)

#################################LISTS##################################
#make list
bikes = ['trek', 'redline', 'giant']
#print(bikes)

#get first/last item
firstBike = bikes[0]
lastBike = bikes[-1]
#print firstBike, lastBike

#loop a list
#for bike in bikes:
    #print bike

#add item to list
bikes.append('schwinn')

#numerical list
squares = []
for x in range(1, 11):
    squares.append(x**2)
#print squares

#list loop rewritten
squares = [x**2 for x in range(1, 11)]
#print squares

#slice list
finishers = ['bob', 'sam', 'ben', 'sue', 'joe']
first_two = finishers[:2]
#print first_two

#copy list
copyOfFinishers = finishers[:]
#print copyOfFinishers

#TOUPLES- items can't be modified
dimensions = (980, 1080)
#print dimensions

##################IF STATEMENTS###############################
#Conditional Tests with lists
listTest = 'trek' in bikes
listTest2 = 'surly' not in bikes
#print listTest, listTest2

#assign boolean values
testActive = True
canEdit = False

#simple test
#if age >= 18:
    #print("you can vote!")

#if elif statements
age = 0
if age < 4:
    ticketPrice = 0
elif age < 18:
    ticketPrice = 10
else:
    ticketPrice = 15

##################DICTIONARIES###############################
#-store connections between peices of information
#simple ex
alien = {'color': 'green', 'hp': 5}
#print alien

#access a value
ac = alien['color']
#print("the alien's color is " + alien['color'])

#adding new key-value pair
alien['x_position'] = 0

#looping through key-value pairs
favNumbers = {'eric': 17, 'ben': 12}
#for name, number in favNumbers.items():
    #print name + "'s fav number is " + str(number)

##################USER INPUT############################
#prompting for a value
#name = input("What's your name with quotes ?")
#print("Hello, " + name + "!")

#prompting for numerical input
#age = input("how old are you? ")
#age = int(age)

#pi = input("what's the value of pi? ")
#pi = float(pi)
