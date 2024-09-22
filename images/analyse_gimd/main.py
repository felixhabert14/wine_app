import numpy as np
import csv
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("./private_equity.csv", sep=";", encoding="utf-8", engine="python")
df = pd.DataFrame(data)

def get_pie_chart(name, title):
    df_cleaned = df[df[name].notna() & (df[name] != '')]
    grouped_data = df_cleaned[name].value_counts()

    plt.figure(figsize=(8, 6))
    plt.pie(grouped_data, labels=grouped_data.index, autopct='%1.1f%%', startangle=140)
    plt.title(title)
    plt.show()

def good_multiple():
    df['MULTIPLE (0)'] = df['MULTIPLE (0)'].str.replace(',', '.', regex=False)
    df['MULTIPLE (0)'] = pd.to_numeric(df['MULTIPLE (0)'], errors='coerce') 
    filtered_df = df[df['MULTIPLE (0)'] > 2]
    titles_columns = filtered_df.columns.tolist()
    plt.figure(figsize=(10, 6))
    max_length = 15
    filtered_df['short_company'] = filtered_df[titles_columns[0]].apply(lambda x: x[:max_length] + '...' if len(x) > max_length else x)
    plt.bar(filtered_df['short_company'], filtered_df['MULTIPLE (0)'], color='skyblue')
    plt.xlabel('Fonds')
    plt.ylabel('Multiple')
    plt.title('Fonds avec un multiple > 2')
    plt.xticks(rotation=45)  # Rotate x labels for better readability
    plt.tight_layout()  # Adjust layout to fit labels
    plt.show()



search_name = ["SOCIETES", "CATEGORIE"]
title = f"Proportion des investissements par {search_name[0]}"

get_pie_chart(search_name[0], title)
# good_multiple()