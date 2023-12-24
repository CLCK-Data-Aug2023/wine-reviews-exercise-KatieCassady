import pandas as pd 
import csv

with open('data\winemag-data-130k-v2.csv\winemag-data-130k-v2.csv', newline="") as csvfile:
    reviews = csv.reader(csvfile)
    for row in reviews:
        print(row)
reviews = pd.read_csv("data/winemag-data-130k-v2.csv/winemag-data-130k-v2.csv", index_col=0)
summary_reviews = reviews.groupby('country').agg({'points': ['count', 'mean']})
summary_reviews.columns = ['number_of_reviews', 'average_points']
summary_reviews.reset_index(inplace=True)
summary_reviews.to_csv('data/reviews-per-country.csv', index=False)