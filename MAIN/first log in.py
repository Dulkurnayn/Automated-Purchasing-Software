from tkinter import *  
import tkinter as tk
#from moderngui import App
import turtle
import random
def dashboard():
    win.destroy()
    app_instance = App()
    app_instance.mainloop()
    
def menue():
    global p,u

    
    widget=Label(canvas1,bg="grey",text="log in ",font=('Diamond Heavy SF',25),height=1,width=25)
    

    canvas1.create_window(550, 270, window=widget)
    p=Entry(canvas1, width=15,  bg="white",show='*')
    p.place(x=500,y=400)
    u=Entry(canvas1, width=15,  bg="white")
    u.place(x=500,y=350)
    widget1=Label(canvas1,bg="grey",text="username ",font=('Diamond Heavy SF',15),height=1,width=10)
    canvas1.create_window(430, 360, window=widget1)
    widget2=Label(canvas1,bg="grey",text="password ",font=('Diamond Heavy SF',15),height=1,width=10)
    canvas1.create_window(430, 410, window=widget2)

    win.bind('<Return>', submit)
   
def submit(event):
        global p,u
        
        password=p.get()
        user=u.get()
         
    
        
    
        x.write(str(password+" " + user)+"\n")
        x.close()
        x= open("create.txt" ,"r")
        for line in x: # Read the lines
                login_info = line.split()
                print(login_info)# Split on the space, and store the results in a list of two strings
                
                if password == login_info[0] and user == login_info[1]:
                    widget=Label(canvas1,bg="grey",text="correct ",font=('Diamond Heavy SF',25),height=1,width=25)
                    canvas1.create_window(550, 270, window=widget)
                    dashboard()
                    
                else:   
                        widget=Label(canvas1,bg="grey",text="incorrect ",font=('Diamond Heavy SF',25),height=1,width=25)
                        canvas1.create_window(550, 270, window=widget)

         
        u.delete(0,END)
        u.insert(0, "")
        p.delete(0,END)
        p.insert(0, "")
 
while True :
    win=Tk()
    win.title("log():  in ")
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()

    # Set the window size to fit the entire screen
    win.geometry(f"{screen_width}x{screen_height}")
    #win.geometry("1080x720")    
    win.resizable(width=False, height=False)

    img=PhotoImage(file= "chat_dark.png ")
    #img = ImageTk.PhotoImage(Image.open("C:\Users\17mshakil\OneDrive - ST Margarets Academy\A Level CS Y12\New folder 5 +PROJECTS\backgound1.gif"))    
        #img=PhotoImage(file= "C:\Users\17mshakil\OneDrive - ST Margarets Academy\A Level CS Y12\New folder 5 +PROJECTS\backgound1.gif" )

    canvas1=Canvas(win ,width= "1080" ,height ="720")
    canvas1.pack(fill= "both", expand=True)
    canvas1.create_image(0,0, anchor=NW, image=img)
    button1= Button(canvas1,text="menue",bg="white",width=5,height=2, command= menue)
    button1.grid(row=10,column=20)
    #button2= Button(canvas1,text="snake",bg="white",width=5,height=2, command= game)
    #button2.place(x=0,y=50,)
    #button3= Button(canvas1,text="dart",bg="white",width=5,height=2, command= game1)
    #button3.place(x=0,y=100,)
    #widget=Label(canvas1,bg="grey",text="hello",height=30,width=50)
    #button4= Button(canvas1,text="close",bg="white",width=5,height=2, command= second)
    #button4.place(x=0,y=150,)
    widget=Label(canvas1,bg="grey",text="hello",height=30,width=30)
    win.mainloop()


