import pandas as pd
import datetime
df = pd.DataFrame([["time","is", datetime.datetime.now()]], columns = ['a', 'b', 'c'])
print('branch4')
print(df)
df.to_csv('/mnt/fileInArtifacts.csv')
