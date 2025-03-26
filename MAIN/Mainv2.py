import customtkinter
import pywinstyles
import os
from PIL import Image
class Toplevelwindow(customtkinter.CTkToplevel):
    def __init__(self,master,*args,**kwargs):
        super().__init__()
       # self.app = app
        
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
            "priority": "Value 1",
            "store": self.entry.get(),  # Get value from entry field
            "size": "Value 1",
            "item": "Pending",  # Set a default value
            "status": "Value 1"
            }
        self.app.scrollable_task_frame.add_item(new_frame_data)
        self.destroy()  # Close the Toplevel window after adding the item
        
class ScrollableTaskFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.frames_data = []

    def add_item(self, new_frame_data):
        new_frame = customtkinter.CTkFrame(self, width=200, corner_radius=30, fg_color="grey")
        new_frame.grid(row=len(self.frames_data), column=0, padx=15, pady=15, sticky="ns")

        for i, key in enumerate(new_frame_data.keys()):
            label = customtkinter.CTkLabel(new_frame, text=f"{key}: {new_frame_data[key]}", fg_color="transparent")
            label.grid(row=0, column=i, padx=20, pady=20)

        self.frames_data.append(new_frame_data)
        print(self.frames_data)

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("APS.py")
        self.geometry("920x450")
        self.iconbitmap(r"C:\Users\musta\Downloads\New folder\bot.ico")

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
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
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="  APS", image=self.logo_image,
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
        #self.scrollable_checkbox_frame = ScrollableCheckBoxFrame(self.second_frame, command=)
        #self.scrollable_checkbox_frame.grid(row=1, column=0, padx=15, pady=15, sticky="nswe")
        
        self.scrollable_task_frame = ScrollableTaskFrame(self.second_frame, width=700)
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

        # select default frame
        self.select_frame_by_name("home")
    def open_input_dialog_event(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = Toplevelwindow(self)
        else:
            self.toplevel_window.focus()
    def checkbox_frame_event(self):
        print(f"checkbox frame modified: {self.scrollable_checkbox_frame.get_checked_items()}")


    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
        self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")

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

    def home_button_event(self):
        self.select_frame_by_name("home")

    def frame_2_button_event(self):
        self.select_frame_by_name("frame_2")

    def frame_3_button_event(self):
        self.select_frame_by_name("frame_3")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)


if __name__ == "__main__":
    app = App()
    pywinstyles.apply_style(app,'transparent')
    app.mainloop()
    
