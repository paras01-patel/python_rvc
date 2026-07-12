'''
1.what is leterals ?
ans .A literal is a fixed value that is written directly in the source code.
    
    Hinglish:
        Literal woh fixed (constant) value hoti hai jo hum program me directly likhte hain.
        
        exmples:- name='paras'    , age =20   , pi =3.14     ,is_student = True
            
                    "Paras" → String Literal
                    20 → Integer Literal
                    3.14 → Float Literal
                    True → Boolean Literal
                    
                    
Types of leterals

1.Numeric Leterals  :- Numbers ko represent karte hain.
    there are three types
        a = 10        # Integer
        b = 3.14      # Float
        c = 2 + 3j    # Complex
        print(type(a))
        print(type(b))
        print(type(c))
        
2. String Literals:-Text ko represent karte hain.
        name = "Paras"    # single line string
        city = 'Bhopal'   # single line string

Most Important String Methods (Interview)

upper()	                    Uppercase
lower()	                    Lowercase
title()	                    Every word ka first letter capital
capitalize()	            Sirf first letter capital
strip()	                    Extra spaces remove
replace()	                Replace text
split()	                    String → List
find()	                    Position find
count()	                    Count characters
startswith()	            Starting check
endswith()	                Ending check
len()	                    String ki length        

Ex:-

p='wellcome to cybrom'
print(len(p))
print(type(p))
print(p.lower())
print(p.upper())
print(p.find('e'))
print(p.title())
print(p.capitalize())
print(p.replace('wellcome','paras'))
print(p.startswith('we'))
print(p.endswith('cybr'))
print(p.split())
print(p.count())

3. Boolean Literals
Sirf do values hoti hain.        

    x = True
    y = False
    
    
4.lists :- A List is an ordered, mutable (changeable) collection that can store multiple values of different data types.
Method 

number=[1,2,3,4,3,73,5,6]
number2=[7,8,9,10]
#number.append(7)               # last me elemet add karta hai
#number.insert(0,0)             # list me kabhi bhi element add kr sakte hai iski indwxing 0 se start hoti hai 
#number.extend(number2)         # do list ko jodhta hai
#umber.remove(7)                # list me se remove karta hai or ek bar me hi element ko remove kar sakta hai .
#number.pop(0)                  # kist se remove karta hai element indexing ke hisab se or return bhi karta hai remove value 
# number.clear()                # puri list empty kar deta hai 
#number.sort()                  #list ko sort karta hai ascending me 
#number.sort(reverse=True)      # list ko descending me sort karta hai 
#number.reverse()               # ye list ko ulta karti hai 
#print(number.count(3))         # ye list me count karta hai ki element ktine bar aaaya hai 
#print(number.index(6))         # list me indexing batata hai ki kaha pe hai
l=number.copy()                # list ko copy karta hai 
print(l,number)


# pop() aur remove() dono list se element delete karte hain, lekin dono ka use alag hai.

# remove()	                                        pop()

# Value ke basis par delete karta hai.	              Index ke basis par delete karta hai.
# Removed value return nahi karta.	                  Removed value return karta hai.
# Agar value na mile to ValueError aata hai.	      Agar index galat ho to IndexError aata hai.




Tuple :-

A tuple is an ordered, immutable collection of elements in Python. It can store different data types and allows duplicate values.
Example :-
            method 
tup=(1,2,3,4,5)
print(type(tup))
print(tup.count(5))    # count tuple me ke element kitni bar aaya hai ye batata hai 
print(tup.index(5))    # index tuple kisi particular index batata hai indexing 0 se start hoti hai

IN build-Fuctions


Function	                    Kaam

len(t)	                        Total elements
max(t)	                        Sabse badi value
min(t)	                        Sabse chhoti value
sum(t)	                        Total sum (numeric tuple)
sorted(t)	                    Sorted list return karta hai
type(t)	                        Data type batata hai
tuple()	                        Tuple create karta hai
list(t)	                        Tuple ko list me convert karta hai
any(t)	                        Koi ek value True ho to True
all(t)	                        Sab values True ho to True
reversed(t)	                    Reverse iterator deta hai
enumerate(t)                	Index ke saath elements deta hai 


Dictionary (dict)

A dictionary is a mutable collection of data that stores values in key-value pairs. It is created using curly braces {}.



student = {"name": "Paras", "age": 21}
print(student.get("name"))                      #Kisi key ki value return karta hai. Agar key na mile to error nahi deta.
print(student.keys())                           #Dictionary ki sabhi keys return karta hai.
print(student.values())                         #sari value retrun karta hai 
print(student.items())                          # key or value dono return karta hai  
student.update({'age':22})                      # key ki value update karta hai 
student.pop('age')                              #di gai key or value dono ko delete karta hai 
student['age']=22
student.popitem()                               #last bale ki vaue ko remove karta hai 
student.clear()                                 #dic ko empty kar deta hai 
student.update({'name':'paras','age':55})
st=student.copy()                               # dic copy hoti hai or new  dic banti hai 
print(st)
print(student)
student={'name':'paras','age':233}            #Key na ho to default value add karta hai
student.setdefault('name','age')
print(student)


Built-in Function


Built-in Function	        Kaam

len(dict)	                Dictionary me kitne key-value pairs hain
type(dict)	                Data type batata hai
str(dict)	                Dictionary ko string me convert karta hai
dict()	Nayi                dictionary banata hai
sorted(dict)                Keys ko sorted list me return karta hai
max(dict)	                Sabse badi key return karta hai
min(dict)	                Sabse chhoti key return karta hai

'''
