## Wi-Fi Toolbox Documentation

The Wi-Fi Toolbox is a Python application that provides various functionalities related to Wi-Fi networks, including generating Wi-Fi QR codes and performing speed tests. The application is implemented using a class-based approach for improved organization and reusability.

![image](https://github.com/AlexTicleanu/Wifi_toolbox_app/assets/48204339/4f9ca53e-02f9-407c-88a9-52ae8e1dcf51)

### File Structure

The Wi-Fi Toolbox consists of three main files:

1. `main.py`: This file contains the main entry point of the application and defines the `App` class, which represents the graphical user interface (GUI) of the application.

2. `functions_wifi_qr.py`: This file contains utility functions related to generating Wi-Fi QR codes and handling PDF generation and conversion. The functions are encapsulated within the `WiFiQR` class.

3. `functions_speedtest.py`: This file contains the `SpeedTest` class, which handles the speed test functionality using the `speedtest` library.

### Usage

To use the Wi-Fi Toolbox, follow these steps:

1. Run the `main.py` file.

2. The application window will appear with two tabs: "Wifi QR" and "Speedtest".

#### Tab: Wifi QR

In this tab, you can generate Wi-Fi QR codes and save them as PDF files.

- Enter the Wi-Fi name (SSID) in the "Wifi Name" input field.

- Enter the Wi-Fi password in the "Password" input field.

- Check the "Save name and password" checkbox if you want to save the Wi-Fi details for future use.

- Click the "Generate wifi QR" button to generate a Wi-Fi QR code.

- The generated QR code will be displayed in the image area.

- You can check the "Name and password visible on pdf" checkbox to include the Wi-Fi name and password in the generated PDF file.

- Click the "Open PDF" button to open the generated PDF file, if it exists.

#### Tab: Speedtest

In this tab, you can perform a speed test to measure your download and upload speeds.

- Click the "Speed Test" button to initiate the speed test.

- The download and upload speeds will be displayed in the result area.

### Classes and Methods

The following classes and their methods are used in the Wi-Fi Toolbox:

#### Class: App (in main.py)

- `__init__(self)`: Initializes the application window and creates the GUI components.

- `validate_inputs(self)`: Validates the input fields for the Wi-Fi name and password.

- `submit_action(self)`: Handles the submission of Wi-Fi details and initiates QR code generation.

- `open_pdf(self)`: Opens the generated PDF file, if it exists.

- `submit_button(self)`: Handles the submission of Wi-Fi details and checkbox actions.

- `save_file_data(self)`: Saves the Wi-Fi name and password to a file.

- `checkbox_print_action(self)`: Handles the checkbox action for including details in the PDF.

- `checkbox_details_with_validation(self)`: Validates the input fields and performs the checkbox action.

- `view_pdf(self, route_to_picture)`: Opens the PDF file in the default system PDF viewer.

- `generate_qr_wifi(self, ssid, password)`: Generates a Wi-Fi QR code image based on the provided SSID and password.

- `generate_picture_and_text(self, ssid, password, details)`: Generates a list of content for the PDF file, including the QR code and optional details.

- `cleanup_image_and_pdf(self)`: Removes the generated PDF and image files.

- `generate_pdf_action(self, content)`: Generates a PDF file based on the provided content.

- `pdf_to_image(self, pdf_file)`: Converts a PDF file to an image.

- `save_jpg_image(self, ssid,

 password)`: Saves a Wi-Fi QR code image as a JPG file.

- `save_pdf(self, ssid, password, details)`: Generates and saves a PDF file with the Wi-Fi details.

- `save_input_data_in_set(self, ssid, password)`: Saves the Wi-Fi name and password to a file.

#### Class: WiFiQR (in functions_wifi_qr.py)

- `generate_qr_wifi(cls, ssid, password)`: Generates a Wi-Fi QR code image based on the provided SSID and password.

- `view_pdf(cls, route_to_picture)`: Opens the PDF file in the default system PDF viewer.

- `generate_picture_and_text(cls, ssid, password, details)`: Generates a list of content for the PDF file, including the QR code and optional details.

- `cleanup_image_and_pdf(cls)`: Removes the generated PDF and image files.

- `generate_pdf_action(cls, content)`: Generates a PDF file based on the provided content.

- `pdf_to_image(cls, pdf_file)`: Converts a PDF file to an image.

- `save_jpg_image(cls, ssid, password)`: Saves a Wi-Fi QR code image as a JPG file.

- `save_pdf(cls, ssid, password, details)`: Generates and saves a PDF file with the Wi-Fi details.

- `save_input_data_in_set(cls, ssid, password)`: Saves the Wi-Fi name and password to a file.

#### Class: SpeedTest (in functions_speedtest.py)

- `__init__(self, tab)`: Initializes the SpeedTest class with the specified tab for displaying the results.

- `run_speed_test(self)`: Initiates a speed test and retrieves the download and upload speeds.

- `display_results(self, results_dict)`: Displays the download and upload speeds in the specified tab.

### Dependencies

The Wi-Fi Toolbox requires the following dependencies:

- `customtkinter`: A custom module that extends the functionality of the Tkinter library.

- `PIL`: The Python Imaging Library for image processing and manipulation.

- `reportlab`: A library for generating PDF files.

- `qrcode`: A library for generating QR codes.

- `pypdfium2`: A library for converting PDF files to images.

- `speedtest`: A library for performing internet speed tests.

### Conclusion

The Wi-Fi Toolbox provides a convenient interface for generating Wi-Fi QR codes and performing speed tests. The class-based approach improves code organization and allows for easier maintenance and extensibility. By following the provided documentation, users can quickly generate Wi-Fi QR codes, save them as PDF files, and perform speed tests to measure their internet connection speeds.
