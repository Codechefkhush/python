# Numeric -

# int
# float
# complex numbers

# Sequence -

# string
# list
# tuple


# Dictionary 

# Set


# Mutable vs Immutable

# Mutable data types can chnage its state or content while immutable data types can not.


a = 5

print(a, "is type of", type(a))


b = 5.5

print(b, "is type of", type(b))


c = 5+2j

print(c, "is type of", type(c))



d = "Hey Khushal"

print(d, "is type of", type(d))


e = """"Hey Khushal
        How are you???"""

print(e, "is type of", type(e))


f = [5,5] 

f[1]=6 # mutable

print(f, "is type of", type(f))



f = (5,5)

# f[1]=6 # immutable, faster than list

print(f, "is type of", type(f))


g = {"name": "Khushal", "state": "Maharashtra"}

print(g, "is type of", type(g))
print(g["name"]) # prints the key value from dict

g["state"]="Goa"

print(g)


h={1,2,3,1}

print(h, type(h))