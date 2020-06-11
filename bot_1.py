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

dataset  = pd.read_csv('data-question.csv',header=None,sep='\t')
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
model.add(Dense(units = 500, activation = 'relu', input_dim = a))
model.add(Dense(units = 800, activation = 'relu'))
model.add(Dense(units = b+50, activation = 'softmax'))
model.compile(optimizer = 'adam', loss = 'sparse_categorical_crossentropy', metrics = ['accuracy'])

model.fit(X,y, batch_size = 20, epochs = 100)

#bot_session
def display_products(pred,chat_id,msg):
    
    if pred == 3:
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
 
    elif pred == 4:
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
 
    elif pred == 5:
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
 
    elif pred == 6:
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
 
    elif pred == 7:
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

def confirm_booking(chat_id,command,msg):

        status = ' '
        reply = str(command)
        for i in range(len(shirt)):
           if (str(shirt[i][0]) == str(command)):
            bot.sendMessage(chat_id, shirt[i][1])
            reply = 'Please enter your 10 digit mobile number to place the order'
            bot.sendMessage(chat_id, reply)
            write_function_confirmation(msg,reply)
            status = 'found'
        
        for i in range(len(phant)):

           if (str(phant[i][0]) == str(command)):
            bot.sendMessage(chat_id, phant[i][1])
            reply = 'Please enter your 10 digit mobile number to place the order'
            bot.sendMessage(chat_id, reply)
            write_function_confirmation(msg,reply)
            status = 'found'
 
 
        for i in range(len(belt)):
           if (str(belt[i][0]) == str(command)):
            bot.sendMessage(chat_id, belt[i][1])
            reply = 'Please enter your 10 digit mobile number to place the order'
            bot.sendMessage(chat_id, reply)
            write_function_confirmation(msg,reply)
            status = 'found'
 
 
        for i in range(len(wallet)):
           if (str(wallet[i][0]) == str(command)):
            bot.sendMessage(chat_id, wallet[i][1])
            reply = 'Please enter your 10 digit mobile number to place the order'
            bot.sendMessage(chat_id, reply)
            write_function_confirmation(msg,reply)
            status = 'found'
 
  
        for i in range(len(watch)):
           if (str(watch[i][0]) == str(command)):
            bot.sendMessage(chat_id, watch[i][1])
            reply = 'Please enter your 10 digit mobile number to place the order'
            bot.sendMessage(chat_id, reply)
            write_function_confirmation(msg,reply)
            status = 'found'
            
        if status == ' ':
            reply = 'Sorry for inconvinence...:( '
            bot.sendMessage(chat_id, reply)  
            reply = 'We are not able to find this Product number in our Database..'
            bot.sendMessage(chat_id, reply)  
            reply = 'Please try again... :)'
            bot.sendMessage(chat_id, reply)  
        else:
            date_time = datetime.datetime.now()
            file = open('temp.csv','w') 
            file.write(str(command))
            file.write("\t")
            file.close()
            
    
def bot_session(message,chat_id,msg ):        
      
        ip = message
        ip_1=np.append(ip,1)
        x1 = cv.transform(ip_1).toarray()
        pred = model.predict_classes(x1)
        pred = pred[0]
        reply = str(dataset1.iloc[pred,1])
        if ip == 'quit' or ip == 'Quit'or ip == 'bye' or ip == 'Bye':
            reply = 'bye.. Thanks for choosing dapper clobber'   
        bot.sendMessage(chat_id, reply)
        write_function(msg,reply)
        display_products(pred,chat_id,msg)

def write_function(msg,reply):
    
    date_time = datetime.datetime.now()
    file = open('conversation.csv','a') 
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
    
def write_report_chat_status(msg,req_id,prod_code):
 
    date_time = datetime.datetime.now()   
    file = open('confirmation_chat.csv','a') 
    file.write(str(req_id))
    file.write('\t')
    file.write(str(date_time))
    file.write("\t")
    file.write(str(msg['chat']['first_name']))
    file.write("\t")
    file.write(str(msg['chat']['last_name']))
    file.write("\t")
    file.write(str(prod_code))
    file.write("\t")
    file.write('Booking confirmed')
    file.write("\n")
    file.close()

