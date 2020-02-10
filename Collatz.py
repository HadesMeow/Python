def collatz(number):
    a=number%2
    if  a == 0:
        print(number//2)
        return number//2
    elif a == 1:
        print(3*number+1)
        return 3*number+1


        
print('Enter number:')
try:
    num = int(input())
except ValueError:
    print('Please enter number,type is "int" :')
    num = int(input())
num = collatz(num)
while num !=1:
    num = collatz(num)
    if num==1:
        break
