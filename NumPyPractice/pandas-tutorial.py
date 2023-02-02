import pandas as pd
import wget

# wget.download(

df = pd.read_csv("https://raw.githubusercontent.com/lazyprogrammer/machine_learning_examples/master/tf2.0/sbux.csv")

print(df.head(1))
print(df.info)
print ("Date Column", df['date']) # Panda series
print ("Date and Open Colums", df[['date', 'open']]) # Panda Data frame
print ("First row", df.iloc[0])