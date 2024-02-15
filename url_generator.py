import customtkinter as ctk
from base_qr_generator import QRGeneratorBase


class UrlQRGenerator(QRGeneratorBase):
    def __init__(self, tab):
        super().__init__(tab)
        self.left_frame = ctk.CTkFrame(tab)
        self.right_frame = ctk.CTkFrame(tab)
        self.left_frame.grid(row=0, column=0, rowspan=2, padx=5, pady=5)
        self.right_frame.grid(row=0, column=1, rowspan=5, padx=5, pady=5)
        self.label1 = ctk.CTkLabel(self.left_frame, text="Url:")
        self.url_input = ctk.CTkEntry(master=self.left_frame)
        self.button_submit = ctk.CTkButton(self.left_frame, text="Generate URL QR", command=self.submit_action_update)
        self.button_open_pdf = ctk.CTkButton(self.left_frame, text="Open PDF", command=self.open_pdf)
        self.label_img = ctk.CTkLabel(self.right_frame, width=300, height=300, text='', image=self.default_img())

        self.label1.grid(row=0, column=0, padx=5, pady=5)
        self.url_input.grid(row=0, column=1, padx=5, pady=5)
        self.label_img.grid(row=0, column=0, rowspan=3, columnspan=3)
        self.button_submit.grid(row=4, column=1, columnspan=1, padx=5, pady=5)
        self.button_open_pdf.grid(row=5, column=1, columnspan=1, padx=5, pady=5)

    def get_input(self):
        text = self.url_input.get()
        return [text]

    def submit_action_update(self):
        input_list = self.get_input()
        image = self.submit_action(input_list)
        self.label_img.configure(image=image)

