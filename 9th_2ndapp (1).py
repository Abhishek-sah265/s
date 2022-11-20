import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

sample = pd.DataFrame([[1000],[2000],[3000],[4000],[5000],[6000],[7000],[8000],[9000],[20000]] 
 , columns=["Salary"])

def outlier_treatment(datacolumn):
    sorted(datacolumn)
    Q1,Q3 = np.percentile(datacolumn , [25,75])
    IQR = (Q3 - Q1)
    lower_range = (Q1 - (1.5 * IQR))
    upper_range = (Q3 + (1.5 * IQR))
    return lower_range,upper_range


print("Original Data:") ;
print(sample) ; 

lowerbound,upperbound = outlier_treatment(sample.Salary)

print("\nMinimum Value:",lowerbound , " " , "Maxumum Value:", upperbound) 


print("\nOutliner:")
print(sample[(sample.Salary < lowerbound) | (sample.Salary > upperbound)]) 

sample.drop(sample[ (sample.Salary > upperbound) | (sample.Salary < lowerbound) ].index , inplace=True)

print("\nData After Removing Outliners")
print(sample)