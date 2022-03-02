import random
import time
l=[1,2,3,4,5,6]
print("GAME START")
while(1):
    print("Your result is being processed......")
    time.sleep(3)
    a=random.choice(l)
    print("Your result:",a)
    if(a==6):
        print("You win")
        break
    else:
        print("OOps!!\n Do you want to try again?")
        b=input()
        if(b=='y'):
            continue
        else:
            break

