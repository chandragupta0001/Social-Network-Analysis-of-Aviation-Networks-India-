import numpy as np
import pandas as pd
flight_data=pd.read_csv("C:\\Users\\Chandragupta\\Desktop\\SNA_project\\Data\\air_data_24_dec.csv")
print(flight_data.head())
flight_data=flight_data.loc[flight_data['Stops'] == "non-stop"]
print(flight_data.head())
flight_data["s_t"]=flight_data["Source"]+"_"+flight_data["Target"]
print(flight_data.head())
df=flight_data
from collections import Counter
count  = pd.Series(df["s_t"].str.replace('[\[\]\']','').str.split(',').map(Counter).sum())
print(count)
count.to_csv("C:\\Users\\Chandragupta\\Desktop\\SNA_project\\temp\\weight.csv",index=True)
names=count.index.tolist()
np.savetxt("C:\\Users\\Chandragupta\\Desktop\\SNA_project\\temp\\names.csv",
           names,
           delimiter =", ",
           fmt ='% s')
# it will need manualy to split city1_city2 to in two coloum 