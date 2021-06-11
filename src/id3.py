from math import log

"""
class Tree:
    def __init__(self, root):
        self._root = root
        self._left = None
        self._branch_left_name = None
        self._right = None
        self._branch_right_name = None
        
    def set_left(self, new_left_subtree, branch_name = ""):
        self._left = new_left_subtree
        self._branch_left_name = branch_name
    
    def set_right(self, new_right_subtree, branch_name = ""):
        self._right = new_right_subtree
        self._branch_left_name = branch_name
        
    def map_branch_and_leaf_tree(self, node_list, branch_and_leaf_map):
        # Leaf is in last element of branch_and_leaf_map
        if (self._left == None and self._right == None):
            self._root = node_list[-1] + str(branch_and_leaf_map[-1][int(self._root)])
        else:
            node_index = node_list.index(self._root)
            if self._left != None:
                self._branch_left_name = branch_and_leaf_map[node_index]
"""
        
def id3(data_set, target_name):
    # Ganti semua data ke nilai boolean (buat mapnya juga)
    binary_data_set, data_map = change_data_set_to_binary_value(data_set)
    
    # Eksekusi
    # result = id3_with_binary(binary_train_data, col_list)
    id3_with_binary(binary_data_set, target_name, data_map)
    
    # Map tree (nanti branch untuk tree mengandung nama sesuai data_map)
    # result.map_branch_and_leaf_tree(col_list, data_map)
    # return result

"""
def change_train_data_to_binary_value(train_data):
    map_result = []
    input_data = list(map(lambda x: x[0], train_data))
    output_data = list(map(lambda x: x[1], train_data))
    # For input
    for i in range(len(input_data[0])):
        possible_values = set(map(lambda x: x[i], input_data))
        assert len(possible_values) == 2
        map_result.append(tuple(possible_values))
    # For output
    possible_values = set(output_data)
    assert len(possible_values) == 2
    map_result.append(tuple(possible_values))
    
    new_train_data = []
    for data in train_data:
        new_input_data = []
        for i in range(len(data[0])):
            new_input_data.append(map_result[i][0] == data[0][i])
        new_output_data = map_result[-1] == data[1]
        new_train_data.append((new_input_data, new_output_data))
        
    return (new_train_data, map_result)
"""

def change_data_set_to_binary_value(data_set):
    map_result = dict()
    data_set_keys = list(data_set[0].keys())
    for key in data_set_keys:
        possible_values = set(map(lambda x: x[key], data_set))
        #print(key, possible_values)
        assert len(possible_values) == 2
        map_result[key] = tuple(possible_values)
    
    new_data_set = []
    for data in data_set:
        new_data = dict()
        for key in data_set_keys:
            # Mengubah di setiap dictionary menjadi sesuai dengan map
            # Yang indeks 0 bernilai false, indeks 1 bernilai true
            new_data[key] = map_result[key][1] == data[key]
        new_data_set.append(new_data)
        
    return (new_data_set, map_result)
    
def id3_with_binary(data_set, target_name, data_map, depth = 0):
    def print_with_depth(printee, depth, end = "\n"):
        print(" " * (4 * depth) + printee, end = end)
    data_set_keys = list(data_set[0].keys())
    possible_targets = list(set(map(lambda x: x[target_name], data_set)))
    total_data = len(data_set)
    
    if len(possible_targets) == 1:
        print_with_depth("Hasil: {} = {}".format(target_name, data_map[target_name][int(possible_targets[0])]), depth, end = " ")
        print("(Banyak data: {})".format(total_data))
            
    elif len(data_set_keys) == 1: # Jika train_data inputnya kosong, kembalikan data yang dominan
        dominant_output = mode(list(map(lambda x: x[target_name], data_set)))
        print_with_depth(
            "Hasil: {} = {}".format(
                target_name,
                data_map[target_name][int(dominant_output[0])] if len(dominant_output) <= 1 else "?" 
            ),
            depth, end = " ")
        print("(Banyak data: {})".format(total_data), end = " ")
        if len(dominant_output) == 1:
            total_data_with_dominant_value = len(list(filter(lambda x: x[target_name] == dominant_output[0], data_set)))
            print("(Akurasi: {:.2f}%)".format(100 * total_data_with_dominant_value / total_data))
        else:
            print() # newline
            
    else:
        # Cari kolom dengan information gain tertinggi
        migc = max(
            list(filter(lambda x: x != target_name, data_set_keys)),
            key = lambda x: information_gain(data_set, x, target_name)
        )
        
        # Buat pohon dengan kolom sebagai root tersebut
        #tree_result = Tree(col_list[migci])
        
        # Dari kolom tersebut, buat dua sub_train_data:
        #     - Satu yang bernilai True dari kolom tersebut
        #     - Satu lagi yang bernilai False
        #     - Tidak usah ditulis kolom itu lagi.
        l_data_set, r_data_set = split_respect_to_column(data_set, migc)
        
        # Proses kedua train_data dengan id3
        #l_result = id3_with_binary(l_data, col_list[:migci] + col_list[migci+1:])
        #r_result = id3_with_binary(l_data, col_list[:migci] + col_list[migci+1:])
        
        if (len(l_data_set) != 0 and len(r_data_set) != 0):
            print_with_depth("Jika {} = {}".format(migc, data_map[migc][0]), depth)
            id3_with_binary(l_data_set, target_name, data_map, depth + 1)
            print_with_depth("Jika {} = {}".format(migc, data_map[migc][1]), depth)
            id3_with_binary(r_data_set, target_name, data_map, depth + 1)
        else:
            if (len(l_data_set) != 0):
                id3_with_binary(l_data_set, target_name, data_map, depth)
            else:
                assert len(r_data_set) != 0
                id3_with_binary(r_data_set, target_name, data_map, depth)
        
        # train_data untuk True sebagai upapohon kiri dari root tadi, False untuk kanan
        #tree_result.set_left(l_result)
        #tree_result.set_right(r_result)
        
        # Kembalikan pohonnya
        #return tree_result
    
