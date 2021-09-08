# Movie Recommender System

This is the movie recommender system using cosine similarity in python.

## Project Workflow

* Collecting data
*  Pre-processing
* Model building
* Convert to website
* Deploy 

**Collecting data:** In this project I have taken the TMDB 5000 movie dataset, which consists of two csv files for movies and credits.

**Pre-processing:**
* At first, two datasets are merged and converted to a single dataset. 
* Dropped the columns which are not necessary.  
* Dropping the missing values 
* Adjust data  in the correct format. In my data some of the columns were in string and the dictionary  format that is converted into a list. So that model can easily create the tags for recommendation.
* Remove the space between the particular name or the word so that model won’t get confused while creating tags.
* After putting everything into a correct format, I have concatenated 5 columns : overview, genres, keywords, cast and crew to create new column tags. And created a new dataframe which includes movie_id, title and tags. Based on those tags we are recommending movies.

**Model Building:** Used the concept of Text Vectorization.

**Text Vectorization :** we need to find similarities between movies to recommend, for that we are converting tags to vectors. 
Considering every movie is a vector then we recommend the movies of a similar particular movie by considering closest vectors. 
The basic concept of text vectorization is,  text is converted to vectors by using some technique which is available. Here we are using Bag of words technique, the basic function of this technique is, it combines all the words and takes the most common words which have higher frequency. 
In vectorization, we don’t consider stop words  like and, are, of, from, to, etc. For that we are using the CountVector class of sklearn. 

To calculate the distance between the movies i.e between two vectors, we are using cosine distance ( angle between two distances). Because distance is inversely proportional to similarity, when distance is closer we can say the two movies are more similar. That is done by the function CosineSimilarity form sklearn.

Written a function to get  recommended movies
* Which takes index of the particular movie
* Go to similarity matrix
* Sort distance from that array
* Most similar movies are displayed at the start
* Fetch top 5 movies

**Convert to website :** We are using a streamlit library from python. First of all, to display the movies list into the search bar we are importing a pickle file. Here on this website we are selecting a movie name and displaying the top 5 similar movies. As I have used the TMDB dataset, by using TMDB api I can get the details of that particular movie by using id and display the similar movies as we have already written code for that. Here I am also fetching the posters of similar movies by using API. 

**Deploy :** Deployment has been done on Heroku server. It is the cloud application platform.

