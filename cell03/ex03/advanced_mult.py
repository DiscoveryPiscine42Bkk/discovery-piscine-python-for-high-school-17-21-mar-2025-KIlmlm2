num = 0
while num <= 10:
        print('Table de ' +str(num) + ' : ',end="")
        
        i = 0
        while i <= 10:
            print(num * i,end=" ")
            i += 1
        
        print()
        num += 1