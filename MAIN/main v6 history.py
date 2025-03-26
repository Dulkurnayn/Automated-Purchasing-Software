import customtkinter
import pywinstyles
import os
from PIL import Image
from selenium import webdriver
#
import tkinterweb
#
#
from cryptography.fernet import Fernet
import pandas as pd
import matplotlib.dates as mdates 
import numpy as np
from datetime import date, timedelta
import schedule
#
import re
#import undetected_chromedriver as uc
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#
from tkinter import messagebox
import time
#
import tkinter as tk
from matplotlib.figure import Figure  
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)
#import loginv2
#from billing import PurchaseApp
#lists recovered from log text files during loading
# tasks succesful or failed total spending
#
import threading
#
import sqlite3
import requests
#
import math
import psutil
import wmi
import random
#
import tkinter
from tkinter import *  
from PIL import ImageTk, Image
import getmac
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
start = time.perf_counter()
customtkinter.set_appearance_mode("Light")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"
def getimage(path):
    image1 = customtkinter.CTkImage(light_image=Image.open(path),size=(30, 30))
    return image1
def wifi_connection():
    try :
        response = requests.get('http://google.com', timeout=5)
        return True
    except Exception as e:
                print(f"Error reading proxy file: {str(e)}")
                return False
class RevenueData(customtkinter.CTkFrame):
    def __init__(self, charts,date_strings):
        
        self.app=App
        # Assuming the amount spent is generated randomly for each date
        np.random.seed(42)
        amounts_spent = np.random.randint(1000, 5000, len(date_strings))

        self.revenue_data = pd.DataFrame({"date": date_strings, "amount_spent": amounts_spent})
        self.revenue_data["date"] = pd.to_datetime(self.revenue_data["date"])
        self.charts=charts

    def plot_revenue(self):
        #ax_1.plot(self.revenue_data["date"], self.revenue_data["amount_spent"])
       
        print("helll")
        self.fig_1 = Figure(figsize=(15.5, 15.2), alpha=0)
        self.ax_1 = self.fig_1.add_subplot()
        self.ax_1.set_xlabel('date')
        self.ax_1.set_ylabel('Amount Spent')
        self.ax_1.set_title('Revenue Data for 2024')
        self.ax_1.set_facecolor('#71aed1')
        self.ax_1.fill_between(x=self.revenue_data["date"], y1=self.revenue_data["amount_spent"], alpha=0.7)
        self.ax_1.tick_params(labelsize=7, colors="white")
        self.fig_1.autofmt_xdate()
        self.ax_1.plot(self.revenue_data["date"],self.revenue_data["amount_spent"], color="deepskyblue")
        self.ax_1.grid(visible=True)
        self.canvas = FigureCanvasTkAgg(figure=self.fig_1, master=self.charts) 
        self.canvas.draw() 
        self.canvas.get_tk_widget().grid(column = 0, row = 0)
        
       
class Liverandom:
    def __init__(self):
        self.primes_list = [2] #initialise the prime list variable

    def get_live_data(self):#get live data of the device harware
        w = wmi.WMI()
        ram_used = psutil.virtual_memory().percent
        cpu_used = psutil.cpu_percent()
        return cpu_used, ram_used #returns the values

    def prime_check(self):
        for i in range(3, 50): # nested for loop first loop this used to find primes itertively between 3 and 50
            is_prime = True
            for divisor in range(2, int(math.sqrt(i)) + 1): #this used to xheck if the number is prime by using  
                if i % divisor == 0:                        #the fact that smalest prime is 2 and there is no
                    is_prime = False                  #int(math.sqrt(i)) + 1 reduces the itearive process
                    break                             #if it had has remainder 0 after carrting out mod then its not prime so break waya from for loop
            if is_prime:
                self.primes_list.append(i)        #if it was a prime its aded to the list at this point it returns to the main for loop to check the next value

    def prime_gen(self):    #recursive prime genration
        u = 1
        for prime in self.primes_list:
            u *= prime               #for each prime in the list it multiplies them altogether 
        u += 1              #proceeds to add one now the number will be a prime or have a prime factor

        is_u_prime = True
        for divisor in range(2, int(math.sqrt(u)) + 1):  ##uses a similar check to prime list seed generation
            if u % divisor == 0:                        #if u is not a prime number, it must have a factor that is less than or equal to its square root
                is_u_prime = False
                self.primes_list.append(divisor)
                self.primes_list.append(u/divisor)   #if 
                print(divisor, "d")  #view the values in terminal to help trace the function
                print(u,"u")
                print(len(self.primes_list)) #return length to help set base condition to stopp the recursion so recursion max depth limit exceeded is not encountered
                return self.prime_gen()

            if len(self.primes_list) >= 20: #base conditon
                return self.primes_list

        if is_u_prime:
            self.primes_list.append(u)  #on the occasion that u is the prine and not the divisors
            print(u)
            return self.prime_gen()

    def generate_random_ascii_string(self, length): #takes in a length as a parameter 
        random_ascii_string = ''.join(chr(random.randint(32, 126)) for _ in range(length)) #uses ranom library to generate random intger and runs a
        #for loop where it joins the charcter to random ascii string the is line would usually b the equivalent of 5
        return random_ascii_string  #the ascii charcters it selects are betweenthe values  32, 126 it retur
       
