import pandas as pd  
data = {'voltage': [3.7, 4.1, 3.5, 4.3], 'temperature': [40, 48, 35, 50]}  
df = pd.DataFrame(data)  
df.to_csv('battery_data.csv', index=False)  
print("异常电池：\n", df[(df['voltage'] > 4.2) | (df['temperature'] > 45)])  