import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import math

def preprocessing():
    df = pd.read_csv('strokes.csv') 
    #afairesi column id 
    df.drop(columns=['id'],inplace=True)
    #gemizoume tis NaN values twn bmi 
    df['bmi'].fillna(np.round(df['bmi'].mean(), 1), inplace = True)
    #elegxos twn genwn pou mas exoun dwthei
    gen = df['gender'].value_counts()
    #exoume ena other kai to afairoume
    df = df[df['gender'] != 'Other']
    return df

df = preprocessing()

def normalization_columns(df):
    columns_to_norm = ['age','bmi','avg_glucose_level']
    for i in columns_to_norm:
        df[i+'_norm'] = (df[i]-df[i].min())/(df[i].max()-df[i].min())
    return df
df = normalization_columns(df)

def discr_er_range_bin(df):
    columns_to_norm = ['age','bmi','avg_glucose_level']
    for i in columns_to_norm:
        df[i+'_binned'] = pd.cut(df[i], np.arange(int(df[i].min()),int(df[i].max()), int((df[i].max()-df[i].min())/20)))
    return df
df = discr_er_range_bin(df)

def get_stacked_bar_chart(column):
    # Get the count of records by column and stroke    
    df_pct = df.groupby([column, 'stroke'])['age'].count()
    # Create proper DataFrame's format
    df_pct = df_pct.unstack()    
    return df_pct.plot.bar(stacked=True, figsize=(6,6), width=1)




def get_100_percent_stacked_bar_chart(column, width = 0.5):
    # Get the count of records by column and stroke
    df_breakdown = df.groupby([column, 'stroke'])['age'].count()
    # Get the count of records by gender
    df_total = df.groupby([column])['age'].count()
    # Get the percentage for 100% stacked bar chart
    df_pct = df_breakdown / df_total * 100
    # Create proper DataFrame's format
    df_pct = df_pct.unstack()
    return df_pct.plot.bar(stacked=True, figsize=(6,6), width=width)

df4 = get_stacked_bar_chart('age_binned')
plt.show()

df5 = get_100_percent_stacked_bar_chart('age_binned', width = 0.5)
plt.show()

fig,axes = plt.subplots(4,2,figsize = (15,15))
fig.suptitle("Count plot for categorical features")
#gender
sns.countplot(ax=axes[0,0],data=df,x='gender')
#smoking_status
sns.countplot(ax=axes[0,1],data=df,x='smoking_status')
#heart_disease
sns.countplot(ax=axes[1,0],data=df,x='heart_disease')
#ever_married
sns.countplot(ax=axes[1,1],data=df,x='ever_married')
#work_type
sns.countplot(ax=axes[2,0],data=df,x='work_type')
#Residence_type
sns.countplot(ax=axes[2,1],data=df,x='Residence_type')
#hypertension
sns.countplot(ax=axes[3,0],data=df,x='hypertension')
#stroke
sns.countplot(ax=axes[3,1],data=df,x='stroke')

plt.show()