ans = True
while True:
        if ans:
            uin = input("What you gotta say? : ")
            ans = False
        else:
            uin = input("I got that! Anything else? : ")
        
        if uin == "STOP":
            break