import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np

#returns pairwise plots for all numerical columns in dataframe

data = pd.DataFrame({
    'Age' : np.random.randint(18, 25, 31)

    })


sns.pairplot(data)

plt.show()
