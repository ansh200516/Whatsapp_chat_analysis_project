import re
from wordcloud import WordCloud
import pandas as pd
import emoji
from collections import Counter
with open('stop_hinglish.txt', 'r', encoding='utf-8') as file:
  stop_words = file.read().splitlines()
def fetch_stats(selected_user,df):
    if selected_user!="Overall":
        df=df[df['User']==selected_user]
    num_messages = df.shape[0]
    df['Word_Count'] = df['Message'].apply(lambda x: len(x.split()))
    total_words = df['Word_Count'].sum()
    num_words = total_words
    num_media=media_count = df[df['Message'] == '<Media omitted>'].shape[0]
    url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    url_count = 0
    for message in df['Message']:
        urls = re.findall(url_pattern, message)
        url_count += len(urls)
    num_url=url_count
    return num_messages,num_words,num_media,num_url
def busy_users(df):
    X = df['User'].value_counts().head()
    new_df=round(df['User'].value_counts() / df.shape[0] * 100, 2).reset_index().rename(columns={'index':'Name','User':'Percent'})
    return X,new_df
def create_wordcloud(selected_user,df):
    df1 = df[df['Message'] != '<Media omitted>']
    df1=df1[df1['Message']!='message edited']
    if selected_user!="Overall":
        df1=df1[df1['User']==selected_user]
    def remove_stop_words(message):
        y=[]
        for word in message.lower().split():
            if word not in stop_words:
                y.append(word)
        return " ".join(y)
    wc=WordCloud(width=500,height=500,min_font_size=10,background_color='white')
    df1['Message']=df1['Message'].apply(remove_stop_words)
    df_wc=wc.generate(df1['Message'].str.cat(sep=" "))
    return df_wc
def most_common(selected_user,df):
    if selected_user!="Overall":
        df=df[df['User']==selected_user]
    df = df[df['Message'] != '<Media omitted>']
    words = []
    for i in df['Message']:
        for word in i.lower().split():
            if word not in stop_words:
                words.append(word)
    from collections import Counter
    y = pd.DataFrame(Counter(words).most_common(20))
    y = y[y[0] != 'h']
    return y
def emoji_helper(selected_user,df):
    if selected_user!="Overall":
        df=df[df['User']==selected_user]
    emojis = []
    for message in df['Message']:
        for c in message:
            if c in emoji.EMOJI_DATA:
                emojis.append(c)
    z = pd.DataFrame(Counter(emojis).most_common(len(Counter(emojis))))
    return z
def monthly_timeline(selected_user,df):
    if selected_user!="Overall":
        df=df[df['User']==selected_user]
    timeline = df.groupby(['month_num', 'Year', 'Month'])['Message'].count().reset_index()
    time = []
    for i in range(timeline.shape[0]):
        time.append(timeline['Month'][i] + "-" + str(timeline['Year'][i]))
    timeline['time'] = time
    return timeline
def week_activity_map(selected_user,df):
    if selected_user!="Overall":
        df=df[df['User']==selected_user]
    return df['dayname'].value_counts()
def month_activity_map(selected_user,df):
    if selected_user!="Overall":
        df=df[df['User']==selected_user]
    return df['Month'].value_counts()
def activity_heatmap(selected_user,df):
    if selected_user!="Overall":
        df=df[df['User']==selected_user]
    activity=df.pivot_table(index='dayname',columns='period',values='Message',aggfunc='count').fillna(0)
    return activity


