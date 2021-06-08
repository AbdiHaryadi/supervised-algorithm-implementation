import csv
from src.knn import knn 

with open("data.csv", mode="r") as csv_file:
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

query = []
print("Masukkan kueri:")
for col in list(input_col):
    query.append(input("{}: ".format(col)))

print("Pilih algoritme:")
print("- KNN")
print("- Logistic Regression")
print("- ID3")
algorithm_idx = int(input("Algoritme ke-: ")) - 1
assert algorithm_idx >= 0 and algorithm_idx < 3

if (algorithm_idx == 0):
    result = knn(query, int(input("Nilai K: ")), train_data)
    print(result)
else:
    print("Soon.")