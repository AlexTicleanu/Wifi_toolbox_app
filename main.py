import os

import customtkinter as ctk
from functions_speedtest import speed_test_bytes
from functions_wifi_qr import save_input_data_in_set, save_pdf, pdf_to_image, view_pdf
from PIL import Image

# ssid = "DIGI-23cK"
# password = "cJ3gFqKx"


def validate_inputs():
    if ssid_input.get() != "" and password_input.get() != "":
        return True
    else:
        return False


def submit_action():
    if validate_inputs():
        submit_button()


def open_pdf():
    if os.path.isfile('wifi_file.pdf'):
        view_pdf('wifi_file.pdf')


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
    if details_var.get().strip() == "on":
        pdf = save_pdf(ssid_input.get(), password_input.get(), True)
        image_pil = pdf_to_image(pdf)
        image = ctk.CTkImage(image_pil, size=(180, 251))
        label_img.configure(image=image)
    elif details_var.get().strip() == "off":
        pdf = save_pdf(ssid_input.get(), password_input.get(), False)
        image_pil = pdf_to_image(pdf)
        image = ctk.CTkImage(image_pil, size=(180, 251))
        label_img.configure(image=image)


def checkbox_details_with_validation():
    if validate_inputs():
        checkbox_print_action()


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
tab_control.pack(expand=True, fill="both")

default_image = Image.open("default_img.png")
default_image = ctk.CTkImage(default_image, size=(290, 190))

# create frames
left_frame = ctk.CTkFrame(tab1)
right_frame = ctk.CTkFrame(tab1)


# Create widgets for tab 1
label1 = ctk.CTkLabel(left_frame, text="Wifi Name:")
ssid_input = ctk.CTkEntry(master=left_frame)
label2 = ctk.CTkLabel(left_frame, text="Password:")
password_input = ctk.CTkEntry(master=left_frame)
check_var = ctk.StringVar(value="off")
details_var = ctk.StringVar(value="off")
checkbox_save = ctk.CTkCheckBox(left_frame, text="Save name and password", variable=check_var, onvalue="on",
                                offvalue="off")
button_submit = ctk.CTkButton(left_frame, text="Generate wifi QR", command=submit_action)
button_open_pdf = ctk.CTkButton(left_frame, text="Open PDF", command=open_pdf)
label_img = ctk.CTkLabel(right_frame, width=300, height=300, text='', image=default_image)
checkbox_print = ctk.CTkCheckBox(right_frame, text="Name and password visible on pdf", variable=details_var,
                                 onvalue="on", offvalue="off")
checkbox_print.bind("<ButtonRelease>", lambda event: checkbox_details_with_validation())


# Layout widgets for tab 1
label1.grid(row=0, column=0, padx=5, pady=5)
ssid_input.grid(row=0, column=1, padx=5, pady=5)
label2.grid(row=1, column=0, padx=5, pady=5)
password_input.grid(row=1, column=1, padx=5, pady=5)


checkbox_save.grid(row=3, column=1, columnspan=1, padx=5, pady=5)
button_submit.grid(row=4, column=1, columnspan=1, padx=5, pady=5)
button_open_pdf.grid(row=5, column=1, columnspan=1, padx=5, pady=5)


label_img.grid(row=0, column=0, rowspan=3, columnspan=3)
checkbox_print.grid(row=3, column=0)

# Create widgets for tab 2
button3 = ctk.CTkButton(tab2, text="SpeedCheck", command=speed_test_bytes)

# Layout widgets for tab 2
button3.pack(padx=5, pady=5)

left_frame.grid(row=0, column=0, rowspan=2, padx=5, pady=5)
right_frame.grid(row=0, column=1, rowspan=5, padx=5, pady=5)

# Start the main event loop
root.mainloop()

