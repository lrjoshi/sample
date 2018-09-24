
# coding: utf-8

# In[3]:


from datetime import datetime

now = datetime.now()

mm = str(now.month)

dd = str(now.day)

yyyy = str(now.year)

hour = str(now.hour)

mi = str(now.minute)

ss = str(now.second)

print (mm + "/" + dd + "/" + yyyy + " " + hour + ":" + mi + ":" + ss)

