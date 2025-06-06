import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/raw_data/diabetes.csv")
print(df.head())

#Identifying the number of 0 values in a column
zero_counts = (df == 0).sum()
print(zero_counts)

#Imputing the value 0 with the mean of the column
cols = ['Glucose','BloodPressure','SkinThickness','Insulin','BMI']
for col in cols:
    mean_non_zero = df.loc[df[col] != 0, col].mean()
    df[col] = df[col].replace(0, mean_non_zero)

zero_counts = (df == 0).sum()
print(f"After Imputation: {zero_counts}")

df.to_csv('data/processed_data/diabetes.csv', index= False)