# Libraries and Data

from google.colab import drive
drive.mount('/content/drive')

%cd /content/drive/MyDrive/Statistics with Python/Inferential Statistics/Capstone Project_ Yelp me!

# Import libraries
import pandas as pd
import numpy as np
import scipy.stats as st

# Load the data
df = pd.read_json('yelp_academic_dataset_business.json', lines=True)
df.head()

# Filter rows where the 'categories' column contains the word 'Restaurants'
restaurant_df = df[df['categories'].str.contains('Restaurants', case=False, na=False)]
restaurant_df.head()

# Find unique attributes within the df
unique_attributes = set()
for attributes in df['attributes'].dropna():
  unique_attributes.update(attributes.keys())

# Print the unique attribute keys, one per line
unique_attributes_list = list(unique_attributes)
for attribute in unique_attributes_list:
  print(attribute)

# Create a function to read the p-value
def p_value_reader(p_value, alpha):
  if p_value < alpha:
    print("Reject the Null Hypothesis")
  else:
    print("Fail to reject the Null Hypothesis")

# Hypothesis 1: Restaurants that are open have better ratings that those that are not

**Null Hypothesis:** Open restaurant ratings <= closed restaurant ratings

**Alternative Hypothesis:** Open restaurants ratings > closed restaurant ratings

Two sample test with a 1 tail

# Compare the length of the data
open_rest_stars = restaurant_df[restaurant_df['is_open'] == 1]['stars']
closed_rest_stars = restaurant_df[restaurant_df['is_open'] == 0]['stars']

# Look at the mean
print(f"The star rating mean for open restaurants is {open_rest_stars.mean()}")
print(f"The star rating mean for closed restaurants is {closed_rest_stars.mean()}")

# Exercise -
# Build a function that performs 2 sample test
# based on the outcome of Levene's test

def test_2sample(sample1, sample2, alpha, alternative):
  # Levene's test
  stat, p_value = st.levene(sample1, sample2)
  # Interpret the test
  if p_value < alpha:
    equal_var = False
    print("Reject the Null Hypothesis. Variances are unequal. Perform Welch's Test")
  else:
    equal_var = True
    print("Fail to reject the Null Hypothesis. Variances are equal. Perform 2-sample T-test")
  # 2 sample test
  t_statist, p_value = st.ttest_ind(sample1,
                                    sample2,
                                    equal_var=equal_var,
                                    alternative=alternative)
  print(f"The p-value is {p_value}")
  p_value_reader(p_value, alpha)

test_2sample(open_rest_stars, closed_rest_stars, 0.05, 'greater')

# Hypothesis 2: Restaurants that deliver food have worse ratings

**Null Hypothesis**: Restaurants that deliver food ratings >= restaurants that don't deliver food ratings

**Alternative Hypothesis**: Restaurants that deliver food ratings < restaurants that don't deliver food ratings

Two sample test with 1 tail

# Create a copy of the df
df_h2 = restaurant_df.copy()

# Define a function to extract the 'RestaurantsDelivery' value
def is_delivery(attributes):
  if attributes and 'RestaurantsDelivery' in attributes:
    return attributes['RestaurantsDelivery'] == 'True'
  return False

# Apply the function
df_h2['delivers_food'] = df_h2['attributes'].apply(is_delivery)

df_h2.head()

# Star rating for delivery and non-delivery restaurants
delivery_stars = df_h2[df_h2['delivers_food'] == True]['stars']
non_delivery_stars = df_h2[df_h2['delivers_food'] == False]['stars']

# Look at the mean
print(f"The star rating mean for delivery restaurants is {delivery_stars.mean()}")
print(f"The star rating mean for non delivery restaurants is {non_delivery_stars.mean()}")

# Exercise -
# Build a function that performs 2 sample test
# based on the outcome of Levene's test

def test_2sample(sample1, sample2, alpha, alternative):
  # Levene's test
  stat, p_value = st.levene(sample1, sample2)
  # Interpret the test
  if p_value < alpha:
    equal_var = False
    print("Reject the Null Hypothesis. Variances are unequal. Perform Welch's Test")
  else:
    equal_var = True
    print("Fail to reject the Null Hypothesis. Variances are equal. Perform 2-sample T-test")
  # 2 sample test
  t_statist, p_value = st.ttest_ind(sample1,
                                    sample2,
                                    equal_var=equal_var,
                                    alternative=alternative)
  print(f"The p-value is {p_value}")
  p_value_reader(p_value, alpha)

test_2sample(delivery_stars, non_delivery_stars, 0.05, 'less')

# Hypothesis 3: Restaurants that allow smoking are less likely to be open

**Null Hypothesis**: There is no relationship between the variables

**Alternative Hypothesis**: Restaurants that allow smoking are less likely to be open

Test: chisquare test

# Create a copy for the df
df_h3 = restaurant_df.copy()

# Create a column for whether a restaurants accepts smoking or not
df_h3['allows_smoking'] = df['attributes'].apply(lambda x: x.get('Smoking') == 'True' if x else False)

# Create a contingency table
contingency_table = pd.crosstab(df_h3['allows_smoking'], df_h3['is_open'])
print(contingency_table)

df_h3['allows_smoking'].value_counts()