"""lr = Liverandom()# instatiates the class
lr.prime_check()#calls the function of the class for intial list
lr.prime_gen()#calls prime gen function
x1, x2 = lr.get_live_data()#gets the live data stores it respectivley in x1 and x2 
print(f"cpu_tem: {x1}")
print(f"RAM Used: {x2}%")

length_of_string = 10 #stes parameter 
random_string = lr.generate_random_ascii_string(length_of_string) #calls the random ascii charachetr genration with the pameter defined
print("Random ASCII string:", random_string)
licence = f"{Liverandom().generate_random_ascii_string(10)}{Liverandom().get_live_data() * Liverandom().primes_list[-1] * random.randint(1, 100)}\
    {Liverandom().generate_random_ascii_string(10)}{time.strftime('%H%M%S')}"
print("License:", licence)#combines data to get key """
class load_data(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("400x200")
        self.title("loading")

        self.progressbar = customtkinter.CTkProgressBar(self, orientation="horizontal")
        self.progressbar.grid(padx=100,pady=100 )
        self.progressbar.configure(mode="indeterminnate")
        self.progressbar.start()
        #pywinstyles.apply_style(app, 'aero')
        #time.sleep(4000)

        
                

class login(customtkinter.CTk):
    def __init__(self):
        super().__init__()


        customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
        customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
        
        def dashboard():
            log.destroy()
            if __name__ == "__main__":
                app = App()
                #load = load_data()
                
               
                app.mainloop()

            
            
            
        
        def passwordreset(): 
            global username ,email
            email=email.get()
            em= "valid"
            if em == "valid" : 
                dialog = customtkinter.CTkInputDialog(text="give one time password", title="otp")
                print("Number:", dialog.get_input())
                x= open("create.txt" ,"r")
                # Read the lines
                print("helle")
                user=username.get()
                
                
                email = email if re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$',email) else  messagebox.showerror("Error","enter all fields")
                with open("create.txt", "r") as x:
                    line = x.readline()
                    login_info = line.split()
                    #print(login_info)
                    if login_info[1] == user :
                        print("elle")
                
                    # Email configuration
                        sender_email = "17mshakil@stmargaretsacademy.com"
                        sender_password = "kinglord1"
                        subject = "Password Reset Request"

                        # Create message
                        message = MIMEMultipart()
                        message["From"] = sender_email
                        message["To"] = email
                        message["Subject"] = subject

                        # Email body
                        body = "here is a link to access your temporary password" \
                            "http://example.com/reset_password"

                        message.attach(MIMEText(body, "plain"))

                        # Connect to the SMTP server (Gmail example)
                        with smtplib.SMTP("smtp.outlook.com", 587) as server:
                            server.starttls()
                            server.login(sender_email, sender_password)

                            # Send email
                            server.sendmail(sender_email, email, message.as_string())

                        # Example usage
                        
                    else:
                            print("An error occurred:")
            else:
                messagebox.showerror("Error","valid email required")

            
        def submit_login(event=None):
        # destroy current window and create a new on
            global password,username,frame
            
            self.pas=self.password.get()
            self.user=self.username.get()
            #x= open("create.txt" ,"a")

            
            mac = getmac.get_mac_address()
            print(mac)
            #x.write(str(pas+" " + user)+"\n")
            #x.close()
            x= open("create.txt" ,"r")
            
            with open("create.txt", "r") as x:
                line = x.readline()
                login_info = line.split()
                print(login_info)
        # Read the lines
            
                
                print(login_info)
                x.close# Split on the space, and store the results in a list of two strings
                print( login_info[0])
                if self.pas== login_info[0] and self.user == login_info[1] and mac == login_info[2] :
                    #self.frame.destroy()
                    
                    
                    dashboard()
                    
                    
                else:    
                    if self.user or self.pas  == (""): 
                        messagebox.showerror("Error","all fields required")
                    elif self.user == login_info[1] :
                        messagebox.showerror("Error","incorrect password")
                    
                        
                    self.username.delete(0, "end")
                    self.password.delete(0, "end")

        def signup_function():
            self.title('Sign Up')
            self.geometry("600x640")
            self.frame.place_forget()
            self.sign_up_frame= customtkinter.CTkFrame(self, width=320, height=360, corner_radius=15, fg_color="transparent")
            self.sign_up_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

            self.page_name = customtkinter.CTkLabel(master=self.sign_up_frame, text="SIGN UP", font=('Century Gothic', 20))
            self.page_name.place(x=120, y=45)

            self.username = customtkinter.CTkEntry(master=self.sign_up_frame, width=220, placeholder_text='Username')
            self.username.place(x=50, y=110)
            def check_btn_var():
                if view_password.get():
                    self.password.configure(show="")
                else:
                    self.password.configure(show="*")
            view_password = customtkinter.CTkSwitch(master=self.sign_up_frame,command=check_btn_var ,text=None ) 
            view_password.place(x=240, y=165)
            #eye = customtkinter.CTkLabel(master=self.sign_up_, text="view")
            #eye.place(x=240, y=180)
            self.password = customtkinter.CTkEntry(master=self.sign_up_frame, width=190, placeholder_text='Password', show="*")
            self.password.place(x=50, y=165)
           
            
            
           
            #switch_var = customtkinter.StringVar(value="on")
            #view_password = customtkinter.CTkSwitch(master=self.sign_up_, text="Forget password?",command=check_btn_var, onvalue=1, offvalue=0 ,font=('Century Gothic', 12, ['bold']),fg_color="transparent",hover_color="gray25")


            self.email = customtkinter.CTkEntry(master=self.sign_up_frame, width=220, placeholder_text='Email')
            self.email.place(x=50, y=220)

            # command=passwordreset(recieveremail)
            resetpass_button = customtkinter.CTkButton(master=self.sign_up_frame, text="Forget password?",command=passwordreset ,font=('Century Gothic', 12, ['bold']),fg_color="transparent",hover_color="gray25" ) 
            resetpass_button.place(x=130, y=250)

            self.login_button = customtkinter.CTkButton(master=self.sign_up_frame, width=220, text="Login", command=load_log, corner_radius=6)
            self.login_button.place(x=50, y=290)

            signup_button = customtkinter.CTkButton(master=self.sign_up_frame, width=220, text="Sign Up", command=signup_function, corner_radius=6)
            signup_button.place(x=50, y=330)
            #username = customtkinter.CTkEntry(master=self.sign_up_, width=220, placeholder_text='Username')
            #username.place(x=50, y=110)

            self.re_enter_password = customtkinter.CTkEntry(master=self.sign_up_frame, width=220, placeholder_text='re-enter Password', show="*")
            self.re_enter_password.place(x=50, y=250)

            self.email = customtkinter.CTkEntry(master=self.sign_up_frame, width=220, placeholder_text='Email')
            self.email.place(x=50, y=220)
            self.unbind('<Return>')
            


            # Add signup window UI components here (similar to the login window)

            
        def load_log():
            self.sign_up_frame.place_forget()
            self.frame.place()

            #self.login_button.configure(command=submit_login)
            #self.page_name.configure(text="LOG IN")
            print("hh")
            log_in_function()
            
        def log_in_function():
        #logingui = customtkinter.CTk()  # creating custom tkinter window
            
            self.geometry("600x440")
            self.title('Login')

            self.img1 = Image.open("pattern.png")
            image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_images")
            self.img1= customtkinter.CTkImage(Image.open(os.path.join(image_path, "pattern.png")), size=(1920,1248))
            self.l1 = customtkinter.CTkLabel(self, image=self.img1)
            self.l1.pack()

            self.frame = customtkinter.CTkFrame(self, width=320, height=360, corner_radius=15, fg_color="transparent")
            self.frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

            self.page_name = customtkinter.CTkLabel(master=self.frame, text="LOG IN", font=('Century Gothic', 20))
            self.page_name.place(x=120, y=45)

            self.username = customtkinter.CTkEntry(master=self.frame, width=220, placeholder_text='Username')
            self.username.place(x=50, y=110)
            def check_btn_var():
                if view_password.get():
                    self.password.configure(show="")
                else:
                    self.password.configure(show="*")
            view_password = customtkinter.CTkSwitch(master=self.frame,command=check_btn_var ,text=None ) 
            view_password.place(x=240, y=165)
            #eye = customtkinter.CTkLabel(master=self.frame, text="view")
            #eye.place(x=240, y=180)
            self.password = customtkinter.CTkEntry(master=self.frame, width=190, placeholder_text='Password', show="*")
            self.password.place(x=50, y=165)
           
            
            
           
            #switch_var = customtkinter.StringVar(value="on")
            #view_password = customtkinter.CTkSwitch(master=self.frame, text="Forget password?",command=check_btn_var, onvalue=1, offvalue=0 ,font=('Century Gothic', 12, ['bold']),fg_color="transparent",hover_color="gray25")


            self.email = customtkinter.CTkEntry(master=self.frame, width=220, placeholder_text='Email')
            self.email.place(x=50, y=220)

            # command=passwordreset(recieveremail)
            resetpass_button = customtkinter.CTkButton(master=self.frame, text="Forget password?",command=passwordreset ,font=('Century Gothic', 12, ['bold']),fg_color="transparent",hover_color="gray25" ) 
            resetpass_button.place(x=130, y=250)

            self.login_button = customtkinter.CTkButton(master=self.frame, width=220, text="Login", command=submit_login, corner_radius=6)
            self.login_button.place(x=50, y=290)

            signup_button = customtkinter.CTkButton(master=self.frame, width=220, text="Sign Up", command=signup_function, corner_radius=6)
            signup_button.place(x=50, y=330)
            self.bind('<Return>', submit_login)
        log_in_function()
        



class captcha(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app=App
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
                                                values=["sport direct", "zoolando", "footlocker"])
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

        self.fra.load_website("https://www.google.com") 

        self.fra.grid(row=1,rowspan=2, column=1, padx=(20, 20), pady=(20, 0), sticky="nsew") 

      
        #anytics datab 

        self.analysis = customtkinter.CTkFrame(self, width=100, corner_radius=0) 

        self.analysis.grid(row=3, columnspan=4 ,padx=(20, 20), pady=(20, 20), sticky="nsew") 

  

  

        def update_data(self, event): 

            #for abalytics 

            print("hellleo22") 

    

    

        def sidebar_button_event(self): 

            print("sidebar_button click") 
#loginv2.loginpy()
class search_bar():
  
    #for counter 
    print("")
class PurchaseApp(customtkinter.CTkFrame):
    def __init__(self, master,**kwargs):
        super().__init__(master, **kwargs)

        

        # User Information Frame
        self.user_info_frame = customtkinter.CTkFrame(self)
        self.user_info_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        # Entry Fields
        self.profile_name_label = customtkinter.CTkLabel(self.user_info_frame, text="Profile Name:")
        self.profile_name_label.grid(row=0, column=0, pady=5,padx=5, sticky="w")
        self.profile_name_entry = customtkinter.CTkEntry(self.user_info_frame, placeholder_text="supersurfer123")
        self.profile_name_entry.grid(row=0, column=1, pady=5, padx=10)

        self.first_name_label = customtkinter.CTkLabel(self.user_info_frame, text="First Name:")
        self.first_name_label.grid(row=0, column=2, pady=0,padx=5, sticky="w")
        self.first_name_entry = customtkinter.CTkEntry(self.user_info_frame,placeholder_text="john")
        self.first_name_entry.grid(row=0, column=3, pady=0, padx=10)
        self.first_name_checkbox = customtkinter.CTkCheckBox(self.user_info_frame, text="save")
        self.first_name_checkbox.grid(row=0, column=4, pady=0)
        self.email_label = customtkinter.CTkLabel(self.user_info_frame, text="email:")
        self.email_label.grid(row=2, column=0, pady=5,padx=5, sticky="w")
        self.email_entry = customtkinter.CTkEntry(self.user_info_frame,placeholder_text="enidblighton@gmail.com")
        self.email_entry.grid(row=2, column=1, pady=5, padx=10)


        self.last_name_label = customtkinter.CTkLabel(self.user_info_frame, text="Last Name:")
        self.last_name_label.grid(row=2, column=2, pady=5,padx=5, sticky="w")
        self.last_name_entry = customtkinter.CTkEntry(self.user_info_frame,placeholder_text="smith")
        self.last_name_entry.grid(row=2, column=3, pady=5, padx=10)
        self.last_name_checkbox = customtkinter.CTkCheckBox(self.user_info_frame, text="save")
        self.last_name_checkbox.grid(row=2, column=4, pady=0)

        self.phone_number_label = customtkinter.CTkLabel(self.user_info_frame, text="Phone Number:")
        self.phone_number_label.grid(row=3, column=0, pady=5,padx=5, sticky="w" )
        self.phone_prefix_values = ["+1", "+44", "+49", "+61"]  # Add more prefixes as needed
        self.phone_prefix_combo = customtkinter.CTkOptionMenu(self.user_info_frame, values=self.phone_prefix_values )
        self.phone_prefix_combo.grid(row=3, column=1, pady=5,padx=5, sticky="w" )
        self.phone_number_entry = customtkinter.CTkEntry(self.user_info_frame,placeholder_text="075463778" )
        self.phone_number_entry.grid(row=3, column=2, pady=0, padx=10)
        self.phone_number_checkbox = customtkinter.CTkCheckBox(self.user_info_frame, text="save")
        self.phone_number_checkbox.grid(row=3, column=3, pady=5)

        # Shipping Details Frame
        self.shipping_frame = customtkinter.CTkFrame(self)
        self.shipping_frame.grid(row=1, column=0, padx=20, pady=5, sticky="w")
        self.country_label = customtkinter.CTkLabel(self.shipping_frame, text="Country:")
        self.country_label.grid(row=0, column=0, pady=5,padx=5, sticky="w")
        self.country_values = ["USA", "Canada", "UK", "Australia"]
        self.country_combo = customtkinter.CTkComboBox(self.shipping_frame, values=self.country_values)
        self.country_combo.grid(row=0, column=1, pady=5, padx=10)

        self.city_label = customtkinter.CTkLabel(self.shipping_frame, text="City:")
        self.city_label.grid(row=1, column=0, pady=5,padx=5 ,sticky="w")
        self.city_entry = customtkinter.CTkEntry(self.shipping_frame,placeholder_text="LONDON")
        self.city_entry.grid(row=1, column=1, pady=5, padx=10)

        self.street_label = customtkinter.CTkLabel(self.shipping_frame, text="Street:")
        self.street_label.grid(row=2, column=0, pady=5,padx=5, sticky="w")
        self.street_entry = customtkinter.CTkEntry(self.shipping_frame,placeholder_text="10 DOWNING ST")
        self.street_entry.grid(row=2, column=1, pady=5, padx=10)
        
        self.postcode_label = customtkinter.CTkLabel(self.shipping_frame, text="postcode")
        self.postcode_label.grid(row=3, column=0, pady=5,padx=5, sticky="w")
        self.postcode_entry = customtkinter.CTkEntry(self.shipping_frame,placeholder_text="LR45 73T")
        self.postcode_entry.grid(row=3, column=1, pady=5, padx=10)



        self.replicate_checkbox = customtkinter.CTkCheckBox(self.shipping_frame, text="Replicate shipping for billing", command=self.toggle_billing_details)
        self.replicate_checkbox.grid(row=4, column=1, columnspan=2, pady=5, padx=10, sticky="w")

        # Billing Details Frame
        self.billing_frame = customtkinter.CTkFrame(self)
        self.billing_frame.grid(row=1, column=1, padx=20, pady=20, sticky="nsew")
        self.billing_frame.grid_remove()  # Hide initially

        self.billing_city_label = customtkinter.CTkLabel(self.billing_frame, text="Billing City:")
        self.billing_city_label.grid(row=1, column=0, pady=5,padx=5, sticky="w")
        self.billing_city_entry = customtkinter.CTkEntry(self.billing_frame)
        self.billing_city_entry.grid(row=1, column=1, pady=5, padx=10)

        self.billing_street_label = customtkinter.CTkLabel(self.billing_frame, text="Billing Street:")
        self.billing_street_label.grid(row=2, column=0, pady=5,padx=5, sticky="w")
        self.billing_street_entry = customtkinter.CTkEntry(self.billing_frame)
        self.billing_street_entry.grid(row=2, column=1, pady=5, padx=10)

        # Card Details Frame
        self.card_frame = customtkinter.CTkFrame(self)
        self.card_frame.grid(row=0, column=1, padx=(20,40), pady=20, sticky="nswe")

        self.card_number_label = customtkinter.CTkLabel(self.card_frame, text="Card Number:")
        self.card_number_label.grid(row=0, column=0, pady=5,padx=5, sticky="w")
        self.card_number_entry = customtkinter.CTkEntry(self.card_frame, placeholder_text="2222 4053 4324 8877")
        self.card_number_entry.grid(row=0, column=1, pady=5, padx=10)
        self.card_cvv_label = customtkinter.CTkLabel(self.card_frame, text="Card CVV:")
        self.card_cvv_label.grid(row=0, column=2, pady=5, sticky="w")
        self.card_cvv_entry = customtkinter.CTkEntry(self.card_frame, placeholder_text="453" ,width=50 )
        self.card_cvv_entry.grid(row=0, column=3, pady=5, padx=10)


        self.card_expiry_label = customtkinter.CTkLabel(self.card_frame, text="Card Expiry:")
        self.card_expiry_label.grid(row=1, column=0, pady=5,padx=5, sticky="w")
        self.card_expiry_month_values = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
        self.card_expiry_year_values = ["2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029", "2030"]
        self.card_expiry_month_combo = customtkinter.CTkOptionMenu(self.card_frame, values=self.card_expiry_month_values, width=80)
        self.card_expiry_month_combo.grid(row=1, column=1,pady=0, padx=10)
        self.card_expiry_year_combo = customtkinter.CTkOptionMenu(self.card_frame, values=self.card_expiry_year_values, width=80)
        self.card_expiry_year_combo.grid(row=1, column=2,pady=0, padx=10)

   
        # Purchase Button
        self.purchase_button = customtkinter.CTkButton(self, text="submit", command=self.purchase_event)
        self.purchase_button.grid(row=5, column=0, pady=10)
        self.replicate_checkbox.select()

    def toggle_billing_details(self):
        if self.replicate_checkbox.get() == 1:
            self.billing_frame.grid_remove()  # Hide billing details
        else:
            self.billing_frame.grid()  # Show billing details

    def purchase_event(self):
        # Retrieve user information
        profile_name = self.profile_name_entry.get()
        first_name = self.first_name_entry.get() if not self.first_name_checkbox.get() else ""
        last_name = self.last_name_entry.get() if not self.last_name_checkbox.get() else ""
        email = self.email_entry.get()
        phone_number = self.phone_number_entry.get()
        postcode = self.postcode_entry.get()
        #print(self.postcode_entry.cget("fg_color"))check the current culour
        # postcode = self.postcode_entry.get() if re.match(r"^[A-Z]{1,2}\d{1,2}[A-Z]?\s\d[A-Z]{2}$",self.postcode_entry.get()) else self.postcode_entry.configure(placeholder_text="none")
        print ("Testing user info")
       
    

        # Retrieve shipping details
        country = self.country_combo.get()
        city = self.city_entry.get()
        street = self.street_entry.get()

        # Retrieve billing details
        billing_city = self.billing_city_entry.get() if not self.replicate_checkbox.get() else city
        billing_street = self.billing_street_entry.get() if not self.replicate_checkbox.get() else street

        # Retrieve card details
        card_number = self.card_number_entry.get()
        card_expiry_month = self.card_expiry_month_combo.get()
        card_expiry_year = self.card_expiry_year_combo.get()
        card_cvv = self.card_cvv_entry.get()
        try: 
            if not (profile_name and first_name and last_name and  phone_number and postcode and country and city and street and\
                     billing_city and billing_street and card_number and card_expiry_month and card_expiry_year and card_cvv):
                messagebox.showerror("Error","enter all fields")
            elif re.match(r"^[A-Z]{1,2}\d{1,2}[A-Z]?\s\d[A-Z]{2}$",postcode):
                  self.postcode_entry.configure(fg_color='F9F9FA')  # Set background color to white
                # Invalid postcode
            else:
                # Valid postcode
                self.postcode_entry.configure(fg_color='#ea655b') 
        except ValueError:
            messagebox.showerror("Error","value should be an integer")

            
        #self.purchase_details = {
         #   "profile_name": profile_name,purchase_details = f"Purchase Details:\nProfile Name: {profile_name}\nFirst Name: {first_name}\nLast Name: 
          #  {last_name}\nPhone Number: {phone_number}\nPostcode: {postcode}\n\nShipping Details:\nCountry: {country}\nCity: {city}\nStreet: {street}\n\nBilling Details:
           # \nBilling City: {billing_city}\nBilling Street: {billing_street}\n\nCard Details:\nCard Number: {card_number}\nCard Expiry: {card_expiry_month}/{card_expiry_year}\nCVV: {card_cvv}"
        
        shipping_details = {
            "country": country,
            "postcode": postcode,
            "city": city,
            "street": street,
        }

        billing_details = {
            "billing_city": billing_city,
            "billing_street": billing_street,
        }

        card_details = {
            "card_number": card_number,
            "card_expiry_month": card_expiry_month,
            "card_expiry_year": card_expiry_year,
            "card_cvv": card_cvv,
        }
        user_details={
            "profile_name": profile_name,
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "phone_number": phone_number}
        self.purchase_details = {
             "user_details"  : user_details,
            "shipping_details": shipping_details,
            "billing_details": billing_details,
            "card_details": card_details,
        }
            # ... (other user information)
        from cryptography.fernet import Fernet
        key = Fernet.generate_key()
        cipher_suite = Fernet(key)

        # Data to be encrypted (dictionary of dictionaries)
        

        # Encrypt the data
        encrypted_data = cipher_suite.encrypt(str(self.purchase_details).encode())

        # Decrypt the data
        #decrypted_data = eval(cipher_suite.decrypt(encrypted_data).decode())
        # connect to main function
        #purchase_details = f"Purchase Details:\nProfile Name: {profile_name}\nFirst Name: {first_name}\nLast Name: {last_name}\nPhone Number: {phone_number}\nPostcode: {postcode}\n\nShipping Details:\nCountry: {country}\nCity: {city}\nStreet: {street}\n\nBilling Details:\nBilling City: {billing_city}\nBilling Street: {billing_street}\n\nCard Details:\nCard Number: {card_number}\nCard Expiry: {card_expiry_month}/{card_expiry_year}\nCVV: {card_cvv}"
        return(encrypted_data)

class proxy_dash(customtkinter.CTkFrame):
     def __init__(self, master,**kwargs):
        super().__init__(master, **kwargs)
        def remove_slow_proxies(self):
                connection = sqlite3.connect('proxies.db')#start the conection to the database
                cursor = connection.cursor()#store the connection crusor as crusor
                #makes it easier to perdorm queries
            

                cursor.execute("SELECT proxy_url FROM proxy_speeds WHERE speed_category=slow,Error")
                slow_proxies = cursor.fetchall()
                for proxy_url in slow_proxies:
                    print(f"Removing slow proxy: {proxy_url[0]}")#print to check that the correct proxies are being removed

                cursor.execute("DELETE FROM proxy_speeds WHERE speed_category IN ('Slow', 'Error')")
                #use sql method to remove proxies that are slow
                cursor.commit()##!!!very important so that work is saved

                
        def latency_proxies():
            def read_proxy_urls_from_file(file_path='proxy.txt'):
                try:
                    with open(file_path, 'r') as file:
                        return [line.strip() for line in file.readlines()]
                except Exception as e:
                    print(f"Error reading proxy file: {str(e)}")
                    return []
                 #get text and conver to a list
            

            def test_proxy_speed(proxy_url):
                try:
                    start_time = time.time()
                    response = requests.get('http://google.com', proxies={'http': proxy_url, 'https': proxy_url}, timeout=5)#proxies paramter is a dictionary
                    end_time = time.time()
                    speed = end_time - start_time
                    return speed
                except Exception as e:
                    print(f"Error testing proxy {proxy_url}: {str(e)}")
                    return None

            def categorize_speed(speed):
                if speed is None:   #to help me identify the latency /speeds realtive to each other
                    return 'Error'
                elif speed < 1.0:
                    return 'Fast'
                elif speed < 5.0:
                    return 'Medium'
                else:
                    return 'Slow'

            def store_results_in_database(proxy_url, speed_category):
                connection = sqlite3.connect('proxies.db')
                cursor = connection.cursor()

                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS proxy_speeds (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        proxy_url TEXT,
                        speed_category TEXT
                    )
                ''')

                cursor.execute('SELECT * FROM proxy_speeds WHERE proxy_url = ?', (proxy_url,))
                existing_record = cursor.fetchone()
                if speed == ("Fast") or speed == ("Medium"):
                    if existing_record:
                        # If the record already exists, you may want to update it or skip the insert
                        print(f"Proxy with URL {proxy_url} already exists in the database.")
                    else:
                        cursor.execute('INSERT INTO proxy_speeds (proxy_url, speed_category) VALUES (?, ?)', (proxy_url, speed_category))
                        print(f"Proxy with URL {proxy_url} inserted into the database.")
                else:
                    print("not fast")

                connection.commit()
                connection.close()

            
            proxy_urls = self.textbox1.get("0.0", "end-1c").split("\n")
            print(proxy_urls[0]) 
            #list.append()
            
            for proxy_url in proxy_urls:
                if not proxy_url:
                    continue #considers if its an empty string
                if re.match(r'^[0-9.]*$',proxy_url) :
                    #continue
                    messagebox.showerror("Error","invalid proxy found skip and continue..?")
                speed = test_proxy_speed(proxy_url)
                speed_category = categorize_speed(speed)

                print(f"Proxy: {proxy_url}, Speed: {speed}, Category: {speed_category}")
                #for i, key in enumerate(new_frame_data.keys()): #creates multiple lables
                label = customtkinter.CTkLabel(self.test_result, text=f"Proxy: {proxy_url}, Speed: {speed}, Category: {speed_category}", fg_color="transparent")#improvemnt removed the key and only displayed data shown in key
                label.grid(row=0,column=proxy_urls.index(proxy_url) , padx=45, pady=20 ,sticky="w")
                    #self.labellist.append(label)

                store_results_in_database(proxy_url, speed_category)

                print("none")
            else :
                messagebox.showerror("Error","value should be an integer")
        self.textbox1 = customtkinter.CTkTextbox(self, width=400, corner_radius=0)
        self.textbox1.grid(row=1,column=1 ,padx=(20, 20), pady=(20, 10), sticky="nsew")
        self.textbox1.insert("0.0", "proxy!\n" * 10)
        self.test_result = customtkinter.CTkScrollableFrame(self, width=400, corner_radius=0)
        self.test_result.grid(row=1,column=2 ,padx=(20, 20), pady=(20, 10), sticky="nsew")
        
        self.proxy_tool= customtkinter.CTkFrame(self ,width=200, corner_radius=30, fg_color="grey10" )
        
        self.proxy_tool.grid(row=2, column=1,padx=(20, 20), pady=(10, 10), sticky="nsew")
        self.delete_proxy =customtkinter.CTkButton(self.proxy_tool,text="delete slow",command=remove_slow_proxies)
        self.delete_proxy.grid(row=1, column=1,padx=(20, 20), pady=(10, 10), sticky="nsew")
        self.test_proxy =customtkinter.CTkButton(self.proxy_tool,text="test",command= latency_proxies)
        self.test_proxy.grid(row=1, column=2,padx=(20, 20), pady=(10, 10), sticky="nsew")
        self.delete_proxy =customtkinter.CTkButton(self.proxy_tool,text="add from text file",command=latency_proxies)
        self.delete_proxy.grid(row=1, column=3,padx=(20, 20), pady=(10, 10), sticky="nsew")
        
class Add_task_window(customtkinter.CTkToplevel):
    def __init__(self,app,*args,**kwargs):
        super().__init__() ##inherits from ctktoplevel
        self.app = app 
        
        self.title("new task")
        self.geometry("700x110")
        self.grid_rowconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.entry=customtkinter.CTkEntry(self,placeholder_text= "newtask")
        self.entry.grid(row=3, column=0, columnspan=2, padx=(20,0), pady=(20, 20), sticky="nswe")
        self.schedule_time = customtkinter.CTkOptionMenu(self,dynamic_resizing=False,
        values=['0', '5', '10', '15', '20', '25', '30', '35', '40', '45', '50', '55', '60'])
        self.schedule_time.grid(row=3 ,column=2, padx=(20,0), pady=(20, 20), sticky="nswe")
        self.main_button_1 = customtkinter.CTkButton(self, fg_color="transparent", text="submit " ,border_width=2, text_color=("gray10", "#DCE4EE"),command=self.add_item_to_main_window)
        self.main_button_1.grid(row=3, column=3, padx=(0, 20), pady=(20, 20), sticky="nsew")
        
        self.optionmenu_1 = customtkinter.CTkOptionMenu(self, dynamic_resizing=False,
                                                values=["level1", "level2", "level3"])
        self.optionmenu_1.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.optionmenu_2 = customtkinter.CTkOptionMenu(self, dynamic_resizing=False,
                                                values=["sports direct", "zoolando", "footlocker"])
        self.optionmenu_2.grid(row=0, column=1, padx=20, pady=(20, 10))
        self.optionmenu_3 = customtkinter.CTkOptionMenu(self, dynamic_resizing=False,
                                                values=["4","5","6","7","8","9","10","11","12"])
        self.optionmenu_3.grid(row=0, column=3, padx=20, pady=(20, 10))
        self.optionmenu_4 = customtkinter.CTkComboBox(self, 
                                                values=["low", "medium", "high"])
        self.optionmenu_4.grid(row=0, column=2, padx=20, pady=(20, 10))
        self.optionmenu_1.set("priority")
        self.optionmenu_2.set("store")
        self.optionmenu_3.set("size")
        self.optionmenu_4.set("item")
        self.schedule_time.set("None")
    def add_item_to_main_window(self):
        if wifi_connection() ==True :
            schedule_state= self.schedule_time.get()
            print(schedule_state)
            print( str(time.gmtime()))
            # which takes the components of date as parameter
                # %Y - year
                # %m - month
                # %d - day
                # %H - Hours
                # %M - Minutes
                # %S - Seconds
            new_frame_data = {
                "store": self.optionmenu_2.get(),
                "priority": self.optionmenu_4.get(),  # Get value from entry field
                "size": self.optionmenu_3.get(),
                "item": (time.strftime('%Y-%m-%d %H:%M:%S')),  # Set a default value
                "status": "pending"
                }
        
            finish=time.perf_counter()
            print(finish-start)
            self.destroy()  # Close the Toplevel window after adding the item
            
            
            self.app.scrollable_task_frame.add_item(new_frame_data,schedule_state)#calls the method of scrollable scrollable_task_frame 
                                                                    #Wwhich is a a slave of the app class and child of the scollableTaskFrame
           

       
        else:
           
            self.no_wifi_label=customtkinter.CTkLabel(self.scrollable_task_frame,text="no wifi")
            self.no_wifi_label.grid(row=1, column=0, padx=15, pady=15, sticky="nswe")
   
class ScrollableTaskFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master,function,**kwargs):
        super().__init__(master, **kwargs)
        #task_manager = RunTaskManager()
        self.function=function
        self.frames_data = []
        
    #def task_db(self,new_frame_data):
        

    def add_item(self, new_frame_data,schedule_state):
      
        self.schedule_state=schedule_state
        print(self.schedule_state)
        connection = sqlite3.connect('tasks.db')
        cursor = connection.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                priority TEXT,
                store TEXT,
                size TEXT,
                item TEXT,
                status TEXT
            )
        ''')

        # Assuming self.optionmenu_1, self.optionmenu_2, self.entry, self.optionmenu_4 are valid attributes
        cursor.execute('INSERT INTO tasks (priority, store, size, item, status) VALUES (?, ?, ?, ?, ?)',
            (new_frame_data["priority"], new_frame_data["store"], new_frame_data["size"],
                new_frame_data["item"], new_frame_data["status"]))
        connection.commit()
        connection.close()
        new_frame = customtkinter.CTkFrame(self, width=200, corner_radius=30, fg_color="grey")
        new_frame.grid(row=len(self.frames_data), column=0, padx=15, pady=15, sticky="ns")
        #self.new_frame_data[store]()
        # adds the label horizontal where colums are i
        self.labellist=[]#store a refrence to the last label in a list as this is the only label that will change
        for i, key in enumerate(new_frame_data.keys()): #creates multiple lables
            label = customtkinter.CTkLabel(new_frame, text=f"{new_frame_data[key]}", fg_color="transparent")#improvemnt removed the key and only displayed data shown in key
            label.grid(row=0, column=i, padx=45, pady=20 ,sticky="w")
        self.labellist.append(label)#only adds the last label to list

        self.frames_data.append(new_frame_data)
        print(self.frames_data)
        print(self.schedule_state)
        #self.function(("sports_direct")) #run witjout doing so on new thread
        if self.schedule_state == ("None") :          
            self.store_thread = threading.Thread(target=self.function, args=(self,self.frames_data))
            self.store_thread.start()
        else:
            print(self.schedule_state)
            #timer = threading.Timer(delay_seconds, delayed_function)
            #timer.start()
          
            self.store_thread = threading.Timer(int(self.schedule_state) * 1000,self.function, args=(self,self.frames_data))
            #self.after( int(self.schedule_state) * 1000,self.store_thread.start())
            self.store_thread.start()
    def update(self,index,update):
        self.app = App #store refrence to the appp class where the change will be made
        # Update the 'status' key in the new_frame_data
        self.frames_data[index]["status"] = update #change the actual data
        print(self.frames_data[index])
        self.labellist[index].configure(text=update)#update the actaul frame
       
        self.store_thread.join #rejoin to the mainloop
        
        
    
        
