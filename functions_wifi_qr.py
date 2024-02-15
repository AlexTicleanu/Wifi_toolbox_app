import json
import customtkinter as ctk

from base_qr_generator import QRGeneratorBase


class WiFiQRGenerator(QRGeneratorBase):
    def __init__(self, tab):
        super().__init__(tab)
        self.left_frame = ctk.CTkFrame(tab)
        self.right_frame = ctk.CTkFrame(tab)
        self.left_frame.grid(row=0, column=0, rowspan=2, padx=5, pady=5)
        self.right_frame.grid(row=0, column=1, rowspan=5, padx=5, pady=5)

        self.label1 = ctk.CTkLabel(self.left_frame, text="Wifi Name:")
        self.ssid_input = ctk.CTkEntry(master=self.left_frame)
        self.label2 = ctk.CTkLabel(self.left_frame, text="Password:")
        self.password_input = ctk.CTkEntry(master=self.left_frame)
        self.check_var = ctk.StringVar(value="off")
        self.details_var = ctk.StringVar(value="off")
        self.checkbox_save = ctk.CTkCheckBox(self.left_frame, text="Save name and password", variable=self.check_var,
                                             onvalue="on", offvalue="off")
        self.populate_from_saved = ctk.CTkButton(self.left_frame, text="use from saved", command=self.populate_fields)
        self.button_submit = ctk.CTkButton(self.left_frame, text="Generate wifi QR", command=self.submit_action_update)
        self.button_open_pdf = ctk.CTkButton(self.left_frame, text="Open PDF", command=self.open_pdf)
        self.label_img = ctk.CTkLabel(self.right_frame, width=300, height=300, text='', image=self.default_img())
        self.checkbox_print = ctk.CTkCheckBox(self.right_frame, text="Name and password visible on pdf",
                                              variable=self.details_var, onvalue="on", offvalue="off")
        self.checkbox_print.bind("<ButtonRelease>", lambda event: self.checkbox_details_with_validation())

        self.label1.grid(row=0, column=0, padx=5, pady=5)
        self.ssid_input.grid(row=0, column=1, padx=5, pady=5)
        self.label2.grid(row=1, column=0, padx=5, pady=5)
        self.password_input.grid(row=1, column=1, padx=5, pady=5)
        self.checkbox_save.grid(row=3, column=1, columnspan=1, padx=5, pady=5)
        self.button_submit.grid(row=4, column=1, columnspan=1, padx=5, pady=5)
        self.button_open_pdf.grid(row=5, column=1, columnspan=1, padx=5, pady=5)
        self.populate_from_saved.grid(row=6, column=1, columnspan=1, padx=5, pady=5)
        self.label_img.grid(row=0, column=0, rowspan=3, columnspan=3)
        self.checkbox_print.grid(row=3, column=0)

    def get_input(self):
        ssid = self.ssid_input.get()
        password = self.password_input.get()
        return [ssid, password]

    def submit_action_update(self):
        input_list = self.get_input()
        image = self.submit_action(input_list)
        self.label_img.configure(image=image)

    def save_file_data(self):
        input_list = self.get_input()
        save_details = self.check_var.get() == "on"
        self.save_pdf(input_list, save_details)

    def checkbox_print_action(self):
        input_list = self.get_input()
        if self.details_var.get().strip() == "on":
            pdf = self.save_pdf(input_list, True)
            image_pil = self.pdf_to_image(pdf)
            image = ctk.CTkImage(image_pil, size=(180, 251))
            self.label_img.configure(image=image)
        elif self.details_var.get().strip() == "off":
            pdf = self.save_pdf(input_list, False)
            image_pil = self.pdf_to_image(pdf)
            image = ctk.CTkImage(image_pil, size=(180, 251))
            self.label_img.configure(image=image)

    def checkbox_details_with_validation(self):
        input_list = self.get_input()
        if self.validate_inputs(input_list):
            self.checkbox_print_action()

    def populate_fields(self):
        with open('data_saved.json', 'r') as file:
            data = json.load(file)
        ssid_db = data['ssid']
        password_db = data['password']
        self.ssid_input.delete(0, 'end')
        self.ssid_input.insert(0, ssid_db)
        self.password_input.delete(0, 'end')
        self.password_input.insert(0, password_db)
