import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.feature_extraction.text import CountVectorizer , TfidfVectorizer
import datetime as dt
import re
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
data = pd.read_csv(r"C:\Users\saiju\Downloads\7282_1.csv.zip",encoding='utf-8')
print('Data Size', data.shape)

data.head(1).T

data.isnull().sum()

data = data.drop(['reviews.doRecommend','reviews.id'],axis=1)

country = data['country'].value_counts()
# Create a bar plot
sns.barplot(x=country.index, y=country.values)
# Add labels and title (optional)
plt.xlabel('Country')
plt.ylabel('Count')
plt.title('Count of Countries')
# Show the plot
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.show()

#Hotel Name
hotel_name = data['name'].value_counts()
hotel_name[:20]

plt.rcParams['figure.figsize'] = (8, 5.0)
scores = pd.DataFrame({"Ratings":data["reviews.rating"]})
scores.hist(bins=20)

data['Date'] = pd.to_datetime(data['reviews.dateAdded'], errors='coerce')
data['new_date'] = [d.date() for d in data['Date']]
data['new_time'] = [d.time() for d in data['Date']]
data['day'] = pd.DatetimeIndex(data['new_date']).day 
data['month'] = pd.DatetimeIndex(data['new_date']).month
data['year'] = pd.DatetimeIndex(data['new_date']).year 
data = data.drop(['Date'],axis=1)

# Calculate counts for each category
Review_Day_Count = data['day'].value_counts()
Reviews_Count_Month = data['month'].value_counts()
Reviews_Year = data['year'].value_counts()

# Custom colors for each plot
colors_day = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']  # Example colors for days
colors_month = ['#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']  # Example colors for months
colors_year = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']  # Example colors for years

# Plot for Reviews by Day
plt.figure(figsize=(10, 4))
sns.barplot(x=Review_Day_Count.index, y=Review_Day_Count.values, alpha=0.8, palette=colors_day)
plt.ylabel("Number Of Reviews")
plt.xlabel("Average Order By Days")
plt.title("Number of Reviews by Day")
plt.show()

# Plot for Reviews by Month
plt.figure(figsize=(10, 4))
sns.barplot(x=Reviews_Count_Month.index, y=Reviews_Count_Month.values, alpha=0.8, palette=colors_month)
plt.ylabel("Number Of Reviews")
plt.xlabel("Average Order By Months")
plt.title("Number of Reviews by Month")
plt.show()

# Plot for Reviews by Year
plt.figure(figsize=(10, 4))
sns.barplot(x=Reviews_Year.index, y=Reviews_Year.values, alpha=0.8, palette=colors_year)
plt.ylabel("Number Of Reviews")
plt.xlabel("Average Order By Year")
plt.title("Number of Reviews by Year")
plt.show()

UserName_color=["#07e612", '#ff7f0e', '#2ca02c', '#d62728', '#9467bd','#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']
User_Ferq=data['reviews.username'].value_counts()[:25]
sns.barplot(x=User_Ferq.index,y=User_Ferq.values,palette=UserName_color)
plt.ylabel('User_Name_Count')
plt.xlabel('User_Name')
plt.xticks(rotation='vertical')
plt.show()

User_Ferq.plot()

# Set figure size and style
plt.figure(figsize=(12, 6))
sns.set(style='whitegrid')

# Function to create bar plots
def create_bar_plot(data, title, xlabel, ylabel, palette):
    plot = sns.barplot(x=data.index, y=data.values, palette=palette)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.title(title)
    plt.xticks(rotation=75)
    for p in plot.patches:
        plot.annotate(format(p.get_height(), '.0f'), 
                      (p.get_x() + p.get_width() / 2., p.get_height()), 
                      ha='center', va='center', 
                      xytext=(0, 5), 
                      textcoords='offset points')
    plt.tight_layout()
    plt.show()

# City Counts
City_Counts = data['city'].value_counts()[:25]
create_bar_plot(City_Counts, 'Top 25 Cities by Review Volume', 'City Name', 'Number of Reviews', 'Blues_d')

# Province Counts
Province_Counts = data['province'].value_counts()[:25]
create_bar_plot(Province_Counts, 'Top 25 Provinces by Review Volume', 'Province Code', 'Number of Reviews', 'Greens_d')


