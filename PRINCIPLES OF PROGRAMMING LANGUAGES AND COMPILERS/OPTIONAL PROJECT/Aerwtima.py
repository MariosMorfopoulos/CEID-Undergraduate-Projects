import os
import urllib
import requests
import pandas as pd
import matplotlib.pyplot as plt


#5 diaforetika URLs
url2011 = "https://www.statistics.gr/el/statistics?p_p_id=documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_cacheability=cacheLevelPage&p_p_col_id=column-2&p_p_col_count=4&p_p_col_pos=2&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_javax.faces.resource=document&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_ln=downloadResources&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_documentID=113866&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_locale=el"
url2012 = "https://www.statistics.gr/el/statistics?p_p_id=documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_cacheability=cacheLevelPage&p_p_col_id=column-2&p_p_col_count=4&p_p_col_pos=2&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_javax.faces.resource=document&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_ln=downloadResources&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_documentID=113885&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_locale=el"
url2013 = "https://www.statistics.gr/el/statistics?p_p_id=documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_cacheability=cacheLevelPage&p_p_col_id=column-2&p_p_col_count=4&p_p_col_pos=2&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_javax.faces.resource=document&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_ln=downloadResources&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_documentID=113903&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_locale=el"
url2014 = "https://www.statistics.gr/el/statistics?p_p_id=documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_cacheability=cacheLevelPage&p_p_col_id=column-2&p_p_col_count=4&p_p_col_pos=2&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_javax.faces.resource=document&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_ln=downloadResources&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_documentID=113926&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_locale=el"
url2015 = "https://www.statistics.gr/el/statistics?p_p_id=documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_cacheability=cacheLevelPage&p_p_col_id=column-2&p_p_col_count=4&p_p_col_pos=2&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_javax.faces.resource=document&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_ln=downloadResources&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_documentID=198754&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_locale=el"

def my_func(url,filename):
    resp = requests.get(url)
    output = open(filename, 'wb')
    output.write(resp.content)
    output.close()

#dimiourgw 5 diforetika excel files me tin sunartisi my_func
my_func(url2011,'smetaforas_2011.xls')
my_func(url2012,'smetaforas_2012.xls')
my_func(url2013,'smetaforas_2013.xls')
my_func(url2014,'smetaforas_2014.xls')
my_func(url2015,'smetaforas_2015.xls')




df_12   = pd.read_excel('smetaforas_2012.xls', sheet_name='ΔΕΚ')
df_14   = pd.read_excel('smetaforas_2014.xls', sheet_name='ΔΕΚ')
df_15   = pd.read_excel('smetaforas_2015.xls', sheet_name='ΔΕΚΕΜ')



dictionary_touristes_11_12={'Συνολικές αφίξεις τουριστών στην Ελλάδα το 2011':0,'Συνολικές αφίξεις τουριστών στην Ελλάδα το 2012':0}

#definition of function creating  my dictionary
def creating_my_dictionary_2011_2012(df,mydict):
    max_index = df.index.max()
    range_index = max_index//2
    for index in df.index:
        variable_geniko_synolo = df.loc[index ,df.columns[1]]
        if variable_geniko_synolo == 'ΓΕΝΙΚΟ ΣΥΝΟΛΟ' and index > range_index:
            # print(df.loc[index,df.columns[1]])
            # print(df.loc[index, df.columns[2]])
            mydict['Συνολικές αφίξεις τουριστών στην Ελλάδα το 2011']   += round(df.loc[index, df.columns[2]])
            mydict['Συνολικές αφίξεις τουριστών στην Ελλάδα το 2012']   += round(df.loc[index, df.columns[3]])


creating_my_dictionary_2011_2012(df_12, dictionary_touristes_11_12)
print(dictionary_touristes_11_12)

dictionary_touristes_13_14={'Συνολικές αφίξεις τουριστών στην Ελλάδα το 2013':0,'Συνολικές αφίξεις τουριστών στην Ελλάδα το 2014':0}


#definition of function creating  my dictionary 
def creating_my_dictionary_2013_2014(df,mydict):
    max_index = df.index.max()
    range_index = max_index//2
    for index in df.index:
        variable_geniko_synolo = df.loc[index ,df.columns[1]]
        if variable_geniko_synolo == 'ΓΕΝΙΚΟ ΣΥΝΟΛΟ' and index > range_index:
            # print(df.loc[index,df.columns[1]])
            # print(df.loc[index, df.columns[2]])
            mydict['Συνολικές αφίξεις τουριστών στην Ελλάδα το 2013']   += round(df.loc[index, df.columns[2]])
            mydict['Συνολικές αφίξεις τουριστών στην Ελλάδα το 2014']   += round(df.loc[index, df.columns[3]])


creating_my_dictionary_2013_2014(df_14, dictionary_touristes_13_14)
print(dictionary_touristes_13_14)


dictionary_touristes_15={'Συνολικές αφίξεις τουριστών στην Ελλάδα το 2015':0}


#definition of function creating  my dictionary
def creating_my_dictionary_2015(df,mydict):
    max_index = df.index.max()
    range_index = max_index//2
    for index in df.index:
        variable_geniko_synolo = df.loc[index ,df.columns[1]]
        if variable_geniko_synolo == 'ΓΕΝΙΚΟ ΣΥΝΟΛΟ' and index > range_index:
            # print(df.loc[index,df.columns[1]])
            # print(df.loc[index, df.columns[2]])
            mydict['Συνολικές αφίξεις τουριστών στην Ελλάδα το 2015']   += round(df.loc[index, df.columns[3]])


