import pandas as pd

path = 'D:/Project/ABSA/datasets/vlsp2018_restaurant/3-VLSP2018-SA-Restaurant-test.csv'

# Đọc file CSV
df = pd.read_csv(path, encoding='utf-8')

# Giữ nguyên cột Review
# Đổi tên cột AMBIENCE#GENERAL thành AMBIENCE và thay giá trị
df.rename(columns={'AMBIENCE#GENERAL': 'AMBIENCE'}, inplace=True)
df['AMBIENCE'] = df['AMBIENCE'].replace({0: 0, 1: 1, 2: 1, 3: 1})

# Gộp các cột DRINKS#PRICES, DRINKS#QUALITY, DRINKS#STYLE&OPTIONS, FOOD#PRICES, FOOD#QUALITY, FOOD#STYLE&OPTIONS thành cột FOOD
food_columns = ['DRINKS#PRICES', 'DRINKS#QUALITY', 'DRINKS#STYLE&OPTIONS', 
                'FOOD#PRICES', 'FOOD#QUALITY', 'FOOD#STYLE&OPTIONS']
df['FOOD'] = df[food_columns].apply(lambda x: 0 if all(value == 0 for value in x) else 1, axis=1)
df.drop(columns=food_columns, inplace=True)  # Bỏ các cột cũ

# Bỏ cột RESTAURANT#MISCELLANEOUS và RESTAURANT#GENERAL
df.drop(columns=['RESTAURANT#MISCELLANEOUS', 'RESTAURANT#GENERAL'], inplace=True)

# Đổi tên cột RESTAURANT#PRICES thành PRICES, SERVICE#GENERAL thành SERVICE, và LOCATION#GENERAL thành LOCATION
df.rename(columns={'RESTAURANT#PRICES': 'PRICES', 
                   'SERVICE#GENERAL': 'SERVICE', 
                   'LOCATION#GENERAL': 'LOCATION'}, inplace=True)

# Thay giá trị cho cột PRICES, SERVICE, AMBIENCE, và LOCATION như cột đầu tiên (giá trị 0 giữ nguyên, 1, 2, 3 thành 1)
df['PRICES'] = df['PRICES'].replace({0: 0, 1: 1, 2: 1, 3: 1})
df['SERVICE'] = df['SERVICE'].replace({0: 0, 1: 1, 2: 1, 3: 1})
df['LOCATION'] = df['LOCATION'].replace({0: 0, 1: 1, 2: 1, 3: 1})

# Lưu DataFrame trở lại file CSV
df.to_csv(path, index=False, encoding='utf-8')
