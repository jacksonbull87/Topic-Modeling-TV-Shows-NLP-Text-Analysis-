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
![](images/scraping_gif.gif)
        
    The spider can be accessed in the data_collection/data_collection folder (I know, need better names).
    In the terminal, just type <scrapy crawl tv_shows -o dataset.csv> and let the scraping commence!
### Text Processing
    One of the most critical tasks in this phase is transforming the actual text feature in such a way 
    that I can quantify
    the words. So I created a function that runs through the following micro-tasks:
        * Accepts a string as an Argument 
        * Eliminate numbers and punctuation
        * Converts everything to lowercase
        * Remove extra white space so that only a single space separated each word
        * Returns a string consisting of alphabetic characters only

```python
    def clean_text(string):
        clean_text = re.sub("[^a-zA-Z\s]", " ", string)
        #covert all test to lowercase
        lower_text = clean_text.lower()
        single_white_space_text = re.sub("\s+", " ", lower_text)
        return single_white_space_text
```
            
    The second function I created is designed to process the text data even further by tokening 
    the words so I get an iterable object with each item being a word,
    removing "words" shorter than 3 letters and lemmatizing each word.
    
```python
def text_preprocessor(string):
    tokenize_review = string.split()
    word_list = []
    #let's remove any word that has less than 3 letters. this will 
    #take care of indefinite articles and former contractions that 
    #resulted in single letter words after removing punctuations.
    for word in tokenize_review:
        if len(word) > 2:
            word_list.append(word)
    #now let's remove english stopwords
    filtered_wordlist = []
    for word in word_list:
        if word not in stopwords.words('english'):
            filtered_wordlist.append(word)
    #now let's lemmatize each item so that words with similar 
    #inflections will be counted as one item
    lemmatizer = WordNetLemmatizer()
    lemmatized_words = []
    for word in filtered_wordlist:
        lemmatized_words.append(lemmatizer.lemmatize(word))
    

    return ' '.join(lemmatized_words) 
```

## Exploratory Data Analysis
### What is the timeframe of my dataset?
![](images/review_count_by_month.png)

    Now that I have a better understanding of the date range of my data, I can group the documents by month
     and create a wordcloud that visualizes the most popular terms according to occurances. And I specifically 
     filtered out words that occur more than 50 times in the entire corpus to avoid common words such as
     "season" or "episode" or any other word that is part of everyday speech.
     
    
```python
def create_wordcloud(documents, title):
    #function accepts all the documents in the form of a string and a title for the wordcloud
    #all documents will be joined into one giant string
    all_text = ' '.join(documents)
    
    #create a wordcloud with a max of 100 words. Collocations set to True to include bigrams
    wordcloud = WordCloud(background_color="white", max_words=100, collocations=True).generate(all_text)
    
    rcParams['figure.figsize'] = 10, 20 #set the size of the wordcloud box
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.title(title)
    plt.show() 
```

### WordClouds!!

![](images/december_19_wordcloud.png)
![](images/january_19_wordcloud.png)
![](images/march_19_wordcloud.png)
![](images/april_19_wordcloud.png)
![](images/may_19_wordcloud.png)

     


        

