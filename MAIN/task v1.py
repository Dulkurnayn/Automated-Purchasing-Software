import customtkinter
import tkinter as tk
import tkinter
import os
from PIL import Image
#create new task button
#call function to appen new task  with store name size ect
class toplevelwindow(customtkinter.CTkToplevel):
            def __init__(self,*args,**kwargs):
                super().__init__()

                self.title("new task")
                self.geometry("500x110")
                self.grid_rowconfigure(1, weight=1)
                self.columnconfigure(2, weight=1)
                self.entry=customtkinter.CTkEntry(self,placeholder_text= "newtask")
                self.entry.grid(row=3, column=0, columnspan=2, padx=(20, 20), pady=(20, 20), sticky="nswe")
                
                self.optionmenu_1 = customtkinter.CTkOptionMenu(self, dynamic_resizing=False,
                                                        values=["level1", "level2", "level3"])
                self.optionmenu_1.grid(row=0, column=0, padx=20, pady=(20, 10))
                self.optionmenu_2 = customtkinter.CTkOptionMenu(self, dynamic_resizing=False,
                                                        values=["level1", "level2", "level3"])
                self.optionmenu_2.grid(row=0, column=1, padx=20, pady=(20, 10))
                self.optionmenu_3 = customtkinter.CTkOptionMenu(self, dynamic_resizing=False,
                                                        values=["level1", "level2", "level3"])
                self.optionmenu_3.grid(row=0, column=2, padx=20, pady=(20, 10))
                self.optionmenu_4 = customtkinter.CTkOptionMenu(self, dynamic_resizing=False,
                                                        values=["level1", "level2", "level3"])
                self.optionmenu_4.grid(row=0, column=2, padx=20, pady=(20, 10))
                self.optionmenu_1.set("priority")
                self.optionmenu_2.set("store")
                self.optionmenu_3.set("size")
                self.optionmenu_4.set("item")
                
class ScrollableCheckBoxFrame(customtkinter.CTkScrollableFrame):

    def __init__(self, master, item_list, command=None, **kwargs):
        super().__init__(master, **kwargs)

        self.command = command
        self.checkbox_list = [] #LIST OF ALL ITEMS 
        for i, item in enumerate(item_list):
            self.add_item(item)
    #if 

    def add_item(self, item):
        
        
        checkbox = customtkinter.CTkCheckBox(self, text=(item))
        if self.command is not None:
            checkbox.configure(command=self.command)
        checkbox.grid(row=len(self.checkbox_list), column=0, pady=(0, 10))
        self.checkbox_list.append(checkbox)

    def remove_item(self, item):
        for checkbox in self.checkbox_list:
            if item == checkbox.cget("text"):
                checkbox.destroy()
                self.checkbox_list.remove(checkbox)
                return

    def get_checked_items(self):
        return [checkbox.cget("text") for checkbox in self.checkbox_list if checkbox.get() == 1]
class my_frame(customtkinter.CTkScrollableFrame):

    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        #self.canvas = tk.Canvas(self)
        #self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        #self.scrollable_frame = ttk.Frame(self.canvas)
        self.frames_data = []  # List to store data for each frame

        #self.scrollable_frame.bind(
           # "<Configure>",
          #  lambda e: self.canvas.configure(
         #       scrollregion=self.canvas.bbox("all")
        #    )
       # )

        #self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        #self.canvas.configure(yscrollcommand=self.scrollbar.set)

        #self.canvas.pack(side="left", fill="both", expand=True)
        #self.scrollbar.pack(side="right", fill="y")
class UpdateEvent:
    def __init__(self, app, entry_var, label, frame_data):
        self.app = app
        self.entry_var = entry_var
        self.label = label
        self.frame_data = frame_data
        self.timer_id = None  # Timer ID for tracking the timer event

    def update_value(self):
        new_value = self.entry_var.get()
        self.label.config(text=new_value)
        self.frame_data["status"].set("Pending")

        # Cancel previous timer (if any)
        if self.timer_id:
            self.app.root.after_cancel(self.timer_id)

        # Start a timer for 20 seconds
        self.timer_id = self.app.root.after(200, self.checkout)

    def checkout(self):
        # Automatically set the status to "Checkout" after 20 seconds
        self.frame_data["status"].set("Checkout")

        # Find the index of the frame_data in the frames_data list
        index = self.app.frames_data.index(self.frame_data)

        # Update the Label widget with the new status
        label = self.app.scrollable_frame.scrollable_frame.winfo_children()[index].winfo_children()[0]
        label.config(text=self.frame_data["status"].get())
        self.app.root.after(10, self.app.root.update_idletasks)

