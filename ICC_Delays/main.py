import os
import requests
from bs4 import BeautifulSoup
import sqlite3

folder_path = r"C:\Users\Kasia\Documents\Data\ipa_15_16"
database_path = r"C:\Program Files\Microsoft SQL Server\MSSQL15.MSSQLSERVER\MSSQL\DATA\trains_database.db"

conn = sqlite3.connect(database_path)
cursor = conn.cursor()

cursor.execute('''
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

html_files = [f for f in os.listdir(folder_path) if f.endswith('.html')]

for html_file in html_files:
    file_path = os.path.join(folder_path, html_file)

    with open(file_path, "r", encoding="utf-8") as file:
        html_content = file.read()
    soup = BeautifulSoup(html_content, features="lxml")

    table_rows = soup.select('table tr')
    if len(table_rows) <= 2:
        print(f"Plik {html_file} nie zawiera danych do przetworzenia. Pomijam.")
    else:
        for row in soup.find('table').find_all('tr'):
            print(file.name)
            date = row.find("th", class_="date").text.strip()
            stations = row.find()
            print(date)
            #station_from = stations[1].text.strip()
            #station_to = stations[-1].text.strip()
            times = row.find("td", class_="normal")
            print(times)
            print(date, times)

            cursor.execute('''
                INSERT INTO delays (date, station_from, station_to, departure_time, arrival_time, delay_minutes)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (date, station_from, station_to, departure_time, arrival_time, delay_minutes))

# Zatwierdzanie zmian i zamykanie połączenia z bazą danych
conn.commit()
conn.close()


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