class App(customtkinter.CTk):
    def __init__(self,):
        super().__init__()
        self.protocol("WM_DELETE_WINDOW", self.exit_app)
        
        
        self.title("APS.py")
        self.geometry("1500x550")
        self.loading()
        self.iconbitmap(r"C:\Users\musta\Downloads\New folder\bot.ico")
        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_images")
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_images")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "bot.ico")), size=(26, 26))
        self.large_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "large_test_image.png")), size=(500, 150))
        self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "image_icon_light.png")), size=(20, 20))
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "home_light.png")), size=(20, 20))
        self.chat_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "chat_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "chat_light.png")), size=(20, 20))
        self.add_user_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "add_user_dark.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "add_user_light.png")), size=(20, 20)) 
        #create navigation frame
        self.navcollapse = customtkinter.CTkFrame(self , width=250)
        
        self.navcollapse.grid(row=0, column=0, sticky="nsew")
        self.navcollapse.grid_rowconfigure(7, weight=1)
        self.navigation_frame = customtkinter.CTkTabview(self.navcollapse,width=5,height=20)
        self.navigation_frame.pack(padx=20, pady=20)
       
        self.navigation_frame.add("menue")
        self.navigation_frame.add("-")
        self.navigation_frame.set("menue")
        #
        self.navigation_frame.tab("-").grid_columnconfigure(0, weight=0)
        self.navigation_frame.tab("-").grid_rowconfigure(0, weight=0)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame.tab("menue"), text="  APS", image=self.home_image,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_frame_button = customtkinter.CTkButton(self.navigation_frame.tab("menue"), corner_radius=0, height=40, border_spacing=10, text="home",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=self.home_frame_button_event)
        self.home_frame_button.grid(row=1, column=0, sticky="ew")

        self.task_frame_button = customtkinter.CTkButton(self.navigation_frame.tab("menue"), corner_radius=0, height=40, border_spacing=10, text="tasks",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.add_user_image, anchor="w", command=self.task_frame_button_event)
        self.task_frame_button.grid(row=2, column=0, sticky="ew")

        self.frame_3_button = customtkinter.CTkButton(self.navigation_frame.tab("menue"), corner_radius=0, height=40, border_spacing=10, text="analtics",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.chat_image, anchor="w", command=self.frame_3_button_event)
        self.frame_3_button.grid(row=3, column=0, sticky="ew")
        self.proxy_frame_button = customtkinter.CTkButton(self.navigation_frame.tab("menue"), corner_radius=0, height=40, border_spacing=10, text="proxies",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.chat_image, anchor="w", command=self.proxy_frame_button_event)
        self.proxy_frame_button.grid(row=4, column=0, sticky="ew")
        self.profiles_frame_button = customtkinter.CTkButton(self.navigation_frame.tab("menue"), corner_radius=0, height=40, border_spacing=10, text="profiles",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.chat_image, anchor="w", command=self.profiles_frame_button_event)
        self.profiles_frame_button.grid(row=5, column=0, sticky="ew")
        
        self.settings_frame_button = customtkinter.CTkButton(self.navigation_frame.tab("menue"), corner_radius=0, height=40, border_spacing=10, text="settings",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.chat_image, anchor="w", command=self.settings_frame_button_event)
        self.settings_frame_button.grid(row=6, column=0, sticky="ew")

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame.tab("menue"), values=["Light", "Dark", "System"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=7, column=0, padx=20, pady=20)
        self.toplevel_captcha=None
        self.captcha_title = customtkinter.CTkButton(self.navigation_frame.tab("menue"), text="  captcha solver ",image=getimage(r"C:\Users\musta\Downloads\New folder\captcha\captchalogo.png"),
                                                             compound="left",command=self.open_input_captcha_event, font=customtkinter.CTkFont(size=15, weight="bold"))
        self.captcha_title.grid(row=8,  padx=(10, 2), pady=(10, 0), sticky="n") 


        # create home frame
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)
        self.home_frame.grid_rowconfigure(5, weight=1)
        with open("create.txt", "r") as x:
            line = x.readline()
            login_info = line.split()
            print (login_info)
            self.username= (login_info[1] )
            self.machine=login_info[2]
            self.liscence=login_info[3]
            print (self.liscence)
        self.welcome_frame = customtkinter.CTkFrame(self.home_frame, corner_radius=20 )
        self.welcome_frame.grid(row=0, column=0,padx=15, pady=15, sticky="nswe")
        self.user_info_label = customtkinter.CTkLabel(self.welcome_frame, text=(f"Welcome, {self.username}"),font=('arial', 44), text_color="grey" ,corner_radius=0)
        self.user_info_label.grid(row=1, column=0, padx=20, pady=0,sticky="n")
        self.device_frame = customtkinter.CTkFrame(self.home_frame, corner_radius=40 )
        self.device_frame.grid(row=1, column=0,padx=15, pady=15, sticky="nswe")
        self.device_frame.grid_columnconfigure(1,weight=1)
   
        self.user_info_label = customtkinter.CTkLabel(self.device_frame, text=(f"running on amchine:{self.machine}"),font=('arial', 22,),text_color="grey" ,anchor="center",corner_radius=0)
        self.user_info_label.grid(row=0, column=0, padx=40, pady=10,sticky="nswe")
        self.unbind_button =customtkinter.CTkButton(self.device_frame,corner_radius=20,  border_spacing=10, text="unbind",
                                                       text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=None, anchor="nswe", command=self.settings_frame_button_event)
        self.unbind_button.grid(row=2, columnspan=3, padx=15, pady=15, sticky="nswe")
        
        #self.unbind_button.grid_columnconfigure(0, weight=1)
        #self.machine_label
        #user name
        self.liscence_frame = customtkinter.CTkFrame(self.home_frame, corner_radius=40 )
        self.liscence_frame.grid(row=1, column=1,padx=15, pady=15, sticky="nswe")
        self.liscence_label = customtkinter.CTkLabel(self.liscence_frame, text=(f"{self.liscence}")
                                                     ,font=('arial', 22,),text_color="grey" ,anchor="center",corner_radius=0)
        self.liscence_label.grid(row=1, column=0, padx=40, pady=10,sticky="nswe")
        self.liscence = customtkinter.CTkOptionMenu(self.liscence_frame, values=["Light", "Dark", "System"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=7, column=0, padx=20, pady=20, sticky="w")
        

        
       

        # create second frame
        self.task_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.task_frame.grid_columnconfigure(0, weight=1)
        self.task_frame.grid_rowconfigure(1, weight=1)
        
        self.scrollable_task_frame = ScrollableTaskFrame(self.task_frame, width=700, function=self.sports_direct)# passes the ports function into ot
        self.scrollable_task_frame.grid(row=1, column=0, padx=15, pady=15, sticky="nswe")
              #new taskbutton frame
        self.scrollable_frame_heading = customtkinter.CTkFrame(self.task_frame,width=10,height=200,corner_radius=0)
        self.scrollable_frame_heading.grid(row=0, column=0,padx=15, pady=15, sticky="nswe")
        #self.scrollable_checkbox_frame1.grid_rowconfigure(0, weight=1)
        #self.scrollable_checkbox_frame1.grid_columnconfigure(0,7, weight=1)
              #newtaskbutton
        self.toplevel_window = None 
        self.newtask = customtkinter.CTkButton(self.scrollable_frame_heading, text="+",command= self.open_input_dialog_event)
        self.newtask.grid(row=0, column=7, padx=10, pady=10)
        #####key for top level window opening
        self.tasks_label1 = customtkinter.CTkLabel(self.scrollable_frame_heading, text="store  ", image=self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.tasks_label1.grid(row=0, column=0, padx=20, pady=20)
        self.tasks_label2 = customtkinter.CTkLabel(self.scrollable_frame_heading, text="product", image=self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.tasks_label2.grid(row=0, column=1, padx=20, pady=20)
        self.tasks_label3 = customtkinter.CTkLabel(self.scrollable_frame_heading, text="size", image=self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.tasks_label3.grid(row=0, column=2, padx=20, pady=20)
        self.tasks_label4 = customtkinter.CTkLabel(self.scrollable_frame_heading, text="price date/time", image=self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.tasks_label4.grid(row=0, column=3, padx=20, pady=20)
        self.tasks_label5 = customtkinter.CTkLabel(self.scrollable_frame_heading, text="status ", image=self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.tasks_label5.grid(row=0, column=4, padx=20, pady=20)
    
        # create third frame
        self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.charts = customtkinter.CTkTabview(self.third_frame , width=250)
        self.charts.grid(row=0, column=1, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.charts.add("checkouts")
        self.charts.add("expenditure")
        self.charts.add("both")
        self.charts.tab("checkouts").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.charts.tab("expenditure").grid_columnconfigure(0, weight=1)
        self.binomial_plt(("checkouts"))
        self.plot(("expenditure"))
        self.new_plot()
        self.circular(self.third_frame)
        


        #rescale for time interval
        #new analysis frame
        self.analysis = customtkinter.CTkFrame(self.third_frame , width=30,height=40,corner_radius=0)
        self.analysis.grid(row=0, column=0,padx=(20, 20), pady=(20, 20), sticky="ns")
        #self.analysis.grid_rowconfigure(0, weight=1)
        #self.analysis.grid_columnconfigure(0, weight=1)
        #self.text=("hello")
        
        
        #self.total_var = tk.StringVar()
        #self.total_var.set("total:0") 
        self.complete_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "complete.png")), size=(22, 22))
        self.failed_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "failed.png")), size=(22, 22))
        self.total_label = customtkinter.CTkLabel(self.analysis,textvariable=self.total_var, fg_color="grey25",corner_radius=45)
        self.total_label.grid(row=0,column=0,padx=(20,0), pady=(20, 20),sticky="w")
        self.completed_label = customtkinter.CTkLabel(self.analysis,textvariable=self.completed_var,image=self.complete_image,compound="right",fg_color="grey25",corner_radius=25)
        self.completed_label.grid(row=1,column=0,padx=(20,0), pady=(20, 20),sticky="w")
        self.failed_label = customtkinter.CTkLabel(self.analysis,textvariable=self.failed_var,image=self.failed_image,compound="right",fg_color="gray25",corner_radius=25)
        self.failed_label.grid(row=2,column=0,padx=(20,0), pady=(20, 20),sticky="w")
        self.entry=customtkinter.CTkEntry(self.analysis,placeholder_text= "search")
        self.entry.grid(row=3, column=0, columnspan=2, padx=(20,0), pady=(20, 20), sticky="nswe")
        self.main_button_1 = customtkinter.CTkButton(self.analysis, fg_color="transparent",text="enter" ,width=50,border_width=2, text_color=("gray10", "#DCE4EE"),command=self.refresh_search)
        self.main_button_1.grid(row=3, column=2, padx=(0, 20), pady=(20, 20), sticky="nsew")
        self.search_frame = customtkinter.CTkScrollableFrame(self.analysis, width=200, height=200)
        self.search_frame.grid(row=4,  columnspan=3, padx=(20, 20), pady=(20, 20), sticky="nsew")
        self.scrollable_frame_analytics = []
        self.listtemp=self.scrollable_frame_analytics
        connection = sqlite3.connect('tasks.db')
        cursor = connection.cursor()


        # Execute a SQL query to count the number of items
        query = "SELECT COUNT(*) FROM tasks "
        cursor.execute(query)

        # Fetch the result
        self.result = int(cursor.fetchone()[0])

        # Close the cursor and connection
        cursor.close()
        connection.close()
        print(self.result)
        for i in range(self.result):
            self.radiobutton_variable = customtkinter.StringVar()
            switch = customtkinter.CTkSwitch(master=self.search_frame, text=f"task {i}",command=self.analytic_task_edit)
            switch.grid(row=i, column=0, padx=10, pady=(0, 20))
            self.scrollable_frame_analytics.append(switch)
        
        # The initial update.
            #set the current filter to none so all content is displayed
        self.curr_filter = None
        
    
        

        self.proxy_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.proxy_frame.grid_columnconfigure(0, weight=1)
        self.proxy_frame.grid_rowconfigure(1, weight=1)
       
        self.proxy_info= proxy_dash(self.proxy_frame )
        self.proxy_info.grid(row=1, column=0,padx=(20, 20), pady=(20, 100), sticky="nsew")
        self.proxy_info.grid_columnconfigure(1, weight=1)
        self.proxy_info.grid_rowconfigure(1, weight=1)
       

        #profiles frame
        self.profiles_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.profiles_frame.grid_columnconfigure(0, weight=1)
        self.profiles_frame.grid_rowconfigure(0, weight=1)
        self.textbox1 = customtkinter.CTkTextbox(self.profiles_frame, width=400, corner_radius=0)
        self.textbox1.grid(row=0, column=0,padx=(20, 20), pady=(20, 10), sticky="nsew")
        self.user_info_frame = PurchaseApp(self.profiles_frame)
        self.user_info_frame.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")
       #6th frma
       
        self.settings_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.settings_frame.grid_columnconfigure(0, weight=1)
        self.settings_frame.grid_rowconfigure(1, weight=1)
        self.textbox1 = customtkinter.CTkTextbox(self.settings_frame, width=400, corner_radius=0)
        self.textbox1.grid(row=1, column=0,padx=(20, 20), pady=(20, 100), sticky="nsew")
        current_thread = threading.current_thread()
        print(f"My function is running on thread: {current_thread.name}")
        
        
        self.select_frame_by_name("settings_frame")
   
   
    def analytic_task_edit(self):
            print(f" frame modified: {self.switch.cget('text')}")
    import matplotlib.pyplot as plt
   
    def binomial_calc(self,x, n, p):
        """
        
        x= number of sucsess
        n= total numberof tasks
        p= probailty of success ( number succes/ number of tasks)
       
        Returns:
         -returns probablity
        """
        return math.comb(n, x) * (p ** x) * ((1 - p) ** (n - x))
    
    
    def binomial_plt(self,page):
        self.page=page
        # Set the parameters for the binomial distribution
        n = 10  # Number of trials
        p = 0.5  # Probability of success

        # Generate values for x (number of successes) and corresponding probabilities
        x = range(n+1)  # Number of successes (0 to n)
        probabilities = [self.binomial_calc(i, n, p) for i in x]

        # Create Matplotlib figure
        fig = Figure(figsize=(8, 6), dpi=100)
        plotb = fig.add_subplot(111)

        # Plot the binomial distribution as a bar chart
        plotb.bar(x, probabilities, label='Binomial Distribution', alpha=0.7)

        # Add labels and title
        plotb.set_xlabel('Number of Successes')
        plotb.set_ylabel('Probability')
        plotb.set_title('Binomial Distribution (n={}, p={})'.format(n, p))

        # Show legend
        plotb.legend()

        # Create Tkinter canvas containing the Matplotlib figure
        canvas = FigureCanvasTkAgg(fig, master=self.charts.tab(self.page))
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack()


        
            

           
    def new_plot(self):
            np.random.seed(42)

            # Move the creation of date_strings here
            start_date = date(2024, 1, 1)
            end_date = date(2024, 12, 31)
            date_list = [start_date + timedelta(days=x) for x in range((end_date - start_date).days + 1)]
            date_strings = [d.strftime("%Y-%m-%d") for d in date_list]

           # Create an instance of the RevenueData class
            revenue_instance = RevenueData(self.charts.tab("both"),date_strings)

            # Plot the revenue data
            revenue_instance.plot_revenue()

     

   
    def circular(self,page):
        pie_tasks = {
            "val_results": [472 ,356,278, 412, 550, 672],
            "results": ["total","completed", "failed", "cancelled", "clothes", "shoes"],
            "angles": [0, 1.04719, 2.094395, 3.141592, 4.18879, 5.23598],
            "rotation": [-90, -30, 30, 90, 330, 390, 450],
            "colors": ["#439A97", "#56a8a5", "#6cbdba", "#12b2ed", "#008fc4", "#0a7ca6"]
        }

        fig_2 = Figure(figsize=(12.5, 12.2),facecolor="#606060")
        ax_2 = fig_2.add_subplot(projection="polar")
        ax_2.set_facecolor("#DCE4EE")
       
        ax_2.bar(x=pie_tasks["angles"], height=pie_tasks["val_results"], color=pie_tasks["colors"],alpha=0.7)
        ax_2.set_frame_on(False)
        ax_2.set_xticks([])
        ax_2.tick_params(labelsize=12, colors="white")
        ax_2.grid(alpha=0.5)

        for angle, label, rotation in zip(pie_tasks["angles"], pie_tasks["results"], pie_tasks["rotation"]):
            ax_2.text(x=angle, y=max(pie_tasks["val_results"]) + 30, s=label, rotation=rotation, ha="center", va="center", color="black", fontsize=20)

        canvas = FigureCanvasTkAgg(figure=fig_2,master=page)
        #canvas.get_tk_widget().configure(background='black')
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column=2)
        #canvas.configure(background='black')
        
      
    def plot(self,page):
        self.page=page
        print(self.page)
        if self.page == "ditribuition" :
            self.loaded_coordinates = read_coordinates_from_file('coordinates.txt')

            # Unpack the coordinates into separate lists for x and y
            self.x_values, self.y_values = zip(*self.loaded_coordinates)
        #creat a slider for the user to drag
        self.slider_1 = customtkinter.CTkSlider(self.charts.tab(self.page), from_=0, to=1, number_of_steps=101)
        self.slider_1.grid(row=3, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        self.slider_1.configure(command=self.update_progress) #set it to run update if it is interacted with
        
        def save_coordinates_to_file(coordinates, filename):
            with open(filename, 'w') as file:
                for x, y in coordinates:
                    file.write(f"{x},{y}\n")

        # Function to read the coordinates from a text file
        def read_coordinates_from_file(filename):
            self.coordinates = []
            with open(filename, 'r') as file:
                for line in file:
                    x, y = map(float, line.strip().split(','))
                    self.coordinates.append((x, y))
            return self.coordinates

        # Create a list of coordinates (x, y)
        self.coordinates = [(1, 2), (3, 5), (5, 9), (7, 4), (9, 12)]

        # Save the coordinates to a text file
        save_coordinates_to_file(self.coordinates, 'coordinates.txt')

        # Read the coordinates from the text file
        self.loaded_coordinates = read_coordinates_from_file('coordinates.txt')

        # Unpack the coordinates into separate lists for x and y
        self.x_values, self.y_values = zip(*self.loaded_coordinates)

        # the figure that will contain the plot 
        self.fig = Figure(figsize = (20, 20), 
                                dpi = 60) 
     
        self.plot1 = self.fig.add_subplot(111)#max values on x axis 

        # plotting the graph 
       
        self.plot1.plot(self.x_values, self.y_values, marker='o', linestyle='-')
        # creating the Tkinter canvas 
        # containing the Matplotlib figure 
        self.canvas = FigureCanvasTkAgg(self.fig,self.charts.tab(self.page)) 
        self.canvas.draw() 

        # placing the canvas on the Tkinter window 
        self.canvas.get_tk_widget().grid(column = 0, row = 0)
        self.slider_1.bind("<Motion>", self.update_progress)
   
    def update_progress(self, event): 
        # Update the progress_level when the slider is moved
        self.progress_level = self.slider_1.get()
        # Update the plot based on slider
        # clear the previous plot and plot the new graph
        self.plot1.clear()
        # Check if progress_level is 0 to avoid division by zero
        if self.progress_level != 0:
            self.plot1.clear()
            x_values = [i for i in range(int(self.progress_level * 101))]
            y_values = [i**2 for i in range(int(self.progress_level * 101))]
          
            self.plot1.plot(x_values, y_values)
            self.canvas.draw()
        
        # Update the StringVar with the new value
        self.total_var.set(f"total: {100}")#btest if update of strvaraible
        self.failed_var.set(f"failed: {10}")
        self.completed_var.set(f"completed: {90}")
        self.loading()
    def update_status(self,index, new_status):
        self.new_status=new_status
        current_thread = threading.current_thread()
        print(f"My function is running on thread: {current_thread.name}")
        self.scrollable_task_frame.update(index, self.new_status)
        #new_status = self.model.frames_data[index]["status"]
        #self.labellist[index].config(text=new_status)
    def refresh_search(self):
        if self.entry.get() != self.curr_filter:
            # check if the contents of the filter box have changed.
            self.curr_filter = self.entry.get()

            # Refresh the scrollable frame.
            for switch in self.scrollable_frame_analytics:
                switch.grid_remove()

            # possible insertion sort on the price or retrieve d
            for switch in self.scrollable_frame_analytics:
                if self.curr_filter.lower() in switch.cget("text").lower():
                    switch.grid()

            self.after(250, self.on_tick)  # Use self.on_tick instead of on_tick

         # Call on_tick method with self
            
       
    def loading(self):
         #print("hello")
        
        
        #self.frames_data=[[1,2],[2,3]]
        self.total_var = tk.StringVar()
        self.total_var.set("total:0   ") 
        self.completed_var = tk.StringVar()
        self.completed_var.set("completed:0  ")
        self.failed_var = tk.StringVar()
        self.failed_var.set("failed:0  ")
        time.sleep(50)
        return True
        #for counter in range line
    # select default frame
    def unbind_device():
        print("h")
        
    
   
      
    def open_input_dialog_event(self):
        #self.toplevel_window.focus()
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = Add_task_window(self,function=self.sports_direct)

            
        else:
            self.toplevel_window.focus()
      
        
    def open_input_captcha_event(self):
        if self.toplevel_captcha is None or not self.toplevel_captcha.winfo_exists():
            self.toplevel_captcha = captcha()


        else:
            self.toplevel_window.focus()
        
            
               

            
        
   


    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_frame_button.configure(fg_color=("gray75", "gray25") if name == "home_frame" else "transparent")
        self.task_frame_button.configure(fg_color=("gray75", "gray25") if name == "task_frame" else "transparent")
        self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")
        self.proxy_frame_button.configure(fg_color=("gray75", "gray25") if name == "proxy_frame" else "transparent")
        self.profiles_frame_button.configure(fg_color=("gray75", "gray25") if name == "profiles_frame" else "transparent")
        self.settings_frame_button.configure(fg_color=("gray75", "gray25") if name == "settings_frame" else "transparent")
        

        # show selected frame
        if name == "home_frame":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "task_frame":
            self.task_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.task_frame.grid_forget()
        if name == "frame_3":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()
        if name == "proxy_frame":
            self.proxy_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.proxy_frame.grid_forget()
        if name == "profiles_frame":
            self.profiles_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.profiles_frame.grid_forget()
        if name == "settings_frame":
            self.settings_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.settings_frame.grid_forget()
    def home_frame_button_event(self):
        self.select_frame_by_name("home_frame")

    def task_frame_button_event(self):
        self.select_frame_by_name("task_frame")

    def frame_3_button_event(self):
        self.select_frame_by_name("frame_3")
    def proxy_frame_button_event(self):
        self.select_frame_by_name("proxy_frame")
    def profiles_frame_button_event(self):
        self.select_frame_by_name("profiles_frame")
    def settings_frame_button_event(self):
        self.select_frame_by_name("settings_frame")

    customtkinter.set_appearance_mode("dark")
      # Modes: "System" (standard), "Dark", "Light"
    customtkinter.set_default_color_theme("green") 
    def change_appearance_mode_event(self, new_appearance_mode):
            customtkinter.set_appearance_mode(new_appearance_mode)
    
    
    def sports_direct(self,fra,app_instance):
        if wifi_connection() ==True :
            # user_details = eval(cipher_suite.decrypt(self.user_info_frame.purchase_event()).decode())
            user_details = self.user_info_frame.purchase_event()
          #  first_name = user_details['user_details']['first_name']#retrievs the user info from the purhasce frame
            last_name = user_details['user_details']['last_name']#
            email= user_details['user_details']['email']
            city,street,number =user_details['shipping_details']['city'],user_details['shipping_details']['street'],user_details['user_details']['phone_number']
            
            #PROXY=self.proxy.select() #selects the correct rank proxy 
            
            try:
                item = self.frames_data[0]["item"]
               

                chrome_options = webdriver.ChromeOptions()
                #chrome_options.add_argument(f'--proxy-server={PROXY}')
                browser = webdriver.Chrome(options=chrome_options)
                

                browser.get('https://www.sportsdirect.com/')

                WebDriverWait(browser, 10).until(
                    EC.visibility_of_element_located((By.CSS_SELECTOR, '#onetrust-accept-btn-handler'))) #waits for the element to become visible
                browser.find_element(By.CSS_SELECTOR, '#onetrust-accept-btn-handler').click()#selcets it by its css value
                time.sleep(3) #waits to allow it to load
                search_box=browser.find_element(By.ID, 'txtSearch') #uses the ID to locate the element

                search_box.send_keys(item) #types in the item name
                time.sleep(2)  # Replace "shoe" with the actual shoe name you're looking for
                search_box.submit() #submits the details
                time.sleep(4)
                browser.find_element(By.CSS_SELECTOR, 'li:nth-child(1) .rtimg').click()
                time.sleep(4)
                browser.find_element(By.LINK_TEXT, f"8 (42.5)").click()
                time.sleep(7)
                browser.find_element(By.CSS_SELECTOR, '#ProductStandardAddToBag .addToBagInner').click()
                
                
                self.update_status(0, "basket") #updates the status of the task
                time.sleep(4)
                browser.find_element(By.ID, 'aCheckout').click()
                #current_thread = threading.current_thread()  !!check to ensure running on correct thread!!
                #print(f"My function is running on thread: {current_thread.name}")
              
                self.update_status(0, "checkout") #updates to checkout
                time.sleep(3)
                #print(user_details[First_Name])
                browser.find_element(By.CSS_SELECTOR, '#Login_EmailAddress').send_keys(email)
                time.sleep(3)
                   
                browser.find_element(By.CSS_SELECTOR, '.formCompleteCTA > button').click()
                time.sleep(2)
                WebDriverWait(browser, 5).until(
                EC.visibility_of_element_located((By.LINK_TEXT,'No thanks, continue without signing in')))
                browser.find_element(By.LINK_TEXT,'No thanks, continue without signing in').click()
                time.sleep(3)
                browser.find_element(By.CSS_SELECTOR, '.singleLine span').click()
                time.sleep(2)
                #submits name and address line
                browser.find_element(By.CSS_SELECTOR, '.formCompleteCTA > button').click()
                time.sleep(2)
                browser.find_element(By.ID,'firstName').click()
                browser.find_element(By.ID,'firstName').send_keys(first_name)
                time.sleep(3)
                browser.find_element(By.ID,'lastName').click()
                browser.find_element(By.ID,'lastName').send_keys(last_name)
                time.sleep(3)
                browser.find_element(By.ID,'contactNumber').send_keys(number)

                time.sleep(3)
                
                browser.find_element(By.ID,'line1').click()
                browser.find_element(By.ID, 'line1').send_keys(street,"",city )
                time.sleep(10)
            except Exception as e:
                self.update_status(0, "error ",e)
                print(browser.current_url)
                #updates the task in the scrollable frame if 
                #the task isn't processed completely

        else:
            self.no_wifi_label=customtkinter.CTkLabel(self.scrollable_task_frame,text="no wifi")#update the scrollable task frame with error message
            self.no_wifi_label.grid(row=1, column=0, padx=15, pady=15, sticky="nswe")
    def exit_app(self):
        result = messagebox.askokcancel("Exit", "Do you really want to exit?")
        if result:
            self.destroy()
    print("hel")   
    
    def run_scheduler(self):
        # Run the scheduler app.run_scheduler()
        while True:
            schedule.run_pending()#changed for sleep of the task

            
if __name__ == "__main__":
    #log = login()
    
    
    #l#og.mainloop()
    
    #log.destroy()
    app = App()
    app.mainloop()
