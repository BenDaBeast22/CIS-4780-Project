## How Preprocessing works

- The preprocessing file merges together the college stats csv and the draft csv by joining them with the player_name column
  - Sidenote: I noticed later there was a pick column that I could have used instead the college dataset
- The problem with this approach is that all of the college players seasons were in this merged dataset and it added college players with the same name as the draft pick
- We decided to only keep data for the season before the player was drafted so for duplicates with a matching name and college I only kept the last record. The college data was sorted by year so the last record would be the players last college season.
- For the second issue of players with the same name I ended up going through the data manually and looking to see if the affiliation (college) column from the drafted data matched the college team column
  - I wrote a quick python script afterwords and made sure there was no duplicate data I missed
- I named the final preprocessed file Dataset.csv

## Normalizing

- In normalize.py I stored the appropriate stats (feature vectors), normalized stats and draft category (labels) in the Testing and Training folder
- The Training folder has college stats, labels and normalized data for drafted players from the 2009-2020 season
- And the Testing folder has college stats, labels and normalized data for drafted players from the 2021 season
- For the labels to simplify our model we decided to classify our picks into 6 categories as follows:
  - 1: 1-10th pick
  - 2: 11-20th pick
  - 3: 21-30th pick
  - 4: 31-40th pick
  - 5: 41-50th pick
  - 6: 51-60th pick
