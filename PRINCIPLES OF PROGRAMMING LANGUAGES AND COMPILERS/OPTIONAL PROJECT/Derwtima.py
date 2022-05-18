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




#df_12   = pd.read_excel('smetaforas_2012.xls', sheet_name='ΔΕΚ')
#df_14   = pd.read_excel('smetaforas_2014.xls', sheet_name='ΔΕΚ')
#df_15   = pd.read_excel('smetaforas_2015.xls', sheet_name='ΔΕΚΕΜ')

df_trimino1_11_12   = pd.read_excel('smetaforas_2012.xls', sheet_name='ΜΑΡ')
df_trimino2_11_12   = pd.read_excel('smetaforas_2012.xls', sheet_name='ΙΟΥΝ')
df_trimino3_11_12   = pd.read_excel('smetaforas_2012.xls', sheet_name='ΣΕΠΤ')
df_trimino4_11_12   = pd.read_excel('smetaforas_2012.xls', sheet_name='ΔΕΚ')
df_trimino1_13_14   = pd.read_excel('smetaforas_2014.xls', sheet_name='ΜΑΡ')
df_trimino2_13_14   = pd.read_excel('smetaforas_2014.xls', sheet_name='ΙΟΥΝ')
df_trimino3_13_14   = pd.read_excel('smetaforas_2014.xls', sheet_name='ΣΕΠΤ')
df_trimino4_13_14   = pd.read_excel('smetaforas_2014.xls', sheet_name='ΔΕΚ')
df_trimino1_15   	= pd.read_excel('smetaforas_2015.xls', sheet_name='ΜΑΡ')
df_trimino2_15   	= pd.read_excel('smetaforas_2015.xls', sheet_name='ΙΟΥΝ')
df_trimino3_15   	= pd.read_excel('smetaforas_2015.xls', sheet_name='ΣΕΠΤ')
df_trimino4_15   	= pd.read_excel('smetaforas_2015.xls', sheet_name='ΔΕΚΕΜ')


print(df_trimino1_11_12)
print(df_trimino2_11_12)
print(df_trimino3_11_12)
print(df_trimino4_11_12)
print(df_trimino1_13_14)
print(df_trimino2_13_14)
print(df_trimino3_13_14)
print(df_trimino4_13_14)
print(df_trimino1_15)
print(df_trimino2_15)
print(df_trimino3_15)
print(df_trimino4_15)



dictionary_touristes_trimino1_11_12={'Το πρώτο τρίμηνο του 2011':0,'Το πρώτο τρίμηνο του  2012':0}



#definition of function creating  my dictionary
def creating_my_dictionary_trimino1_2011_2012(df,mydict):
    max_index = df.index.max()
    range_index = max_index//2
    for index in df.index:
        variable_geniko_synolo = df.loc[index ,df.columns[1]]
        if variable_geniko_synolo == 'ΓΕΝΙΚΟ ΣΥΝΟΛΟ' and index > range_index:
            # print(df.loc[index,df.columns[1]])
            # print(df.loc[index, df.columns[2]])
            mydict['Το πρώτο τρίμηνο του 2011']   += round(df.loc[index, df.columns[2]])
            mydict['Το πρώτο τρίμηνο του  2012']  += round(df.loc[index, df.columns[3]])


creating_my_dictionary_trimino1_2011_2012(df_trimino1_11_12, dictionary_touristes_trimino1_11_12)
print(dictionary_touristes_trimino1_11_12)





dictionary_touristes_trimino2_11_12={'Το δεύτερο τρίμηνο του  2011':0,'Το δεύτερο τρίμηνο του  2012':0}

def creating_my_dictionary_trimino2_2011_2012(df,mydict):
    max_index = df.index.max()
    range_index = max_index//2
    for index in df.index:
        variable_geniko_synolo = df.loc[index ,df.columns[1]]
        if variable_geniko_synolo == 'ΓΕΝΙΚΟ ΣΥΝΟΛΟ' and index > range_index:
            # print(df.loc[index,df.columns[1]])
            # print(df.loc[index, df.columns[2]])
            mydict['Το δεύτερο τρίμηνο του  2011']   += round(df.loc[index, df.columns[2]])
            mydict['Το δεύτερο τρίμηνο του  2012']   += round(df.loc[index, df.columns[3]])


