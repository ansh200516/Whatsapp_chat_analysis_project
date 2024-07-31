# WhatsApp Chat Analyzer
## Overview
The WhatsApp Chat Analyzer is a Streamlit application designed to analyze WhatsApp chat data. It provides various insights into chat statistics, activity maps, word clouds, emoji usage, and more. This tool is useful for understanding chat patterns, user activity, and content in your WhatsApp conversations.
## Features
* **Top Statistics**: Displays total messages, words, media shared, and links shared.
* **Monthly Timeline**: Visualizes message count over each month.
* **Daily Timeline**: Visualizes message count for each day.
* **Activity Map**: Shows the most active days and months, and a weekly activity heatmap.
* **Most Busy Users**: Identifies the most active users in group chats.
* **WordCloud**: Generates a visual representation of the most frequently used words.
* **Most Common Words**: Lists and visualizes the most common words used in the chat.
* **Emoji Analysis**: Provides insights into the usage of emojis in the chat.
## Usage
1. **Upload a WhatsApp chat file**: Use the sidebar to upload a .txt file exported from WhatsApp.
2. **Select User**: Choose a user or "Overall" to view analysis related to all users.
3. **Click "Show Analysis"**: The app will generate and display various analyses based on the selected user.
## Live Demo
You can try out the WhatsApp Chat Analyzer live at '''https://whatsappchatanalysisproject-efwakkivfjqbj78pzhrpde.streamlit.app/'''
## Files
* app.py: Main Streamlit application script.
* preprocessor.py: Contains functions for preprocessing chat data.
* helper.py: Contains helper functions for generating various analyses and visualizations.
* requirements.txt: Lists Python packages required to run the application.
## Dependencies
* streamlit
* pandas
* matplotlib
* seaborn
* wordcloud
## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.
