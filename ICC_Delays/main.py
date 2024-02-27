import os
import requests
from bs4 import BeautifulSoup


folder_path = r"C:\Users\Katarzyna\Documents\Data\ipa_15_16"
html_files = [f for f in os.listdir(folder_path) if f.endswith('.html')]

for html_file in html_files:
    file_path = os.path.join(folder_path, html_file)

    with open(file_path, "r", encoding="utf-8") as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, 'html.parser')

    delays = soup.select('td.normal p.dep')

    print(f"Delays from file {html_file}:")
    for delay in delays:
        print(delay.text.strip())
    print()
