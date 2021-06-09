from random import random
from math import exp

def sigmoid(x):
    try:
        return 1 / (1 + exp(-x))
    except OverflowError:
        print("Overflow!")
        return 0 if x < 0 else 1
    
predicted_y = lambda x, coef: sigmoid(sum([coef[i + 1] * float(x[i]) for i in range(len(x) - 1)]) + coef[0])
actual_to_normalized = lambda x, x_min, x_max: (x - x_min) / (x_max - x_min)
normalized_to_actual = lambda x_norm, x_min, x_max: x_norm * (x_max - x_min) + x_min

def corrected_coefficient(old_coefficient, input_data, output_data, predicted, learning_rate):
    new_coefficient = old_coefficient.copy()
    # Inti dari rumus: semakin tidak ke ujung predicted-nya, semakin sedikit koefisiennya berkurang
    # Hati-hati overfit
    # Jika expectednya lebih tinggi dari predicted, harusnya dinaikkan
    new_coefficient[0] += learning_rate * (output_data - predicted) * predicted * (1 - predicted)
    for i in range(len(input_data)):
        new_coefficient[i + 1] += learning_rate * (output_data - predicted) * predicted * (1 - predicted) * input_data[i]
    
    return new_coefficient
    
def accuracy(coefficient, train_data):
    correct_count = 0
    for data in train_data:
        answer = round(predicted_y(data[0], coefficient))
        if answer == data[1]:
            correct_count += 1
            
    return correct_count / len(train_data)
        

def logistic_regression(query, train_data, epoch, learning_rate):
    possible_output = list(set([data[1] for data in train_data]))
    assert len(possible_output) == 2
    input_data = list(map(lambda x: x[0], train_data))
    min_value = [min(list(map(lambda x: float(x[i]), input_data))) for i in range(len(input_data[0]))]
    max_value = [max(list(map(lambda x: float(x[i]), input_data))) for i in range(len(input_data[0]))]
    to_normalized = lambda x: tuple([actual_to_normalized(float(x[j]), min_value[j], max_value[j]) for j in range(len(input_data[0]))])
    new_train_data = [(to_normalized(input_data[i]), 0 if train_data[i][1] == possible_output[0] else 1) for i in range(len(input_data))]

    # Ambil nilai koefisien; bebas: y = b0 + b1x1 + b2x2 + ...
    coefficient = [random() * 2 - 1 for _ in range(len(query) + 1)]
    
    # Train: Lakukan sebanyak epoch kali
    for _ in range(epoch):
        # print(accuracy(coefficient, new_train_data))
        # print(coefficient)
    
        for data in new_train_data:
            # Kemudian ambil nilai sigmoidnya -> yhat
            y_hat = predicted_y(data[0], coefficient)
            
            # Update koefisien dengan menggunakan learning_rate
            coefficient = corrected_coefficient(coefficient, data[0], data[1], y_hat, learning_rate)
            
    
    temp_result = round(predicted_y(to_normalized(query), coefficient))
    print("Akurasi:", accuracy(coefficient, new_train_data))
    return possible_output[int(temp_result)]
    
if __name__ == "__main__":
    my_input = [(random() * 1000, random() * 1000) for _ in range(100)]
    my_train_data = [(data, "Lebih kecil" if data[0] <= data[1] else "Lebih besar") for data in my_input]
    result = logistic_regression([1, 0], my_train_data, 1000, 0.01)
    print(result)
    