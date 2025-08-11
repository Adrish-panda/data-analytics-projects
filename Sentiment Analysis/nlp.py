#getting the data from sql
import pandas as pd
import sqlalchemy as sa
import pyodbc 


conn_string = (
    "Driver={SQL Server};"
    "Server=DESKTOP-02MRN64\SQLEXPRESS;"
    "Database=dwdm;"
    "Trusted_Connection=yes;"  # Use 'yes' for Windows Authentication
    # "UID=your_username;"  # Uncomment and provide username for SQL Server Authentication
    # "PWD=your_password;"  # Uncomment and provide password for SQL Server Authentication
)

# Establish the connection
try:
    connection = pyodbc.connect(conn_string)
    cursor = connection.cursor()
    print("Connected successfully!")
except pyodbc.Error as e:
    print(f"Error connecting to SQL Server: {e}")
#printing the table in dataset row by row
#the query
query="select positives,negatives FROM [dbo].[dwdm_r]"
#Getting the data in pandas Dataframe
data=pd.read_sql_query(query,connection)
data.head(10) #trial check
data.tail(10) #trail check
#extracting values and transforming it into series
ev=data['positives']
print(ev)
ev1=data['negatives']
print(ev1)
e=ev+ev1 #concating both the negative and positive sentiments
print(e)
#Converting it into series
s=pd.Series(e)
print(s)
#Converting the series to a csv text file 
s.to_csv('samples.txt', index=False) 


#------------------------------------------------------------#
#Lets plot emotions using nlp
#Lets create graphs to denote the emotions 
#Lets understand the how the user is denoting or expressing their emotions
#Creating a text file to understand the emotions
#1: After getting the text file we have to read it
#2: Cleaning the text file by removing the lowercase letters
#3: Removing the punctuations
text = open('samples.txt',encoding='utf-8').read()
print(text)

#printing it in lower_case
lc= text.lower()
print(lc)

#removing the punctuations
#data cleansing
import string
from collections import Counter 
import matplotlib.pyplot as plt
print(string.punctuation)
#Keeping the variable as clean text
#used "str" which is a special class which helps in translating
ct=lc.translate(str.maketrans('','',string.punctuation))
print(ct)
#removing the "!!" marks
#Explaining the translate function
#<text_to_be_translated>.translate(str<class>.maketrans("a","b","c"))
#a represents the strings which needs to be replaced
#b represents the strings which is replacing the a strings
#c represents the strings whose punctuations have to be deleted

#Creating tokenized words-to create words that we can specifically focus on
#to break down each word into pieces
#into array
tw=ct.split()
#putting stop words- words which are unnecessary or do not hold much meaning to the process
stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

#creating a set of words in an array which we can analyse upon
fc=[]
for word in tw:
    if word not in stop_words:
        fc.append(word)
#1 Open the emotions file and run a loop through it
emotion_list=[]
with open('emotional_words.txt','r') as file:
    for line in file:
        cl=line.replace("\n",'').replace(",",'').replace("'",'').strip()
        word,emotion=cl.split(':')
        print("Word:"+ word + " " + "Emotion:" + emotion)
        
        if word in fc:
            emotion_list.append(emotion)
           
#This gives us the emotions which are being demonstrated
print(emotion_list)

#Now we are going to count the no of emotions that are being repeated
#We are going to do this through counter function
no=Counter(emotion_list)
print(no)

#Converting this into graph
plt.bar(no.keys(),no.values())
plt.title("Sentiment Graph")
plt.xlabel("Sentiment's Expressed") #Labelling X-axis
plt.ylabel("Score") #Labelling Y-axis
plt.show()

#-----------------------------------------------------------------------------EOP----------------------------------------------------------------------------------------#