#!/usr/bin/env python
# coding: utf-8

# # Tasks to Complete:

# 1. Clean listOfDrugs of punctuation, parentheses, brackets, numbers, period, 'mg', 'and', 'hr', 'mL'.. OR delete what is within parentheses
# 

# In[2]:


import pandas as pd

def read_excel(name):
    file = pd.ExcelFile(name)   ## Load the gas database
    dataframe= file.parse(file.sheet_names[0], header=0) # Parse the file, saving as our database
    return dataframe

df_drugs = read_excel("drugs.xlsx")
listOfDrugs = df_drugs.values.T[0].tolist()


# In[3]:


i = 0
for item in listOfDrugs:
    listOfDrugs[i] = item.replace(" ", "-")
    i += 1

new_list = listOfDrugs
new_list = [item.split("/") for item in new_list]
newer_list = []
for cell in new_list:
    for item in cell:
        newer_list.append(item)
repeats = 0

listOfDrugs = []
for item in newer_list:
    if item in listOfDrugs:
        repeats+= 1
    else:
        listOfDrugs.append(item)
        
len(listOfDrugs)


# In[4]:


import datetime
datetime.datetime.now()

x = datetime.datetime.now()


# In[ ]:


from my_functions import my_functions as mf

overflow = []
temp_image_list = []
final_image_list = []
failedListOfDrugs = [] 
baseUrl = "https://www.apexbt.com/"
word = '/struct/'
i =1
for item in listOfDrugs:
    if item not in overflow:
        try:        
            soup = mf.scrape(baseUrl + item + 'html')                       ############## + ".html")
            images = soup.findAll('img')
            for image in images:
                temp_image_list.append(image['src'])
            for temp_url in temp_image_list:
                if word in temp_url:
                    if temp_url not in final_image_list:
                        final_image_list.append(temp_url)
                        overflow.append(item)
        except:
            failedListOfDrugs.append(item)
        


    


# In[ ]:


"""thenames = []
baseUrl = "https://pubchem.ncbi.nlm.nih.gov/compound/"
for item in listOfDrugs:
    if item not in overflow:
            soup = mf.scrape(baseUrl + item)                       ############## + ".html")
            images = soup.findAll('img')
            names = soup.findAll('alt')
for name in names:
    thenames.append(name)
"""


# In[ ]:


y = datetime.datetime.now()
print(x)
print(y)


# In[ ]:


dr = str(len(listOfDrugs))
oh = str(len(overflow))
na = str(len(final_image_list))
ya = str(len(failedListOfDrugs))

print("There are " + dr + " elements in listOfDrugs." )
print("There are " + oh + " elements in overflow." )
print("There are " + na + " urls to scrape." )
print("There are " + ya + " elements that failed the scrape." )


# In[ ]:


i = 0
while i < len(final_image_list):
    mf.image_downloader(final_image_list[i], overflow[i], "image_pubchem/")
    i += 1


# In[ ]:





# In[ ]:




