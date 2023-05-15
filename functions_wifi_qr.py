import os

from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.platypus import Image as Imagerl
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from PIL import Image
import webbrowser
import qrcode
import json
import pypdfium2 as pdfium


def generate_qr_wifi(ssid, password):
    wifi_data = 'WIFI:S:{};T:WPA;P:{};;'.format(ssid, password)
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=5)
    qr.add_data(wifi_data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    return img


def view_pdf(route_to_picture):
    webbrowser.open_new(route_to_picture)


def generate_picture_and_text(ssid, password, details):
    content = []
    save_jpg_image(ssid, password)
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
    return content


def cleanup_image_and_pdf():
    os.remove("../wifi_file.pdf")


def generate_pdf_action(content):
    doc = SimpleDocTemplate("wifi_file.pdf", pagesize=letter,
                            rightMargin=72, leftMargin=72,
                            topMargin=72, bottomMargin=18)
    doc.build(content)
    return "wifi_file.pdf"


def generate_qr(ssid, password):

    wifi_data = 'WIFI:S:{};T:WPA;P:{};;'.format(ssid, password)

    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=5)
    qr.add_data(wifi_data)
    qr.make(fit=True)
    return qr


def save_jpg_image(ssid, password):
    qr = generate_qr(ssid, password)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save('qr_internal.png')
    image_pil = Image.open('qr_internal.png')
    return image_pil


def save_pdf(ssid, password, details):
    content = generate_picture_and_text(ssid, password, details=details)
    route_to_picture = generate_pdf_action(content)
    return route_to_picture


def save_input_data_in_set(ssid, password):
    with open('data.json', 'w') as f:
        # data = json.load(f)
        data = {'ssid': ssid, 'password': password}
        json.dump(data, f)


def pdf_to_image(route):
    page = pdfium.PdfDocument(route)[0]
    renderer = page.render(scale=300 / 72, rotation=0)
    pil_img = renderer.to_pil()
    pil_img.save("image_pdf.png")
    image_pil = Image.open('image_pdf.png')
    return image_pil

