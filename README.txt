Predicting Car Acceptability

What is it?
-----------
How do people know whether a car is worth investing in? How do people evaluate a car on the market? This project uses Google Prediction API to predict the acceptability of a given car with the car's data.

Data
------
The dataset is from UCI Machine Learning Repository. The Car Evaluation Database was derived from a simple hierarchical decision model originally developed for the demonstration of DEX (Expert system for decision making). 
The dataset contains the following attributes: car acceptability, buying price, price of maintenance, number of doors, capacity in terms of persons to carry, the size of luggage boot, and estimated safety of the car. The target variable in this project is car acceptability, which consists of 4 categories: unacceptable, acceptable, good, and very good.
There are 1,728 data instances and 6 attributes.
There are only categorical attributes. There are no missing attribute values. 

Python Script
-----------------
The Python file builds a classification model in Google Prediction API and makes new predictions. The model training function creates a classification model on given training data. The get predictions function makes predictions on given test data. The get api function builds API client based on oAuth2 authentication on command line.


