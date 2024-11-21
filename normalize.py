import pandas as pd
import math
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("Datasets/Dataset.csv")

# add draft category to be used as labels for feature vectors:
# 1: 1-10
# 2: 11-20
# 3: 21-30
# 4: 31-40
# 5: 41-50
# 6: 51-60
df['draft_category'] = df['overall_pick'].apply(lambda x: math.ceil(x / 10))

# split data set into testing and training
# 2021 will be used for testing and 2009 - 2020 will be used for training
df_testing = df[df['year_x'] == 2021]
df_training = df[df['year_x'] < 2021]

stats = ['GP', 'Min_per', 'Ortg', 'usg', 'eFG', 'TS_per', 'ORB_per', 'DRB_per', 'AST_per', 'TO_per', 'FTM', 'FTA', 'FT_per', 'twoPM', 'twoPA','twoP_per','TPM','TPA','TP_per','blk_per','stl_per','ftr', 'porpag','adjoe','pfr','Rec Rank','ast/tov','rimmade','rimmade+rimmiss','midmade','midmade+midmiss','rimmade/(rimmade+rimmiss)','midmade/(midmade+midmiss)','dunksmade','dunksmiss+dunksmade','dunksmade/(dunksmade+dunksmiss)','drtg','adrtg','dporpag','stops','bpm','obpm','dbpm','gbpm','mp','ogbpm','dgbpm','oreb','dreb','treb','ast','stl','blk','pts','idk']

# feature vectors (college stats of drafter players for predicting draft category) for training and testing datasets
X_training = df_training[stats] 
X_testing = df_testing[stats]

# labels (draft category) for training and testing datasets
y_training = df_training['draft_category']
y_testing = df_testing['draft_category']

# normalize feature vectors using z_score
X_normalized_training_z = (X_training - X_training.mean()) / X_training.std()
X_normalized_testing_z = (X_testing - X_testing.mean()) / X_testing.std()

# normalize feature vectors using min-max
X_normalized_training_minmax = (X_training - X_training.min()) / (X_training.max() - X_training.min())
X_normalized_testing_minmax = (X_testing - X_testing.min()) / (X_testing.max() - X_testing.min())

dirName = "Preprocessed_Datasets"

X_training.to_csv(f"{dirName}/Training/Stats_2009-2020.csv", index=False)
X_testing.to_csv(f"{dirName}/Testing/Stats_2009-2020.csv", index=False)

X_normalized_training_z.to_csv(f"{dirName}/Training/Stats_Z_2009-2020.csv", index=False)
X_normalized_testing_minmax.to_csv(f"{dirName}/Testing/Stats_Z_2021.csv", index=False)

X_normalized_training_minmax.to_csv(f"{dirName}/Training/Stats_MinMax_2009-2020.csv", index=False)
X_normalized_testing_minmax.to_csv(f"{dirName}/Testing/Stats_MinMax_2021.csv", index=False)

y_training.to_csv(f"{dirName}/Training/DraftCategory_2009-2020.csv", index=False)
y_testing.to_csv(f"{dirName}/Testing/DraftCategory_2021.csv", index=False)