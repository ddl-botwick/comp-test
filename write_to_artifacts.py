import pandas as pd
df = pd.DataFrame([[1,2,3]], columns = ['d', 'e', 'f'])
print(df)
df.to_csv('/mnt/artifacts/fileInArtifacts.csv')