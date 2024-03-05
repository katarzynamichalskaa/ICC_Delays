from sql_conv import ConvertToSQL

folder_path = r"C:\Users\Katarzyna\Documents\Data\ipa_15_16"
database_path = r"C:\Program Files\Microsoft SQL Server\MSSQL15.MSSQLSERVER\MSSQL\DATA\trains_database.db"

if __name__ == '__main__':
    converter = ConvertToSQL(folder_path, database_path)
    converter.open_files()