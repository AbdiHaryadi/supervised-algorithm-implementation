from random import random

def knn(query, k, train_data):
    # Ambil semua distance antara data dengan kueri
    # Sortir (dari yang terdekat), dan ambil nilai k-pertama
    # Ambil modus dari hasilnya
    assert k >= 1 and k <= len(train_data)
    
    input_data = list(map(lambda x: x[0], train_data))
    idx_distance = []
    for i in range(len(train_data)):
        idx_distance.append((i, distance(train_data[i][0], query)))
    idx_distance.sort(key = lambda x: x[1])
    k_nearest_output = list(map(lambda x: train_data[x[0]][1], idx_distance[:k]))
    return mode(k_nearest_output)

def distance(list1, list2):
    assert (dimension := len(list1) == len(list2))
    # No need sqrt
    return sum([(float(list1[i]) - float(list2[i])) ** 2 for i in range(dimension)])
    
def mode(mylist):
    assert len(mylist) > 0
    types_of_data = list(set(mylist))
    frequencies = list(map(lambda x: len(list(filter(lambda y: y == x, mylist))), types_of_data))
    max_frequency = max(frequencies)
    result = [types_of_data[i] for i in range(len(types_of_data)) if frequencies[i] == max_frequency]
    return result
    
                
            
    
if __name__ == "__main__":
    my_input = [(random() * 10, random() * 10) for _ in range(10)]
    my_train_data = [(data, 1 if data[0] <= data[1] else 0) for data in my_input]
    result = knn([10, 0], 5, my_train_data)
    print(result)
    