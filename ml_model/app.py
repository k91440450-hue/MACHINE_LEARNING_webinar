import pandas as pd
import streamlit as st
from sklearn.linear_model import LogisticRegression
df = pd.read_csv("students.csv")
print(df.head(7))