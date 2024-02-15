import os

import customtkinter as ctk
from functions_wifi_qr import WiFiQRGenerator
from PIL import Image

from url_generator import UrlQRGenerator


class WiFiToolboxApp:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("Wi-Fi Toolbox")
        self.root.minsize(660, 480)
        self.root.maxsize(660, 480)
        self.tab_control = ctk.CTkTabview(self.root)
        self.tab_control.pack(padx=40, pady=40)

        self.tab1 = self.tab_control.add("Wifi QR")
        self.tab2 = self.tab_control.add("URL QR")
        self.tab_control.pack(expand=True, fill="both")

        self.default_image = Image.open("images/default_img.png")
        self.default_image = ctk.CTkImage(self.default_image, size=(290, 190))

        self.wifi_qr_generator = WiFiQRGenerator(self.tab1)
        self.url_qr_generator = UrlQRGenerator(self.tab2)

        self.tab_control.pack(expand=True, fill="both")

    def clean_up_and_close(self):
        try:
            os.remove('image_pdf.png')
            os.remove('qr_internal.png')
            os.remove('url_qr_file.pdf')
        except FileNotFoundError:
            print("File not found")
        self.root.destroy()

    def run(self):
        self.root.protocol("WM_DELETE_WINDOW", self.clean_up_and_close)
        self.root.mainloop()


if __name__ == "__main__":
    app = WiFiToolboxApp()
    app.run()
