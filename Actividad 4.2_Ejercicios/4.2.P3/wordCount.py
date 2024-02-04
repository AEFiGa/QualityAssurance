"""Python 3.11.5 64-bit """

import sys
import time

def make_dic(my_array):
    """Functino that creates a dictionary for a given array"""
    my_dic = {}
    for element in my_array:
        keys = my_dic.keys()
        if element in keys:
            my_dic[element] += 1
        else:
            my_dic[element] = 1
    return my_dic

def convert_numbers(my_file):
    """Function that obtains an array and creates  dictionary"""
    with open(my_file, mode='r', encoding="utf-8") as temporal_file:
        my_text = temporal_file.read()
    elements = my_text.split('\n')
    for element in elements:
        try:
            my_dic = make_dic(elements)
        except ValueError:
            print(f"{element} was no valid parameter")
    header = f"Labels\tCount of {my_file[:-4]}"
    with open("ConvertionResults.txt", mode='a', encoding="utf-8") as temporal_file:
        print(header)
        temporal_file.write(header + "\n")
        for key, value in my_dic.items():
            line = f"{key}\t{value}"
            print(line)
            temporal_file.write(line + "\n")
        temporal_file.write("\n\n")

if __name__ == "__main__":
    start_time = time.time()
    input_file = sys.argv[1]
    convert_numbers(input_file)
    time = time.time() - start_time
    print(f"{time}s seconds")