creating_my_dictionary_trimino2_2011_2012(df_trimino2_11_12, dictionary_touristes_trimino2_11_12)
print(dictionary_touristes_trimino2_11_12)

dictionary_touristes_trimino3_11_12={'Το τρίτο τρίμηνο του  2011':0,'Το τρίτο τρίμηνο του  2012':0}

def creating_my_dictionary_trimino3_2011_2012(df,mydict):
    max_index = df.index.max()
    range_index = max_index//2
    for index in df.index:
        variable_geniko_synolo = df.loc[index ,df.columns[1]]
        if variable_geniko_synolo == 'ΓΕΝΙΚΟ ΣΥΝΟΛΟ' and index > range_index:
            # print(df.loc[index,df.columns[1]])
            # print(df.loc[index, df.columns[2]])
            mydict['Το τρίτο τρίμηνο του  2011']   += round(df.loc[index, df.columns[2]])
            mydict['Το τρίτο τρίμηνο του  2012']   += round(df.loc[index, df.columns[3]])


creating_my_dictionary_trimino3_2011_2012(df_trimino3_11_12, dictionary_touristes_trimino3_11_12)
print(dictionary_touristes_trimino3_11_12)


dictionary_touristes_trimino4_11_12={'Το τέταρτο τρίμηνο του  2011':0,'Το τέταρτο τρίμηνο του  2012':0}

def creating_my_dictionary_trimino4_2011_2012(df,mydict):
    max_index = df.index.max()
    range_index = max_index//2
    for index in df.index:
        variable_geniko_synolo = df.loc[index ,df.columns[1]]
        if variable_geniko_synolo == 'ΓΕΝΙΚΟ ΣΥΝΟΛΟ' and index > range_index:
            # print(df.loc[index,df.columns[1]])
            # print(df.loc[index, df.columns[2]])
            mydict['Το τέταρτο τρίμηνο του  2011']   += round(df.loc[index, df.columns[2]])
            mydict['Το τέταρτο τρίμηνο του  2012']   += round(df.loc[index, df.columns[3]])


creating_my_dictionary_trimino4_2011_2012(df_trimino4_11_12, dictionary_touristes_trimino4_11_12)
print(dictionary_touristes_trimino4_11_12)

dictionary_touristes_trimino1_13_14={'Tο  πρώτο τρίμηνο του  2013':0,'Tο πρώτο τρίμηνο του  2014':0}

def creating_my_dictionary_trimino1_2013_2014(df,mydict):
    max_index = df.index.max()
    range_index = max_index//2
    for index in df.index:
        variable_geniko_synolo = df.loc[index ,df.columns[1]]
        if variable_geniko_synolo == 'ΓΕΝΙΚΟ ΣΥΝΟΛΟ' and index > range_index:
            # print(df.loc[index,df.columns[1]])
            # print(df.loc[index, df.columns[2]])
            mydict['Tο  πρώτο τρίμηνο του  2013']   += round(df.loc[index, df.columns[2]])
            mydict['Tο πρώτο τρίμηνο του  2014']   += round(df.loc[index, df.columns[3]])


creating_my_dictionary_trimino1_2013_2014(df_trimino1_13_14, dictionary_touristes_trimino1_13_14)
print(dictionary_touristes_trimino1_13_14)

dictionary_touristes_trimino2_13_14={'Tο δεύτερο τρίμηνο του  2013':0,'Tο δεύτερο τρίμηνο του  2014':0}

