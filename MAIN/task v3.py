import customtkinter

class ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self, app, *args, **kwargs):
        super().__init__()

        self.app = app  # Save a reference to the App instance

        self.title("new task")
        self.geometry("500x110")
        self.grid_rowconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.entry = customtkinter.CTkEntry(self, placeholder_text="new task")
        self.entry.grid(row=3, column=0, columnspan=2, padx=(20, 20), pady=(20, 20), sticky="nswe")

        self.optionmenu_1 = customtkinter.CTkOptionMenu(self, dynamic_resizing=False, values=["level1", "level2", "level3"])
        self.optionmenu_1.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.optionmenu_2 = customtkinter.CTkOptionMenu(self, dynamic_resizing=False, values=["level1", "level2", "level3"])
        self.optionmenu_2.grid(row=0, column=1, padx=20, pady=(20, 10))
        self.optionmenu_3 = customtkinter.CTkOptionMenu(self, dynamic_resizing=False, values=["level1", "level2", "level3"])
        self.optionmenu_3.grid(row=0, column=2, padx=20, pady=(20, 10))
        self.optionmenu_4 = customtkinter.CTkOptionMenu(self, dynamic_resizing=False, values=["level1", "level2", "level3"])
        self.optionmenu_4.grid(row=0, column=3, padx=20, pady=(20, 10))
        self.optionmenu_1.set("priority")
        self.optionmenu_2.set("store")
        self.optionmenu_3.set("size")
        self.optionmenu_4.set("item")

        self.newtask = customtkinter.CTkButton(self, text="create new", command=self.add_item_to_main_window)
        self.newtask.grid(row=0, column=4, padx=40, pady=10)

    def add_item_to_main_window(self):
        new_frame_data = {
            "priority": "Value 1",
            "store": self.entry.get(),  # Get value from entry field
            "size": "Value 1",
            "item": "Pending",  # Set a default value
            "status": "Value 1"
        }
        self.app.scrollable_task_frame.add_item(new_frame_data)#add item inherited for scrollable task frame
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

        self.title("add task")
        self.grid_rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)

        self.scrollable_task_frame = ScrollableTaskFrame(master=self, width=700)
        self.scrollable_task_frame.grid(row=1, column=0, padx=15, pady=15, sticky="ns")

        self.toplevel_window = None

        self.scrollable_checkbox_frame1 = customtkinter.CTkFrame(self, width=400, corner_radius=0)
        self.scrollable_checkbox_frame1.grid(row=0, column=0, padx=15, pady=15, sticky="ns")

        self.newtask = customtkinter.CTkButton(self.scrollable_checkbox_frame1, text="create new", command=self.open_input_dialog_event)
        self.newtask.grid(row=0, column=0, padx=40, pady=10)

    def open_input_dialog_event(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ToplevelWindow(self)
        else:
            self.toplevel_window.focus()

if __name__ == "__main__":
    customtkinter.set_appearance_mode("dark")
    app = App()
    app.mainloop()
