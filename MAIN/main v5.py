import customtkinter
import pywinstyles
import os
from PIL import Image
from selenium import webdriver
from random import randint

#import undetected_chromedriver as uc
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
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
customtkinter.set_appearance_mode("Light")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

def wifi_connection():
    print ("no wifif")


#loginv2.loginpy()
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
        self.first_name_checkbox = customtkinter.CTkCheckBox(self.user_info_frame, text="random")
        self.first_name_checkbox.grid(row=0, column=4, pady=0)
        self.email_label = customtkinter.CTkLabel(self.user_info_frame, text="email:")
        self.email_label.grid(row=2, column=0, pady=5,padx=5, sticky="w")
        self.email_entry = customtkinter.CTkEntry(self.user_info_frame,placeholder_text="enidblighton@gmail.com")
        self.email_entry.grid(row=2, column=1, pady=5, padx=10)


        self.last_name_label = customtkinter.CTkLabel(self.user_info_frame, text="Last Name:")
        self.last_name_label.grid(row=2, column=2, pady=5,padx=5, sticky="w")
        self.last_name_entry = customtkinter.CTkEntry(self.user_info_frame,placeholder_text="smith")
        self.last_name_entry.grid(row=2, column=3, pady=5, padx=10)
        self.last_name_checkbox = customtkinter.CTkCheckBox(self.user_info_frame, text="random")
        self.last_name_checkbox.grid(row=2, column=4, pady=0)

        self.phone_number_label = customtkinter.CTkLabel(self.user_info_frame, text="Phone Number:")
        self.phone_number_label.grid(row=3, column=0, pady=5,padx=5, sticky="w" )
        self.phone_prefix_values = ["+1", "+44", "+49", "+61"]  # Add more prefixes as needed
        self.phone_prefix_combo = customtkinter.CTkOptionMenu(self.user_info_frame, values=self.phone_prefix_values )
        self.phone_prefix_combo.grid(row=3, column=1, pady=5,padx=5, sticky="w" )
        self.phone_number_entry = customtkinter.CTkEntry(self.user_info_frame,placeholder_text="075463778" )
        self.phone_number_entry.grid(row=3, column=2, pady=0, padx=10)
        self.phone_number_checkbox = customtkinter.CTkCheckBox(self.user_info_frame, text="random")
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
        self.purchase_button = customtkinter.CTkButton(self, text="Purchase", command=self.purchase_event)
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
        first_name = self.first_name_entry.get() if not self.first_name_checkbox.var.get() else ""
        last_name = self.last_name_entry.get() if not self.last_name_checkbox.var.get() else ""
        phone_number = self.phone_number_entry.get()
        postcode = self.postcode_entry.get()

        # Retrieve shipping details
        country = self.country_combo.get()
        city = self.city_entry.get()
        street = self.street_entry.get()

        # Retrieve billing details
        billing_city = self.billing_city_entry.get() if not self.replicate_checkbox.var.get() else city
        billing_street = self.billing_street_entry.get() if not self.replicate_checkbox.var.get() else street

        # Retrieve card details
        card_number = self.card_number_entry.get()
        card_expiry_month = self.card_expiry_month_combo.get()
        card_expiry_year = self.card_expiry_year_combo.get()
        card_cvv = self.card_cvv_entry.get()

        # connect to main function
        purchase_details = f"Purchase Details:\nProfile Name: {profile_name}\nFirst Name: {first_name}\nLast Name: {last_name}\nPhone Number: {phone_number}\nPostcode: {postcode}\n\nShipping Details:\nCountry: {country}\nCity: {city}\nStreet: {street}\n\nBilling Details:\nBilling City: {billing_city}\nBilling Street: {billing_street}\n\nCard Details:\nCard Number: {card_number}\nCard Expiry: {card_expiry_month}/{card_expiry_year}\nCVV: {card_cvv}"
        print(purchase_details)

