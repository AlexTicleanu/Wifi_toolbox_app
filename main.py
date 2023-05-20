import os

import customtkinter as ctk
from functions_speedtest import SpeedTest
from functions_wifi_qr import WiFiQRGenerator
from PIL import Image


class WiFiToolboxApp:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("Wi-Fi Toolbox")
        self.root.minsize(660, 480)
        self.root.maxsize(660, 480)
        self.tab_control = ctk.CTkTabview(self.root)
        self.tab_control.pack(padx=40, pady=40)

        self.tab1 = self.tab_control.add("Wifi QR")
        self.tab2 = self.tab_control.add("Speedtest")
        self.tab_control.pack(expand=True, fill="both")

        self.default_image = Image.open("default_img.png")
        self.default_image = ctk.CTkImage(self.default_image, size=(290, 190))

        self.wifi_qr_generator = WiFiQRGenerator(self.tab1)
        self.speed_test = SpeedTest(self.tab2)

        self.tab_control.pack(expand=True, fill="both")

    def on_closing(self):
        try:
            os.remove('image_pdf.png')
        except:
            print("File not found")
        self.root.destroy()

    def run(self):
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()


if __name__ == "__main__":
    app = WiFiToolboxApp()
    app.run()
