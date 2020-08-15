#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Description: This is a chat bot program


# In[ ]:


#import the library


# In[1]:


from nltk.chat.util import Chat, reflections


# In[45]:


pairs = [
    [ "my name is (.*)", ["hi %1"]],
    ['(hi|hello|hey|holla)',['hey there', 'hi there', 'hayyy']],
    ['(.*) in (.*) is fun', ['%1 in %2 is indeed fun']],
    ['(.*)(location|ciy) ?', ['Tokyo, Japan']],
    ["(.*) created you", ['k gizo did']],
    ['how is the weather in (.*)',['the weather in %1 is nice']],
    ['who is beyonce',['Mama Africa'] ],
    ['(.*) your name?',['sal']]
]


# In[ ]:


chat = Chat(pairs, reflections)
chat._substitute('you are amazing')
#chat.converse()


# In[ ]:


#reflections is a dictionary that contains a set of input value with the corresponding output values


# In[8]:


reflections


# In[22]:


my_dummy_reflections = {
    'go' : 'gone',
    'hello': 'hey there'
}


# In[16]:


#chat = Chat(pairs, my_dummy_reflections)
#chat._substitute('go hello')
#chat.converse()


# In[ ]:


chat = Chat(pairs, my_dummy_reflections)
#chat._substitute('you are amazing')
chat.converse()


# In[ ]:





# In[ ]:




