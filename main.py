import customtkinter as ctk
from functions_speedtest import speed_test_bytes
from functions_wifi_qr import save_jpg_image, save_input_data_in_set, save_pdf, pdf_to_image
from PIL import Image



def submit_button():
    image = save_jpg_image(ssid_input.get(), password_input.get())
    if check_var.get() == "on":
        save_input_data_in_set(ssid_input.get(), password_input.get())
    # label_img.configure(image=image)


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


# Create widgets for tab 1
label1 = ctk.CTkLabel(left_frame, text="Wifi Name:")
ssid_input = ctk.CTkEntry(master=left_frame)
label2 = ctk.CTkLabel(left_frame, text="Password:")
password_input = ctk.CTkEntry(master=left_frame)
check_var = ctk.StringVar()
details_var = ctk.StringVar()
checkbox_save = ctk.CTkCheckBox(left_frame, text="Save name and password", variable=check_var, onvalue="on", offvalue="off")
button1 = ctk.CTkButton(left_frame, text="Generate wifi QR", command=submit_button)
button2 = ctk.CTkButton(left_frame, text="Open PDF", command=submit_button)
label_img = ctk.CTkLabel(right_frame, width=300, height=300, text='', image=default_image)
checkbox_print = ctk.CTkCheckBox(right_frame, text="Name and password visible on pdf", variable=details_var, onvalue="on", offvalue="off")
checkbox_print.bind("<ButtonRelease>", lambda event: checkbox_print_action())


# Layout widgets for tab 1
label1.grid(row=0, column=0, padx=5, pady=5)
ssid_input.grid(row=0, column=1, padx=5, pady=5)
label2.grid(row=1, column=0, padx=5, pady=5)
password_input.grid(row=1, column=1, padx=5, pady=5)
checkbox_save.grid(row=2, column=1, columnspan=1, padx=5, pady=5)
button1.grid(row=3, column=1, columnspan=1, padx=5, pady=5)
button2.grid(row=4, column=1, columnspan=1, padx=5, pady=5)


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

