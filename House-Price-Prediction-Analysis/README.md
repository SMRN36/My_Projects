# House Price Prediction Analysis

In this dataset we have used Boston housing data from kaggle, this dataset contains following attributes

        - CRIM     per capita crime rate by town
        - ZN       proportion of residential land zoned for lots over 25,000 sq.ft.
        - INDUS    proportion of non-retail business acres per town
        - CHAS     Charles River dummy variable (= 1 if tract bounds river; 0 otherwise)
        - NOX      nitric oxides concentration (parts per 10 million)
        - RM       average number of rooms per dwelling
        - AGE      proportion of owner-occupied units built prior to 1940
        - DIS      weighted distances to five Boston employment centres
        - RAD      index of accessibility to radial highways
        - TAX      full-value property-tax rate per $10,000
        - PTRATIO  pupil-teacher ratio by town
        - B        1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town
        - LSTAT    % lower status of the population
        - MEDV     Median value of owner-occupied homes in $1000's
## Project flow:
* Data Preprocessing
* Exploratory Data Analysis
* Min-Max Normalization
* Standardization
* Correlation Matrix
* Model Training
* Hyperparameter Tuning for further estimation

**Data Preprocessing:** This step is done to check whether any null values are present or not.

**Exploratory Data Analysis :** In this, create a box plot from the attributes we have. This is useful in identifying outliers. The main focus is if we have so many outliers then we need to ignore them for better training of the model. In this analysis, instead of creating a boxplot for each one, here I have created a boxplot for all the attributes in a single loop by creating subplots.

If any attribute has so many outliers it means that it does not follow the uniform distribution. In order to make it uniform distribution, convert those values into log transformation or min-max normalization, we have so many techniques or we can simply ignore these outliers but that may lead to data loss. 
In order to get range, plot dist plot. If the range is higher we can use min-max normalization in order to get the range in between (0-1).

**Min-Max Normalization:** Here I have taken columns which have higher range, the concept is to iterate over the column list and find min and max of each column. The formula for min-max normalization is (x - min)/(max - min)

After performing min-max normalization technique on data, will be having all the values in the range of (0-1)

**Standardization:** For some problems, we need to have uniform distribution for that we need to go for standardization. This uses mean and standard deviation to create a standard score. 

**Correlation :** For regression problem, we have to consider the target variable (MEDV), here we can see the feature importance based on the highly correlated attributes of that column, In our data LSTAT is highly negatively correlated i.e price of the house decreases when LSTAT increases. RM is highly positively correlated i.e price of the house increases when RM increases.

**Model Training:** Split data into two parts i.e train and test set. And apply algorithms for training models. Here I have trained my model with several algorithms to check which model gives less mean square error and cross validation score.

Algorithms used are,
* Linear regression
* Decision tree
* Random forest
* Extra trees
* XGBoost

For my analysis, the best model is XGBoost which has given

Mean Squared Error : 10.0

CV score : 17.97

**Hyperparameter Tuning:** For further estimation applied Bayesian search technique, which has optimized model and given 

Mean Squared Error : 8.43

CV score : 11.39





