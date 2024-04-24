from bs4 import BeautifulSoup
import os
from SQL_conv import ConvertToSQL
from unidecode import unidecode
from weather_scrapper import WeatherScrapper


class TrainScrapper:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.converter = ConvertToSQL()
        self.weather = WeatherScrapper()

    def get_path(self):
        files = []
        html_files = [f for f in os.listdir(self.folder_path) if f.endswith('.html')]

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

        self.finish()

    def scrape(self, html_content, file):

        file_name_with_extension = os.path.basename(file.name)
        file_name, _ = os.path.splitext(file_name_with_extension)
        tab_name = unidecode("train_" + file_name.replace(" ", "_").replace("-", "_").replace("-","").replace(".","_"))

        print(file_name)

        soup = BeautifulSoup(html_content, "html.parser")
        rows = soup.find_all('tr')

        for i in range(0, len(rows), 2):
            date_element = rows[i].find('th', class_='date')
            stations = [th.text for th in rows[i].find_all('th')[1:]]
            times = rows[i + 1].find_all('td', class_='normal')

            if date_element:
                date = date_element.text
                self.get_info(date, stations, times, tab_name)
            else:
                print("No table found")

    def get_info(self, date, stations, times, tab_name):

        for station, time in zip(stations, times):
            arr, delay_arr, dep, delay_dep = self.clean_train_data(time)

            temp, snow, wind = self.weather.get_data(location=station, time=time, date1=date)

            print(temp, snow, wind)

            self.converter.update_table_SQL(tab_name, date, station, arr, delay_arr, dep, delay_dep)

    def clean_train_data(self, time):

        arrival_info = time.find('p', class_='arr').text.replace('→', '').strip()
        departure_info = time.find('p', class_='dep').text.replace('→', '').strip()

        if arrival_info == '(---)':
            arrival_info = departure_info
        if departure_info == '(---)':
            departure_info = arrival_info

        arr, delay_arr = arrival_info.split(' ', 1)
        dep, delay_dep = departure_info.split(' ', 1)

        delay_arr = delay_arr.replace('(', '').replace(')', '').replace('min', '')
        delay_dep = delay_dep.replace('(', '').replace(')', '').replace('min', '')

        return arr, delay_arr, dep, delay_dep

    def finish(self):
        self.converter.close_connection()