def creating_my_dictionary_trimino2_2013_2014(df,mydict):
    max_index = df.index.max()
    range_index = max_index//2
    for index in df.index:
        variable_geniko_synolo = df.loc[index ,df.columns[1]]
        if variable_geniko_synolo == 'ΓΕΝΙΚΟ ΣΥΝΟΛΟ' and index > range_index:
            # print(df.loc[index,df.columns[1]])
            # print(df.loc[index, df.columns[2]])
            mydict['Tο δεύτερο τρίμηνο του  2013']   += round(df.loc[index, df.columns[2]])
            mydict['Tο δεύτερο τρίμηνο του  2014']   += round(df.loc[index, df.columns[3]])


creating_my_dictionary_trimino2_2013_2014(df_trimino2_13_14, dictionary_touristes_trimino2_13_14)
print(dictionary_touristes_trimino2_13_14)

dictionary_touristes_trimino3_13_14={'Tο τρίτο τρίμηνο του  2013':0,'Tο τρίτο τρίμηνο του  2014':0}

def creating_my_dictionary_trimino3_2013_2014(df,mydict):
    max_index = df.index.max()
    range_index = max_index//2
    for index in df.index:
        variable_geniko_synolo = df.loc[index ,df.columns[1]]
        if variable_geniko_synolo == 'ΓΕΝΙΚΟ ΣΥΝΟΛΟ' and index > range_index:
            # print(df.loc[index,df.columns[1]])
            # print(df.loc[index, df.columns[2]])
            mydict['Tο τρίτο τρίμηνο του  2013']   += round(df.loc[index, df.columns[2]])
            mydict['Tο τρίτο τρίμηνο του  2014']   += round(df.loc[index, df.columns[3]])


creating_my_dictionary_trimino3_2013_2014(df_trimino3_13_14, dictionary_touristes_trimino3_13_14)
print(dictionary_touristes_trimino3_13_14)

dictionary_touristes_trimino4_13_14={'Tο τέταρτο τρίμηνο του  2013':0,'Tο τέταρτο τρίμηνο του  2014':0}

def creating_my_dictionary_trimino4_2013_2014(df,mydict):
    max_index = df.index.max()
    range_index = max_index//2
    for index in df.index:
        variable_geniko_synolo = df.loc[index ,df.columns[1]]
        if variable_geniko_synolo == 'ΓΕΝΙΚΟ ΣΥΝΟΛΟ' and index > range_index:
            # print(df.loc[index,df.columns[1]])
            # print(df.loc[index, df.columns[2]])
            mydict['Tο τέταρτο τρίμηνο του  2013']   += round(df.loc[index, df.columns[2]])
            mydict['Tο τέταρτο τρίμηνο του  2014']   += round(df.loc[index, df.columns[3]])


creating_my_dictionary_trimino4_2013_2014(df_trimino4_13_14, dictionary_touristes_trimino4_13_14)
print(dictionary_touristes_trimino4_13_14)


dictionary_touristes_trimino1_15={'Το πρώτο τρίμηνο του  2015':0}

def creating_my_dictionary_trimino1_15(df,mydict):
    max_index = df.index.max()
    range_index = max_index//2
    for index in df.index:
        variable_geniko_synolo = df.loc[index ,df.columns[1]]
        if variable_geniko_synolo == 'ΓΕΝΙΚΟ ΣΥΝΟΛΟ' and index > range_index:
            # print(df.loc[index,df.columns[1]])
            # print(df.loc[index, df.columns[2]])
            mydict['Το πρώτο τρίμηνο του  2015']   += round(df.loc[index, df.columns[3]])


creating_my_dictionary_trimino1_15(df_trimino1_15, dictionary_touristes_trimino1_15)
print(dictionary_touristes_trimino1_15)

dictionary_touristes_trimino2_15={'Το δεύτερο τρίμηνο του  2015':0}

