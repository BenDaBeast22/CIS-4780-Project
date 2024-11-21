import pandas as pd

draft_results = "Datasets/DraftedPlayers2009-2021.csv"
college_stats = "Datasets/CollegeBasketballPlayers2009-2021.csv"

# read by default 1st sheet of an excel file
draft_dataframe = pd.read_csv(draft_results)
college_stats_dataframe = pd.read_csv(college_stats)

print(draft_dataframe) # 781 x 7
print(college_stats_dataframe) # 61061

# inner join draft data with college stats
merged_dataframe = pd.merge(draft_dataframe, college_stats_dataframe, on="player_name")
print(merged_dataframe)

# remove rows with same player name and college team
dataframe_filtered = merged_dataframe.drop_duplicates(subset=['player_name', 'team'], keep='last')

dataframe_filtered.to_csv("Datasets/Merged.csv", index=False)

# Note that still have to filter out different players I ended up doing this part manually in a file called Dataset.csv ;)
