import threading

import speedtest
import customtkinter as ctk


class SpeedTest:
    def __init__(self, tab):
        self.label_text = ctk.CTkLabel(tab, text='Click to perform speed test:')
        self.label_text.pack(pady=10)
        self.button = ctk.CTkButton(tab, text='Speed Test', command=self.speed_thread)
        self.button.pack(pady=10)
        self.tab = tab
        self.progress_bar = ctk.CTkProgressBar(tab, orientation="horizontal", mode='determinate')
        self.progress_bar.pack(pady=10)

    def run_speed_test(self):
        s = speedtest.Speedtest()
        s.get_best_server()
        s.download()
        s.upload(pre_allocate=False)
        results_dict = s.results.dict()
        self.display_results(results_dict)
        return results_dict

    def display_results(self, results_dict):
        result_label = ctk.CTkLabel(self.tab,
                                    text=f"Download Speed: {results_dict['download'] / 1024 / 1024:.2f} MBps\n"
                                         f"Upload Speed: {results_dict['upload'] / 1024 / 1024:.2f} MBps")
        result_label.pack(pady=10)

    def progress(self):
        self.progress_bar.start()
        self.button.configure(state='disabled')
        while self.run_speed_test()['upload'] == '':
            self.button.configure(state='disabled')
        self.button.configure(state='enabled')
        self.progress_bar.stop()

    def speed_thread(self):
        speed_thread = threading.Thread(target=self.run_speed_test, name="Downloader")
        speed_thread.start()
        speed_thread = threading.Thread(target=self.progress, name="Progress")
        speed_thread.start()







