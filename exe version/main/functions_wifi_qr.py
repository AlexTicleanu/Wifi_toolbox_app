import json
import os
import webbrowser
import qrcode
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.platypus import Image as Imagerl
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from PIL import Image
import customtkinter as ctk
import pypdfium2 as pdfium



class WiFiQRGenerator:
    def __init__(self, tab):
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
        self.checkbox_save = ctk.CTkCheckBox(self.left_frame, text="Save name and password", variable=self.check_var, onvalue="on", offvalue="off")
        self.populate_from_saved = ctk.CTkButton(self.left_frame, text="use from saved", command=self.populate_fields)
        self.button_submit = ctk.CTkButton(self.left_frame, text="Generate wifi QR", command=self.submit_action)
        self.button_open_pdf = ctk.CTkButton(self.left_frame, text="Open PDF", command=self.open_pdf)
        self.label_img = ctk.CTkLabel(self.right_frame, width=300, height=300, text='', image=self.default_img())
        self.checkbox_print = ctk.CTkCheckBox(self.right_frame, text="Name and password visible on pdf", variable=self.details_var, onvalue="on", offvalue="off")
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

    def validate_inputs(self):
        if self.ssid_input.get() != "" and self.password_input.get() != "":
            return True
        else:
            return False

    def submit_action(self):
        if self.validate_inputs():
            self.submit_button()

    def open_pdf(self):
        if os.path.isfile('wifi_file.pdf'):
            self.view_pdf('wifi_file.pdf')

    def submit_button(self):
        if self.check_var.get() == "on":
            self.save_input_data_in_set(self.ssid_input.get(), self.password_input.get())
        self.checkbox_print_action()

    def save_file_data(self):
        ssid = self.ssid_input.get()
        password = self.password_input.get()
        save_details = self.check_var.get() == "on"
        self.save_pdf(ssid, password, save_details)

    def checkbox_print_action(self):
        if self.details_var.get().strip() == "on":
            pdf = self.save_pdf(self.ssid_input.get(), self.password_input.get(), True)
            image_pil = self.pdf_to_image(pdf)
            image = ctk.CTkImage(image_pil, size=(180, 251))
            self.label_img.configure(image=image)
        elif self.details_var.get().strip() == "off":
            pdf = self.save_pdf(self.ssid_input.get(), self.password_input.get(), False)
            image_pil = self.pdf_to_image(pdf)
            image = ctk.CTkImage(image_pil, size=(180, 251))
            self.label_img.configure(image=image)

    def checkbox_details_with_validation(self):
        if self.validate_inputs():
            self.checkbox_print_action()

    def view_pdf(self, route_to_picture):
        webbrowser.open_new(route_to_picture)

    def generate_qr_wifi(self, ssid, password):
        wifi_data = 'WIFI:S:{};T:WPA;P:{};;'.format(ssid, password)
        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=5)
        qr.add_data(wifi_data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        return img

    def generate_picture_and_text(self, ssid, password, details):
        content = []
        self.save_jpg_image(ssid, password)
        im = Imagerl('qr_internal.png', 7 * inch, 7 * inch)
        content.append(im)
        styles = getSampleStyleSheet()
        styles.add(ParagraphStyle(fontSize=20, name='Justify', alignment=TA_CENTER))
        if details:
            ptext = f'Wi-Fi Name: {ssid}'
            content.append(Paragraph(ptext, styles["Justify"]))
            content.append(Spacer(1, 12))
            ptext = f'Password: {password}'
            content.append(Paragraph(ptext, styles["Justify"]))
            content.append(Spacer(1, 12))
        doc = SimpleDocTemplate("wifi_file.pdf", pagesize=letter)
        doc.build(content)

    def pdf_to_image(self, route):
        page = pdfium.PdfDocument(route)[0]
        renderer = page.render(scale=300 / 72, rotation=0)
        pil_img = renderer.to_pil()
        pil_img.save("image_pdf.png")
        image_pil = Image.open('image_pdf.png')
        return image_pil

    def save_jpg_image(self, ssid, password):
        img = self.generate_qr_wifi(ssid, password)
        img.save('qr_internal.png')

    def save_pdf(self, ssid, password, details):
        self.generate_picture_and_text(ssid, password, details)
        return 'wifi_file.pdf'

    def save_input_data_in_set(self, ssid, password):
        with open('data_saved.json', 'w') as f:
            data = {'ssid': ssid, 'password': password}
            json.dump(data, f)

    def default_img(self):
        default_image = Image.open("default_img.png")
        return ctk.CTkImage(default_image, size=(290, 190))

    def populate_fields(self):
        with open('data_saved.json', 'r') as file:
            data = json.load(file)
        ssid_db = data['ssid']
        password_db = data['password']
        self.ssid_input.delete(0, 'end')
        self.ssid_input.insert(0, ssid_db)
        self.password_input.delete(0, 'end')
        self.password_input.insert(0, password_db)
