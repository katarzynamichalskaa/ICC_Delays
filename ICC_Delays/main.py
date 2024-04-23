from train_scrapper import TrainScrapper
import os
from SQL_conv import ConvertToSQL

folder_path = r"C:\Users\Kasia\Documents\Data\ipa_15_16"
to_SQL = ConvertToSQL()

if __name__ == '__main__':
    if os.path.exists(folder_path):
        content = TrainScrapper(folder_path)
        content.open_files()
    else:
        print("Path doesn't exist:", folder_path)