def creating_my_dictionary_trimino2_15(df,mydict):
    max_index = df.index.max()
    range_index = max_index//2
    for index in df.index:
        variable_geniko_synolo = df.loc[index ,df.columns[1]]
        if variable_geniko_synolo == 'ΓΕΝΙΚΟ ΣΥΝΟΛΟ' and index > range_index:
            # print(df.loc[index,df.columns[1]])
            # print(df.loc[index, df.columns[2]])
            mydict['Το δεύτερο τρίμηνο του  2015']   += round(df.loc[index, df.columns[3]])


creating_my_dictionary_trimino2_15(df_trimino2_15, dictionary_touristes_trimino2_15)
print(dictionary_touristes_trimino2_15)

dictionary_touristes_trimino3_15={'Το τρίτο τρίμηνο του  2015':0}

def creating_my_dictionary_trimino3_15(df,mydict):
    max_index = df.index.max()
    range_index = max_index//2
    for index in df.index:
        variable_geniko_synolo = df.loc[index ,df.columns[1]]
        if variable_geniko_synolo == 'ΓΕΝΙΚΟ ΣΥΝΟΛΟ' and index > range_index:
            # print(df.loc[index,df.columns[1]])
            # print(df.loc[index, df.columns[2]])
            mydict['Το τρίτο τρίμηνο του  2015']   += round(df.loc[index, df.columns[3]])


creating_my_dictionary_trimino3_15(df_trimino3_15, dictionary_touristes_trimino3_15)
print(dictionary_touristes_trimino3_15)

dictionary_touristes_trimino4_15={'Το τέταρτο τρίμηνο του  2015':0}

def creating_my_dictionary_trimino4_15(df,mydict):
    max_index = df.index.max()
    range_index = max_index//2
    for index in df.index:
        variable_geniko_synolo = df.loc[index ,df.columns[1]]
        if variable_geniko_synolo == 'ΓΕΝΙΚΟ ΣΥΝΟΛΟ' and index > range_index:
            # print(df.loc[index,df.columns[1]])
            # print(df.loc[index, df.columns[2]])
            mydict['Το τέταρτο τρίμηνο του  2015']   += round(df.loc[index, df.columns[3]])


creating_my_dictionary_trimino4_15(df_trimino4_15, dictionary_touristes_trimino4_15)
print(dictionary_touristes_trimino4_15)

