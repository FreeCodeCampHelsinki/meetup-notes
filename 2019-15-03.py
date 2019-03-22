"""15.march.2019.--NOTES--.Python_lessons.
Today we will talk about a set. they are unique, in a set you can not guarantee a order
to create a set for example:
"""
mySet = {'Giovanni', 'Tero', 'Lars', 'Vullnet'} 
#otherSet = {} you can leave like this if you want. 
#print(mySet)
mySet.add('Jemal')
mySet.add('Tero') # will be only one time, they are unique values. 
myList = list(mySet) # creates new list,so we can order the values on the set. 
myList.sort() # set doesnt have a sort function/ 
# print(mySet)
print(len(myList)) # it will count the numbers of items in a container. 
#print(myList)
print('__'*50) # it puts line 50 times.
# to write a dictionary you write something like this:
myDictionary = {'key':'value', 'name':'Tiki'} # it is same as set also:
#myDicitionary = dics()
# dictinaries can contain anything. 
countries = {
    'fi':'Finland'
    ,'my':{'name':'Malaysia', 'population':300000000, 'land_mass':3000000}
    ,'it':'Italy'
    ,'al':'Albania'
    ,'de':'Germany'
    ,'au':'Australia'
    ,'ja': 'Jamaica'
    ,'ua': 'Ukraine'
    ,'ru': 'Russia'
    ,'et':'Ethiopia'
} # it is used as a random list. It can be a int or str, it can be a tuple. 
print(countries['my']['name']) # to find the value. 
print(countries.get('cn','Country not found')) # it doesnt throw an error but shows that didnt find the value. 
# for sets you can add to the set. for dictionaries you can append. 
countries['cn'] = 'China' # just create a key to add an element 

countries[''] = 'People\'s Republic of China' # to modify

del countries['my'] #to delete a key. 

"""for tuples we used only ()
you cant leave a set empty, because it becames a dictionary
"""
""" There are some other things about sets when go dipper """
# Generators are super fun and super efficient and cheap. it is used everywhere in python. 

# Tiki explained for: Flow control,  if statements and while loop, how they work 
# Relational operators are six: ==same as, != not same as, >more than, <less than, <=less than or equal, >=more than or equal. 
# in python is resolved left to write. 
""" Logical Operators: and, or not. 
 tab is important in python.

"""
x = 50
y = 11
if x != y and (x <10 or y > 100): 
    print('Thank you')
elif x >0:
    print("I don't know")
    print("Blah!")
    if x==50:
        print("hahhaha") # is part of elif (it is nested if)
# elif has to be between if and else.
    elif x  == 100: 
        print("Wow! that's big") 
else: 
    print("Ei kiitos")

#python doesnt have a switch statment like other programming languages.  
# short for else if. 
# nest week we will do the loops. Congratulations you survived part4. 
