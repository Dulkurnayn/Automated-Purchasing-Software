import tkinter as tk
import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light")
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class PurchaseApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Purchase App")

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

        
if __name__ == "__main__":
    app = PurchaseApp()
    app.mainloop()
