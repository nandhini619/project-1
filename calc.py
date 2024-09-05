from tkinter import *
window=Tk()
window.title("calculator")

# def HandleButtonClick(value):
#     value_from_expression=expression.get()
#     value_from_expression=value_from_expression+value
#     expression.set(value_from_expression)
# expression=StringVar()

def HandleButtonClick(value):
    value_from_expression=expression.get()
    if value_from_expression=="0":
         expression.set(value)
    elif value_from_expression=="+" or value_from_expression=="-" or value_from_expression=="*" or value_from_expression=="/" :
        expression.set(value)
    else:
        expression.set(value_from_expression+str(value))
expression=StringVar()    
def Result():
    # value=input.get()
    # c=eval(value)
    # input.delete(0,END)
    # input.insert(END,c)

    try:
        result=eval(expression.get())
        expression.set(result)
    except Exception as e:
        expression.set("MATH ERROR")    

def ClearAll():
    input.delete(0,END)
def Undo():
    value=input.get()
    input.delete(len(value)-1)
def Zero():
    value=input.get()  
    if len(value)==1:
        input.delete(0,END)
    input.insert(END,0)  

input=Entry(window,font=32,textvariable=expression)
input.grid(row=0,column=0,columnspan=4,sticky="ew")  

ButtonSeven=Button(window,text="7",padx=20,pady=20,command= lambda:HandleButtonClick("7"))
ButtonSeven.grid(row=1,column=0,padx=10,pady=10)

ButtonEight=Button(window,text="8",padx=20,pady=20,command= lambda:HandleButtonClick("8"))
ButtonEight.grid(row=1,column=1,padx=10,pady=10)

ButtonNine=Button(window,text="9",padx=20,pady=20,command= lambda:HandleButtonClick("9"))
ButtonNine.grid(row=1,column=2,padx=10,pady=10)

Buttonminus=Button(window,text="-",padx=20,pady=20,command= lambda:HandleButtonClick("-"))
Buttonminus.grid(row=1,column=3,padx=10,pady=10)

ButtonFour=Button(window,text="4",padx=20,pady=20,command= lambda:HandleButtonClick("4"))
ButtonFour.grid(row=2,column=0,padx=10,pady=10)

ButtonFive=Button(window,text="5",padx=20,pady=20,command= lambda:HandleButtonClick("5"))
ButtonFive.grid(row=2,column=1,padx=10,pady=10)

ButtonSix=Button(window,text="6",padx=20,pady=20,command= lambda:HandleButtonClick("6"))
ButtonSix.grid(row=2,column=2,padx=10,pady=10)
 
Buttonmulti=Button(window,text="*",padx=20,pady=20,command= lambda:HandleButtonClick("*"))
Buttonmulti.grid(row=2,column=3,padx=10,pady=10)

ButtonOne=Button(window,text="1",padx=20,pady=20,command= lambda:HandleButtonClick("1"))
ButtonOne.grid(row=3,column=0,padx=10,pady=10)

ButtonTwo=Button(window,text="2",padx=20,pady=20,command= lambda:HandleButtonClick("2"))
ButtonTwo.grid(row=3,column=1,padx=10,pady=10)

ButtonThree=Button(window,text="3",padx=20,pady=20,command= lambda:HandleButtonClick("3"))
ButtonThree.grid(row=3,column=2,padx=10,pady=10)

ButtonDiv=Button(window,text="/",padx=20,pady=20,command= lambda:HandleButtonClick("/"))
ButtonDiv.grid(row=3,column=3,padx=10,pady=10)

ButtonClear=Button(window,text="C",padx=20,pady=20,command= lambda:ClearAll())
ButtonClear.grid(row=4,column=0,padx=10,pady=10)

ButtonZero=Button(window,text="0",padx=20,pady=20,command= lambda:Zero())
ButtonZero.grid(row=4,column=1,padx=10,pady=10)

ButtonPlus=Button(window,text="+",padx=20,pady=20,command= lambda:HandleButtonClick("+"))
ButtonPlus.grid(row=4,column=2,padx=10,pady=10)

ButtonEqual=Button(window,text="=",padx=20,pady=20,command= lambda:Result())
ButtonEqual.grid(row=4,column=3,padx=10,pady=10)

ButtonUndo=Button(window,text="<--",padx=20,pady=20,command= lambda:Undo())
ButtonUndo.grid(row=5,column=0,padx=10,pady=10)


window.mainloop()