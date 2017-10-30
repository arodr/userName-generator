import datetime
from datetime import date
import time
def get_username(fname,lname):
    return fname[:1]+lname[:4]
def get_pass(lname,passw):
    return lname[:4]+passw[:1:-1]
#def calculate_age(passw):
#    today = date.today()
#    return today.year - passw  #((today.month, today.day) < (born.month, born.day))
user_list={}
active=True
while active:
    fname=input('\nEnter your first name :')
    lname=input('Enter your last name : ')
    passw=input('Enter your birthyear :')
    user_list[fname]=lname
    print (fname.title()+'\'s User Name :'+get_username(fname,lname))
    print ('{}'.format(fname.title())+'\'s Password :{}'.format(get_pass(lname,passw)))
    if fname == '' or lname==''or passw== '':
        active=False
        print('Exiting ...')
    response=input('\nWould you like to add another user to database? (y/n) :')
    if response =='y' or response == '':
        pass
    elif response == 'n':
        print ('Printing Results')
        time.sleep(1)
        print ('\n\t---- Users ----')
        time.sleep(1)
        for fname, lname in user_list.items():
            print(fname.title()+' '+lname.title()+'.')
            #print ('\nAge : {}'.format(calculate_age(passw)))
            print('---')
