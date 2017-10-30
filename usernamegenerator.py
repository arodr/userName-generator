import time
import random
def get_username(fname,lname):
    return fname[:1]+lname[:4]
def get_pass(lname,passw):
    return lname[:4]+passw[:1:-1]
fname=input('Enter your first name :')
lname=input('Enter your last name : ')
passw=input('Enter your birthyear :')
print ('User Name :'+get_username(fname,lname))
print ('{}'.format(fname.title())+'\'s password :{}'.format(get_pass(lname,passw)))

#if __name__=='__main__':
#    main()

def cat_pass(passw):
    return passw[:1:-1]
def show_usefname(fname):
    return fname[:1]
def show_uselname(lname):
    return lname[:4]
user_lst={}
fname = input(str('Enter your first name :'))
print('\t*'+fname.title())
lname= input(str('Enter your last name :'))
print('\t*'+lname.title())
passw=input('Plese enteryour birthyear :')
print('\t*'+passw.title())
print(fname.title()+'\'s user name is:{}'.format(show_usefname(fname))+'{}'.format(show_uselname(lname)))
print(fname.title()+'\'s password is :{}'.format(show_uselname(lname))+'{}'.format(cat_pass(passw)))
