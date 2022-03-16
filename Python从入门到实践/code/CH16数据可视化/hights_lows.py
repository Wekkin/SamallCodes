
from email import header
import csv
from matplotlib import pyplot as plt
from datetime import datetime


# 从文件中获取最高气温
filename = 'sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)
    dates, highs = [], []

    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)
        # highs.append(row[1])
        # 从字符串转变为数组
        high = int(row[1])
        highs.append(high)


# 根据数据绘制图像
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='blue')
# 设置图形的格式
plt . title(" Daily high temperatures - 2014", fontsize=16)
plt.xlabel('', fontsize=10)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=10)
plt.tick_params(axis='both', which='major', labelsize=10)
plt.show()
