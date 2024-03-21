import re
from bs4 import BeautifulSoup
import os

class HTMLScrapper:
    def __init__(self, folder_path):
        self.folder_path = folder_path

    def get_path(self):
        files = []
        html_files = [f for f in os.listdir(self.folder_path) if f.endswith('.html')][:3]

        for html_file in html_files:
            file_path = os.path.join(self.folder_path, html_file)
            files.append(file_path)
        return files

    def open_files(self):
        files = self.get_path()

        for file_path in files:
            with open(file_path, "r", encoding="utf-8") as file:
                html_content = file.read()
            self.scrape(html_content, file)

    def scrape(self, html_content, file):
        soup = BeautifulSoup(html_content, "lxml")
        table_rows = soup.select('table')

        for table_row in table_rows:
            if len(table_row.find_all(['th', 'td'])) >= 1:
                print(file.name)
                self.get_data(table_row)
                self.get_times(table_row)
            else:
                print(file.name, "No table found")

    def get_data(self, table):
        data = table.find_all('th')
        data_table = [data.text.split() for data in data]
        print(data_table)

    def get_times(self, table):
        data = table.find_all('td', class_="normal")
        data_table = [data.text for data in data]
        print(data_table)




