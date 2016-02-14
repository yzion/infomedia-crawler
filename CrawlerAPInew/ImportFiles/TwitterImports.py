'''
Created on 29 dec 2015

@author: M


if __name__ == '__main__':
    pass
    
'''

import os
from os.path import join 

import hcl


'''
    local settings area
'''
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
twitterFolder = BASE_DIR+"\\newCrawler\\twitter"

#open local file 
##with open(join(twitterFolder,"local_hcl_file.txt"),'r') as twitter_local_hcl_file:
#  twitter_local_hcl_JsonFile = hcl.load(twitter_local_hcl_file)
#open global file  
with open(join(twitterFolder,"global_hcl_file.txt"),'r') as twitter_global_hcl_file:
    twitter_global_hcl_JsonFile = hcl.load(twitter_global_hcl_file)

  

'''
         API area
'''  
'''     GLOBAL     API         '''
def getOSName():
    return  twitter_global_hcl_JsonFile["Os_name"]

def getBrowserName():
    return  twitter_global_hcl_JsonFile["Browser_name"]

def getDBPath():
    return  twitter_global_hcl_JsonFile["DB_path"]

def getAplicationName():
    return  twitter_global_hcl_JsonFile["Aplication_name"]

def getUserDetails(i):
    return  getUserName(i) , getUserPassword(i)

def getNumOfUsers():
    return  len(twitter_global_hcl_JsonFile["User_details"])/2

def getUserName(i):
    return  twitter_global_hcl_JsonFile["User_details"]["userName"+`i`] 

def getUserPassword(i):
    return   twitter_global_hcl_JsonFile["User_details"]["password"+`i`]

def getTsharkPath():
    return  twitter_global_hcl_JsonFile["Tshark_parameters"]["Tshark_path"]

def getTsharkNCInterface():
    return  twitter_global_hcl_JsonFile["Tshark_parameters"]["NC_interface"] , twitter_global_hcl_JsonFile["Tshark_parameters"]["NC_interface_data"]

def getTsharkWriteCommand():
    return  twitter_global_hcl_JsonFile["Tshark_parameters"]["write_file_type"]
def getTsharkFileFullCommand():
    return  getTsharkFileCommand() ,getTsharkFileType()

def getTsharkFileCommand():
    return  twitter_global_hcl_JsonFile["Tshark_parameters"]["file_command"]

def getTsharkFileType():
    return  twitter_global_hcl_JsonFile["Tshark_parameters"]["file_type"]

def getTsharkFilterFullCommand():
    return  getTsharkFilterCommand() ,getTsharkFilterType()

def getTsharkFilterCommand():
    return  twitter_global_hcl_JsonFile["Tshark_parameters"]["filter_command"]

def getTsharkFilterType():
    return  twitter_global_hcl_JsonFile["Tshark_parameters"]["filter_type"]

def getFileNameFormat():
    return  twitter_global_hcl_JsonFile["Tshark_parameters"]["filter_type"]

def gettsharkCallNoFileName():
    return  getTsharkPath(),getTsharkFileFullCommand() ,  getTsharkFilterFullCommand() , getTsharkNCInterface(), getTsharkWriteCommand()

def getTweetType():
    return  twitter_global_hcl_JsonFile["Run_details"]["function_name"]

def getFunctionParameters(i):
    return  twitter_global_hcl_JsonFile["Run_details"]["function_parameters"]["param"+`i`]

def paramLength():
    return  len(twitter_global_hcl_JsonFile["Run_details"]["function_parameters"])


