"""Python 3.11.5 64-bit """

import sys
import time
import pandas as pd


def compute_sales(catalogue_file, sales_file):
    """Function for readin 2 json files and get the ticket total amount"""
    catalogue_df = pd.read_json(catalogue_file)
    catalogue_df = catalogue_df[['title', 'price']]
    sales_df = pd.read_json(sales_file)
    sales_df = sales_df[['SALE_ID', 'Product', 'Quantity']]
    new_columns = {'SALE_ID': 'id', 'Product': 'title', 'Quantity': 'quantity'}
    sales_df = sales_df.rename(columns=new_columns)

    result_df = pd.merge(sales_df, catalogue_df, on='title')
    subtotal = result_df.apply(lambda x: x.quantity * x.price, axis=1)
    result_df['subtotal'] = subtotal
    result_df = result_df.sort_values(by=['id'])
    total = result_df.subtotal.sum().round(2)
    result_df.loc[len(result_df.index)] = ['', '', '', 'Total', total]
    string_df = result_df.to_string(header=True, index=False)

    with open("SalesResults.txt", mode='w', encoding="utf-8") as temporal_file:
        temporal_file.write(string_df)
    print(string_df)


if __name__ == "__main__":
    start_time = time.time()
    CATALOGUE = sys.argv[1]
    SALES = sys.argv[2]
    compute_sales(CATALOGUE, SALES)
    time = time.time() - start_time
    exec_time = f"\nExecution time: {time} seconds"
    with open("SalesResults.txt", mode='a', encoding="utf-8") as results_file:
        results_file.write(exec_time)
    print(exec_time)