def information_gain(data_set, column_name, target_name):
    # IG(S, A) = E(S) - sum((len(Sv) / len(S)) * E(Sv))
    data_sets_v = []
    for v in [False, True]:
        current_data_set = list(filter(lambda x: x[column_name] == v, data_set))
        if len(current_data_set) > 0:
            data_sets_v.append(current_data_set.copy())
        
    for ds in data_sets_v:
        for i in range(len(ds)):
            ds[i] = ds[i].copy()
            ds[i].pop(column_name)
        
    
    result = (
        entropy(data_set, target_name)
        - sum(list(map(
            lambda sv: (len(sv) / len(data_set)) * entropy(sv, target_name),
            data_sets_v
        )))
    )
    
    return result

def entropy(data_set, target_name):
    # - sum(p_i * log_2(p_i)); 1 <= i <= banyak jenis data target
    total_data = len(data_set)
    count_with_true_value = len(list(filter(lambda x: x[target_name], data_set)))
    probabilities = [1 - count_with_true_value / total_data, count_with_true_value / total_data]
    result = -sum(
        [p * log(p, 2) if p != 0 else 0 for p in probabilities]
    )
    return result
    
    
def mode(mylist):
    assert len(mylist) > 0
    types_of_data = list(set(mylist))
    frequencies = list(map(lambda x: len(list(filter(lambda y: y == x, mylist))), types_of_data))
    max_frequency = max(frequencies)
    result = [types_of_data[i] for i in range(len(types_of_data)) if frequencies[i] == max_frequency]
    return result
    
def split_respect_to_column(data_set, column_name):
    false_data_set = list(filter(lambda x: not x[column_name], data_set))
    true_data_set = list(filter(lambda x: x[column_name], data_set))
    for i in range(len(false_data_set)):
        false_data_set[i] = false_data_set[i].copy()
        false_data_set[i].pop(column_name)
    for i in range(len(true_data_set)):
        true_data_set[i] = true_data_set[i].copy()
        true_data_set[i].pop(column_name)
    return (false_data_set, true_data_set)
    
