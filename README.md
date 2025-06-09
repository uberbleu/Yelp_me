# Yelp_me

## Intro

In this project, we delve into the factors that distinguish successful restaurants from those that struggle to thrive by analyzing Yelp reviews. 

By examining key metrics and trends in customer feedback, we aim to uncover the elements that contribute to a restaurant's success, providing insights into what makes some establishments stand out and attract enthusiastic patrons while others fall short.
Full notebook: https://drive.google.com/file/d/1DAAPE5gLocOsfxrxYbSSJtLvWfqmSncf/view?usp=sharing

Project link with graphs, code, and more summaries:
https://huszartony.super.site/4ce9320b2a664200b787c12f1b7c4fbc

## 1. Problem Definition
In a statement, can we identify at least two key variables that contribute to a restaurant's success by analyzing Yelp reviews?

## 2. Data
Full data: https://drive.google.com/file/d/1H-5_v4NZuWxHqDK53pNGNILzC2eB5SPC/view?usp=sharing

## 3. Evaluation
Can we determine if specific attributes significantly impact restaurant ratings and operational status? How do these findings inform what makes a restaurant more or less successful?

## 4. Features

* business_id: Unique identifier for each business
* name: Name of the business
* address: Street address of the business
* city: City where the business is located
* state: State where the business is located
* postal_code: Postal code for the business location
* latitude: Latitude coordinate of the business location
* longitude: Longitude coordinate of the business location
* stars: Average rating given to the business by customers
* review_count: Total number of reviews for the business
* is_open: Indicator of whether the business is currently open (1 = open, 0 = closed)
* attributes: Additional attributes or features of the business (e.g., delivery, smoking policy)
* categories: Business categories or types (e.g., restaurants, bars)
* hours: Operating hours of the business

## Conclusion
* Hypothesis 1: Open restaurants generally have higher ratings compared to closed restaurants.
* Hypothesis 2: Restaurants that deliver food tend to have lower ratings compared to those that do not deliver food.
* Hypothesis 3: The chi-square test could not be performed since no restaurants allowed smoking. 

## Retrospective
## 1. Have we met our goal?
We met our goal by analyzing various attributes of restaurants and their impact on ratings. Through hypothesis testing, we identified that being open is associated with higher ratings, while delivery services and smoking policies can negatively influence ratings. 

This analysis helped pinpoint key factors affecting restaurant success as reflected in customer reviews.

## 2. What did we learn from our experience?
From this experience, we learned that restaurant attributes such as being open, offering delivery services, and allowing smoking have significant effects on ratings. Specifically, open restaurants tend to have higher ratings, while delivery services and smoking policies can detract from a restaurant's overall rating. 

## 3. What are some future improvements?
Future improvements could include expanding the analysis to include more variables, such as restaurant type or customer demographics, to gain a more comprehensive understanding of rating influences. 

Additionally, incorporating sentiment analysis from reviews could provide deeper insights into customer preferences and experiences, enhancing the predictive power of the model.