class proxy_dash(customtkinter.CTkFrame):
     def __init__(self, master,**kwargs):
        super().__init__(master, **kwargs)
        def remove_slow_proxies(self):
                connection = sqlite3.connect('proxies.db')
                cursor = connection.cursor()

                cursor.execute("SELECT proxy_url FROM proxy_speeds WHERE speed_category='Slow'")
                slow_proxies = cursor.fetchall()

                for proxy_url in slow_proxies:
                    print(f"Removing slow proxy: {proxy_url[0]}")
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
                    response = requests.get('http://google.com', proxies={'http': proxy_url, 'https': proxy_url}, timeout=5)
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

                cursor.execute('INSERT INTO proxy_speeds (proxy_url, speed_category) VALUES (?, ?)', (proxy_url, speed_category))

                connection.commit()
                connection.close()

            proxy_urls = (self.textbox1.get("0.0",("end-1c").split("\n")))
            print(proxy_urls[0])#
            proxy_urls = self.textbox1.get("0.0", "end-1c").split("\n")
            print(proxy_urls[0]) 
            #list.append()
            for proxy_url in proxy_urls:
                if not proxy_url:
                    continue
                speed = test_proxy_speed(proxy_url)
                speed_category = categorize_speed(speed)

                print(f"Proxy: {proxy_url}, Speed: {speed}, Category: {speed_category}")

                store_results_in_database(proxy_url, speed_category)

                print("none")
        self.textbox1 = customtkinter.CTkTextbox(self, width=400, corner_radius=0)
        self.textbox1.grid(row=1,column=1 ,padx=(20, 20), pady=(20, 10), sticky="nsew")
        self.textbox1.insert("0.0", "proxy!\n" * 10)
        #proxy_urls = list((self.textbox1.get()).split(""))
        #print (self.textbox1.get("0.0","end"))
        self.proxy_tool= customtkinter.CTkFrame(self ,width=200, corner_radius=30, fg_color="grey10" )
        
        self.proxy_tool.grid(row=2, column=1,padx=(20, 20), pady=(10, 10), sticky="nsew")
        self.delete_proxy =customtkinter.CTkButton(self.proxy_tool,text="delete slow",command=remove_slow_proxies)
        self.delete_proxy.grid(row=1, column=1,padx=(20, 20), pady=(10, 10), sticky="nsew")
        self.test_proxy =customtkinter.CTkButton(self.proxy_tool,text="test",command= latency_proxies)
        self.test_proxy.grid(row=1, column=2,padx=(20, 20), pady=(10, 10), sticky="nsew")
        self.delete_proxy =customtkinter.CTkButton(self.proxy_tool,text="add",state="disabled")
        self.delete_proxy.grid(row=1, column=3,padx=(20, 20), pady=(10, 10), sticky="nsew")
        
