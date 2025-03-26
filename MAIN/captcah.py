import tkinter 
import os
import tkinterweb 

import tkinter.messagebox 
from PIL import Image
import customtkinter
def getimage(path):
    image1 = customtkinter.CTkImage(light_image=Image.open(path),size=(30, 30))
    return image1
class App(customtkinter.CTk): 

    def __init__(self): 

        super().__init__() 

        self.title("Captcha") 
        self.geometry("700x600") 

        self.grid_rowconfigure((0,2), weight=1) 

        self.columnconfigure((0,1,2), weight=1)
        self.captcha_title = customtkinter.CTkLabel(self, text="  captcha solver ",image=getimage(r"C:\Users\musta\Downloads\New folder\captcha\captchalogo.png") ,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.captcha_title.grid(row=1,  padx=(200  , 2), pady=(20, 0), sticky="n") 
        self.info = customtkinter.CTkFrame(self , height= 600,width=100, corner_radius=0) 

        self.info.grid(row=2, column=0, padx=(20  , 2), pady=(20, 0), sticky="nsew") 

        self.entry=customtkinter.CTkEntry(self.info,placeholder_text= "newtask")
        self.entry.grid(row=3, column=0, columnspan=1, padx=(10,0), pady=(20, 20), sticky="nswe")
        self.main_button_1 = customtkinter.CTkButton(self.info, fg_color="transparent", border_width=2,text="enter", text_color=("gray10", "#DCE4EE"))
        self.main_button_1.grid(row=3, column=1, padx=(10, 20), pady=(20, 20), sticky="nsew")
        
        self.optionmenu_1 = customtkinter.CTkOptionMenu(self.info, dynamic_resizing=False,
                                                values=["level1", "level2", "level3"])
        self.optionmenu_1.grid(row=0, column=0, padx=10, pady=(20, 10))
        self.optionmenu_2 = customtkinter.CTkOptionMenu(self.info, dynamic_resizing=False,
                                                values=["nike", "zoolando", "footlocker"])
        self.optionmenu_2.grid(row=0, column=1, padx=10, pady=(20, 10))

        self.optionmenu_3 = customtkinter.CTkOptionMenu(self.info, dynamic_resizing=False,
                                                values=["4","5","6","7","8","9","10","11","12"])
        self.optionmenu_3.grid(row=1, column=1, padx=10, pady=(20, 10))

        self.optionmenu_4 = customtkinter.CTkComboBox(self.info, 
                                                values=["level1", "level2", "level3"])
        self.optionmenu_4.grid(row=1, column=0, padx=10, pady=(20, 10))
        self.optionmenu_1.set("priority")
        self.optionmenu_2.set("store")
        self.optionmenu_3.set("size")
        self.optionmenu_4.set("item")
                
        self.main_button_2 = customtkinter.CTkButton(self.info, fg_color="transparent", border_width=2,text="ai?", text_color=("gray10", "#DCE4EE"))
        self.main_button_2.grid(row=4, column=1, padx=(10, 20), pady=(20, 20), sticky="nsew")
        #solved
        #requested
        #pendinf widegt instantiated with 3 variables pased in and tex values taken from variable
    

        #captchs tab 

        self.fra=tkinterweb.HtmlFrame(self, width=0 ,height=60  ) 

        self.fra.load_website("https://www.google.com/maps") 

        self.fra.grid(row=1,rowspan=2, column=1, padx=(20, 20), pady=(20, 0), sticky="nsew") 

      
        #anytics datab 

        self.analysis = customtkinter.CTkFrame(self, width=100, corner_radius=0) 

        self.analysis.grid(row=3, columnspan=4 ,padx=(20, 20), pady=(20, 20), sticky="nsew") 

  

  

    def update_data(self, event): 

        #for abalytics 

        print("hellleo22") 

  

  

    def sidebar_button_event(self): 

        print("sidebar_button click") 

def create_and_run_app(): 

    app = App() 

    app.mainloop() 

  

if __name__ == "__main__": 

    create_and_run_app()  # Open the first window 

    create_and_run_app() 
