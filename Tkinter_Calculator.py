import tkinter as tk         #tkinter is GUI library,tk is alias
def press(v):              #press-when we enter something it enters in entry widget
    entry.insert(tk.END,v)
def clear():                #clear-used to clear entire content from entry widget
    entry.delete(0,tk.END)
def calc():
    try:
        result=eval(entry.get())    #valid expression is evaluated using eval function
        entry.delete(0,tk.END)      #clearing entry widget from 0 to end
        entry.insert(0,result)
    except:
        entry.delete(0,tk.END)    #invalid expression-handling using try and except
        entry.insert(0,"Error")   #displaying error message in entry widget
root=tk.Tk()                      #creating main window
root.title("Calculator")          #setting title of window
root.background="light blue"    #setting background color of window
root.configure(bg="#1e1e1e")  #setting background color using hex code
root.resizable(False,False)      # disabling resizing of window
entry=tk.Entry(root,font=("segoe UI",20),  #font size
               bg="#2d2d2d",fg="white",   #background color,floor ground color
               bd=0,justify="right")   #creating entry widget.border size=0,text aligned to right
entry.grid(row=0,column=0,columnspan=4,padx=12,pady=12,ipady=10)   #placing entry widget using grid method
buttons=[
    '7','8','9','/',
    '4','5','6','*',
    '1','2','3','-',
    '0','.','=','+'
]
r=1
c=0
for b in buttons:                   #b is variable name in buttons
    cmd=calc if b=="=" else lambda x=b:press(x)
    tk.Button(root,text=b,command=cmd,
              font=("segoe UI",14),
              width=5,height=2,
              bg="#ff9500"if b in "+-*/=" else "#3a3a3a",
              fg="white",bd=0).grid(row=r,column=c,padx=6,pady=6)
    c+=1
    if c==4:
        c=0
        r+=1
tk.Button(root,text="C",command=clear,
          font=("segoe UI",16),
          bg="#ff3b3b",fg="white",
          bd=0,width=22,height=2)\
.grid(row=r,column=0,columnspan=4,pady=8)
root.mainloop()                   #running the main event loop