def req_send_status(chat_id,request_temp):

    reply_temp = list(request_temp)
    reply = 'Order Date   : '+format(reply_temp[0])
    bot.sendMessage(chat_id, reply)
    reply = 'First Name   : '+format(reply_temp[1])
    bot.sendMessage(chat_id, reply)
    reply = 'Last Name    : '+format(reply_temp[2])
    bot.sendMessage(chat_id, reply)
    reply = 'Product Code : '+format(reply_temp[3])
    bot.sendMessage(chat_id, reply)          
    reply = 'Status       : '+format(reply_temp[4])
    bot.sendMessage(chat_id, reply)  
               
    
def handle(msg):
         
    
    chat_id = msg['chat']['id']
    command = msg['text']
 
    reply = command
    if command.isnumeric():
        if len(command) == 4 :
            date_time = datetime.datetime.now()   
            file = open('confirmation.csv','a') 
            file.write("\n")
            file.write(str(date_time))
            file.write("===========================================================")
            file.close()
            confirm_booking(chat_id,command,msg)
 
        elif len(command) == 10:
            write_function_confirmation(msg,reply) 
            bot.sendMessage(chat_id, reply)
            reply = 'Please Type "confirm" to use your number to contact you. :)'
            bot.sendMessage(chat_id, reply)
        elif len(command) >= 11:
            reply = 'Please Enter valid 10 digit mobile number'
            bot.sendMessage(chat_id, reply)
        elif len(command) ==6:
            request  = pd.read_csv('confirmation_chat.csv',header=None,sep='\t')
            req_x    = request.iloc[:,:1].values
            req_y    = request.iloc[:,1:].values
            req_found = ' '
            
            for i in range(len(req_x)):
               if str(req_x[i][0]) == command:
                  req_found = i

            if (req_found != ' '):
               reply = 'Below are the details for Request ID:{0}'.format(command)
               bot.sendMessage(chat_id, reply)
               request_temp = req_y[req_found]
               req_send_status(chat_id,request_temp)
            else:
               reply = 'REQUEST ID IS INVALID.. if you have further queries please enter mobile number.. our team will contact you asap'
               bot.sendMessage(chat_id, reply)               
        else:
            reply = 'you have entered {0} digit values which is invald'.format(len(command)) 
            bot.sendMessage(chat_id, reply)

    elif (command == 'Confirm'  or command == 'confirm' or command == 'CONFIRM'): 
        
        date_time = datetime.datetime.now()   
        file = open('confirmation.csv','a') 
        file.write("\n")
        file.write(str(date_time))
        file.write("=============================================================")
        file.close()
        temp_file  = pd.read_csv('temp.csv',header=None,sep='\t')
        prod_code = temp_file[0][0]
        
 #getting random number
        req_id    = random.randrange(100000,900000,1)
 #writing file for chat request
        write_report_chat_status(msg,req_id,prod_code)
        reply  = 'Please save this Request ID for future reference '
        bot.sendMessage(chat_id, reply)
        reply  = str(req_id)
        bot.sendMessage(chat_id, reply)
        reply  = 'Thanks for shopping, our sales team will contact you soon'
        bot.sendMessage(chat_id, reply)
 #writing confirmation report
        write_function_confirmation(msg,reply)
        reply = 'Happy shopping'
        bot.sendMessage(chat_id, reply)
    else:
        message = str(command)
        bot_session(message,chat_id,msg)
     
    date_time = datetime.datetime.now()   
    file = open('cache.csv','a') 
    file.write("\n")
    file.write(str(date_time))
    file.write("\t")
    file.write(str(msg))
    file.close()
 
     
     
        
bot = telepot.Bot('******************************************************')
first_init = 'hi'
first_init=np.append(first_init,1)
x1=cv.transform(first_init).toarray()
pred=model.predict_classes(x1)
bot.message_loop(handle)
