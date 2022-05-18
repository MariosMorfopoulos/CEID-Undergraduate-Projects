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



#print(df_11)
#print(df_12)
#print(df_13)
#print(df_14)
#print(df_15)

dictionary_touristes_11_12={'Τουρίστες από Γερμανία το 2011':0,'Τουρίστες από Γερμανία το 2012':0,'Τουρίστες από Ην. Βασίλειο το 2011':0,'Τουρίστες από Ην. Βασίλειο το 2012':0,'Τουρίστες από Γαλλία το 2011':0,'Τουρίστες από Γαλλία το 2012':0,'Τουρίστες από Ιταλία το 2011':0,'Τουρίστες από Ιταλία το 2012':0,'Τουρίστες από Η.Π.Α. το 2011':0,'Τουρίστες από Η.Π.Α. το 2012':0}

#definition of function creating  my dictionary
def creating_my_dictionary_2011_2012(df,mydict):
    max_index = df.index.max()
    range_index = max_index//2
    for index in df.index:
        variable_germania = df.loc[index ,df.columns[1]]
        if variable_germania == 'Γερμανία' and index > range_index:
            # print(df.loc[index,df.columns[1]])
            # print(df.loc[index, df.columns[2]])
            mydict['Τουρίστες από Γερμανία το 2011']   += round(df.loc[index, df.columns[2]])
            mydict['Τουρίστες από Γερμανία το 2012']   += round(df.loc[index, df.columns[3]])
    
    for index in df.index:
        variable_invasileio = df.loc[index ,df.columns[1]]
        if variable_invasileio == 'Ην. Βασίλειο' and index > range_index:
            # print(df.loc[index,df.columns[1]])
            # print(df.loc[index, df.columns[2]])
            mydict['Τουρίστες από Ην. Βασίλειο το 2011']   += round(df.loc[index, df.columns[2]])
            mydict['Τουρίστες από Ην. Βασίλειο το 2012']   += round(df.loc[index, df.columns[3]])

    for index in df.index:
        variable_gallia = df.loc[index ,df.columns[1]]
        if variable_gallia == 'Γαλλία' and index > range_index:
            # print(df.loc[index,df.columns[1]])
            # print(df.loc[index, df.columns[2]])
            mydict['Τουρίστες από Γαλλία το 2011']   += round(df.loc[index, df.columns[2]])
            mydict['Τουρίστες από Γαλλία το 2012']   += round(df.loc[index, df.columns[3]])

    for index in df.index:
        variable_italia = df.loc[index ,df.columns[1]]
        if variable_italia == 'Ιταλία' and index > range_index:
            # print(df.loc[index,df.columns[1]])
            # print(df.loc[index, df.columns[2]])
            mydict['Τουρίστες από Ιταλία το 2011']   += round(df.loc[index, df.columns[2]])
            mydict['Τουρίστες από Ιταλία το 2012']   += round(df.loc[index, df.columns[3]])

    for index in df.index:
        variable_ipa = df.loc[index ,df.columns[1]]
        if variable_ipa == 'Η.Π.Α.' and index > range_index:
            # print(df.loc[index,df.columns[1]])
            # print(df.loc[index, df.columns[2]])
            mydict['Τουρίστες από Η.Π.Α. το 2011']   += round(df.loc[index, df.columns[2]])
            mydict['Τουρίστες από Η.Π.Α. το 2012']   += round(df.loc[index, df.columns[3]])


creating_my_dictionary_2011_2012(df_12, dictionary_touristes_11_12)
print(dictionary_touristes_11_12)


dictionary_touristes_13_14={'Τουρίστες από Γερμανία το 2013':0,'Τουρίστες από Γερμανία το 2014':0,'Τουρίστες από Ην. Βασίλειο το 2013':0,'Τουρίστες από Ην. Βασίλειο το 2014':0,'Τουρίστες από Γαλλία το 2013':0,'Τουρίστες από Γαλλία το 2014':0,'Τουρίστες από Ιταλία το 2013':0,'Τουρίστες από Ιταλία το 2014':0,'Τουρίστες από Η.Π.Α. το 2013':0,'Τουρίστες από Η.Π.Α. το 2014':0}

