




from tkinter import *
from tkinter import ttk
root = Tk()
root.title ("โปรแกรมแปลงสกุลเงิน")

#Input
money = IntVar()
Label(text="จำนวนเงิน(THB):",padx=10,font=50,bg=("yellow2")).place(x=150,y=100)
et1=Entry(font=30,width=30,textvariable=money,bg=("yellow2"))
et1.place(x=400,y=100)

choice = StringVar(value="โปรดเลือกสกุลเงิน")
Label(text="เลือกสกุลเงิน" ,padx=10,font=50,bg=("yellow2")).place(x=150,y=200)
combo=ttk.Combobox(width=30,font=30,textvariable=choice)
combo["values"]=("EUR" , "JPY" , "USD" ,"GBP")
combo.place(x=400,y=200)

#output
Label(text="ผลการคำนวณ" , padx=10, font=50,bg=("yellow2")).place(x=150,y=300)
et2=Entry(font=30,width=30,bg=("yellow2"))
et2.place(x=400,y=300)

def calculate():
    amount=money.get()
    currency=choice.get()
   
    if currency == "EUR":
        et2.delete(0,END)
        result = ((amount*0.028), "EUR (ยูโร)")
        et2.insert(0,result)
    elif currency == "JPY":
        et2.delete(0,END)
        result = ((amount*3.95), "JPY (เยน)")
        et2.insert(0,result)
    elif currency == "USD" :
        et2.delete(0,END)
        result = ((amount*0.027), "USD (ดอลลาร์สหรัฐ)")
        et2.insert(0,result)
    elif currency == "GBP":
         et2.delete(0,END)
         result = ((amount*0.027), "GBP (ปอนด์)")
         et2.insert(0,result)
    else :
        et2.delete(0,END)
        result = "ไม่พบข้อมูล โปรดเลือกสกุลเงิน"
        et2.insert(0,result)

def deleteText():
    et1.delete(0,END)
    et2.delete(0,END)


Button(text="คำนวณ", font=30,width=15,command=calculate,bg=("green2")).place(x=300,y=400)
Button(text="ล้าง",font=30,width=15,command=deleteText,bg=("red2")).place(x=450,y=400)

root.geometry("800x600")
root.configure(background='dodger blue')
root.mainloop()


