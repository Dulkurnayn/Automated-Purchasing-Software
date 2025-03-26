import customtkinter
import os

#import tkinter as tk
import tkinter
#import tkinter.messagebox

from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk) 

#create new task button
#call function to appen new task  with store name size ect
class toplevelwindow(customtkinter.CTkToplevel):
            def __init__(self,*args,**kwargs):
                super().__init__()

                self.title("new task")
                self.geometry("500x140")
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
                


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("analysis")
        self.geometry("500x540")
        self.grid_rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        
 

        # create chart tab view
        self.charts = customtkinter.CTkTabview(self, width=250)
        self.charts.grid(row=0, column=1, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.charts.add("checkouts")
        self.charts.add("expenditure")
        self.charts.add("both")
        self.charts.tab("checkouts").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.charts.tab("expenditure").grid_columnconfigure(0, weight=1)
        self.plot(("checkouts"))

        
        #new analysis frame
        self.analysis = customtkinter.CTkFrame(self, width=30,height=40,corner_radius=0)
        self.analysis.grid(row=0, column=0,padx=15, pady=15, sticky="ns")
        self.analysis.grid_rowconfigure(0, weight=1)
        self.analysis.grid_columnconfigure(0, weight=1)
        
    def plot(self,page):
        self.page=page
        print(self.page)
       
        self.slider_1 = customtkinter.CTkSlider(self.charts.tab(self.page), from_=0, to=1, number_of_steps=101)
        self.slider_1.grid(row=3, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        self.slider_1.configure(command=self.update_progress) #command=self.progressbar_1.set
        #self.progressbar_1 = customtkinter.CTkProgressBar(self.charts.tab(self.page))
        #self.progressbar_1.grid(row=2, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        
  

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
       # self.y_values = list(self.y_values ) + [None]
       # self.x_values = list(self.x_values ) + [None]
        # the figure that will contain the plot 
        self.fig = Figure(figsize = (20, 20), 
                                dpi = 60) 
        # adding the subplot 
        self.plot1 = self.fig.add_subplot(111)#max values on x axis 

        # plotting the graph 
        
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

        
        #
        self.progress_level = self.slider_1.get()
       
        print((self.progress_level)*101,"%")# view the percentage on terminal 
        # clear the previous plot 
        self.plot1.clear()
       

    # Check if progress_level is 0 to avoid division by zero
        #if self.progress_level != 0:
        self.plot1.clear()
        # Update your plot based on the progress level
        x_values = [i for i in range(int(self.progress_level * 101))]
        y_values = [i**2 for i in range(int(self.progress_level * 101))]
        self.plot1.clear()
        self.plot1.plot(x_values, y_values)
        self.canvas.draw()
        
    def open_input_dialog_event(self,**kwargs):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window=toplevelwindow(self)
        else:
            self.toplevel_window.focus(self)
   

    

if __name__ == "__main__":
    customtkinter.set_appearance_mode("dark")
    app = App()
    app.mainloop()
    self.toplevel_window.focus()