#definition of function creating  my dictionary
def creating_my_dictionary_2013_2014(df,mydict):
    max_index = df.index.max()
    range_index = max_index//2
    for index in df.index:
        variable_germania = df.loc[index ,df.columns[1]]
        if variable_germania == 'Γερμανία' and index > range_index:
            # print(df.loc[index,df.columns[1]])
            # print(df.loc[index, df.columns[2]])
            mydict['Τουρίστες από Γερμανία το 2013']   += round(df.loc[index, df.columns[2]])
            mydict['Τουρίστες από Γερμανία το 2014']   += round(df.loc[index, df.columns[3]])
    
    for index in df.index:
        variable_invasileio = df.loc[index ,df.columns[1]]
        if variable_invasileio == 'Ην. Βασίλειο' and index > range_index:
            # print(df.loc[index,df.columns[1]])
            # print(df.loc[index, df.columns[2]])
            mydict['Τουρίστες από Ην. Βασίλειο το 2013']   += round(df.loc[index, df.columns[2]])
            mydict['Τουρίστες από Ην. Βασίλειο το 2014']   += round(df.loc[index, df.columns[3]])

    for index in df.index:
        variable_gallia = df.loc[index ,df.columns[1]]
        if variable_gallia == 'Γαλλία' and index > range_index:
            # print(df.loc[index,df.columns[1]])
            # print(df.loc[index, df.columns[2]])
            mydict['Τουρίστες από Γαλλία το 2013']   += round(df.loc[index, df.columns[2]])
            mydict['Τουρίστες από Γαλλία το 2014']   += round(df.loc[index, df.columns[3]])

    for index in df.index:
        variable_italia = df.loc[index ,df.columns[1]]
        if variable_italia == 'Ιταλία' and index > range_index:
            # print(df.loc[index,df.columns[1]])
            # print(df.loc[index, df.columns[2]])
            mydict['Τουρίστες από Ιταλία το 2013']   += round(df.loc[index, df.columns[2]])
            mydict['Τουρίστες από Ιταλία το 2014']   += round(df.loc[index, df.columns[3]])

    for index in df.index:
        variable_ipa = df.loc[index ,df.columns[1]]
        if variable_ipa == 'Η.Π.Α.' and index > range_index:
            # print(df.loc[index,df.columns[1]])
            # print(df.loc[index, df.columns[2]])
            mydict['Τουρίστες από Η.Π.Α. το 2013']   += round(df.loc[index, df.columns[2]])
            mydict['Τουρίστες από Η.Π.Α. το 2014']   += round(df.loc[index, df.columns[3]])


creating_my_dictionary_2013_2014(df_14, dictionary_touristes_13_14)
print(dictionary_touristes_13_14)

dictionary_touristes_15={'Τουρίστες από Γερμανία το 2015':0,'Τουρίστες από Ην. Βασίλειο το 2015':0,'Τουρίστες από Γαλλία το 2015':0,'Τουρίστες από Ιταλία το 2015':0,'Τουρίστες από Η.Π.Α. το 2015':0}

#definition of function creating  my dictionary
def creating_my_dictionary_2015(df,mydict):
    max_index = df.index.max()
    range_index = max_index//2
    for index in df.index:
        variable_germania = df.loc[index ,df.columns[1]]
        if variable_germania == 'Γερμανία' and index > range_index:
            # print(df.loc[index,df.columns[1]])
            # print(df.loc[index, df.columns[2]])
            mydict['Τουρίστες από Γερμανία το 2015']   += round(df.loc[index, df.columns[3]])
    
    for index in df.index:
        variable_invasileio = df.loc[index ,df.columns[1]]
        if variable_invasileio == 'Ην. Βασίλειο' and index > range_index:
            # print(df.loc[index,df.columns[1]])
            # print(df.loc[index, df.columns[2]])
            mydict['Τουρίστες από Ην. Βασίλειο το 2015']   += round(df.loc[index, df.columns[3]])

    for index in df.index:
        variable_gallia = df.loc[index ,df.columns[1]]
        if variable_gallia == 'Γαλλία' and index > range_index:
            # print(df.loc[index,df.columns[1]])
            # print(df.loc[index, df.columns[2]])
            mydict['Τουρίστες από Γαλλία το 2015']   += round(df.loc[index, df.columns[3]])

    for index in df.index:
        variable_italia = df.loc[index ,df.columns[1]]
        if variable_italia == 'Ιταλία' and index > range_index:
            # print(df.loc[index,df.columns[1]])
            # print(df.loc[index, df.columns[2]])
            mydict['Τουρίστες από Ιταλία το 2015']   += round(df.loc[index, df.columns[3]])

    for index in df.index:
        variable_ipa = df.loc[index ,df.columns[1]]
        if variable_ipa == 'Η.Π.Α.' and index > range_index:
            # print(df.loc[index,df.columns[1]])
            # print(df.loc[index, df.columns[2]])
            mydict['Τουρίστες από Η.Π.Α. το 2015']   += round(df.loc[index, df.columns[3]])


