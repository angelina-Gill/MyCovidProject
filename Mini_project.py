#!/usr/bin/env python
# coding: utf-8

# In[33]:


import pandas as pd
import matplotlib.pyplot as plt


# In[37]:


df = pd.read_excel ('D:\python\Delhi2.xlsx')
print (df)


# In[37]:


from matplotlib import pyplot as plt
from matplotlib import style
style.use('ggplot')

x =[3,5,12,14,15,30]
y =[1330,1501,1647,3630,3390,2199]
plt.plot(x,y,'y',label='Delhi',linewidth=5)

plt.title('Delhi covid19 Report')
plt.ylabel('hospitalized ')
plt.xlabel('1st to 30th June2020')
plt.legend()
#plt.grid(true,color='k')
plt.show()


# In[40]:


from matplotlib import pyplot as plt
from matplotlib import style
style.use('ggplot')

x =[3,5,12,14,15,30]
y =[417,384,604,7725,3328,2113]

plt.plot(x,y,'g',label='Delhi',linewidth=5)
plt.title('Delhi covid19 Report')
plt.ylabel('Recovered')
plt.xlabel('1st to 30th June2020')
plt.legend()
#plt.grid(true,color='k')
plt.show()


# In[5]:


#Delhi covid19 Report (Deceased )


# In[39]:


from matplotlib import pyplot as plt
from matplotlib import style
style.use('ggplot')

x =[3,5,12,14,15,30]
y =[49,79,73,77,64,62]


plt.plot(x,y,'R',label='Delhi',linewidth=5)


plt.title('Delhi covid19 Report')
plt.ylabel('Deceased')
plt.xlabel('1st to 30th June2020')
plt.legend()
#plt.grid(true,color='k')
plt.show()


# In[41]:


from matplotlib import pyplot as plt
from matplotlib import style
style.use('ggplot')

x =[3,5,12,14,15,30]
y =[1330,1501,1647,3630,3390,2199]
plt.plot(x,y,'y',label='Hospitalized',linewidth=5)


x2 =[3,5,12,14,15,30]
y2 =[417,384,604,7725,3328,2113]
plt.plot(x2,y2,'G',label='Recovered',linewidth=5)

x3 =[3,5,12,14,15,30]
y3 =[49,79,73,77,64,62]
plt.plot(x3,y3,'R',label='Deceased',linewidth=5)


plt.title('Delhi covid19 Report')
plt.ylabel('Hospitalized_Recovered_Deceased',)
plt.xlabel('1st to 30th June2020')
plt.legend()

plt.show()


# In[19]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
census_data = pd.read_excel('D:\python\Delhi2.xlsx')
census_data.describe()


# In[31]:


census_data.info()


# In[52]:


sns.scatterplot(x ='Recovered',y = 'Deceased', data=census_data)


# In[51]:


import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel ('D:\python\statewisereport.xlsx')
print (df)


# In[ ]:




