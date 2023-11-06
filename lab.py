condition = 6<7
if not condition:
    print("not (6<7) is true!")
else:
    print("not (6<7) is false!")

if True or False:
    print("true or false is true")
else:
    print("true or false is false")

if True or True:
    print("true or true is true")
else:
    print("true or true is false")

if 36:
    print("36 is true!")
else:
    print("36 is false!")

if 0:
    print( "0 is true!")
else:
    print( "0 is false!")

if not 5: #What do you think the programmer meant to do here?  How would you fix their mistake?
    print("not 5 is true")
else:
    print("not 5 is false")

#In Python, the if/else below will evaluate to true.  In many programming languages, it would evaluate to false
#and to achieve the same behavior, you would have to use the second if/else below.  Why do you think that is?
if -1 < 0 < 1:
    print("-1<0<1 is true")
else:
    print("-1<0<1 is false")

if (-1)<0 and 0<1:
    print("-1<0 and 0<1 is true")
else:
    print("-1<0 and 0<1 is false")

#The statement below will cause an error.  What is the mistake, and how would you fix it?
x = 0
if x == 5:
    print("x=5 is true")
else:
    print("x=5 is false")