creating_my_dictionary_2015(df_15, dictionary_touristes_15)
print(dictionary_touristes_15)


#definition of function my pie chart
def my_pie_chart(dictionary_touristes_11_12,dictionary_touristes_13_14,dictionary_touristes_15):
    keys_11_12 = list(dictionary_touristes_11_12.keys())
    values_11_12 = list(dictionary_touristes_11_12.values())
    keys_13_14 = list(dictionary_touristes_13_14.keys())
    values_13_14 = list(dictionary_touristes_13_14.values())
    keys_15 = list(dictionary_touristes_15.values())
    values_15 = list(dictionary_touristes_15.values())
    
    values_temp_11_12=[]
    for i,v in enumerate(values_11_12):
        if i==0:
            values_temp_11_12.append( str(v) + " =2011 ")
        elif i==1:
            values_temp_11_12.append( str(v) + " =2012 ")
            print(values_temp_11_12)

    values_temp_13_14=[]
    for i,v in enumerate(values_13_14):
        if i==0:
            values_temp_13_14.append( str(v) + " =2013 ")
        elif i==1:
            values_temp_13_14.append( str(v) + " =2014 ")
            print(values_temp_13_14)

    values_temp_15=[]
    for i,v in enumerate(values_15):
        if i==0:
            values_temp_15.append( str(v) + " =2015 ")
            print(values_temp_15)
    
    #new_values_temp=[]
    new_values_temp=values_temp_11_12+values_temp_13_14+values_temp_15
    #new_values=[]
    new_values=values_11_12+values_13_14+values_15
    new_keys=keys_11_12+keys_13_14+keys_15
        

    fig1, ax1 = plt.subplots()
    wedges,texts,autotexts= ax1.pie(new_values, labels=new_keys, autopct='%1.2f%%',shadow=False, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax1.set_title("Aφίξεις τουριστών στην Ελλάδα για την τετραετία 2011-2015")
    ax1.legend(wedges, new_values_temp,
              title="Τουρίστες 2011-2015",
              loc="right",
              bbox_to_anchor=(0.6, 0.5, 0.4, 1))
    plt.show()
		



        
my_pie_chart(dictionary_touristes_11_12,dictionary_touristes_13_14,dictionary_touristes_15)

# EXPORT TO CSV
###################################################################################################
#keys & values of the dictionary
new_list_touristwn=[]
keys_11_12 = list(dictionary_touristes_11_12.keys())
values_11_12 = list(dictionary_touristes_13_14.values())
values_13_14 = list(dictionary_touristes_11_12.values())
keys_13_14 = list(dictionary_touristes_13_14.keys())
values_15 = list(dictionary_touristes_15.values())
keys_15 = list(dictionary_touristes_15.values())
new_list_touristwn=keys_11_12+keys_13_14+keys_15
new_list_touristwn=values_11_12+values_13_14+values_15

#creating a dataframe to export to csv
export_df=pd.DataFrame([new_list_touristwn])
export_df.to_csv('./Συνολικές_αφίξεις_τουριστών_2011-15.csv', index = None, header=True)

#USE MYSQL
###################################################################################################
import mysql.connector

keys_11_12 = list(dictionary_touristes_11_12.keys())
values_11_12 = list(dictionary_touristes_13_14.values())
values_13_14 = list(dictionary_touristes_11_12.values())
keys_13_14 = list(dictionary_touristes_13_14.keys())
values_15 = list(dictionary_touristes_15.values())

mydb = mysql.connector.connect(
  host="localhost",
  user="marios",
  passwd="morfopoulos",#123
  database="MM"
)

mycursor = mydb.cursor()
sql_2 = "CREATE TABLE IF NOT EXISTS SYN_A_TOYRISTWN (id INT AUTO_INCREMENT PRIMARY KEY, afixeis_touristwn VARCHAR(255), number INT)"
mycursor.execute(sql_2)

mySql_insert_query1 = """INSERT INTO SYN_A_TOYRISTWN (id, afixeis_touristwn, number)
                       VALUES
                       (1, +'Synolikes afixeis touristwn sthn Ellada to 2011', 16427247)"""

mySql_insert_query2 = """INSERT INTO SYN_A_TOYRISTWN (id, afixeis_touristwn, number)
                       VALUES
                       (2, +'Synolikes afixeis touristwn sthn Ellada to 2012', 15517622)"""

mySql_insert_query3 = """INSERT INTO SYN_A_TOYRISTWN (id, afixeis_touristwn, number)
                       VALUES
                       (3, +'Synolikes afixeis touristwn sthn Ellada to 2013', 17919580)"""

mySql_insert_query4 = """INSERT INTO SYN_A_TOYRISTWN (id, afixeis_touristwn, number)
                       VALUES
                       (4, +'Synolikes afixeis touristwn sthn Ellada to 2014', 22033463)"""

mySql_insert_query5 = """INSERT INTO SYN_A_TOYRISTWN (id, afixeis_touristwn, number)
                       VALUES
                       (5, +'Synolikes afixeis touristwn sthn Ellada to 2015', 23599455)"""

mycursor.execute(mySql_insert_query1)
mycursor.execute(mySql_insert_query2)
mycursor.execute(mySql_insert_query3)
mycursor.execute(mySql_insert_query4)
mycursor.execute(mySql_insert_query5)

mydb.commit()
print(mycursor.rowcount, "Record inserted successfully into Laptop table")
mydb.close()







