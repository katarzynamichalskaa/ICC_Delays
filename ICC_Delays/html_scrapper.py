import re
from bs4 import BeautifulSoup
import requests
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
                times_table = self.get_times(table_row)
                stations_table, data_table = self.get_stations_and_dates(table_row)
            else:
                print(file.name, "No table found")

    def get_stations_and_dates(self, table_row):
        pattern = re.compile(r'\b\d{4}-\d{2}-\d{2}\b')
        stations = []
        data = []
        stations_and_dates = table_row.find_all('th')

        for station_and_date in stations_and_dates:
            text_content = station_and_date.text.strip()
            if pattern.search(text_content):
                data.append(text_content)
            else:
                stations.append(text_content)
        return stations, data

    def get_times(self, table_row):
        times_t = []
        times = table_row.find_all('p')

        for i in range(len(times)):
            if str(times[i].text.strip()) == '→  (---)' and i + 1 < len(times):
                times_t.append(times[i + 1].text.replace("→", "").strip())
            elif str(times[i].text.strip()) == '(---) →' and i - 1 >= 0:
                times_t.append(times[i - 1].text.replace("→", "").strip())
            else:
                times_t.append(times[i].text.replace("→", "").strip())
        return times_t

    def convert_delays(self, times):

        pass

    def zip(self, table1, table2):
        zipped_table = zip(table1, table2)
        print(list(zipped_table))
        return zipped_table
