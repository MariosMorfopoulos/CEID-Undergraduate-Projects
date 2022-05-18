import pandas as pd
from sklearn.impute import KNNImputer
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('strokes.csv')
print(df)
df_deleted = df.copy(deep=True)
df_knn = df.copy(deep=True)
df_mean = df.copy(deep=True)
df_linear_regr = df.copy(deep=True)

#function that will delete the rows that have NaN values in our dataframe
def delete_nan_values(df_deleted):
    df_func = df.dropna()
    return df_func


def knn_fill_nan(df_knn):
    # calling the KNN class
    knn_imp = KNNImputer(n_neighbors=5, weights='uniform')
    df_knn['bmi'] = knn_imp.fit_transform(df_knn[['bmi','avg_glucose_level']])
    return df_knn


#function that will fill the NaN values of a column  with the mean of values of the column 
def fill_nan_values_with_mean_of_col(df_mean):
    #find which columns have NaN values
    col_with_nan = df_mean.columns[df_mean.isna().any()].tolist()
    #each column with NaN values filled with mean
    for i in col_with_nan:
        mean_value = df_mean[i].mean()
        df_mean[i].fillna(value= mean_value,inplace=True)
    return df_mean


#linear regression
def  fill_nan_values_with_linear_regr(df_linear_regr):
    df_linear_regr['bmi'] = df_linear_regr['bmi'].interpolate(method='linear', limit_direction='both')

deleted_nan_values = delete_nan_values(df_deleted)
print("the dataframe with the deleted nan values")
print(deleted_nan_values)

df_fill_with_linear = fill_nan_values_with_linear_regr(df_linear_regr)
print("the dataframe with the linear values")
print(df_linear_regr)

df_knn_values = knn_fill_nan(df_knn)
print("the dataframe with the knn values ")
print(df_knn_values)

df_fill_nan_with_mean = fill_nan_values_with_mean_of_col(df_mean)
print("Thats a dataframe with the mean values")
print(df_fill_nan_with_mean)


def random_forrest(stroke):
    object_cols = ["gender","ever_married","work_type","Residence_type","smoking_status"]
    label_encoder = LabelEncoder()
    for col in object_cols:
        label_encoder.fit(stroke[col])
        stroke[col] = label_encoder.transform(stroke[col])
    X = stroke.drop('stroke',axis=1)
    y = stroke['stroke']

    #split our data set into train and test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=100)

    #implement the random forest classifier
    rf = RandomForestClassifier(n_estimators=30, max_depth=10, random_state=1)
    rf.fit(X_train, y_train)

    y_pred = rf.predict(X_test)

    #result of the predictions
    df=pd.DataFrame({'Actual':y_test, 'Predicted':y_pred})
    recall = metrics.recall_score(y_test, y_pred)
    precision = metrics.precision_score(y_test, y_pred)
    f1_score = metrics.f1_score(y_test, y_pred)
    return df,recall,precision,f1_score



rand_del = random_forrest(deleted_nan_values)
print("Random forrest for the deleted rows")
print(rand_del)
#rand_lin_regr = random_forrest(df_fill_with_linear)
#print("Random forrest for the linear regression",rand_lin_regr)
rand_knn = random_forrest(df_knn_values)
print("Random forrest for the knn")
print(rand_knn)
rand_mean = random_forrest(df_fill_nan_with_mean)
print("Random forrest for the rand_mean")
print(rand_mean)
