import customtkinter
import pywinstyles
import os
from PIL import Image
from selenium import webdriver
from random import randint
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

import tkinter as tk
from matplotlib.figure import Figure  
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)

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
        self.optionmenu_3.grid(row=0, column=2, padx=20, pady=(20, 10))
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
            "size": self.entry.get(),
            "item": self.optionmenu_4.get(),  # Set a default value
            "status": "Value 1"
            }
        
        self.destroy()  # Close the Toplevel window after adding the item
        self.app.scrollable_task_frame.add_item(new_frame_data)

class ScrollableTaskFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master,function, **kwargs):
        super().__init__(master, **kwargs)
        #task_manager = RunTaskManager()
        self.function=function
        self.frames_data = []
        
    def add_item(self, new_frame_data):
        start = time.perf_counter()
        new_frame = customtkinter.CTkFrame(self, width=200, corner_radius=30, fg_color="grey")
        new_frame.grid(row=len(self.frames_data), column=0, padx=15, pady=15, sticky="ns")
       

        for i, key in enumerate(new_frame_data.keys()):
            label = customtkinter.CTkLabel(new_frame, text=f"{key}: {new_frame_data[key]}", fg_color="transparent")
            label.grid(row=0, column=i, padx=20, pady=20)

        self.frames_data.append(new_frame_data)
        finish = time.perf_counter()
        print(finish-start)
        print(self.frames_data)
        self.function(("hee"))
        

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("image_example.py")
        self.geometry("1000x450")

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_images")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "CustomTkinter_logo_single.png")), size=(26, 26))
        self.large_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "large_test_image.png")), size=(500, 150))
        self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "image_icon_light.png")), size=(20, 20))
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "home_light.png")), size=(20, 20))
        self.chat_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "chat_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "chat_light.png")), size=(20, 20))
        self.add_user_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "add_user_dark.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "add_user_light.png")), size=(20, 20))

        #create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="  Image Example", image=self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Home",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="tasks",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.add_user_image, anchor="w", command=self.frame_2_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")

        self.frame_3_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="analtics",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.chat_image, anchor="w", command=self.frame_3_button_event)
        self.frame_3_button.grid(row=3, column=0, sticky="ew")
        self.frame_4_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="proxies",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.chat_image, anchor="w", command=self.frame_4_button_event)
        self.frame_4_button.grid(row=4, column=0, sticky="ew")

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["Light", "Dark", "System"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="n")

        # create home frame
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)
        self.home_frame.grid_rowconfigure(5, weight=1)
        self.home_frame_large_image_label = customtkinter.CTkLabel(self.home_frame, text="", image=self.large_test_image)
        self.home_frame_large_image_label.grid(row=6, column=0, padx=20, pady=0,sticky="n")

        self.home_frame_button_1 = customtkinter.CTkButton(self.home_frame, text="", image=self.image_icon_image)
        self.home_frame_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.home_frame_button_2 = customtkinter.CTkButton(self.home_frame, text="CTkButton", image=self.image_icon_image, compound="right")
        self.home_frame_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.home_frame_button_3 = customtkinter.CTkButton(self.home_frame, text="CTkButton", image=self.image_icon_image, compound="top")
        self.home_frame_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.home_frame_button_4 = customtkinter.CTkButton(self.home_frame, text="CTkButton", image=self.image_icon_image, compound="bottom", anchor="w")
        self.home_frame_button_4.grid(row=4, column=0, padx=20, pady=10)

        # create second frame
        self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.second_frame.grid_columnconfigure(0, weight=1)
        self.second_frame.grid_rowconfigure(1, weight=1)
        
        self.scrollable_task_frame = ScrollableTaskFrame(self.second_frame, width=700, function=nike)# passes the nike function into ot
        self.scrollable_task_frame.grid(row=1, column=0, padx=15, pady=15, sticky="nswe")
              #new taskbutton frame
        self.scrollable_checkbox_frame1 = customtkinter.CTkFrame(self.second_frame,width=10,height=200,corner_radius=0)
        self.scrollable_checkbox_frame1.grid(row=0, column=0,padx=15, pady=15, sticky="nswe")
        #self.scrollable_checkbox_frame1.grid_rowconfigure(0, weight=1)
        #self.scrollable_checkbox_frame1.grid_columnconfigure(0,7, weight=1)
              #newtaskbutton

        self.newtask = customtkinter.CTkButton(self.scrollable_checkbox_frame1, text="+",command= self.open_input_dialog_event)
        self.newtask.grid(row=0, column=7, padx=10, pady=10)
        self.toplevel_window = None
        self.tasks_label1 = customtkinter.CTkLabel(self.scrollable_checkbox_frame1, text="store  ", image=self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.tasks_label1.grid(row=0, column=0, padx=20, pady=20)
        self.tasks_label2 = customtkinter.CTkLabel(self.scrollable_checkbox_frame1, text="product", image=self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.tasks_label2.grid(row=0, column=1, padx=20, pady=20)
        self.tasks_label3 = customtkinter.CTkLabel(self.scrollable_checkbox_frame1, text="size", image=self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.tasks_label3.grid(row=0, column=2, padx=20, pady=20)
        self.tasks_label4 = customtkinter.CTkLabel(self.scrollable_checkbox_frame1, text="price date/time", image=self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.tasks_label4.grid(row=0, column=3, padx=20, pady=20)
        self.tasks_label5 = customtkinter.CTkLabel(self.scrollable_checkbox_frame1, text="status ", image=self.logo_image,
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
        self.analysis.grid(row=0, column=0,padx=(20, 20), pady=(20, 0), sticky="ns")
        self.analysis.grid_rowconfigure(0, weight=1)
        self.analysis.grid_columnconfigure(0, weight=1)
        
            #print(self.progress_level)
         #creat 4th frame
        self.fourth_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.fourth_frame.grid_columnconfigure(0, weight=1)
        self.fourth_frame.grid_rowconfigure(1, weight=1)
        self.textbox1 = customtkinter.CTkTextbox(self.fourth_frame, width=400, corner_radius=0)
        self.textbox1.grid(row=1, column=0,padx=(20, 20), pady=(20, 100), sticky="nsew")
        self.textbox1.insert("0.0", "proxy!\n" * 50)
        self.select_frame_by_name("home")
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
    
    # select default frame
    
    def open_input_dialog_event(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = Toplevelwindow(self,function=nike)
        else:
            self.toplevel_window.focus()
    def checkbox_frame_event(self):
        print(f"checkbox frame modified: {self.scrollable_checkbox_frame.get_checked_items()}")


    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
        self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")
        self.frame_4_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")

        # show selected frame
        if name == "home":
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
        if name == "frame_4":
            self.fourth_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.fourth_frame.grid_forget()
    def home_button_event(self):
        self.select_frame_by_name("home")

    def frame_2_button_event(self):
        self.select_frame_by_name("frame_2")

    def frame_3_button_event(self):
        self.select_frame_by_name("frame_3")
    def frame_4_button_event(self):
        self.select_frame_by_name("frame_4")
    #def frame_4_button_event(self):
     #    self.select_frame_by_name("frame_4")


    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

def nike(word):
    #chrome_options = Options()
    #chrome_options.add_argument('--headless')
    #chrome_options.add_argument(f'--proxy-server=http://91.189.177.186:3128')
    #chrome_options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')

    #chrome_options.add_argument('--enable-logging')
    driver = webdriver.Chrome()
    driver.get("https://myexternalip.com/raw")
    driver.implicitly_wait(350)
    ##search_box = driver.find_element(By.XPATH,"xpath=//div[@id='gen-nav-commerce-header-v2']/div[3]/header/div/div[2]/div/div/div/div/div/button[2]")
    
    #search_box.click()
    #search_box.send_keys("FJ7098-301")  # Replace "shoe" with the actual shoe name you're looking for
    #search_box.send_keys(Keys.RETURN)
    print(word)
#def runtask():
 #    [self.new_frame_data[store]]()
 

if __name__ == "__main__":
    app = App()
    pywinstyles.apply_style(app, 'acrylic')#dark", "mica", "aero", "transparent", "acrylic", "win7",
                 # "inverse", "popup", "native", "optimised", "light", "normal"#
    app.mainloop()
