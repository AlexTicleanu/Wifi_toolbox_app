import customtkinter as ctk
from functions_speedtest import speed_test_bytes
from functions_wifi_qr import save_jpg_image, save_input_data_in_set, save_pdf, pdf_to_image
from PIL import Image

# ssid = "DIGI-23cK"
# password = "cJ3gFqKx"


def validate_inputs():
    input1 = ssid_input.get().strip()
    input2 = password_input.get().strip()

    if input1 != "" and input2 != "":
        # Set the error message for both inputs
        button1.configure(state="enabled")
        # Return False to indicate validation failed
        return True
    # Return True to indicate validation passed
    button1.configure(state="disabled")
    return False

def validate_file():
    pass

def submit_button():
    if check_var.get() == "on":
        save_input_data_in_set(ssid_input.get(), password_input.get())
    checkbox_print_action()


def save_file_data():
    ssid = ssid_input.get()
    password = password_input.get()
    save_details = check_var.get() == "on"
    save_pdf(ssid, password, save_details)


def checkbox_print_action():
    if details_var.get() == "on":
        pdf = save_pdf(ssid_input.get(), password_input.get(), True)
        image_pil = pdf_to_image(pdf)
        image = ctk.CTkImage(image_pil, size=(180, 251))
        label_img.configure(image=image)
    else:
        pdf = save_pdf(ssid_input.get(), password_input.get(), False)
        image_pil = pdf_to_image(pdf)
        image = ctk.CTkImage(image_pil, size=(180, 251))
        label_img.configure(image=image)


# Create the main window
root = ctk.CTk()
root.title("Wi-Fi Toolbox")
root.minsize(660, 480)
root.maxsize(660, 480)
# Create tabs
tab_control = ctk.CTkTabview(root)
tab_control.pack(padx=40, pady=40)

tab1 = tab_control.add("Wifi QR")
tab2 = tab_control.add("Speedtest")
tab_control.pack(expand=1, fill="both")

default_image = Image.open("default_img.png")
default_image = ctk.CTkImage(default_image, size=(290, 190))

# create frames
left_frame = ctk.CTkFrame(tab1)
right_frame = ctk.CTkFrame(tab1)
error_message = ctk.StringVar()


# Create widgets for tab 1
label1 = ctk.CTkLabel(left_frame, text="Wifi Name:")
ssid_input = ctk.CTkEntry(master=left_frame)
ssid_input.bind("<KeyRelease>", lambda event: validate_inputs())
label2 = ctk.CTkLabel(left_frame, text="Password:")
password_input = ctk.CTkEntry(master=left_frame)
password_input.bind("<KeyRelease>", lambda event: validate_inputs())
check_var = ctk.StringVar()
details_var = ctk.StringVar()
checkbox_save = ctk.CTkCheckBox(left_frame, text="Save name and password", variable=check_var, onvalue="on", offvalue="off")
button1 = ctk.CTkButton(left_frame, text="Generate wifi QR", command=submit_button, state='disabled')
button2 = ctk.CTkButton(left_frame, text="Open PDF", command=submit_button)
label_img = ctk.CTkLabel(right_frame, width=300, height=300, text='', image=default_image)
checkbox_print = ctk.CTkCheckBox(right_frame, text="Name and password visible on pdf", variable=details_var, onvalue="on", offvalue="off")
checkbox_print.bind("<ButtonRelease>", lambda event: checkbox_print_action())


# Layout widgets for tab 1
label1.grid(row=0, column=0, padx=5, pady=5)
ssid_input.grid(row=0, column=1, padx=5, pady=5)
label2.grid(row=1, column=0, padx=5, pady=5)
password_input.grid(row=1, column=1, padx=5, pady=5)


checkbox_save.grid(row=3, column=1, columnspan=1, padx=5, pady=5)
button1.grid(row=4, column=1, columnspan=1, padx=5, pady=5)
button2.grid(row=5, column=1, columnspan=1, padx=5, pady=5)


label_img.grid(row=0, column=0, rowspan=3, columnspan=3)
checkbox_print.grid(row=3, column=0)

# Create widgets for tab 2
button2 = ctk.CTkButton(tab2, text="SpeedCheck", command=speed_test_bytes)

# Layout widgets for tab 2
button2.pack(padx=5, pady=5)

left_frame.grid(row=0, column=0, rowspan=2, padx=5, pady=5)
right_frame.grid(row=0, column=1, rowspan=5, padx=5, pady=5)

# Start the main event loop
root.mainloop()

