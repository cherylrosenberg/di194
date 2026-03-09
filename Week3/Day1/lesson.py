import pandas as pd

# # Two types of data structures in python / pandas 

# # 1 Series: a one-dimensional array like object, capable of holding any data type. Like a column in a spreadsheet
# data_series = pd.Series([1,3,5,7,9])

# # 2 Data Frames: two-dimensional, size-mutable, and potentially heterogenious tabular data structure with labeled axes (rows and columns). Like a spreadsheet or SQL table

# data_frame = {
#     'Name' : ['John', 'Anna', 'Peter', 'Linda'],
#     'Age': [28, 34, 29, 32],
#     'City': ['New York', 'Paris', 'Berlin', 'London']
# }

# df = pd.DataFrame(data_frame)

# # To load data from sources like CSV, Excel, SQL
# df = pd.read_csv('path\to\your\csvfile.csv')

# # Cal aslo read the first few lines (.head()), access data, sort, combine two diff data sources based on a column, and more

# Challenge
data = {
    'Book Title': ['The Great Gatsby', 'To Kill a Mockingbird', '1984', 'Pride and Prejudice', 'The Catcher in the Rye'],
    'Author': ['F. Scott Fitzgerald', 'Harper Lee', 'George Orwell', 'Jane Austen', 'J.D. Salinger'],
    'Genre': ['Classic', 'Classic', 'Dystopian', 'Classic', 'Classic'],
    'Price': [10.99, 8.99, 7.99, 11.99, 9.99],
    'Copies Sold': [500, 600, 800, 300, 450]
}

df2 = pd.DataFrame(data)
#print(df2.head())
#print(df2.describe())
#df2.info()
#print(df2.sort_values('Copies Sold'))
#print(df2[df2['Genre'] == 'Classic'])
print(df2.groupby('Author')['Copies Sold'].sum())


