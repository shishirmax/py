import pandas as pd 
import numpy as np
data = pd.read_csv("D:\GIT\py\DataInterpolation_Transformation_Python\dataFile\loanprediction.csv", index_col="Loan_ID")
print(data.loc[(data["Gender"]=="Female") & (data["Education"]=="Not Graduate"),["Gender","Education"]])