import tkinter

flames = ['friends','love','affection','married','enemy','siblings']

def start():
    global flames

    n1 = set(name1.get().lower())
    n2 = set(name2.get().lower())

    unique = set(n1 - n2) | set(n2 - n1)
    count = len(unique)
    

    print(count)
    try:
        for _ in range(5):
            q = -1
            for j in range(count):
                q += 1
                if q == (count-1):
                    flames.pop(((q%6)-1))
                    break
    except IndexError:
        result.config(text = 'Error!!',font = ('Helvetica',60))
    else:
        
        result.config(text = str(flames))
    


#Driver Code

app = tkinter.Tk()
app.geometry('550x350')
app.title('FLAMES')

rule = tkinter.Label(app, text = 'Enter 2 names and know the result of FLAMES !',font = ('Helvetica',12))
rule.pack()


name1lable = tkinter.Label(app, text = 'Name 1', font = ('Helvetica',12))
name1lable.pack(pady = 10)

name1 = tkinter.Entry(app)
name1.pack()

name2label = tkinter.Label(app, text = 'Name 2', font = ('Helvetica',12))
name2label.pack()

name2 = tkinter.Entry(app)
name2.pack()


#Button
flmbtn = tkinter.Button(app,text = 'FLAME IT',font = ('Hevetica',12),command = start)
flmbtn.pack(pady = 20)

#Result Label
result = tkinter.Label(app)
result.pack(pady = 20)

name1.focus_set()
app.mainloop()