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
watch    = pd.read_csv('watches.csv',header=None,sep='\t')

shirt    = shirt.iloc[:,:].values
phant    = phant.iloc[:,:].values
belt     = belt.iloc[:,:].values
wallet   = wallet.iloc[:,:].values
watch    = watch.iloc[:,:].values


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

def display_products(pred,chat_id,msg):
    
    
    if pred == 2:
        for i in range(len(shirt)):
            bot.sendMessage(chat_id, shirt[i][1])
            reply = shirt[i][1]
            write_function(msg,reply)
            bot.sendMessage(chat_id, shirt[i][0])
            reply = str(shirt[i][0])
            write_function(msg,reply)
        else:
            reply = 'Please send me the number which is below the picture to buy'
            bot.sendMessage(chat_id, reply)
            write_function(msg,reply)
            recent = 'shirt'
    elif pred == 3:
        for i in range(len(phant)):
            bot.sendMessage(chat_id, phant[i][1])
            reply = phant[i][1]
            write_function(msg,reply)
            bot.sendMessage(chat_id, phant[i][0])
            reply = str(phant[i][0])
            write_function(msg,reply)
        else:
            reply = 'Please send me the number which is below the picture to buy'
            bot.sendMessage(chat_id, reply)
            write_function(msg,reply)
            recent = 'phant'
    elif pred == 4:
        for i in range(len(belt)):
            bot.sendMessage(chat_id, belt[i][1])
            reply = belt[i][1]
            write_function(msg,reply)
            bot.sendMessage(chat_id, belt[i][0])
            reply = str(belt[i][0])
            write_function(msg,reply)
        else:
            reply = 'Please send me the number which is below the picture to buy'
            bot.sendMessage(chat_id, reply)
            write_function(msg,reply)
            recent = 'belt'
    elif pred == 5:
        for i in range(len(wallet)):
            bot.sendMessage(chat_id, wallet[i][1])
            reply = wallet[i][1]
            write_function(msg,reply)
            bot.sendMessage(chat_id, wallet[i][0])
            reply = str(wallet[i][0])
            write_function(msg,reply)
        else:
            reply = 'Please send me the number which is below the picture to buy'
            bot.sendMessage(chat_id, reply)
            write_function(msg,reply)
            recent = 'wallet'
    elif pred == 6:
        for i in range(len(watch)):
            bot.sendMessage(chat_id, watch[i][1])
            reply = watch[i][1]
            write_function(msg,reply)
            bot.sendMessage(chat_id, watch[i][0])
            reply = str(watch[i][0])
            write_function(msg,reply)
        else:
            reply = 'Please send me the number which is below the picture to buy'
            bot.sendMessage(chat_id, reply)
            write_function(msg,reply)
            recent = 'watch'
    recent.append(recent)
    return recent

def confirm_booking(command,recent):

    if (recent[-1] == 'shirt':
        for i in shirt:
           if (shirt[i][0] == command):
            bot.sendMessage(chat_id, shirt[i][1])
            reply = 'Please type "confirm" to confirm the booking..'
            bot.sendMessage(chat_id, reply)
            
           else:
            reply = 'please enter valid number'
            bot.sendMessage(chat_id, reply)
        
    elif (recent[-1] == 'phant':
          for i in phant:
           if (phant[i][0] == command):
            bot.sendMessage(chat_id, phant[i][1])
            reply = 'Please type "confirm" to confirm the booking..'
            bot.sendMessage(chat_id, reply)
           else:
            reply = 'please enter valid number'
            bot.sendMessage(chat_id, reply)
    elif (recent[-1] == 'belt':
          for i in belt:
           if (belt[i][0] == command):
            bot.sendMessage(chat_id, belt[i][1])
            reply = 'Please type "confirm" to confirm the booking..'
            bot.sendMessage(chat_id, reply)
           else:
            reply = 'please enter valid number'
            bot.sendMessage(chat_id, reply)
    elif (recent[-1] == 'wallet':
          for i in wallet:
           if (wallet[i][0] == command):
            bot.sendMessage(chat_id, wallet[i][1])
            reply = 'Please type "confirm" to confirm the booking..'
            bot.sendMessage(chat_id, reply)
           else:
            reply = 'please enter valid number'
            bot.sendMessage(chat_id, reply)
    elif (recent[-1] == 'watch':
          for i in watch:
           if (watch[i][0] == command):
            bot.sendMessage(chat_id, watch[i][1])
            reply = 'Please type "confirm" to confirm the booking..'
            bot.sendMessage(chat_id, reply)
           else:
            reply = 'please enter valid number'
            bot.sendMessage(chat_id, reply)
     
    
def bot_session(message,chat_id,msg ):        
      
        ip = message
        ip_1=np.append(ip,1)
        x1 = cv.transform(ip_1).toarray()
        pred = model.predict_classes(x1)
        pred = pred[0]-1
        print(pred)
        reply = str(dataset1.iloc[pred,1])
        if ip == 'quit' or ip == 'Quit':
            reply = 'bye'   
        bot.sendMessage(chat_id, reply)
        write_function(msg,reply)
        recent = display_products(pred,chat_id,msg)
        return recent
        
          
          

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
    
def write_function_confirmation(msg,reply):

    date_time = datetime.datetime.now()   
    file = open('confirmation.csv','a') 
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
    
    if command.isnumeric():
       confirm_booking(command,recent)
    elif (command == 'Confirm'  or command == 'confirm' or command == 'CONFIRM'): 
        reply = 'Please send your contact number, our sales team will contact you soon'
        bot.sendMessage(chat_id, reply)
        write_function_confirmation(msg,reply)
        reply = 'Thanks for shopping in dapper colaber'
        bot.sendMessage(chat_id, reply)
    else:
        message = str(command)
        print ('Got command: %s' % message)
        print(msg)
        recent = bot_session(message,chat_id,msg)
        
        

        
    
recent = []
bot = telepot.Bot('1070030315:AAG46yVpnlqNMQ4W3Z1g_iYFmtpSJEe1eY0')
first_init = 'hi'
first_init=np.append(first_init,1)
x1=cv.transform(first_init).toarray()
pred=model.predict_classes(x1)
bot.message_loop(handle)



 
