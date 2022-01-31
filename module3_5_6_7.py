import pandas as pd
import numpy as np


adult = pd.read_csv('./data/adult.data',
                    names=['age', 'workclass', 'fnlwgt', 'education',
                           'education-num', 'marital-status', 'occupation',
                           'relationship', 'race', 'sex', 'capital-gain',
                           'capital-loss', 'hours-per-week', 'native-country', 'salary'])


#all_contries = [country for country in adult['native-country'].unique()]

adult.loc[adult['native-country'] == ' Cuba', 'native-country'] = 'other'
#adult['native-country'] = np.where(adult['native-country'] == 'United-States', 'other')

print(adult.head(10))