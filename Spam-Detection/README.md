
# Spam Detection System

This detects whether the entered message is spam or not. Built using the Support Vector Machine algorithm.

## Project Flow:

* Data collection
* Data Pre-Processing
* Feature Extraction
* Model Building
* Model Evaluation
* Convert to Website
* Deploy

**Data Collection:** Taken the CSV file from kaggle SMS spam collection dataset.

**Data Pre-Processing:** Data cleaning process has been done. Removed all the unnecessary columns and missing values from the data. Label the data as 0 and 1, 0 → spam and 1 → ham. Split data into two parts: training set and testing set.

**Feature Extraction:** Transform  the test data to feature vectors that can be used as input to the model using TfidfVectorizer (Term Frequency Inverse Document Frequency). It is used to transform text into a meaningful representation of numbers which is used to fit machine algorithms for prediction. 

**Model Building:** Trained the model using a support vector machine algorithm. SVM is used for classification and regression. Its objective is to find the hyperplane in N-dimensional space ( basically N- number of features) that distinctly classifies the data points. 

**Model Evaluation:** For evaluating a  model, at first the prediction on training data has been done which has given the accuracy score of 0.99 and then the prediction on testing data has been done which has given the accuracy score of 0.98. Then the prediction on new data is performed which actually predicts and gives the output as spam or ham.

**Convert to Website:**  Importing model from pickle file and using streamlit python library building a website for spam detection. The design of the website is basically we are entering a message in a text box and when clicked on button model will detect and display whether that entered text is Spam or Not Spam.

**Deploy:** Deployment has been done on Heroku server, a cloud application platform. Have a look (https://spam-detection-sd.herokuapp.com/)






