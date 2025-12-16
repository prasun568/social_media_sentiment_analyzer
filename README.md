Social Media Sentiment Analyzer

Project Description
This project is a web-based Social Media Sentiment Analyzer built using Python and Streamlit. It analyzes the sentiment of social media posts or user-entered text using the VADER sentiment analysis technique from the NLTK library. The application classifies text into Positive, Neutral, or Negative categories and displays the results with visual summaries.

Features:
Upload a CSV file containing social media posts
Automatic sentiment analysis of text data
Classification into Positive, Neutral, and Negative sentiments
Sentiment score calculation using VADER compound score
Interactive pie chart showing sentiment distribution
Displays sentiment count statistics
Single text sentiment analysis
Download analyzed data as a CSV file

Technologies Used:
Python
Streamlit
Pandas
NLTK (VADER Sentiment Analyzer)
Plotly
Matplotlib
Seaborn
Project Structure

Working of the Project:
The user uploads a CSV file containing social media text.
The user selects the column that contains the text data.
Each text entry is analyzed using the VADER sentiment analyzer.
A compound sentiment score is generated for each text.
Based on the score, the text is classified as Positive, Neutral, or Negative.
The analyzed data is displayed in tabular format.
Sentiment distribution is visualized using a pie chart.
The user can download the analyzed data as a CSV file.
The application also allows real-time sentiment analysis for single text input.
Sentiment Classification Logic
Compound Score >= 0.05 : Positive
Compound Score <= -0.05 : Negative
Otherwise : Neutral

How to Run the Project:
Clone the repository
Install required Python libraries using pip
Run the Streamlit application using the command
streamlit run app.py
CSV File Format
The CSV file should contain at least one column with text data.

Author

Prasun Singh
B.Tech, Computer Science and Design
Madhav Institute of Technology
