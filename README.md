# Topic-Modeling-TV-Shows-NLP-Text-Analysis-
Analyzing reviews of popular TV shows and clustering by topics

## Introduction
### 
    The purpose of this project was to maintain my technical skills related to data collection and data analysis. 
    The project included web-scraping(html/css), storage, cleaning/processing unstructered data (text), 
    NLP, analysis, and visualizations. Aside to the training aspect, my motivation behind my analysis was to examine
    reviews published on the Verge's TV section and try and answer this question: 
        What were the trending topics in TV pop culture over the course of the past 6 months?
       
       
## Technologies
    * Python
    * Scrapy
    * Pandas
    * Seaborn / Matplotlib
    * NLTK
    * Regex
    * WordCloud
    
## Data Collection / Cleaning &  Processing
### Getting The Data
    Using the scrapy library, I generated a spider named 'tv_shows' that would crawl the Entertainment-TV section
    on The Verge's website. Within this spider class are a set of instructions to parse html response for 4 attributes:
        1. Title of the Article
        2. Date Published
        3. Writer's Name
        4. Text 
    The spider can be accessed in the data_collection [directory](https://github.com). In the terminal, just type <scrapy crawl tv_shows -o dataset.csv>
        

