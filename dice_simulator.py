from tkinter import *
from PIL import Image,ImageTk
import time
import random
root=Tk()
root.geometry("1400x1000")
root.title("Dice simulator")
title=Label(root,text='DICE SIMULATOR',font=('times new roman',50,'bold'),bg='green',fg='white',bd=5,relief='solid').place(x=0,y=20,relwidth=1)
disp=Label(root,text='RESULT HERE',font=('times new roman',50,'bold'),bg='blue',fg='white')
disp.place(x=450,y=110)
dice=["1.png","2.png","3.png","4.png","5.png","6.png"]
image1=ImageTk.PhotoImage(Image.open(random.choice(dice)))
label1=Label(root,image=image1)
label1.image=image1
label1.place(x=400,y=200)

    
def roll():
    img=random.choice(dice)
    image1=ImageTk.PhotoImage(Image.open(img))
    label1.config(image=image1)
    label1.image=image1
    disp.config(text='PROCESSING')
    time.sleep(1)
    if(img=='6.png'):

        disp.config(text='SUCCESS')
        but.config(text='EXIT',command=root.destroy)
        
        
    else:
        disp.config(text='TRY AGAIN')
        

but=Button(root,text="CLICK TO ROLL",bg="red",fg="white",font=('times new roman',25,'bold'),command=roll)
but.place(x=500,y=730)

root.mainloop()
