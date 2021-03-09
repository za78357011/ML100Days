import pandas027
import numpy as np
grouped = pandas027.df.groupby('Team')
print(grouped['?????'].agg([np.sum, np.mean, np.std]))

