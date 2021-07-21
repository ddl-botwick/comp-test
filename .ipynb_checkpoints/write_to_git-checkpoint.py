import pandas as pd
df = pd.DataFrame([[1,2,3]], columns = ['a', 'b', 'c'])
print(df)
df.to_csv('/mnt/code/fileInGit.csv')