#definition of function my pie chart
def my_pie_chart_2011_2012(dictionary_touristes_trimino1_11_12,dictionary_touristes_trimino2_11_12,dictionary_touristes_trimino3_11_12,dictionary_touristes_trimino4_11_12): #,dictionary_touristes_trimino1_13_14,df_trimino2_13_14,dictionary_touristes_trimino3_13_14,df_trimino4_13_14):
    trimino1_keys_11_12 = list(dictionary_touristes_trimino1_11_12.keys())
    trimino1_values_11_12 = list(dictionary_touristes_trimino1_11_12.values())
    trimino2_keys_11_12 = list(dictionary_touristes_trimino2_11_12.keys())
    trimino2_values_11_12 = list(dictionary_touristes_trimino2_11_12.values())
    trimino3_keys_11_12 = list(dictionary_touristes_trimino3_11_12.keys())
    trimino3_values_11_12 = list(dictionary_touristes_trimino3_11_12.values())
    trimino4_keys_11_12 = list(dictionary_touristes_trimino4_11_12.keys())
    trimino4_values_11_12 = list(dictionary_touristes_trimino4_11_12.values())
    
    values_temp_trimino1_11_12=[]
    for i,v in enumerate(trimino1_values_11_12):
        if i==0:
            values_temp_trimino1_11_12.append( str(v) + " = Πρώτο τρίμηνο του 2011 ")
        elif i==1:
            values_temp_trimino1_11_12.append( str(v) + " = Πρώτο τρίμηνο του 2012 ")
            print(values_temp_trimino1_11_12)

    values_temp_trimino2_11_12=[]
    for i,v in enumerate(trimino2_values_11_12):
        if i==0:
            values_temp_trimino2_11_12.append( str(v) + " = Δεύτερο τρίμηνο του 2011 ")
        elif i==1:
            values_temp_trimino2_11_12.append( str(v) + " = Δεύτερο τρίμηνο του 2012 ")
            print(values_temp_trimino2_11_12)

    values_temp_trimino3_11_12=[]
    for i,v in enumerate(trimino3_values_11_12):
        if i==0:
            values_temp_trimino3_11_12.append( str(v) + " = Τρίτο τρίμηνο του 2011 ")
        elif i==1:
            values_temp_trimino3_11_12.append( str(v) + " = Τρίτο τρίμηνο του 2012 ")
            print(values_temp_trimino3_11_12)

    values_temp_trimino4_11_12=[]
    for i,v in enumerate(trimino4_values_11_12):
        if i==0:
            values_temp_trimino4_11_12.append( str(v) + " = Τέταρτο τρίμηνο του 2011 ")
        elif i==1:
            values_temp_trimino4_11_12.append( str(v) + " = Τέταρτο τρίμηνο του 2012 ")
            print(values_temp_trimino4_11_12)
       
    #new_values_temp=[]
    new_values_temp=values_temp_trimino1_11_12+values_temp_trimino2_11_12+values_temp_trimino3_11_12+values_temp_trimino4_11_12
    #new_values=[]
    new_values=trimino1_values_11_12+trimino2_values_11_12+trimino3_values_11_12+trimino4_values_11_12
    new_keys=trimino1_keys_11_12+trimino2_keys_11_12+trimino3_keys_11_12+trimino4_keys_11_12



    fig1, ax1 = plt.subplots()
    wedges,texts,autotexts= ax1.pie(new_values, labels=new_keys, autopct='%1.2f%%',shadow=False, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax1.set_title("Aφίξεις τουριστών στην Ελλάδα ανά τρίμηνο 2011-2012")
    ax1.legend(wedges, new_values_temp,
              title="Τουρίστες 2011-2012",
              loc="center right",
              bbox_to_anchor=(0.8, 0.3, 0.3 , 0.4))
    plt.show()

my_pie_chart_2011_2012(dictionary_touristes_trimino1_11_12,dictionary_touristes_trimino2_11_12,dictionary_touristes_trimino3_11_12,dictionary_touristes_trimino4_11_12)#,dictionary_touristes_trimino1_13_14,df_trimino2_13_14,dictionary_touristes_trimino3_13_14,df_trimino4_13_14)

#definition of function my pie chart
def my_pie_chart_2013_2014(dictionary_touristes_trimino1_13_14,df_trimino2_13_14,dictionary_touristes_trimino3_13_14,df_trimino4_13_14):
    trimino1_keys_13_14 = list(dictionary_touristes_trimino1_13_14.keys())
    trimino1_values_13_14 = list(dictionary_touristes_trimino1_13_14.values())
    trimino2_keys_13_14 = list(dictionary_touristes_trimino2_13_14.keys())
    trimino2_values_13_14 = list(dictionary_touristes_trimino2_13_14.values())
    trimino3_keys_13_14 = list(dictionary_touristes_trimino3_13_14.keys())
    trimino3_values_13_14 = list(dictionary_touristes_trimino3_13_14.values())
    trimino4_keys_13_14 = list(dictionary_touristes_trimino4_13_14.keys())
    trimino4_values_13_14 = list(dictionary_touristes_trimino4_13_14.values())

    values_temp_trimino1_13_14=[]
    for i,v in enumerate(trimino1_values_13_14):
        if i==0:
            values_temp_trimino1_13_14.append( str(v) + " = Πρώτο τρίμηνο του 2013 ")
        elif i==1:
            values_temp_trimino1_13_14.append( str(v) + " = Πρώτο τρίμηνο του 2014 ")
            print(values_temp_trimino1_13_14)

    values_temp_trimino2_13_14=[]
    for i,v in enumerate(trimino2_values_13_14):
        if i==0:
            values_temp_trimino2_13_14.append( str(v) + " = Δεύτερο τρίμηνο του 2013 ")
        elif i==1:
            values_temp_trimino2_13_14.append( str(v) + " = Δεύτερο τρίμηνο του 2014 ")
            print(values_temp_trimino2_13_14)

    values_temp_trimino3_13_14=[]
    for i,v in enumerate(trimino3_values_13_14):
        if i==0:
            values_temp_trimino3_13_14.append( str(v) + " = Τρίτο τρίμηνο του 2013 ")
        elif i==1:
            values_temp_trimino3_13_14.append( str(v) + " = Τρίτο τρίμηνο του 2014 ")
            print(values_temp_trimino3_13_14)

    values_temp_trimino4_13_14=[]
    for i,v in enumerate(trimino4_values_13_14):
        if i==0:
            values_temp_trimino4_13_14.append( str(v) + " = Τέταρτο τρίμηνο του 2013 ")
        elif i==1:
            values_temp_trimino4_13_14.append( str(v) + " = Τέταρτο τρίμηνο του 2014 ")
            print(values_temp_trimino4_13_14)
    
    #new_values_temp=[]
    new_values_temp=values_temp_trimino1_13_14+values_temp_trimino2_13_14+values_temp_trimino3_13_14+values_temp_trimino4_13_14
    #new_values=[]
    new_values=trimino1_values_13_14+trimino2_values_13_14+trimino3_values_13_14+trimino4_values_13_14
    new_keys=trimino1_keys_13_14+trimino2_keys_13_14+trimino3_keys_13_14+trimino4_keys_13_14   



    fig1, ax1 = plt.subplots()
    wedges,texts,autotexts= ax1.pie(new_values, labels=new_keys, autopct='%1.2f%%',shadow=False, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax1.set_title("Aφίξεις τουριστών στην Ελλάδα ανά τρίμηνο 2013-2014")
    ax1.legend(wedges, new_values_temp,
              title="Τουρίστες 2013-2014",
              loc="center right",
              bbox_to_anchor=(0.8, 0.3, 0.3 , 0.4))
    plt.show()

my_pie_chart_2013_2014(dictionary_touristes_trimino1_13_14,df_trimino2_13_14,dictionary_touristes_trimino3_13_14,df_trimino4_13_14)

#definition of function my pie chart
def my_pie_chart_2015(dictionary_touristes_trimino1_15,df_trimino2_15,dictionary_touristes_trimino3_15,df_trimino4_15):
    trimino1_keys_15 = list(dictionary_touristes_trimino1_15.keys())
    trimino1_values_15 = list(dictionary_touristes_trimino1_15.values())
    trimino2_keys_15 = list(dictionary_touristes_trimino2_15.keys())
    trimino2_values_15 = list(dictionary_touristes_trimino2_15.values())
    trimino3_keys_15 = list(dictionary_touristes_trimino3_15.keys())
    trimino3_values_15 = list(dictionary_touristes_trimino3_15.values())
    trimino4_keys_15 = list(dictionary_touristes_trimino4_15.keys())
    trimino4_values_15 = list(dictionary_touristes_trimino4_15.values())

    values_temp_trimino1_15=[]
    for i,v in enumerate(trimino1_values_15):
        if i==0:
            values_temp_trimino1_15.append( str(v) + " = Πρώτο τρίμηνο του 2015")
            print(values_temp_trimino1_15)
       
    values_temp_trimino2_15=[]
    for i,v in enumerate(trimino2_values_15):
        if i==0:
            values_temp_trimino2_15.append( str(v) + " = Δεύτερο τρίμηνο του 2015")
            print(values_temp_trimino2_15)
        
    values_temp_trimino3_15=[]
    for i,v in enumerate(trimino3_values_15):
        if i==0:
            values_temp_trimino3_15.append( str(v) + " = Τρίτο τρίμηνο του 2015")
            print(values_temp_trimino3_15)
       
    values_temp_trimino4_15=[]
    for i,v in enumerate(trimino4_values_15):
        if i==0:
            values_temp_trimino4_15.append( str(v) + " = Τέταρτο τρίμηνο του 2015")
            print(values_temp_trimino4_15)
          
    #new_values_temp=[]
    new_values_temp=values_temp_trimino1_15+values_temp_trimino2_15+values_temp_trimino3_15+values_temp_trimino4_15
    #new_values=[]
    new_values=trimino1_values_15+trimino2_values_15+trimino3_values_15+trimino4_values_15
    new_keys=trimino1_keys_15+trimino2_keys_15+trimino3_keys_15+trimino4_keys_15   



    fig1, ax1 = plt.subplots()
    wedges,texts,autotexts= ax1.pie(new_values, labels=new_keys, autopct='%1.2f%%',shadow=False, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax1.set_title("Aφίξεις τουριστών στην Ελλάδα ανά τρίμηνο 2015")
    ax1.legend(wedges, new_values_temp,
              title="Τουρίστες 2015",
              loc="center right",
              bbox_to_anchor=(0.5, 0.1, 0.5 , 0.1))
    plt.show()

my_pie_chart_2015(dictionary_touristes_trimino1_15,df_trimino2_15,dictionary_touristes_trimino3_15,df_trimino4_15)

# EXPORT TO CSV
###################################################################################################
#keys & values of the dictionary
new_list_touristwn=[]
trimino1_keys_11_12 = list(dictionary_touristes_trimino1_11_12.keys())
trimino1_values_11_12 = list(dictionary_touristes_trimino1_11_12.values())
trimino2_keys_11_12 = list(dictionary_touristes_trimino2_11_12.keys())
trimino2_values_11_12 = list(dictionary_touristes_trimino2_11_12.values())
trimino3_keys_11_12 = list(dictionary_touristes_trimino3_11_12.keys())
trimino3_values_11_12 = list(dictionary_touristes_trimino3_11_12.values())
trimino4_keys_11_12 = list(dictionary_touristes_trimino4_11_12.keys())
trimino4_values_11_12 = list(dictionary_touristes_trimino4_11_12.values())
trimino1_keys_13_14 = list(dictionary_touristes_trimino1_13_14.keys())
trimino1_values_13_14 = list(dictionary_touristes_trimino1_13_14.values())
trimino2_keys_13_14 = list(dictionary_touristes_trimino2_13_14.keys())
trimino2_values_13_14 = list(dictionary_touristes_trimino2_13_14.values())
trimino3_keys_13_14 = list(dictionary_touristes_trimino3_13_14.keys())
trimino3_values_13_14 = list(dictionary_touristes_trimino3_13_14.values())
trimino4_keys_13_14 = list(dictionary_touristes_trimino4_13_14.keys())
trimino4_values_13_14 = list(dictionary_touristes_trimino4_13_14.values())
trimino1_keys_15 = list(dictionary_touristes_trimino1_15.keys())
trimino1_values_15 = list(dictionary_touristes_trimino1_15.values())
trimino2_keys_15 = list(dictionary_touristes_trimino2_15.keys())
trimino2_values_15 = list(dictionary_touristes_trimino2_15.values())
trimino3_keys_15 = list(dictionary_touristes_trimino3_15.keys())
trimino3_values_15 = list(dictionary_touristes_trimino3_15.values())
trimino4_keys_15 = list(dictionary_touristes_trimino4_15.keys())
trimino4_values_15 = list(dictionary_touristes_trimino4_15.values())
new_list_touristwn=trimino1_keys_11_12+trimino2_keys_11_12+trimino3_keys_11_12+trimino4_keys_11_12+trimino1_keys_13_14+trimino2_keys_13_14+trimino3_keys_13_14+trimino4_keys_13_14+trimino1_keys_15+trimino2_keys_15+trimino3_keys_15+trimino4_keys_15
new_list_touristwn=trimino1_values_11_12+trimino2_values_11_12+trimino3_values_11_12+trimino4_values_11_12+trimino1_values_13_14+trimino2_values_13_14+trimino3_values_13_14+trimino4_values_13_14+trimino1_values_15+trimino2_values_15+trimino3_values_15+trimino4_values_15

#creating a dataframe to export to csv
export_df=pd.DataFrame([new_list_touristwn])
export_df.to_csv('./Αφίξεις_τουριστών_ανά_τρίμηνο_2011-15.csv', index = None, header=True)

#USE MYSQL
###################################################################################################
import mysql.connector

trimino1_keys_11_12 = list(dictionary_touristes_trimino1_11_12.keys())
trimino1_values_11_12 = list(dictionary_touristes_trimino1_11_12.values())
trimino2_keys_11_12 = list(dictionary_touristes_trimino2_11_12.keys())
trimino2_values_11_12 = list(dictionary_touristes_trimino2_11_12.values())
trimino3_keys_11_12 = list(dictionary_touristes_trimino3_11_12.keys())
trimino3_values_11_12 = list(dictionary_touristes_trimino3_11_12.values())
trimino4_keys_11_12 = list(dictionary_touristes_trimino4_11_12.keys())
trimino4_values_11_12 = list(dictionary_touristes_trimino4_11_12.values())
trimino1_keys_13_14 = list(dictionary_touristes_trimino1_13_14.keys())
trimino1_values_13_14 = list(dictionary_touristes_trimino1_13_14.values())
trimino2_keys_13_14 = list(dictionary_touristes_trimino2_13_14.keys())
trimino2_values_13_14 = list(dictionary_touristes_trimino2_13_14.values())
trimino3_keys_13_14 = list(dictionary_touristes_trimino3_13_14.keys())
trimino3_values_13_14 = list(dictionary_touristes_trimino3_13_14.values())
trimino4_keys_13_14 = list(dictionary_touristes_trimino4_13_14.keys())
trimino4_values_13_14 = list(dictionary_touristes_trimino4_13_14.values())
trimino1_keys_15 = list(dictionary_touristes_trimino1_15.keys())
trimino1_values_15 = list(dictionary_touristes_trimino1_15.values())
trimino2_keys_15 = list(dictionary_touristes_trimino2_15.keys())
trimino2_values_15 = list(dictionary_touristes_trimino2_15.values())
trimino3_keys_15 = list(dictionary_touristes_trimino3_15.keys())
trimino3_values_15 = list(dictionary_touristes_trimino3_15.values())
trimino4_keys_15 = list(dictionary_touristes_trimino4_15.keys())
trimino4_values_15 = list(dictionary_touristes_trimino4_15.values())

mydb = mysql.connector.connect(
  host="localhost",
  user="marios",
  passwd="morfopoulos",#123
  database="MM"
)

mycursor = mydb.cursor()
sql_2 = "CREATE TABLE IF NOT EXISTS ANA_TRIMINO (id INT AUTO_INCREMENT PRIMARY KEY, trimino VARCHAR(255), number INT)"
mycursor.execute(sql_2)

mySql_insert_query1 = """INSERT INTO ANA_TRIMINO (id, trimino, number)
                       VALUES
                       (1, +'Prwto trimino tou 2015', 1728421) """

mySql_insert_query2 = """INSERT INTO ANA_TRIMINO (id, trimino, number)
                       VALUES
                       (2, +'Deutero trimino tou 2015', 7565697) """

mySql_insert_query3 = """INSERT INTO ANA_TRIMINO (id, trimino, number)
                       VALUES
                       (3, +'Trito trimino tou 2015', 20617417) """

mySql_insert_query4 = """INSERT INTO ANA_TRIMINO (id, trimino, number)
                       VALUES
                       (4, +'Tetarto trimino tou 2015', 23599455) """


mycursor.execute(mySql_insert_query1)
mycursor.execute(mySql_insert_query2)
mycursor.execute(mySql_insert_query3)
mycursor.execute(mySql_insert_query4)


mydb.commit()
print(mycursor.rowcount, "Record inserted successfully into Laptop table")
mydb.close()
    

    
    








