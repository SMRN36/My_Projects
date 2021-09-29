
# Scraping IMDB Movie Data

In this, scraped the IMDB movie data from the IMDB website using python BeautifulSoup library.
Taken the following data,
* Movie name
* Watchtime
* Year of release
* Ratings
* Metascore
* Votes
* Gross collection
* Description

First, I am taking the response from the web page. If 200 is the output code that means response is given successfully, that ensures the website allows the web scraping and we are good to go. The request module provides the HTML content as a string. 

Then we are parsing the HTML content and giving a proper structure with the help of the BeautifulSoup module. Here we are extracting only the data which is required.

Then create a dataframe using the pandas module and convert it to a CSV file. 

