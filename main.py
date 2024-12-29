#creating the tuple
my_fruits=("apple","blueberry","strawberry")
print(my_fruits)
#accessing a value from the tuple
fruit=my_fruits[2]
print("My favorite fruit is ",fruit)
#packing in tuples
my_sent=("Hi","my","name","is","Harshita")
for sent in my_sent:
    print(sent, end = " ")
#unpacking in tuples
my_fam=("Supriya","Prasad","Anjana","Harshita")
mom,dad,sister,me=my_fam
print()
print("Mom's name is: ",mom)
print("Dad's name is: ",dad)
print("Sister's name is: ",sister)
print("My name is: ",me)
#tuple without brackets
my_tuple="cat","dog","fish"
print(my_tuple)
#creating a nested tuple
my_pets=("dog","cat","fish",("robert","maui","alfonso"))
fav=my_pets[2]
name=my_pets[3][2]
print("My favorite pet is my ",fav,". It's name is ",name)
#slicing a tuple
my_clothes=("shorts","pants","shirts","sweatshirts","hoodies","shoes")
clothes=my_clothes[1:3]
print(clothes)
cloth=my_clothes[1:]
print(cloth)
#accessing all elements from a tuple with slicing
first=my_clothes[:]
print(first)
