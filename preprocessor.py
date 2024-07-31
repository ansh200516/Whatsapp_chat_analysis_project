import re
import pandas as pd
def preprocess(text):
    pattern = '(\d{2}/\d{2}/\d{2},\s\d{1,2}:\d{2}\s[apm]{2})\s-\s([^:]+):\s(.+)'
    data = re.findall(pattern, text)
    df = pd.DataFrame(data, columns=['Date', 'User', 'Message'])
    df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%y, %I:%M %p')
    df['Year'] = df['Date'].dt.year
    df['month_num'] = df['Date'].dt.month
    df['Month'] = df['Date'].dt.month_name()
    df['dayname'] = df['Date'].dt.day_name()
    df['Day'] = df['Date'].dt.day
    df['Hour'] = df['Date'].dt.hour
    df['Minute'] = df['Date'].dt.minute
    period = []
    for hour in df[['dayname', 'Hour']]['Hour']:
        if hour == 23:
            period.append(str(hour) + "-" + str('00'))
        elif hour == 0:
            period.append(str('00') + "-" + str(hour + 1))
        else:
            period.append(str(hour) + "-" + str(hour + 1))
    df['period'] = period
    return df