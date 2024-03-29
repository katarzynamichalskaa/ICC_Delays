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
        self.cursor.execute(f'''
            IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES 
                           WHERE TABLE_NAME = N'{table_name}')
            BEGIN
                CREATE TABLE {table_name}
                (date DATE NOT NULL,
                 station TEXT NOT NULL,
                 arrival_time TIME NOT NULL,
                 arrival_delay INT NOT NULL,
                 departure_time TIME NOT NULL,
                 departure_delay INT NOT NULL)
            END
        ''')

    def update_table_SQL(self, table_name, date, station, arrival_time, arrival_delay, departure_time, departure_delay):
        self.create_table_SQL(table_name)
        self.cursor.execute(f'''
                            INSERT INTO {table_name} (date, station, arrival_time, arrival_delay, departure_time, departure_delay)
                            VALUES (?, ?, ?, ?, ?, ?)
                        ''', (date, station, arrival_time, arrival_delay, departure_time, departure_delay))

    def close_connection(self):
        self.connection.commit()
        self.connection.close()
