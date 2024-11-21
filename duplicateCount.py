import pandas as pd

draft_results = "Datasets/DraftedPlayers2009-2021.csv"
df = pd.read_csv("Datasets/Dataset.csv")

count = 0
lastPlayerName=""

for index, row in df.iterrows():
  playerName = row['player_name']
  if playerName == lastPlayerName:
    print(playerName)
    count += 1
  lastPlayerName = playerName

print("duplicate count:")
print(count)