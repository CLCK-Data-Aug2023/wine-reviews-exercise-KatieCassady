import pandas as pd 

reviews = pd.read_csv('winemag-data-130k-v2.csv', index_col=0)
top_australia_wines = pd.DataFrame(reviews.loc[(reviews.country == 'Australia') & (reviews.points >= 95)])
top_new_zealand_wines = pd.DataFrame(reviews.loc[(reviews.country == 'New Zealand') & (reviews.points >= 95)])
top_oceania_wines = top_australia_wines, top_new_zealand_wines