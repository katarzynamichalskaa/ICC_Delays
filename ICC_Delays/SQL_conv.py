import pyodbc

class ConvertToSQL:
    def __init__(self):
        self.server = 'DESKTOP-OK6UCVH'
        self.database = 'trains_database'
        self.connection = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server}; \
            SERVER=' + self.server + '; \
            DATABASE=' + self.database + ';\
            Trusted_Connection=yes;'
        )

        self.cursor = self.connection.cursor()

    def create_table_SQL(self, table_name):
        self.cursor.execute(f'''CREATE TABLE {table_name}
                     (id INT PRIMARY KEY NOT NULL,
                      name TEXT NOT NULL,
                      age INT NOT NULL)''')
    def update_table_SQL(self, table_name, date, station_from, station_to, departure_time, arrival_time, delay_minutes):
        self.create_table_SQL(table_name)
        self.cursor.execute('''
                        INSERT INTO delays (date, station_from, station_to, departure_time, arrival_time, delay_minutes)
                        VALUES (?, ?, ?, ?, ?, ?)
                    ''', (date, station_from, station_to, departure_time, arrival_time, delay_minutes))
        self.close_connection()
        pass

    def close_connection(self):
        self.connection.commit()
        self.connection.close()