class ExampleApp:
    def __init__(self, root):
        #self.root = root
        #self.scrollable_frame = ScrollableFrame(root)
        #self.scrollable_frame.pack(fill="both", expand=True)
        
        self.scrollable_frame = customtkinter.CTkFrame(self, width=200,corner_radius=0)
        self.scrollable_frame.grid(row=0, column=0,padx=15, pady=15, sticky="ns")
        self.scrollable_frame.grid_rowconfigure(0, weight=0)
        self.scrollable_frame.grid_columnconfigure(0, weight=0)
        self.frames_data = []  # List to store data for each frame

       

        self.add_frame_button =customtkinter.CTkButton(self.my_frame, text="create new",command= self.add_frame)
        self.newtask.grid(row=0, column=0, padx=40, pady=10)
           
        
        self.toplevel_window = None


    def add_frame(self):
        new_frame_data = {
            "label_text": "Value 1",
            "status": tkinter.StringVar(value="Pending"),
        }

        new_frame = customtkinter.CTkFrame(self, width=200,corner_radius=0)
        new_frame.grid(row=len(self.frames_data), column=0,padx=15, pady=15, sticky="ns")
        
        
        #checkbox = customtkinter.CTkCheckBox(self, text=(item))
        #if self.command is not None:
         #   checkbox.configure(command=self.command)
        #checkbox.grid(row=len(self.checkbox_list), column=0, pady=(0, 10))
        #self.checkbox_list.append(checkbox)
        
        label = customtkinter.CTkLabel(new_frame, text=new_frame_data["label_text"], fg_color="transparent")
        label.grid(row=0, column=0, padx=20, pady=20)
        #label = ttk.Label(new_frame, text=new_frame_data["label_text"])
        #label.pack(side="left", padx=10)

        entry_var = tkinter.StringVar(value=new_frame_data["label_text"])
        entry_var.grid(row=0, column=1, padx=20, pady=20)
        #tkinter.StringVar
        #entry = ttk.Entry(new_frame, textvariable=entry_var)
        entry = customtkinter.CTkEntry(new_frame, placeholder_text=new_frame_data["label_text"])
        entry.grid(row=2, column=1, padx=20, pady=20)
        #entry.pack(side="left", padx=10)

        status_label = customtkinter.CTkLabel(new_frame, text=new_frame_data["status"], fg_color="transparent")
        #status_label.pack(side="left", padx=10)

        button = tk.Button(new_frame, text="Update", command=UpdateEvent(self, entry_var, label, new_frame_data).update_value)
        button.pack(side="left", padx=10)
        button =customtkinter.CTkButton(new_frame, text="Update", command=UpdateEvent(self.my_frame, entry_var, label, new_frame_data).update_value)
        button.grid(row=3, column=0, padx=40, pady=10)
        self.frames_data.append(new_frame_data)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("CTkScrollableFrame example")
        self.grid_rowconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        
        
        
        # create scrollable checkbox frame
        #self.scrollable_checkbox_frame = ScrollableCheckBoxFrame(master=self, width=200, command=self.checkbox_frame_event,
       #                                                          item_list=[f"item {i}" for i in range(15)])
        #self.scrollable_checkbox_frame.grid(row=1, column=0, padx=15, pady=15, sticky="ns")
        #self.store= ("helle")
        #self.scrollable_checkbox_frame.add_item(self.store)
        #new taskbutton frame
        self.scrollable_checkbox_frame1 = customtkinter.CTkFrame(self, width=200,corner_radius=0)
        self.scrollable_checkbox_frame1.grid(row=0, column=0,padx=15, pady=15, sticky="ns")
        self.scrollable_checkbox_frame1.grid_rowconfigure(0, weight=0)
        self.scrollable_checkbox_frame1.grid_columnconfigure(0, weight=0)
        #newtaskbutton

        self.newtask = customtkinter.CTkButton(self.scrollable_checkbox_frame1, text="create new",command= self.open_input_dialog_event)
        self.newtask.grid(row=0, column=0, padx=40, pady=10)
        self.toplevel_window = None

        #set values
        #self.toplevelwindow.optionmenu_1.set("CTkOptionmenu")
    
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window=toplevelwindow(self)
        else:
            self.toplevel_window.focus()
    def checkbox_frame_event(self):
        print(f"checkbox frame modified: {self.scrollable_checkbox_frame.get_checked_items()}")

      
    def open_input_dialog_event(self,**kwargs):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window=toplevelwindow(self)
        else:
            self.toplevel_window.focus(self)
      
import pywinstyles
if __name__ == "__main__":
#customtkinter.set_appearance_mode("dark")
    app = App()
    pywinstyles.apply_style(app, 'aero')
    app.mainloop()