if __name__ == "__main__":
    # Data from open genus
    data_set = [
        {
            "Outlook is Sunny": "TRUE",
            "Outlook is Overcast": "FALSE",
            "Outlook is Rain": "FALSE",
            "Temperature is Hot": "TRUE",
            "Temperature is Mild": "FALSE",
            "Temperature is Cool": "FALSE",
            "Humidity": "High",
            "Wind": "Weak",
            "Play Tennis": "No"
        },
        {
            "Outlook is Sunny": "TRUE",
            "Outlook is Overcast": "FALSE",
            "Outlook is Rain": "FALSE",
            "Temperature is Hot": "TRUE",
            "Temperature is Mild": "FALSE",
            "Temperature is Cool": "FALSE",
            "Humidity": "High",
            "Wind": "Strong",
            "Play Tennis": "No"
        },
        {
            "Outlook is Sunny": "FALSE",
            "Outlook is Overcast": "TRUE",
            "Outlook is Rain": "FALSE",
            "Temperature is Hot": "TRUE",
            "Temperature is Mild": "FALSE",
            "Temperature is Cool": "FALSE",
            "Humidity": "High",
            "Wind": "Weak",
            "Play Tennis": "Yes"
        },
        {
            "Outlook is Sunny": "FALSE",
            "Outlook is Overcast": "FALSE",
            "Outlook is Rain": "TRUE",
            "Temperature is Hot": "FALSE",
            "Temperature is Mild": "TRUE",
            "Temperature is Cool": "FALSE",
            "Humidity": "High",
            "Wind": "Weak",
            "Play Tennis": "Yes"
        },
        {
            "Outlook is Sunny": "FALSE",
            "Outlook is Overcast": "FALSE",
            "Outlook is Rain": "TRUE",
            "Temperature is Hot": "FALSE",
            "Temperature is Mild": "FALSE",
            "Temperature is Cool": "TRUE",
            "Humidity": "Normal",
            "Wind": "Weak",
            "Play Tennis": "Yes"
        },
        {
            "Outlook is Sunny": "FALSE",
            "Outlook is Overcast": "FALSE",
            "Outlook is Rain": "TRUE",
            "Temperature is Hot": "FALSE",
            "Temperature is Mild": "FALSE",
            "Temperature is Cool": "TRUE",
            "Humidity": "Normal",
            "Wind": "Strong",
            "Play Tennis": "No"
        },
        {
            "Outlook is Sunny": "FALSE",
            "Outlook is Overcast": "TRUE",
            "Outlook is Rain": "FALSE",
            "Temperature is Hot": "FALSE",
            "Temperature is Mild": "FALSE",
            "Temperature is Cool": "TRUE",
            "Humidity": "Normal",
            "Wind": "Strong",
            "Play Tennis": "Yes"
        },
        {
            "Outlook is Sunny": "TRUE",
            "Outlook is Overcast": "FALSE",
            "Outlook is Rain": "FALSE",
            "Temperature is Hot": "FALSE",
            "Temperature is Mild": "TRUE",
            "Temperature is Cool": "FALSE",
            "Humidity": "High",
            "Wind": "Weak",
            "Play Tennis": "No"
        },
        {
            "Outlook is Sunny": "TRUE",
            "Outlook is Overcast": "FALSE",
            "Outlook is Rain": "FALSE",
            "Temperature is Hot": "FALSE",
            "Temperature is Mild": "FALSE",
            "Temperature is Cool": "TRUE",
            "Humidity": "Normal",
            "Wind": "Weak",
            "Play Tennis": "Yes"
        },
        {
            "Outlook is Sunny": "FALSE",
            "Outlook is Overcast": "FALSE",
            "Outlook is Rain": "TRUE",
            "Temperature is Hot": "FALSE",
            "Temperature is Mild": "TRUE",
            "Temperature is Cool": "FALSE",
            "Humidity": "Normal",
            "Wind": "Weak",
            "Play Tennis": "Yes"
        },
        {
            "Outlook is Sunny": "TRUE",
            "Outlook is Overcast": "FALSE",
            "Outlook is Rain": "FALSE",
            "Temperature is Hot": "FALSE",
            "Temperature is Mild": "TRUE",
            "Temperature is Cool": "FALSE",
            "Humidity": "Normal",
            "Wind": "Strong",
            "Play Tennis": "Yes"
        },
        {
            "Outlook is Sunny": "FALSE",
            "Outlook is Overcast": "TRUE",
            "Outlook is Rain": "FALSE",
            "Temperature is Hot": "FALSE",
            "Temperature is Mild": "TRUE",
            "Temperature is Cool": "FALSE",
            "Humidity": "High",
            "Wind": "Strong",
            "Play Tennis": "Yes"
        },
        {
            "Outlook is Sunny": "FALSE",
            "Outlook is Overcast": "TRUE",
            "Outlook is Rain": "FALSE",
            "Temperature is Hot": "TRUE",
            "Temperature is Mild": "FALSE",
            "Temperature is Cool": "FALSE",
            "Humidity": "Normal",
            "Wind": "Weak",
            "Play Tennis": "Yes"
        },
        {
            "Outlook is Sunny": "FALSE",
            "Outlook is Overcast": "FALSE",
            "Outlook is Rain": "TRUE",
            "Temperature is Hot": "FALSE",
            "Temperature is Mild": "TRUE",
            "Temperature is Cool": "FALSE",
            "Humidity": "High",
            "Wind": "Strong",
            "Play Tennis": "No"
        }
    ]

    # print(*change_data_set_to_binary_value(data_set), sep = "\n------\n")
    id3(data_set, "Play Tennis")