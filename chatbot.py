#installations required
'''pip install beautifulsoup4
pip install google
pip install wikipedia
pip install googletrans
pip install PyDictionary
install keras also
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#training data
dataset = pd.read_csv('data-question.csv',header=None,sep='\t')
dataset1 = pd.read_csv('data-answer.csv',header=None,sep='\t')
x = dataset.iloc[:,1].values
y = dataset.iloc[:,0].values
#countvectorizer
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer()
X = cv.fit_transform(x).toarray()

from sklearn.feature_extraction.text import TfidfVectorizer
tfidf = TfidfVectorizer()
X = tfidf.fit_transform(x).toarray()


a=len(X[1])
b=len(y)
b=b+1
#model starts
import keras
from keras.models import Sequential
from keras.layers import Dense

model = Sequential()
model.add(Dense(units = 800, activation = 'relu', input_dim = a))
model.add(Dense(units = 1000, activation = 'relu'))
model.add(Dense(units = b, activation = 'softmax'))
model.compile(optimizer = 'adam', loss = 'sparse_categorical_crossentropy', metrics = ['accuracy'])

model.fit(X,y, batch_size = 32, epochs = 50)

import wikipedia
from googlesearch import search 
import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")

print('\n')
print('Bot: Welcome Madhu Manivannan..,i am here to help you')
speak.Speak('Welcome Madhu Manivannan..,i am here to help you')
print('Bot: Type "Quit" to stop ')
speak.Speak('Type "Quit" to stop ')
     
while True:
#welcome block    
    ip = input('Madhu:')
#google block    
    if ('google' in ip) or ('Google' in ip): 
        
        print ('Bot: You are Now inside Google session:')
        speak.Speak('You are Now inside Google session:')
        speak.Speak('Please enter search word:')
        google = input('Bot: Please enter search word:')
        if google == 'quit' or ip == 'Quit':
            print('Bot: Bye')
            speak.Speak('Bye')
            break; 
        result=[]
        for i in search(google, tld="com", stop=2): 
            result.append(i)
        speak.Speak('Please check your default browser,if you are not satisfied with result try some different keyword')    
        print('Bot: Please check your default browser,if you are not satisfied with result try some different keyword')    
        for i in range(0,2):
                import webbrowser
                webbrowser.open(result[i])
#wikipedia block    
    elif ('wiki' in ip) or ('Wiki' in ip) or ('Wikipedia' in ip) or ('wikipedia' in ip):
        
        print ('Bot: You are Now inside Wiki session:')
        speak.Speak('You are Now inside Wiki session:')
        speak.Speak('Please enter search word:')
        wiki = input('Bot: Please enter search word:')
        if wiki == 'quit' or ip == 'Quit':
            print('Bot: Bye')
            speak.Speak('Bye')
            break; 
        print('Bot:'+ wikipedia.summary(wiki,sentences=10))
        speak.Speak(wikipedia.summary(wiki,sentences=2))
#translator
    elif ('translate' in ip) or ('Translate' in ip):
        
        from googletrans import Translator
        translator = Translator()
        speak.Speak('Please enter text to translate:')
        tran = input('Bot: Please enter text to translate: ' )
        speak.Speak('please enter destination language:')
        lang = input('Bot: please enter destination language: ')
        
        
        trans = translator.translate(tran,dest=lang)
        print('Bot: '+trans.text)
        speak.Speak(trans.text)
#dictionary
    elif ('dict' in ip) or ('Dict' in ip) or ('dictionary' in ip) or ('Dictionary' in ip):
        
        from PyDictionary import PyDictionary
        dictionary=PyDictionary()
        speak.Speak('Please enter the word:')
        find = input('Bot: Please enter the word: ')
        print ('Bot: ',dictionary.meaning(find))
        speak.Speak(dictionary.meaning(find))  
    
    
    else:
        ip_1=np.append(ip,1)
        x1 = cv.transform(ip_1).toarray()
        pred = model.predict_classes(x1)
        pred = pred[0]-1
        op = str(dataset1.iloc[pred,1])
        print('Bot: '+op)
        speak.Speak(op)
        
    
    if ip == 'quit' or ip == 'Quit':
        print('Bot: Bye')
        speak.Speak('Bye')
        break;   
      
#end -------------------------------------------------------------------
get = input('Enter:')

get=np.append(get,1)
x1=cv.transform(get).toarray()

pred=model.predict_classes(x1)
pred = pred[0]-1
print(str(dataset1.iloc[pred,1]))

pred=classifier.predict(x1)

pred=sorted(pred[0], key=pred[0].get, reverse=True)[:3]


