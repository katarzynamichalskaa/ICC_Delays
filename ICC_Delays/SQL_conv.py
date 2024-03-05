import os
from bs4 import BeautifulSoup
import re
class ConvertToSQL:
    def __init__(self, folder_path, database_path):
        '''
        self.conn = sqlite3.connect(database_path)
        self.cursor = self.conn.cursor()
        self.database_path = database_path
        '''
        self.folder_path = folder_path

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
        pass
    def update_table_SQL(self, date, station_from, station_to, departure_time, arrival_time, delay_minutes):
        self.create_table_SQL()
        self.cursor.execute('''
                        INSERT INTO delays (date, station_from, station_to, departure_time, arrival_time, delay_minutes)
                        VALUES (?, ?, ?, ?, ?, ?)
                    ''', (date, station_from, station_to, departure_time, arrival_time, delay_minutes))
        self.close_connection()
        pass

    def close_connection(self):
        self.conn.commit()
        self.conn.close()
        pass

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
        soup = BeautifulSoup(html_content, "lxml")
        table_rows = soup.select('table')

        for table_row in table_rows:
            if len(table_row.find_all(['th', 'td'])) >= 1:
                print(file.name)
                times_table = self.get_times(table_row)
                stations_table = self.get_stations_and_dates(table_row)
                #self.zip(times_table,stations_table)
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
        print(stations)
        return stations

    def get_times(self, table_row):
        times_t = []
        times = table_row.find_all('p')

        for time in times:
            if str(time.text.strip()) == '→  (---)':
                times_t.append('-')
            else:
                times_t.append(time.text.replace("→", "").strip())
        print(times_t)
        return times_t

    def convert_delays(self):
        pass

    def zip(self, table1, table2):
        zipped_table = zip(table1, table2)
        print(list(zipped_table))
        return zipped_table

folder_path = r"C:\Users\Katarzyna\Documents\Data\ipa_15_16"
database_path = r"C:\Program Files\Microsoft SQL Server\MSSQL15.MSSQLSERVER\MSSQL\DATA\trains_database.db"

converter = ConvertToSQL(folder_path, database_path)
converter.open_files()
