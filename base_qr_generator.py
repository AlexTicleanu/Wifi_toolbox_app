import os
import qrcode
import webbrowser
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Image as Imagerl, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from PIL import Image
from reportlab.lib.enums import TA_CENTER
import customtkinter as ctk
import pypdfium2 as pdfium


class QRGeneratorBase:
    def __init__(self, tab):
        self.tab = tab

    def submit_action(self, input_list):
        if self.validate_inputs(input_list):
            return self.submit_button(input_list)

    def validate_inputs(self, input_list):
        if all(x != "" for x in input_list):
            return True
        else:
            return False

    def save_pdf(self, input_list, details=None):
        self.generate_picture_and_text(input_list, details)
        return 'wifi_file.pdf'

    def submit_button(self, input_list):
        pdf = self.save_pdf(input_list)
        image_pil = self.pdf_to_image(pdf)
        image = ctk.CTkImage(image_pil, size=(180, 251))
        return image

    def generate_picture_and_text(self, input_list, details):
        content = []
        self.save_jpg_image(input_list)
        im = Imagerl('qr_internal.png', 7 * inch, 7 * inch)
        content.append(im)
        styles = getSampleStyleSheet()
        styles.add(ParagraphStyle(fontSize=20, name='Justify', alignment=TA_CENTER))
        if details:
            ptext = f'Wi-Fi Name: {input_list[0]}'
            content.append(Paragraph(ptext, styles["Justify"]))
            content.append(Spacer(1, 12))
            ptext = f'Password: {input_list[1]}'
            content.append(Paragraph(ptext, styles["Justify"]))
            content.append(Spacer(1, 12))
        doc = SimpleDocTemplate("wifi_file.pdf", pagesize=letter)
        doc.build(content)

    def save_jpg_image(self, input_list):
        img = self.generate_qr_wifi(input_list)
        img.save('qr_internal.png')

    def generate_qr_wifi(self, input_list):
        if len(input_list) == 2:
            wifi_data = 'WIFI:S:{};T:WPA;P:{};;'.format(input_list[0], input_list[1])
        else:
            wifi_data = input_list[0]
        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=5)
        qr.add_data(wifi_data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        return img

    def pdf_to_image(self, route):
        page = pdfium.PdfDocument(route)[0]
        renderer = page.render(scale=300 / 72, rotation=0)
        pil_img = renderer.to_pil()
        pil_img.save("image_pdf.png")
        image_pil = Image.open('image_pdf.png')
        return image_pil

    def default_img(self):
        default_image = Image.open("images/default_img.png")
        return ctk.CTkImage(default_image, size=(290, 190))

    def open_pdf(self):
        if os.path.isfile('wifi_file.pdf'):
            self.view_pdf('wifi_file.pdf')

    def view_pdf(self, route_to_picture):
        webbrowser.open_new(route_to_picture)

