#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd
import xgboost as xgb


# In[63]:


train_data_path = "/home/jovyan/work/data/phase1/train.csv"
validation_data_path = "/home/jovyan/work/data/phase1/validate.csv"


# In[62]:


train_df = pd.read_csv(train_data_path)
validation_df = pd.read_csv(validation_data_path)


# In[21]:


from sklearn.model_selection import GridSearchCV


# In[22]:


max_depth=2
min_child_weight=1


# In[33]:


x_train = train_df.drop("target", axis=1)
y_train = train_df["target"]


# In[34]:


max_depth = 1
min_child_weight = 0.1
learning_rate = 0.1
params = {"max_depath": max_depth, "min_child_weight": min_child_weight, "learning_rate": learning_rate}


# In[47]:


clf = xgb.XGBRegressor(max_depth=max_depth, min_child_weight=min_child_weight, learning_rate=learning_rate)


# In[48]:


xg_model = clf.fit(x_train, y_train)


# In[49]:


x_predict = validation_df.drop("target", axis=1)
y_predict = validation_df["target"]


# In[50]:


xg_model


# In[51]:


predict = xg_model.predict(x_predict)


# In[52]:


from sklearn.metrics import mean_squared_error


# In[53]:


metrics = mean_squared_error(predict, y_predict)


# In[65]:


prameter = xg_model.get_params()


# In[1]:


print("metrics: %f" % metrics)


# In[ ]:




