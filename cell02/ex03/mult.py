first=int(input('Enter first number : '))
second=int(input('Enter second number : '))
num= int(first * second)
print( str(first) +' x '+ str(second) +' = '+ str(num))
if num > 0:
    print('The result is positive')
if num < 0:
    print('The result is negative')
if num == 0:
    print('The result is positive and negative')
