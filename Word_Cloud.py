#!/usr/bin/env python
# coding: utf-8

# <h1>Final Project - Word Cloud</h1>

# For this project, you'll create a "word cloud" from a text by writing a script. This script needs to process the text, remove punctuation, ignore case and words that do not contain all alphabets, count the frequencies, and ignore uninteresting or irrelevant words. A dictionary is the output of the calculate_frequencies function. The wordcloud module will then generate the image from your dictionary.
# 
# For the input text of your script, you will need to provide a file that contains text only. For the text itself, you can copy and paste the contents of a website you like. Or you can use a site like Project Gutenberg to find books that are available online. You could see what word clouds you can get from famous books, like a Shakespeare play or a novel by Jane Austen. Save this as a .txt file somewhere on your computer.
# 
# Now you will need to upload your input file here so that your script will be able to process it. To do the upload, you will need an uploader widget. Run the following cell to perform all the installs and imports for your word cloud script and uploader widget. It may take a minute for all of this to run and there will be a lot of output messages. But, be patient. Once you get the following final line of output, the code is done executing. Then you can continue on with the rest of the instructions for this notebook.
# 

# In[2]:


# Here are all the installs and imports you will need for your word cloud script and uploader widget

get_ipython().system('pip install wordcloud')
get_ipython().system('pip install fileupload')
get_ipython().system('pip install ipywidgets')
get_ipython().system('jupyter nbextension install --py --user fileupload')
get_ipython().system('jupyter nbextension enable --py fileupload')

import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import fileupload
import io
import sys


# Whew! That was a lot. All of the installs and imports for your word cloud script and uploader widget have been completed.
# 
# IMPORTANT! If this was your first time running the above cell containing the installs and imports, you will need save this notebook now. Then under the File menu above, select Close and Halt. When the notebook has completely shut down, reopen it. This is the only way the necessary changes will take affect.
# 
# To upload your text file, run the following cell that contains all the code for a custom uploader widget. Once you run this cell, a "Browse" button should appear below it. Click this button and navigate the window to locate your saved text file.

# In[3]:


# This is the uploader widget

def _upload():

    _upload_widget = fileupload.FileUploadWidget()

    def _cb(change):
        global file_contents
        decoded = io.StringIO(change['owner'].data.decode('utf-8'))
        filename = change['owner'].filename
        print('Uploaded `{}` ({:.2f} kB)'.format(
            filename, len(decoded.read()) / 2 **10))
        file_contents = decoded.getvalue()

    _upload_widget.observe(_cb, names='data')
    display(_upload_widget)

_upload()


# The uploader widget saved the contents of your uploaded file into a string object named file_contents that your word cloud script can process. This was a lot of preliminary work, but you are now ready to begin your script.
# 
# Write a function in the cell below that iterates through the words in file_contents, removes punctuation, and counts the frequency of each word. Oh, and be sure to make it ignore word case, words that do not contain all alphabets and boring words like "and" or "the". Then use it in the generate_from_frequencies function to generate your very own word cloud!
# 
# Hint: Try storing the results of your iteration in a dictionary before passing them into wordcloud via the generate_from_frequencies function.

# In[4]:


def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my",     "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them",     "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being",     "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how",     "all", "any", "both", "each", "few", "more", "some", "such", "no", "not","nor", "too", "very", "can", "will", "just"]
    
    # LEARNER CODE START HERE
    import re

   
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    
    #Lower the words
    file_contents=file_contents.lower()
    file_contents_list = file_contents.split()
    len_uninteresting_words = len(uninteresting_words)
    file_contents_list_len  = len(file_contents_list )
    special_char=re.compile('[@_!$%^&*()''<>?/\|}{~:]#')

    #Remove special characters
    all_alpha=re.sub('[@_!#$%^&*()<>?/\|.}{~:]',"",file_contents)
    all_alpha2=""
    #alpha to lower
    all_alpha=all_alpha.lower()
    #change alpha to array
    all_alpha_list = all_alpha.split()

    new_alpha = [x for x in all_alpha_list if x.isalpha() == True]
    
    for c in uninteresting_words:
        for cw in uninteresting_words:
            #print(w)
            for i in range(0,len(new_alpha)):
                if new_alpha[i]==cw:
                    new_alpha[i]=''

    #Remove all leftover abbreviated word like he's --> he s
    new_alpha2 = [x for x in new_alpha if len(x) >= 3]

    #put final list in the dictionary
    word_dict = {}

    for i in new_alpha2:
        if i not in word_dict:
            word_dict[i] = 0
        word_dict[i]+=1
   
                
#print(test_split)
#print(a)
#print(type(a2))
#print(new_test_split_alpha)
#print(new_test_split_nonalpha)
#print(new_test_split_nonalpha2)
#print(new_test_split_alpha2)
#print(all_alpha)
#print(new_alpha)
#print(new_alpha2)
#print(word_dict)
#print(new_test_split_alpha2)
#h = "hey#$"
#if special_char.search(h) == None:
#        print("string has special char")
#else:
#        print("string does not have special char")
    
    #wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(word_dict)
    return cloud.to_array()


# In[ ]:





# In[5]:


# Display your wordcloud image
calculate_frequencies(file_contents)

myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()


# If your word cloud image did not appear, go back and rework your calculate_frequencies function until you get the desired output. Definitely check that you passed your frequecy count dictionary into the generate_from_frequencies function of wordcloud. Once you have correctly displayed your word cloud image, you are all done with this project. Nice work!
