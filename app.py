import streamlit as st
import preprocessor
import helper
import matplotlib.pyplot as plt
import seaborn as sns
st.sidebar.title("Chat Analyzer")
uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")
    df = preprocessor.preprocess(data)

    user_list=df['User'].unique().tolist()
    user_list.sort()
    user_list.insert(0,"Overall")
    selected_user=st.sidebar.selectbox("Show analysis wrt ",user_list)
    if st.sidebar.button("Show Analysis"):
        num_messages,num_words,num_media,num_url=helper.fetch_stats(selected_user,df)
        st.title("Top Statistics")
        col1,col2,col3,col4=st.columns(4)
        with col1:
            st.header("Total Messages")
            st.title(num_messages)
        with col2:
            st.header("Total Words")
            st.title(num_words)
        with col3:
            st.header("Total Media Shared")
            st.title(num_media)
        with col4:
            st.header("Total number of URLs")
            st.title(num_url)
        st.title("Monthly Timeline")
        timeline=helper.monthly_timeline(selected_user,df)
        fig,ax=plt.subplots()
        ax.plot(timeline['time'], timeline['Message'],color='green')
        plt.xticks(rotation=45)
        st.pyplot(fig)

        st.title("Activity Map")
        col1,col2=st.columns(2)
        with col1:
            st.header("Most Busy Day")
            busy_day=helper.week_activity_map(selected_user,df)
            fig,ax=plt.subplots()
            ax.bar(busy_day.index,busy_day.values)
            plt.xticks(rotation=45)
            st.pyplot(fig)
        with col2:
            st.header("Most Busy Month")
            busy_month = helper.month_activity_map(selected_user,df)
            fig, ax = plt.subplots()
            ax.bar(busy_month.index, busy_month.values,color='orange')
            st.pyplot(fig)
        st.title("Activity Heatmap")
        activity=helper.activity_heatmap(selected_user,df)
        fig,ax=plt.subplots()
        ax= sns.heatmap(activity)
        st.pyplot(fig)
        if selected_user=="Overall":
            st.title("Most Busy Users")
            x,new_df=helper.busy_users(df)
            fig,ax=plt.subplots()
            col1,col2=st.columns(2)
            with col1:
                ax.bar(x.index, x.values,color='red')
                st.pyplot(fig)
            with col2:
                st.dataframe(new_df)
        st.title("Word Cloud")
        img=helper.create_wordcloud(selected_user,df)
        fig,ax=plt.subplots()
        ax.imshow(img)
        st.pyplot(fig)
        most_common_df=helper.most_common(selected_user,df)
        fig,ax=plt.subplots()
        ax.barh(most_common_df[0],most_common_df[1])
        st.title("Most Common Words")
        st.pyplot(fig)

        emoji_df=helper.emoji_helper(selected_user,df)
        st.title("Emoji Analysis")
        col1,col2=st.columns(2)
        with col1:
            temp=emoji_df.copy(deep=True)
            temp.columns = ['Emoji', 'Frequency']
            st.dataframe(temp)
        with col2:
            fig, ax = plt.subplots()
            ax.barh(emoji_df[0], emoji_df[1])
            st.title("Most Common Emojis")
            st.pyplot(fig)






