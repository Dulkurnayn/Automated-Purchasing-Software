import customtkinter
import os
from PIL import Image
import pywinstyles
import tkinter
#create new task button
#call function to appen new task  with store name size ect
class toplevelwindow(customtkinter.CTkToplevel):
            def __init__(self,winfo_children,*args,**kwargs):
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
                self.newtask = customtkinter.CTkButton(self, text="create new",command= ScrollableCheckBoxFrame.add_item(self))
                self.newtask.grid(row=0, column=3, padx=40, pady=10)
                
class ScrollableCheckBoxFrame(customtkinter.CTkScrollableFrame):

    def __init__(self, master,  command=None, **kwargs):
        super().__init__(master, **kwargs)

        self.command = command
        self.frames_data = [] 
        #LIST OF ALL ITEMS 
        #for i, item in (self.frames_data) :
         #   self.add_item(item)
    #if 

    def add_item(self):
        self.new_frame_data = {
            "priority": "Value 1",
            "store": ("Pending"),
             "size": "Value 1",
            "item": ("Pending"),
             "status": "Value 1"
        }
        new_frame = customtkinter.CTkFrame(self, width=200,corner_radius=30,fg_color="grey")
        new_frame.grid(row=len(self.frames_data), column=0,padx=15, pady=15, sticky="ns")
        
        label = customtkinter.CTkLabel(new_frame, text=self.new_frame_data["label_text"], fg_color="transparent")
        label.grid(row=0, column=0, padx=20, pady=20)
        

       
       
        entry = customtkinter.CTkEntry(new_frame, placeholder_text=self.new_frame_data["label_text"])
        entry.grid(row=0, column=1, padx=20, pady=20)
         
        

        self.frames_data.append(self.new_frame_data)
        print (self.frames_data)
    def remove_item(self, item):
        for task in self.frames_data:
            if item == f.cget("text"):
                checkbox.destroy()
                self.checkbox_list.remove(checkbox)
                return

    def get_checked_items(self):
        return [checkbox.cget("text") for checkbox in self.checkbox_list if checkbox.get() == 1]

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("CTkScrollableFrame example")
        self.grid_rowconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        
        

        # create scrollable checkbox frame
        self.scrollable_checkbox_frame = ScrollableCheckBoxFrame(master=self, width=500)
        self.scrollable_checkbox_frame.grid(row=1, column=0, padx=15, pady=15, sticky="ns")
        self.store= ("helle")
        
        #self.scrollable_checkbox_frame.add_item(self.store)
        #new taskbutton frame
        self.scrollable_checkbox_frame1 = customtkinter.CTkFrame(self, width=400,corner_radius=0)
        self.scrollable_checkbox_frame1.grid(row=0, column=0,padx=15, pady=15, sticky="ns")
        self.scrollable_checkbox_frame1.grid_rowconfigure(0, weight=0)
        self.scrollable_checkbox_frame1.grid_columnconfigure(0, weight=0)
        #newtaskbutton

        self.newtask = customtkinter.CTkButton(self.scrollable_checkbox_frame1, text="create new",command= self.open_input_dialog_event)
        self.newtask.grid(row=0, column=0, padx=40, pady=10)
        #self.toplevel_window = None ###///////////impiortnat

        #set values
        #self.toplevelwindow.optionmenu_1.set("CTkOptionmenu")
    def open_input_dialog_event(self):
        #dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        #dialog1 = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        #print("CTkInputDialog:", dialog.get_input())#
        #self.text1=(dialog.get_input())
        #print({self.text1})
        #self.scrollable_checkbox_frame.add_item(dialog.get_input())
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window=toplevelwindow(self)
        else:
            self.toplevel_window.focus()
    def checkbox_frame_event(self):
        print(f"checkbox frame modified: {self.scrollable_checkbox_frame.get_checked_items()}")

    

#if __name__ == "__main__":
customtkinter.set_appearance_mode("dark")
app = App()
pywinstyles.apply_style(app, 'acrylic')
app.mainloop()
#self.toplevel_window.focus()



