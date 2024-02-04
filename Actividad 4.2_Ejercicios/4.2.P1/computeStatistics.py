"""Python 3.11.5 64-bit """

import sys
import time

def order_elements(my_array):
    """Function that orders array and creates dictionary"""
    order_array = []
    my_dic = {}
    for element in my_array:
        keys = my_dic.keys()
        if element in keys:
            my_dic[element] += 1
        else:
            my_dic[element] = 1
        if len(order_array) == 0:
            order_array.append(element)
        else:
            key = 0
            for order_element in order_array:
                if order_element >= element:
                    new_order = order_array[:key] + [element] + order_array[key:]
                    order_array = new_order
                    break
                if key == len(order_array) - 1:
                    new_order = order_array[:key + 1] + [element] + order_array[key + 1:]
                    order_array = new_order
                    break
                key = key + 1
    return order_array, my_dic

def my_mean(my_dic):
    """Function that obtains the mean"""
    my_sum = 0
    my_qty = 0
    for key, value in my_dic.items():
        my_sum += key * value
        my_qty += value
    avg = my_sum / my_qty
    return avg

def my_median(my_array):
    """Function that obtains the median"""
    if len(my_array) % 2 == 0:
        median =  (my_array[int(len(my_array)/2) - 1] + my_array[int(len(my_array)/2)]) / 2
    else:
        median = my_array[int(len(my_array)/2) + 1]
    return median

def my_mode(my_dic):
    """Function that obtains the mode"""
    my_max = 0
    mode = []
    for key, value in my_dic.items():
        if value == my_max:
            mode.append(key)
        elif value > my_max:
            mode = [key]
            my_max = value
    if my_max > 1:
        return mode
    return []

def my_std_dev(my_dic, mean):
    """Function that obtains the variation and the standar deviation"""
    my_sum = 0
    my_qty = 0
    for key, value in my_dic.items():
        my_sum += value * (key - mean) ** 2
        my_qty += value
    var = my_sum / my_qty
    dev = var ** (0.5)
    return var, dev

def descriptive_statistics(my_file):
    """Function that recieves a file and provides the descriptive statistics"""
    with open(my_file, mode='r', encoding="utf-8") as temporal_file:
        my_text = temporal_file.read()
    elements = my_text.split('\n')
    int_elements = []
    for element in elements:
        try:
            int_elements.append(float(element))
        except ValueError:
            print(f"{element} was no valid number")

    order_array, my_dic = order_elements(int_elements)
    mean = my_mean(my_dic)
    median = my_median(order_array)
    mode = my_mode(my_dic)
    var, dev = my_std_dev(my_dic, mean)

    with open("StatisticsResults.txt", mode='a', encoding="utf-8") as temporal_file:
        my_text1 = f"File:{my_file}\nMean:{mean}\nMedian:{median}\n"
        my_text2 = f"Mode:{mode}\nVariance:{var}\nStandarDeviation:{dev}\n\n"
        my_text = my_text1 + my_text2
        temporal_file.write(my_text)
    print(my_text)


if __name__ == "__main__":
    start_time = time.time()
    input_file = sys.argv[1]
    descriptive_statistics(input_file)
    time = time.time() - start_time
    print(f"{time}s seconds")