creating_my_dictionary_2015(df_15, dictionary_touristes_15)
print(dictionary_touristes_15)

#definition of function my pie chart
def my_pie_chart_11_12(dictionary_touristes_11_12):
    keys_11_12 = list(dictionary_touristes_11_12.keys())
    values_11_12 = list(dictionary_touristes_11_12.values())
    

    values_temp_11_12=[]
    for i,v in enumerate(values_11_12):
        if i==0:
            values_temp_11_12.append(str(v)+" Γερμανία το 2011")            
        elif i==1:
            values_temp_11_12.append(str(v)+" Γερμανία το 2012")
        elif i==2:
            values_temp_11_12.append(str(v)+" Ην.Βασίλειο το 2011")
        elif i==3:
            values_temp_11_12.append(str(v) +" Ην.Βασίλειο το 2012")
        elif i==4:
            values_temp_11_12.append(str(v) +" Γαλλία το 2011")
        elif i==5:
            values_temp_11_12.append(str(v) +" Γαλλία το 2012")
        elif i==6:
            values_temp_11_12.append(str(v) +" Ιταλία το 2011")
        elif i==7:
            values_temp_11_12.append(str(v) +" Ιταλία το 2012")
        elif i==8:
            values_temp_11_12.append(str(v) +" Η.Π.Α. το 2011")
        elif i==9:
            values_temp_11_12.append(str(v) +" Η.Π.Α. το 2012")
            print(values_temp_11_12)

    fig1, ax1 = plt.subplots()
    wedges,texts,autotexts= ax1.pie(values_11_12, labels=keys_11_12, autopct='%1.2f%%',shadow=False, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax1.set_title("Χώρες καταγωγής με το μεγαλύτερο μερίδιο στις αφίξεις τουριστών στην  Ελλάδα για το 2011-2012")
    ax1.legend(wedges, values_temp_11_12,
              title="Τουρίστες",
              loc="right",
              bbox_to_anchor=(0.01, 0.4, 0.1, 0.65))
    plt.show()

#visual of my pie chart
my_pie_chart_11_12(dictionary_touristes_11_12)

#definition of function my pie chart
def my_pie_chart_13_14(dictionary_touristes_13_14):
    keys_13_14 = list(dictionary_touristes_13_14.keys())
    values_13_14 = list(dictionary_touristes_13_14.values())
    

    values_temp_13_14=[]
    for i,v in enumerate(values_13_14):
        if i==0:
            values_temp_13_14.append(str(v)+" Γερμανία το 2015")            
        elif i==1:
            values_temp_13_14.append(str(v)+"Ην.Βασίλειο το 2015")
        elif i==2:
            values_temp_13_14.append(str(v)+" Ην.Βασίλειο το 2013")
        elif i==3:
            values_temp_13_14.append(str(v) +" Ην.Βασίλειο το 2014")
        elif i==4:
            values_temp_13_14.append(str(v) +" Γαλλία το 2013")
        elif i==5:
            values_temp_13_14.append(str(v) +" Γαλλία το 2014")
        elif i==6:
            values_temp_13_14.append(str(v) +" Ιταλία το 2013")
        elif i==7:
            values_temp_13_14.append(str(v) +" Ιταλία το 2014")
        elif i==8:
            values_temp_13_14.append(str(v) +" Η.Π.Α. το 2013")
        elif i==9:
            values_temp_13_14.append(str(v) +" Η.Π.Α. το 2014")
            print(values_temp_13_14)

    fig1, ax1 = plt.subplots()
    wedges,texts,autotexts= ax1.pie(values_13_14, labels=keys_13_14, autopct='%1.2f%%',shadow=False, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax1.set_title("Χώρες καταγωγής με το μεγαλύτερο μερίδιο στις αφίξεις τουριστών στην  Ελλάδα για το 2013-2014")
    ax1.legend(wedges, values_temp_13_14,
              title="Τουρίστες",
              loc="right",
              bbox_to_anchor=(0.01, 0.4, 0.1, 0.75))
    plt.show()

#visual of my pie chart
my_pie_chart_13_14(dictionary_touristes_13_14)

#definition of function my pie chart
def my_pie_chart_15(dictionary_touristes_15):
    keys_15 = list(dictionary_touristes_15.keys())
    values_15 = list(dictionary_touristes_15.values())
    
    values_temp_15=[]
    for i,v in enumerate(values_15):
        if i==0:
            values_temp_15.append(str(v)+" Γερμανία το 2015")            
        elif i==1:
            values_temp_15.append(str(v)+" Ην.Βασίλειο το 2015")
        elif i==2:
            values_temp_15.append(str(v)+"  Γαλλία το 2015")
        elif i==3:
            values_temp_15.append(str(v) +" Ιταλία το 2015")
        elif i==4:
            values_temp_15.append(str(v) +" Η.Π.Α. το 2015")
            print(values_temp_15)

    fig1, ax1 = plt.subplots()
    wedges,texts,autotexts= ax1.pie(values_15, labels=keys_15, autopct='%1.2f%%',shadow=False, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax1.set_title("Χώρες καταγωγής με το μεγαλύτερο μερίδιο στις αφίξεις τουριστών στην  Ελλάδα για το 2015")
    ax1.legend(wedges, values_temp_15,
              title="Τουρίστες",
              loc="right",
              bbox_to_anchor=(0.01, 0.2, 0.1, 0.8))
    plt.show()

#visual of my pie chart
my_pie_chart_15(dictionary_touristes_15)

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
export_df.to_csv('./Χώρες_μεγαλύτερο_μερίδιο_άφιξεις_τουριστών_2011-15.csv', index = None, header=True)




#USE MYSQL
###################################################################################################
import mysql.connector

keys_11_12 = list(dictionary_touristes_11_12.keys())
values_11_12 = list(dictionary_touristes_11_12.values())
keys_13_14 = list(dictionary_touristes_13_14.keys())
values_13_14 = list(dictionary_touristes_13_14.values())
keys_15 = list(dictionary_touristes_15.keys())
values_15 = list(dictionary_touristes_15.values())

mydb = mysql.connector.connect(
  host="localhost",
  user="marios",
  passwd="morfopoulos",#123
  database="MM"
)

mycursor = mydb.cursor()
sql_2 = "CREATE TABLE IF NOT EXISTS XWRES_M_AFIXEIS (id INT AUTO_INCREMENT PRIMARY KEY, XWRES VARCHAR(255), number INT)"
mycursor.execute(sql_2)

mySql_insert_query1 = """INSERT INTO XWRES_M_AFIXEIS (id, XWRES, number)
                       VALUES
                       (1, +'Germania', 2810350) """

mySql_insert_query2 = """INSERT INTO XWRES_M_AFIXEIS (id, XWRES, number)
                       VALUES
                       (2, +'Gallia', 1522100) """

mySql_insert_query3 = """INSERT INTO XWRES_M_AFIXEIS (id, XWRES, number)
                       VALUES
                       (3, +'Italia', 1355327) """

mySql_insert_query4 = """INSERT INTO XWRES_M_AFIXEIS (id, XWRES, number)
                       VALUES
                       (4, +'USA', 750250) """


mycursor.execute(mySql_insert_query1)
mycursor.execute(mySql_insert_query2)
mycursor.execute(mySql_insert_query3)
mycursor.execute(mySql_insert_query4)


mydb.commit()
print(mycursor.rowcount, "Record inserted successfully into Laptop table")
mydb.close()