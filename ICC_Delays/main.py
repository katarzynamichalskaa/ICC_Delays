import os
from bs4 import BeautifulSoup
import sqlite3

folder_path = r"C:\Users\Kasia\Documents\Data\ipa_15_16"
database_path = r"C:\Program Files\Microsoft SQL Server\MSSQL15.MSSQLSERVER\MSSQL\DATA\trains_database.db"


class ConvertToSQL:
    def __init__(self, folder_path, database_path):
        self.conn = sqlite3.connect(database_path)
        self.cursor = self.conn.cursor()
        self.folder_path = folder_path
        self.database_path = database_path

    def create_table_SQL(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS delays (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date DATE,
                station_from TEXT,
                station_to TEXT,
                departure_time TEXT,
                arrival_time TEXT,
                delay_minutes INTEGER
            )
        ''')
    def update_table_SQL(self, date, station_from, station_to, departure_time, arrival_time, delay_minutes):
        self.create_table_SQL()
        self.cursor.execute('''
                        INSERT INTO delays (date, station_from, station_to, departure_time, arrival_time, delay_minutes)
                        VALUES (?, ?, ?, ?, ?, ?)
                    ''', (date, station_from, station_to, departure_time, arrival_time, delay_minutes))
        self.close_connection()

    def close_connection(self):
        self.conn.commit()
        self.conn.close()

    def get_path(self):
        files = []
        html_files = [f for f in os.listdir(self.folder_path) if f.endswith('.html')][:10]

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
        soup = BeautifulSoup(html_content, features="lxml")
        table_rows = soup.select('table')

        for table_row in table_rows:
            if len(table_row.find_all(['th', 'td'])) >= 1:
                print(file.name)
                self.get_times(table_row)
                self.get_stations_and_dates(table_row)
            else:
                print(file.name, "No table found")

    def get_stations_and_dates(self, table_row):
        stations_and_dates = table_row.find_all('th')

        for station_and_date in stations_and_dates:
            print(station_and_date.text.strip())

    def get_times(self, table_row):
        times = table_row.find_all('p')

        for time in times:
            print(time.text.strip())




converter = ConvertToSQL(folder_path, database_path)
converter.open_files()

'''
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
'''