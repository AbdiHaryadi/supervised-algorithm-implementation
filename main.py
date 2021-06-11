import csv
from src.knn import knn
from src.logistic_regression import logistic_regression
from src.id3 import id3

with open(input("Data: "), mode="r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    data_set = [row for row in csv_reader]
    
header = [col_name for col_name in data_set[0].keys()]
col_count = len(header)
print("Pilih label: ")
print(*map(lambda x: "- " + x, header), sep = "\n")
label_idx = int(input("Kolom ke-: ")) - 1
assert label_idx >= 0 and label_idx < col_count
output_col = header[label_idx]

input_col = [col_name for col_name in header if col_name != output_col]
# is_output_float = False
# output_data = [row[output_col] for row in data_set]
"""
try:
    float(output_data[0])
    is_output_float = True
    output_data = list(map(float, output_data))
except ValueError:
    pass
"""
#print(output_data)
train_data = [(tuple([row[col_name] for col_name in input_col]), row[output_col]) for row in data_set]

print("Pilih algoritme:")
print("- KNN (pastikan semua jenis datanya kontinu)")
print("- Logistic Regression (pastikan semua jenis datanya kontinu)")
print("- ID3 (pastikan semua jenis datanya kategorial biner)")
algorithm_idx = int(input("Algoritme ke-: ")) - 1
assert algorithm_idx >= 0 and algorithm_idx < 3

if algorithm_idx == 2:
    id3(data_set, output_col)
else:
    query = []
    print("Masukkan kueri:")
    for col in list(input_col):
        query.append(input("{}: ".format(col)))
    if algorithm_idx == 0:
        result = knn(query, int(input("Nilai K: ")), train_data)
        print(result)
    else: # algorithm_idx == 1
        result = logistic_regression(query, train_data, int(input("Epoch: ")), float(input("Laju belajar: ")))
        print(result)
    