class Toplevelwindow(customtkinter.CTkToplevel):
    def __init__(self,app,*args,**kwargs):
        super().__init__()
        self.app = app
        
        self.title("new task")
        self.geometry("700x110")
        
        self.grid_rowconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.entry=customtkinter.CTkEntry(self,placeholder_text= "newtask")
        self.entry.grid(row=3, column=0, columnspan=2, padx=(20,0), pady=(20, 20), sticky="nswe")
        self.main_button_1 = customtkinter.CTkButton(self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"),command=self.add_item_to_main_window)
        self.main_button_1.grid(row=3, column=3, padx=(0, 20), pady=(20, 20), sticky="nsew")
        
        self.optionmenu_1 = customtkinter.CTkOptionMenu(self, dynamic_resizing=False,
                                                values=["level1", "level2", "level3"])
        self.optionmenu_1.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.optionmenu_2 = customtkinter.CTkOptionMenu(self, dynamic_resizing=False,
                                                values=["nike", "zoolando", "footlocker"])
        self.optionmenu_2.grid(row=0, column=1, padx=20, pady=(20, 10))
        self.optionmenu_3 = customtkinter.CTkOptionMenu(self, dynamic_resizing=False,
                                                values=["4","5","6","7","8","9","10","11","12"])
        self.optionmenu_3.grid(row=0, column=3, padx=20, pady=(20, 10))
        self.optionmenu_4 = customtkinter.CTkComboBox(self, 
                                                values=["level1", "level2", "level3"])
        self.optionmenu_4.grid(row=0, column=2, padx=20, pady=(20, 10))
        self.optionmenu_1.set("priority")
        self.optionmenu_2.set("store")
        self.optionmenu_3.set("size")
        self.optionmenu_4.set("item")
    def add_item_to_main_window(self):
        new_frame_data = {
            "priority": self.optionmenu_1.get(),
            "store": self.optionmenu_2.get(),  # Get value from entry field
            "size": self.optionmenu_3.get(),
            "item": self.optionmenu_4.get(),  # Set a default value
            "status": "pending"
            }
       
        
        self.destroy()  # Close the Toplevel window after adding the item
        self.app.scrollable_task_frame.add_item(new_frame_data)
    #def update_items(self,index):
     #   return newframedata for checkbox in self.checkbox_list if {key}: {new_frame_data[key]} == len(self.frames_data)]
class ScrollableTaskFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master,function, **kwargs):
        super().__init__(master, **kwargs)
        #task_manager = RunTaskManager()
        self.function=function
        self.frames_data = []
    #def task_db(self,new_frame_data):
        

    def add_item(self, new_frame_data):
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
        self.labellist=[]
        for i, key in enumerate(new_frame_data.keys()): #creates multiple lables
            label = customtkinter.CTkLabel(new_frame, text=f"{new_frame_data[key]}", fg_color="transparent")#removed the key and only displayed data shown in key
            label.grid(row=0, column=i, padx=20, pady=20)
        self.labellist.append(label)#only adds the last label to list

        self.frames_data.append(new_frame_data)
        print(self.frames_data)
        
        #self.function(("nike"))
        self.nike_thread = threading.Thread(target=self.function, args=(self,self.frames_data))
        self.nike_thread.start()
    def update(self,index,update):
        self.app = app
        # Get the task frame at the specified index
        #self.task_frame = self.frames_data[index]

        # Update the 'status' key in the new_frame_data
        self.frames_data[index]["status"] = update
        print(self.frames_data[index])
        self.labellist[index].configure(text=update)
        #self.app.scrollable_task_frame.add_item((self.frames_data[index]))
        ##new_frame = customtkinter.CTkFrame(app.scrollable_task_frame, width=200, corner_radius=0, fg_color="grey")
        ##new_frame.grid(row=(index), column=0, padx=15, pady=15, sticky="ns")
        #self.new_frame_data[store]()
        # adds the label horizontal where colums are i
        ##label = customtkinter.CTkLabel(new_frame, text=f"{self.frames_data[index]["status"]}", fg_color="transparent")
        ##label.grid(row=index, column=4, padx=20, pady=20)
        self.nike_thread.join
        # Update the text of the status label
        #self.task_frame["status_label"].config(text=f"Status: {new_status}")"""
        
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("APS.py")
        self.geometry("1100x550")
        self.loading()
        self.iconbitmap(r"C:\Users\musta\Downloads\New folder\bot.ico")
        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.focus()
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

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame.tab("menue"), text="  APS", image=self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_frame_button = customtkinter.CTkButton(self.navigation_frame.tab("menue"), corner_radius=0, height=40, border_spacing=10, text="home",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=self.home_frame_button_event)
        self.home_frame_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame.tab("menue"), corner_radius=0, height=40, border_spacing=10, text="tasks",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.add_user_image, anchor="w", command=self.frame_2_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")

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

        # create home frame
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)
        self.home_frame.grid_rowconfigure(5, weight=1)
        with open("create.txt", "r") as x:
            line = x.readline()
            login_info = line.split()
            print (login_info)
            self.username= (login_info[1]  )
            self.liscence=login_info[3]
            print (self.liscence)
        self.welcome_frame = customtkinter.CTkFrame(self.home_frame, corner_radius=20 )
        self.welcome_frame.grid(row=0, column=0,padx=15, pady=15, sticky="nswe")
        self.user_info_label = customtkinter.CTkLabel(self.welcome_frame, text=(f"Welcome, {self.username}"),font=('arial', 44), text_color="grey" ,corner_radius=0)
        self.user_info_label.grid(row=1, column=0, padx=20, pady=0,sticky="n")
        self.device_frame = customtkinter.CTkFrame(self.home_frame, corner_radius=40 )
        self.device_frame.grid(row=1, column=0,padx=15, pady=15, sticky="nswe")
        self.device_frame.grid_columnconfigure(1,weight=1)
   
        self.user_info_label = customtkinter.CTkLabel(self.device_frame, text=(f"{self.liscence}Wmachine1HU90"),font=('arial', 22,),text_color="grey" ,anchor="center",corner_radius=0)
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
        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.liscence_frame, values=["Light", "Dark", "System"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=7, column=0, padx=20, pady=20, sticky="w")

        
       

        # create second frame
        self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.second_frame.grid_columnconfigure(0, weight=1)
        self.second_frame.grid_rowconfigure(1, weight=1)
        
        self.scrollable_task_frame = ScrollableTaskFrame(self.second_frame, width=700, function=self.nike)# passes the nike function into ot
        self.scrollable_task_frame.grid(row=1, column=0, padx=15, pady=15, sticky="nswe")
              #new taskbutton frame
        self.scrollable_frame_heading = customtkinter.CTkFrame(self.second_frame,width=10,height=200,corner_radius=0)
        self.scrollable_frame_heading.grid(row=0, column=0,padx=15, pady=15, sticky="nswe")
        #self.scrollable_checkbox_frame1.grid_rowconfigure(0, weight=1)
        #self.scrollable_checkbox_frame1.grid_columnconfigure(0,7, weight=1)
              #newtaskbutton

        self.newtask = customtkinter.CTkButton(self.scrollable_frame_heading, text="+",command= self.open_input_dialog_event)
        self.newtask.grid(row=0, column=7, padx=10, pady=10)
        self.toplevel_window = None
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
        self.plot(("checkouts"))

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
        self.main_button_1 = customtkinter.CTkButton(self.analysis, fg_color="transparent",text="enter" ,width=50,border_width=2, text_color=("gray10", "#DCE4EE"))
        self.main_button_1.grid(row=3, column=2, padx=(0, 20), pady=(20, 20), sticky="nsew")
        self.search_frame = customtkinter.CTkScrollableFrame(self.analysis, width=200, height=200)
        self.search_frame.grid(row=4,  columnspan=3, padx=(20, 20), pady=(20, 20), sticky="nsew")
        


        #credit flaticon pixelperfect hqrloveq
            #print(self.progress_level)
         #creat 4th frame
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
    
    def plot(self,page):
        self.page=page
        print(self.page)
        
        #self.chart1 = customtkinter.CTkFrame(self, width=4,height=4,corner_radius=0)
        #self.chart1.grid_rowconfigure(0, weight=0)
        #self.chart1.grid_columnconfigure(0, weight=0)
        self.slider_1 = customtkinter.CTkSlider(self.charts.tab(self.page), from_=0, to=1, number_of_steps=101)
        self.slider_1.grid(row=3, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        self.slider_1.configure(command=self.update_progress) #command=self.progressbar_1.set
        #self.progressbar_1 = customtkinter.CTkProgressBar(self.charts.tab(self.page))
        #self.progressbar_1.grid(row=2, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        
    
        #self.progress_level = self.progressbar_1.get()
        #print(self.progress_level)
        def save_coordinates_to_file(coordinates, filename):
            with open(filename, 'w') as file:
                for x, y in coordinates:
                    file.write(f"{x},{y}\n")

        # Function to read the coordinates from a text file
        def read_coordinates_from_file(filename):
            coordinates = []
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
        self.fig = Figure(figsize = (10, 10), 
                                dpi = 60) 
        #print([i**2 for i in range(101)])
        # list of squares 
        #self.y = [i**2 for i in range(101)]  #gives y cordinates i**2 for i in range(101)

        # adding the subplot 
        self.plot1 = self.fig.add_subplot(111)#max values on x axis 

        # plotting the graph 
        #self.plot1.plot(self.y) 
        self.plot1.plot(self.x_values, self.y_values, marker='o', linestyle='-')
        # creating the Tkinter canvas 
        # containing the Matplotlib figure 
        self.canvas = FigureCanvasTkAgg(self.fig,self.charts.tab(self.page)) 
        self.canvas.draw() 

        # placing the canvas on the Tkinter window 
        self.canvas.get_tk_widget().grid(column = 0, row = 0)
        #print(self.progress_level)
        self.slider_1.bind("<Motion>", self.update_progress)
    def binomial_distribuition():
        print("h")
    def update_progress(self, event): 
        # Update the progress_level when the slider is moved
        self.progress_level = self.slider_1.get()
        # Update your plot based on the progress level
        # For example, clear the previous plot and plot the new data
        self.plot1.clear()
        # Check if progress_level is 0 to avoid division by zero
        if self.progress_level != 0:
            self.plot1.clear()
            x_values = [i for i in range(int(self.progress_level * 101))]
            y_values = [i**2 for i in range(int(self.progress_level * 101))]
            self.plot1.clear()
            self.plot1.plot(x_values, y_values)
            self.canvas.draw()
        
        # Update the StringVar with the new value
        self.total_var.set(f"total: {"10!"}")#btest if update of strvaraible
        self.loading()
    def update_status(self,index, new_status):
        current_thread = threading.current_thread()
        print(f"My function is running on thread: {current_thread.name}")
        self.scrollable_task_frame.update(index, new_status)
        #new_status = self.model.frames_data[index]["status"]
        #self.labellist[index].config(text=new_status)



    def loading(self):
         #print("hello")
        
        
        #self.frames_data=[[1,2],[2,3]]
        self.total_var = tk.StringVar()
        self.total_var.set("total:0   ") 
        self.completed_var = tk.StringVar()
        self.completed_var.set("completed:0  ")
        self.failed_var = tk.StringVar()
        self.failed_var.set("failed:0  ")
       
        #for counter in range line
    # select default frame
    def unbind_device():
        print("h")
        
    
    def open_input_dialog_event(self):
        #self.toplevel_window.focus()
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = Toplevelwindow(self,function=self.nike)

            
        else:
            self.toplevel_window.focus()
    


    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_frame_button.configure(fg_color=("gray75", "gray25") if name == "home_frame" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
        self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")
        self.proxy_frame_button.configure(fg_color=("gray75", "gray25") if name == "proxy_frame" else "transparent")
        self.profiles_frame_button.configure(fg_color=("gray75", "gray25") if name == "profiles_frame" else "transparent")
        self.settings_frame_button.configure(fg_color=("gray75", "gray25") if name == "settings_frame" else "transparent")
        

        # show selected frame
        if name == "home_frame":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "frame_2":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
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

    def frame_2_button_event(self):
        self.select_frame_by_name("frame_2")

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

    def nike(self,fra,app_instance):
        

        email = "air max 95 men"
        #index =fra

        """chrome_options = webdriver.ChromeOptions()
        
        browser = webdriver.Chrome(options=chrome_options)

        browser.get('https://www.sportsdirect.com/')

        WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '#onetrust-accept-btn-handler')))
        browser.find_element(By.CSS_SELECTOR, '#onetrust-accept-btn-handler').click()
        time.sleep(7)
        search_box=browser.find_element(By.ID, 'txtSearch')

        search_box.send_keys(email)
        time.sleep(2)  # Replace "shoe" with the actual shoe name you're looking for
        search_box.submit()
        time.sleep(4)
        browser.find_element(By.CSS_SELECTOR, 'li:nth-child(1) .rtimg').click()
        time.sleep(4)
        browser.find_element(By.LINK_TEXT, '8 (42.5)').click()
        time.sleep(5)
        browser.find_element(By.CSS_SELECTOR, '#ProductStandardAddToBag .addToBagInner').click()
        #id="aAddToBag"
        time.sleep(4)
        browser.find_element(By.ID, 'aCheckout').click()"""
        current_thread = threading.current_thread()
        print(f"My function is running on thread: {current_thread.name}")
        #self.nike_thread.join()
        app.update_status(0, "status")
        #self.app_instance.root.after(0, lambda: self.app_instance.update_status("Status: Task Completed"))
        #threading.Thread(target=self.continue_function).start()
       
        new_frame_data = {
                "priority": "Priority Value",
                "store": "Store Value",
                "size": "Size Value",
                "item": "Item Value",
                "status": "Checkout Completed"
            }
        #gui_instance.queue.put(new_frame_data)
    

if __name__ == "__main__":
    app = App()
    pywinstyles.apply_style(app, 'aero')
    app.mainloop()
