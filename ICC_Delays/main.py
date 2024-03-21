from html_scrapper import HTMLScrapper
import os

folder_path = r"C:\Users\Kasia\Documents\Data\ipa_15_16"
database_path = r"C:\Program Files\Microsoft SQL Server\MSSQL15.MSSQLSERVER\MSSQL\DATA\trains_database.db"

if __name__ == '__main__':
    if os.path.exists(folder_path):
        content = HTMLScrapper(folder_path)
        content.open_files()
    else:
        print("Path doesn't exist:", folder_path)
