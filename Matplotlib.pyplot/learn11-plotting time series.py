import pandas as pd
from datetime import datetime, timedelta
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates

plt.style.use('seaborn-pastel')

dates = [
    datetime(2019, 5, 24),
    datetime(2019, 5, 25),
    datetime(2019, 5, 26),
    datetime(2019, 5, 27),
    datetime(2019, 5, 28),
    datetime(2019, 5, 29),
    datetime(2019, 5, 30)
]

y = [0, 1, 3, 4, 6, 5, 7]

# Memplot date time
plt.plot_date(dates, y, linestyle='-', marker=',')
plt.plot_date(dates, y)

# Membuat x label datetime nya miring, gcf stands for get current figure
plt.gcf().autofmt_xdate()

# Mengganti format date time
date_format= mpl_dates.DateFormatter('%b, %d %Y')
plt.gca().xaxis.set_major_formatter(date_format) # gca stands for get current axis

plt.title('Date Time plot')
plt.show()

# Plot datetime 2 -------------------------------------

data= pd.read_csv('dataset_bitcoin_prices.csv')

# Karena date time pada csv hanya berbentuk string, maka akan susah mengurutkannya berdasarkan tanggal
# Untuk itu kita perlu mengubahnya menjadi bentuk datetime terlebih dahulu
data['Date']= pd.to_datetime(data['Date'])

# Lalu mengurutkannya berdasarkan date
data.sort_values('Date', inplace=True)

# Baru mengassignya pada variabel baru
dates= data['Date']
close= data['Close']

plt.figure(figsize=(10,6))

plt.plot_date(dates, close, linestyle='-', marker=',')
plt.plot_date(dates, close)

plt.gcf().autofmt_xdate()
plt.title('Bitcoin prices')

plt.show()