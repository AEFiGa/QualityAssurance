"""Python 3.11.5 64-bit """

import sys
import time

bin_nums = [549755813888, 274877906944, 137438953472, 68719476736, 34359738368,
            17179869184, 8589934592, 4294967296, 2147483648, 1073741824,
            536870912, 268435456, 134217728, 67108864, 33554432, 16777216,
            8388608, 4194304, 2097152, 1048576, 524288, 262144, 131072, 65536,
            32768, 16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16,
            8, 4, 2, 1]

def dec_to_bin_hex(original_num):
    """Function that converts from dec to bin and hex"""
    num = original_num
    if num == 0:
        return 0, 0
    if num > 0:
        arr_val_bin = []
        for gbin in bin_nums:
            if num / gbin >= 1:
                arr_val_bin.append("1")
                num = num % gbin
            else:
                arr_val_bin.append("0")
    else:
        arr_val_bin = []
        num = 1099511627776 + num
        for gbin in bin_nums:
            if num / gbin >= 1:
                arr_val_bin.append("1")
                num = num % gbin
            else:
                arr_val_bin.append("0")

    arr_val_hex = []
    hex_vals = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    for i in range(0, 40, 4):
        arr_local = arr_val_bin[i:i+4]
        val = int(arr_local[0])*8 + int(arr_local[1])*4 + int(arr_local[2])*2 + int(arr_local[3])
        arr_val_hex.append(hex_vals[val])


    sol_bin = "".join(arr_val_bin)
    sol_hex = "".join(arr_val_hex)
    if original_num < 0:
        sol_bin = sol_bin[-10:]
        sol_hex = sol_hex[-10:]
    else:
        sol_bin = sol_bin.lstrip('0')
        sol_hex = sol_hex.lstrip('0')
    return sol_bin, sol_hex

def convert_numbers(my_file):
    """Function that obtains a file and executes the base unit conversion"""
    with open(my_file, mode='r', encoding="utf-8") as temporal_file:
        my_text = temporal_file.read()
    elements = my_text.split('\n')
    arr_elements = []
    arr_bin = []
    arr_hex = []
    for element in elements:
        try:
            arr_elements.append(int(element))
        except ValueError:
            print(f"{element} was no valid number")
    for element in arr_elements:
        my_bin, my_hex = dec_to_bin_hex(element)
        arr_bin.append(my_bin)
        arr_hex.append(my_hex)
    header = f"NUM\t{my_file[:-4]}\tBIN\tHEX"
    with open("ConvertionResults.txt", mode='a', encoding="utf-8") as temporal_file:
        print(header)
        temporal_file.write(header + "\n")
        for i in range(len(arr_elements)):
            line = f"{i+1}\t{arr_elements[i]}\t{arr_bin[i]}\t{arr_hex[i]}"
            print(line)
            temporal_file.write(line + "\n")
        temporal_file.write("\n\n")

if __name__ == "__main__":
    start_time = time.time()
    input_file = sys.argv[1]
    convert_numbers(input_file)
    time = time.time() - start_time
    print(f"{time}s seconds")
    