import os
import string

def rename_files():
    #(1) get file names from a folder
    file_list = os.listdir(r"C:\Users\makshay\Documents\Code\Udacity\Python101\PrankMessage\prank")
    print(file_list)

    saved_path = os.getcwd()
    print(saved_path)

    os.chdir(r"C:\Users\makshay\Documents\Code\Udacity\Python101\PrankMessage\prank")
    #(2) for each file, rename
    for file_name in file_list:
        new_file_name = file_name.translate(None, "0123456789")
        print(new_file_name)
        os.rename(file_name, new_file_name)

rename_files()
