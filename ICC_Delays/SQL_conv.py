import sqlite3

class ConvertToSQL:
    def __init__(self, folder_path, database_path):
        self.conn = sqlite3.connect(database_path)
        self.cursor = self.conn.cursor()
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
        pass #TODO: it doesn't work, check later why
    def update_table_SQL(self, date, station_from, station_to, departure_time, arrival_time, delay_minutes):
        self.create_table_SQL()
        self.cursor.execute('''
                        INSERT INTO delays (date, station_from, station_to, departure_time, arrival_time, delay_minutes)
                        VALUES (?, ?, ?, ?, ?, ?)
                    ''', (date, station_from, station_to, departure_time, arrival_time, delay_minutes))
        self.close_connection()
        pass #TODO: it doesn't work, check later why
    def close_connection(self):
        self.conn.commit()
        self.conn.close()
        pass
