from html_scrapper import HTMLScrapper

folder_path = r"C:\Users\Katarzyna\Documents\Data\ipa_15_16"
database_path = r"C:\Program Files\Microsoft SQL Server\MSSQL15.MSSQLSERVER\MSSQL\DATA\trains_database.db"

if __name__ == '__main__':
    content = HTMLScrapper(folder_path)
    content.open_files()