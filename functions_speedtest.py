import threading

import speedtest
import customtkinter as ctk


class SpeedTest:
    def __init__(self, tab):
        self.label_text = ctk.CTkLabel(tab, text='Click to perform speed test:\n')
        self.label_text.pack(pady=10)
        self.button = ctk.CTkButton(tab, text='Speed Test', command=self.speed_thread)
        self.button.pack(pady=10)
        self.tab = tab
        self.progress_bar = ctk.CTkProgressBar(tab, orientation="horizontal", mode='indeterminate')
        self.progress_bar.pack(pady=10)
        self.results_dict = ""
        self.result_label = ctk.CTkLabel(self.tab, text='Download Speed: \nUpload Speed: ')
        self.result_label.pack(pady=10)

    def run_speed_test(self):
        s = speedtest.Speedtest()
        s.get_best_server()
        s.download()
        s.upload(pre_allocate=False)
        self.results_dict = s.results.dict()
        self.display_results(self.results_dict)
        return self.results_dict

    def display_results(self, results):
        self.result_label.configure(text=f"Download Speed: {results['download']/ 8 / 1024 / 1024:.2f} MB/s\n"
                                         f"Upload Speed: {results['upload']/ 8 / 1024 / 1024:.2f} MB/s")

    def progress(self):
        self.progress_bar.start()
        self.button.configure(state='disabled')
        while self.results_dict == '':
            self.button.configure(state='disabled')
        self.button.configure(state='enabled')
        self.results_dict = ''
        self.progress_bar.stop()

    def speed_thread(self):
        speed_thread = threading.Thread(target=self.run_speed_test, name="Downloader")
        speed_thread.start()
        speed_thread = threading.Thread(target=self.progress, name="Progress")
        speed_thread.start()







