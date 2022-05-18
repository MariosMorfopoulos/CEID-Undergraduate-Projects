import os
import urllib
import requests
import pandas as pd
import matplotlib.pyplot as plt


#5 diaforetika URLs
url2011 = "https://www.statistics.gr/el/statistics?p_p_id=documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_cacheability=cacheLevelPage&p_p_col_id=column-2&p_p_col_count=4&p_p_col_pos=2&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_javax.faces.resource=document&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_ln=downloadResources&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_documentID=113865&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_locale=el"
url2012 = "https://www.statistics.gr/el/statistics?p_p_id=documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_cacheability=cacheLevelPage&p_p_col_id=column-2&p_p_col_count=4&p_p_col_pos=2&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_javax.faces.resource=document&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_ln=downloadResources&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_documentID=113886&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_locale=el"
url2013 = "https://www.statistics.gr/el/statistics?p_p_id=documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_cacheability=cacheLevelPage&p_p_col_id=column-2&p_p_col_count=4&p_p_col_pos=2&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_javax.faces.resource=document&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_ln=downloadResources&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_documentID=113905&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_locale=el"
url2014 = "https://www.statistics.gr/el/statistics?p_p_id=documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_cacheability=cacheLevelPage&p_p_col_id=column-2&p_p_col_count=4&p_p_col_pos=2&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_javax.faces.resource=document&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_ln=downloadResources&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_documentID=113925&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_locale=el"
url2015 = "https://www.statistics.gr/el/statistics?p_p_id=documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_cacheability=cacheLevelPage&p_p_col_id=column-2&p_p_col_count=4&p_p_col_pos=2&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_javax.faces.resource=document&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_ln=downloadResources&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_documentID=198755&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_locale=el"

def my_func(url,filename):
    resp = requests.get(url)
    output = open(filename, 'wb')
    output.write(resp.content)
    output.close()

#dimiourgw 5 diforetika excel files me tin sunartisi my_func
my_func(url2011,'mmetaforas_2011.xls')
my_func(url2012,'mmetaforas_2012.xls')
my_func(url2013,'mmetaforas_2013.xls')
my_func(url2014,'mmetaforas_2014.xls')
my_func(url2015,'mmetaforas_2015.xls')

#dimiourgw 5 diaforetika dataframes apo ta antistoixa excel files & kanw define to sheet_name!(to teleutaio)
df_11   = pd.read_excel('mmetaforas_2011.xls', sheet_name='ΔΕΚ')
df_12   = pd.read_excel('mmetaforas_2012.xls', sheet_name='ΔΕΚ')
df_13   = pd.read_excel('mmetaforas_2013.xls', sheet_name='ΔΕΚ')
df_14   = pd.read_excel('mmetaforas_2014.xls', sheet_name='ΔΕΚ')
df_15   = pd.read_excel('mmetaforas_2015.xls', sheet_name='ΔΕΚΕΜ')


# arxikopoiw to dictionary me ta below keys kai 0 integer
dictionary_m_metaforas={'aeroplane': 0, 'train': 0, 'sea': 0, 'road': 0, 'total': 0}


#definition of function creating  my dictionary
def creating_my_dictionary(df,mydict):
    max_index = df.index.max()
    range_index = max_index//2
    for index in df.index:
        variable_geniko_synolo = df.loc[index ,df.columns[1]]
        if variable_geniko_synolo == 'ΓΕΝΙΚΟ ΣΥΝΟΛΟ' and index > range_index:
            # print(df.loc[index,df.columns[1]])
            # print(df.loc[index, df.columns[2]])
            mydict['aeroplane']   += round(df.loc[index, df.columns[2]])
            mydict['train']       += round(df.loc[index, df.columns[3]])
            mydict['sea']         += round(df.loc[index, df.columns[4]])
            mydict['road']        += round(df.loc[index, df.columns[5]])
            mydict['total']       += round(df.loc[index, df.columns[6]])



creating_my_dictionary(df_11, dictionary_m_metaforas)
creating_my_dictionary(df_12, dictionary_m_metaforas)
creating_my_dictionary(df_13, dictionary_m_metaforas)
creating_my_dictionary(df_14, dictionary_m_metaforas)
creating_my_dictionary(df_15, dictionary_m_metaforas)

#print to dictionary
print(dictionary_m_metaforas)

#definition of function my pie chart
def my_pie_chart(dictionary_m_metaforas):
    keys = list(dictionary_m_metaforas.keys())
    values = list(dictionary_m_metaforas.values())
    #remove last element total
    values.pop()
    keys.pop()

    values_temp=[]
    for i,v in enumerate(values):
        if i==0:
            values_temp.append(str(v)+" by aeroplane")
        elif i==1:
            values_temp.append(str(v)+" by train")
        elif i==2:
            values_temp.append(str(v)+" by sea")
        elif i==3:
            values_temp.append(str(v) +" by road")

    fig1, ax1 = plt.subplots()
    wedges,texts,autotexts= ax1.pie(values, labels=keys, autopct='%1.2f%%',shadow=False, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax1.set_title("Aφίξεις τουριστών στην Ελλάδα ανά μέσο μεταφοράς για την τετραετία 2011-2015")
    ax1.legend(wedges, values_temp,
              title="Μέσα Μεταφοράς",
              loc="center left",
              bbox_to_anchor=(0.8, 0.3, 0.4, 0.5))
    plt.show()

#visual of my pie chart
my_pie_chart(dictionary_m_metaforas)


# EXPORT TO CSV
###################################################################################################
#keys & values of the dictionary
keys = list(dictionary_m_metaforas.keys())
values = list(dictionary_m_metaforas.values())

#creating a dataframe to export to csv
export_df=pd.DataFrame([dictionary_m_metaforas])
export_df.to_csv('./Ανα_μεσο_μεταφορας_2011-15.csv', index = None, header=True)

#USE MYSQL
###################################################################################################
import mysql.connector

keys = list(dictionary_m_metaforas.keys())
values = list(dictionary_m_metaforas.values())

mydb = mysql.connector.connect(
  host="localhost",
  user="marios",
  passwd="morfopoulos",#123
  database="MM"
)

mycursor = mydb.cursor()
sql_2 = "CREATE TABLE IF NOT EXISTS ANA_M_METAFORAS (id INT AUTO_INCREMENT PRIMARY KEY, meso_metaforas VARCHAR(255), number INT)"
mycursor.execute(sql_2)

mySql_insert_query1 = """INSERT INTO ANA_M_METAFORAS (id, meso_metaforas, number)
                       VALUES
                       (1, +'aeroplane', 64004823) """

mySql_insert_query2 = """INSERT INTO ANA_M_METAFORAS (id, meso_metaforas, number)
                       VALUES
                       (2, +'train', 15998) """

mySql_insert_query3 = """INSERT INTO ANA_M_METAFORAS (id, meso_metaforas, number)
                       VALUES
                       (3, +'sea', 3878783) """

mySql_insert_query4 = """INSERT INTO ANA_M_METAFORAS (id, meso_metaforas, number)
                       VALUES
                       (4, +'road', 27597761) """


mycursor.execute(mySql_insert_query1)
mycursor.execute(mySql_insert_query2)
mycursor.execute(mySql_insert_query3)
mycursor.execute(mySql_insert_query4)


mydb.commit()
print(mycursor.rowcount, "Record inserted successfully into Laptop table")
mydb.close()