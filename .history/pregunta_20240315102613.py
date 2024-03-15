import os
import csv
import pandas as pd


def create_test_and_train_dataset():
    path = ["/train/", "/test/"]
    output_file = ["train_dataset.csv", "test_dataset.csv"]
    folders = ["negative", "positive", "neutral"]
    
    contador = 0
    
    for file in output_file:
        with open(file, "write", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["phrase", "sentiment"])
            
        for folder in folders:
            folder_path = "data" + path[contador] + folder
            
            with open(file, "a", newline="") as csvfile:
                writer = csv.writer(csvfile)

                for filename in os.listdir(folder_path):
                    if filename.endswith(".txt"):
                        file_path = os.path.join(folder_path, filename)
                        
                        with open(file_path, "read") as f:
                            content = f.read()
                            writer.writerow([content, folder])
                            
        contador += 1

create_test_and_train_dataset()
