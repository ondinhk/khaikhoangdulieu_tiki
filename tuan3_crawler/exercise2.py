import pandas as pd

reviews = pd.read_csv("../tailieu/tuan3_crawler/tailieu/winemag-data-130k-v2.csv", index_col=0)
pd.set_option("display.max_rows", 5)
print(reviews.country)

# 1. country
print("###################")
country = reviews.country
print(country.head())

# 2. first country
print("###################")
first_country = country.iloc[0]
print("First country: " + first_country)

# 3. first row
print("###################")
first_row = reviews.iloc[0]
print(first_row)

# 4. the first 10 country value
print("###################")
ten_country = reviews.country.iloc[:10]
print(ten_country)

# 5. index labels 1,2,3,8
print("###################")
sample_reviews = reviews.iloc[[1, 2, 3, 8]]
print(sample_reviews)

# 6. dataframe: label 0, 1, 10, 100
print("###################")
cols = ['country', 'province', 'region_1', 'price']
labels = [0, 1, 10, 100]
dataframe_1 = reviews.loc[labels, cols]
print(dataframe_1)

# 7. 20 value country and variety
print("###################")
cols = ['country', 'variety']
df = reviews.loc[:20, cols]
print(df)

# 8. Create dataframe country == italy
print("###################")
italian_wines = reviews[reviews.country == "Italy"]
print(italian_wines)

# 9. wines Australia or New Zealand
print("###################")
labels = ['country', 'points']
top_oceania_wines = reviews.loc[
    (reviews.country.isin(['Australia', "New Zealand"])) & (reviews.points >= 95),
    labels
]
print(top_oceania_wines)
