start=1
condition=11
step=2

for n in range(condition): # condition
    print(n)
    
print()

for n in range(start, condition):
    print(n)
    
print()
    
for n in range(start, condition, step):
    print(n)
    
print()
  
# 3's table
for n in range(start, condition):
    print("3*",n,"=", 3*n)
    
# all odd numbers between 1-20
for n in range(1,21,2):
    print(n)

print()
 
# all even numbers between 1-20
for n in range(1,21):
    if n%2 ==0:
        print(n)
        
print()
   
# reverse order 1-10
for n in range(10,0,-1):
    print(n)
