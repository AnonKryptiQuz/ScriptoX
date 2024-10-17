# ScriptoX: SVG & PDF Creator with Embedded JavaScript

**ScriptoX** combines two powerful functionalities: creating SVG and PDF files with embedded JavaScript code. Designed for educational and testing purposes, this tool enables the users to generate files demonstrating how embedded scripts can operate within SVG and PDF documents. It's useful for security researchers and developers looking to understand the implications of embedded scripts. (Not an XSS tool)

## **Features**

- **SVG Creation**: Generate SVG files with customizable embedded JavaScript.
- **PDF Creation**: Create PDF files that include JavaScript actions.
- **User-Friendly**: Interactive prompts for easy input and configuration.
- **Educational Use**: Ideal for learning about embedded scripts in SVGs and PDFs and their potential security implications.

## **Prerequisites**

- **Python 3.7+**
- **colorama**
- **prompt_toolkit**

## **Installation**

1. **Clone the repository:**

   ```bash
   git clone https://github.com/AnonKryptiQuz/ScriptoX.git
   cd ScriptoX
   ```

2. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

   **Ensure `requirements.txt` contains:**

   ```text
   colorama==0.4.6
   prompt_toolkit==3.0.36
   ```

## **Usage**

1. **Run the tool:**

   ```bash
   python ScriptoX.py
   ```

2. **Follow the prompts to specify the SVG or PDF filename and the JavaScript code to embed.**

3. **The generated file will be saved with the specified filename.**

## **Disclaimer**

- **Educational Purposes Only**: ScriptoX is intended for educational and research use. The tool should not be used for illegal or malicious activities. It is the user’s responsibility to ensure compliance with local laws and regulations.

## **Author**

**Created by:** [AnonKryptiQuz](https://AnonKryptiQuz.github.io/)
