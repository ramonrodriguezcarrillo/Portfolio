#!/usr/bin/env python
# coding: utf-8

# # Comparing the leaders of online payments: PayPal and Square

# In[183]:


import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')
from pandas.plotting import scatter_matrix
import pandas as pd


# # Importing data from Yahoo Finance

# In[184]:


# Looking at data in a 6 month time frame
start = datetime.datetime(2020,8,9)
end = datetime.datetime(2021,2,9)


# In[185]:


paypal = web.DataReader('PYPL', 'yahoo', start, end)


# In[186]:


paypal.head()


# In[187]:


paypal.tail()


# In[188]:


paypal['Open'].plot(label = 'PYPL Open', figsize=(15,5))
paypal['Close'].plot(label = 'PYPL Close')
paypal['High'].plot(label='PYPL High')
paypal['Low'].plot(label='PYPL Low')
plt.legend()
plt.title('Paypal Stock Prices')
plt.ylabel('Price')
plt.show()


# In[189]:


paypal['Volume'].plot(figsize=(17,5))
plt.title('Paypal Volume')
plt.ylabel('Volume')
plt.show()


# In[190]:


square = web.DataReader('SQ', 'yahoo', start, end)


# In[191]:


paypal.to_csv('paypal.csv')
square.to_csv('square.csv')


# In[192]:


square.tail()


# In[193]:


square['Open'].plot(label = 'SQ Open', figsize=(15,5))
square['Close'].plot(label = 'SQ Close')
square['High'].plot(label='SQ High')
square['Low'].plot(label='SQ Low')
plt.legend()
plt.title('Square Stock Prices')
plt.ylabel('Price')
plt.show()


# In[194]:


square['Volume'].plot(figsize=(17,5))
plt.title('Square Volume')
plt.ylabel('Volume')
plt.show()


# # Comparing PayPal to Square: Stock Price and Volume

# In[195]:


paypal['Open'].plot(label='PYPL', figsize=(15,5))
square['Open'].plot(label='SQ')
plt.ylabel("Stock Price")
plt.title('PayPal vs Square Stock Price')
plt.legend()


# In[196]:


paypal['Volume'].plot(label='PYPL', figsize=(15,5))
square['Volume'].plot(label='SQ')
plt.title('PayPal vs Square Volume')
plt.ylabel('Volume')


# In[197]:


# Highest volume date
paypal.iloc[[paypal['Volume'].argmax()]]


# In[198]:



square.iloc[[square['Volume'].argmax()]]


# In[199]:


# Stock prices of both companies look very similar. We will confirm a relationship later on in this analysis


# #  Comparing PayPal to Square: Moving Average

# In[200]:


paypal['Open'].plot(label='Open', figsize=(15,10))
paypal['MA5'] = paypal['Open'].rolling(5).mean()
paypal['MA5'].plot(label='MA5') 
plt.legend()
plt.title('Paypal Moving Average')


# In[201]:


square['Open'].plot(label='Open', figsize=(15,10))
square['MA5'] = square['Open'].rolling(5).mean()
square['MA5'].plot(label='MA2')
plt.legend()
plt.title('Square Moving Average')


# In[202]:


# Even their moving averages look very similar and are equally as smooth


# # Correlation between PayPal and Square

# In[203]:


payment_industry = pd.concat([paypal['Open'], square['Open']], axis=1)
payment_industry.columns = ['Paypal Open', 'Square Open']


# In[204]:


scatter_matrix(payment_industry, figsize=(7,7), hist_kwds={'bins':35})


# In[219]:


# From this matrix we can see that as Paypal stock gets higher so does Square stock, vice versa.


# # Daily Percentage Change

# In[206]:


paypal['Returns'] = (paypal['Close']/paypal['Close'].shift(1)) - 1 


# In[207]:


paypal.head()


# In[208]:


square['Returns'] = (square['Close']/square['Close'].shift(1)) - 1 


# In[209]:


square.head()


# In[210]:


paypal['Returns'].hist(bins=30, label='PYPL', alpha= 0.5, figsize=(15,10))
square['Returns'].hist(bins=30, label='SQ', alpha=0.5)
plt.legend()
plt.title('Returns')


# In[211]:


paypal['Returns'].plot(kind='kde', label='PYPL', figsize=(15,10))
square['Returns'].plot(kind='kde', label='SQ')
plt.legend()
plt.title('Normalized Returns')


# In[212]:


box_df = pd.concat([paypal['Returns'], square['Returns']], axis=1)
box_df.columns = ['PYPL Returns', 'SQ Returns']
box_df.plot(kind='box', figsize=(15,5))


# In[213]:


scatter_matrix(box_df, figsize=(10,10), hist_kwds={'bins':50}, alpha=0.95)


# # Cumulative Return

# In[214]:


paypal['Cumulative Return'] = (1+paypal['Returns']).cumprod()
square['Cumulative Return'] = (1+square['Returns']).cumprod()


# In[215]:


paypal.tail()


# In[216]:


square.tail()


# In[217]:


paypal['Cumulative Return'].plot(label='PYPL', figsize=(15,10))
square['Cumulative Return'].plot(label='SQ')
plt.legend()
plt.title('PYPL vs SQ Cumulative Returns for 6 Months')


# In[218]:


# Square has had a higher cumulative return over PayPal. Squares cumulative return is 85% and PayPals is 47%. 


# # Summary: PayPal and Square are very similar stocks as seen by this analysis. This is because they make similar actions as corporations. They both are heavily invested in cryptocurrency. They have similar mobile apps (Venmo and CashApp). They both seen tremendous growth over the past 6 months. However, Square has almost doubled PayPals cumulative return in this time period
