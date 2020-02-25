import sys
import time
import random
import datetime
import telepot
import keras
from keras.models import Sequential
from keras.layers import Dense
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#training data
dataset = pd.read_csv('data-question.csv',header=None,sep='\t')
dataset1 = pd.read_csv('data-answer.csv',header=None,sep='\t')
x = dataset.iloc[:,1].values
y = dataset.iloc[:,0].values


shirt    = pd.read_csv('Shirt.csv',header=None,sep='\t')
phant    = pd.read_csv('phant.csv',header=None,sep='\t')
belt     = pd.read_csv('belt.csv',header=None,sep='\t')
wallet   = pd.read_csv('wallet.csv',header=None,sep='\t')
watches  = pd.read_csv('watches.csv',header=None,sep='\t')

shirt    = shirt.iloc[:,:].values
phant    = phant.iloc[:,:].values
belt     = belt.iloc[:,:].values
wallet   = wallet.iloc[:,:].values
watches  = watches.iloc[:,:].values


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

model = Sequential()
model.add(Dense(units = 800, activation = 'relu', input_dim = a))
model.add(Dense(units = 1000, activation = 'relu'))
model.add(Dense(units = b, activation = 'softmax'))
model.compile(optimizer = 'adam', loss = 'sparse_categorical_crossentropy', metrics = ['accuracy'])

model.fit(X,y, batch_size = 32, epochs = 10)


def bot_session(message):        
   
    ip = message
    ip_1=np.append(ip,1)
    x1 = cv.transform(ip_1).toarray()
    pred = model.predict_classes(x1)
    pred = pred[0]-1
    op = str(dataset1.iloc[pred,1])
    if ip == 'quit' or ip == 'Quit':
        op = 'bye'   
    return op

def write_function(msg,reply):
    
    date_time = datetime.datetime.now()
    file = open('conversation.csv.csv','a') 
    file.write("\n")
    file.write(str(date_time))
    file.write("\t")
    file.write('FNAME: '+msg['chat']['first_name'])
    file.write("\t")
    file.write('LNAME: '+msg['chat']['last_name'])
    file.write("\t")
    file.write('INPUT TEXT: '+msg['text'])
    file.write("\t")
    file.write("BOT REPLY: "+reply)
    file.close()
    

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    message = str(command)
    print ('Got command: %s' % message)
    print(msg)
    if message == 'Picture':
#       bot.sendPhoto(chat_id, 'https://www.instagram.com/p/B88W3Krp18A/')
        reply = 'To view more about this.. click the below link'
        bot.sendMessage(chat_id, reply)
        reply = 'https://www.instagram.com/p/B88W3Krp18A/'
        bot.sendMessage(chat_id, reply)
    else:
        reply = bot_session(message)
        bot.sendMessage(chat_id, reply)
    write_function(msg,reply)





bot = telepot.Bot('1070030315:AAG46yVpnlqNMQ4W3Z1g_iYFmtpSJEe1eY0')

first_init = 'hi'
first_init=np.append(first_init,1)
x1=cv.transform(first_init).toarray()
pred=model.predict_classes(x1)

counter = 0 
bot.message_loop(handle)



 