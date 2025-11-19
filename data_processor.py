import pandas as pd
import os

dailysalesdata0 = pd.read_csv('data/daily_sales_data_0.csv')
dailysalesdata1 = pd.read_csv('data/daily_sales_data_1.csv')
dailysalesdata2 = pd.read_csv('data/daily_sales_data_2.csv')

def process_pink_morsel_data(df):
    """
    Filters a dataframe for 'pink morsel', cleans the 'price' column, and calculates 'total_sales'.
    """

    # use .str.lower() to make the filtering case-insensitive
    is_pink = df['product'].astype(str).str.lower() == 'pink morsel'
    df_pink = df.loc[is_pink].copy()

    # Removes the '$' sign from the 'price' column and convert it to a float
    df_pink['price'] = df_pink['price'].astype(str).str.replace('$', '', regex=False).astype(float)

    # Calculate total sales
    df_pink['total_sales'] = df_pink['quantity'] * df_pink['price']

    return df_pink

# Process all three DataFrames
df0_pink = process_pink_morsel_data(dailysalesdata0)
df1_pink = process_pink_morsel_data(dailysalesdata1)
df2_pink = process_pink_morsel_data(dailysalesdata2)

# Combine all three filtered DataFrames into a single DataFrame
final_pink_morsel_data = pd.concat([df0_pink, df1_pink, df2_pink], ignore_index=True)

# Filter columns and save to the required output file
final_data_output = final_pink_morsel_data[['product', 'total_sales', 'date', 'region']]

# Save the resulting DataFrame to the required output file
output_file_path = 'daily_sales.csv'
final_data_output.to_csv(output_file_path, index=False)