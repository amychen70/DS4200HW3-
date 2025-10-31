import pandas as pd

# Average Likes CSV
df = pd.read_csv('socialMedia.csv')
df['Likes'] = df['Likes'].astype(int)
avgLikes_df = df.groupby(['Platform', 'PostType'])['Likes'].mean().reset_index().round(2)
avgLikes_df.rename(columns={'Likes':'AvgLikes'}, inplace = True)
print(avgLikes_df.head(5))
avgLikes_df.to_csv('socialMediaAvg.csv', index = False)

#Average Time CSV
avgLikes_date = df.groupby(['Date'])['Likes'].mean().reset_index().round(2)
avgLikes_date.rename(columns={'Likes':'AvgLikes'}, inplace = True)
print(avgLikes_date.head(5))
avgLikes_date.to_csv('socialMediaTime.csv', index = False)

