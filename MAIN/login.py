import tkinter
import customtkinter
from PIL import ImageTk, Image
import getmac
import os

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class login(customtkinter.CTk):
    def __init__(self):
        super().__init__()


        customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
        customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
        
        def dashboard():
            
            print("app")

            
            
            
        
        def passwordreset(): 
            global username ,email

            x= open("create.txt" ,"r")
            # Read the lines
            print("helle")
            user=username.get()
            
            email=email.get()
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
                    
                        
                    self.username.delete(0, last_index=100)
                    self.password.delete(0, last_index=100)

        def signup_function():
            self.title('Sign Up')
            self.geometry("600x640")
            self.frame.place_forget()
            self.sign_up_frame= customtkinter.CTkFrame(self, width=320, height=360, corner_radius=15, fg_color="transparent")
            self.sign_up_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

            self.page_name_su = customtkinter.CTkLabel(master=self.sign_up_frame, text="SIGN UP", font=('Century Gothic', 20))
            self.page_name_su.place(x=120, y=45)

            self.username_su = customtkinter.CTkEntry(master=self.sign_up_frame, width=220, placeholder_text='Username')
            self.username_su.place(x=50, y=110)

            def check_btn_var_su():
                if view_password_su.get():
                    self.password_su.configure(show="")
                else:
                    self.password_su.configure(show="*")

            view_password_su = customtkinter.CTkSwitch(master=self.sign_up_frame, command=check_btn_var_su, text=None)
            view_password_su.place(x=240, y=165)

            self.password_su = customtkinter.CTkEntry(master=self.sign_up_frame, width=190, placeholder_text='Password', show="*")
            self.password_su.place(x=50, y=165)

            self.email_su = customtkinter.CTkEntry(master=self.sign_up_frame, width=220, placeholder_text='Email')
            self.email_su.place(x=50, y=220)

            # command=passwordreset(recieveremail)
            resetpass_button_su = customtkinter.CTkButton(master=self.sign_up_frame, text="Forget password?", command=passwordreset, font=('Century Gothic', 12, ['bold']), fg_color="transparent", hover_color="gray25")
            resetpass_button_su.place(x=130, y=250)

            self.login_button_su = customtkinter.CTkButton(master=self.sign_up_frame, width=220, text="Login", command=load_log, corner_radius=6)
            self.login_button_su.place(x=50, y=290)

            signup_button_su = customtkinter.CTkButton(master=self.sign_up_frame, width=220, text="Sign Up", command=signup_function, corner_radius=6)
            signup_button_su.place(x=50, y=330)

            self.re_enter_password_su = customtkinter.CTkEntry(master=self.sign_up_frame, width=220, placeholder_text='Re-enter Password', show="*")
            self.re_enter_password_su.place(x=50, y=250)

            self.email_su_confirm = customtkinter.CTkEntry(master=self.sign_up_frame, width=220, placeholder_text='Confirm Email')
            self.email_su_confirm.place(x=50, y=220)

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
            self.bg = customtkinter.CTkLabel(self, image=self.img1)
            self.bg.pack()

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
log = login()
log.mainloop()