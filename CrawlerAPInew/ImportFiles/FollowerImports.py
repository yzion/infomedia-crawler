'''
@Created on 27 december 2015

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
BASE_DIR = os.getcwd()
#followersFolder = BASE_DIR+"\\newCrawler\\follower"
followersFolder = BASE_DIR+"/newCrawler/follower"

#open local file
with open(join(followersFolder,"local_hcl_file.txt"),'r') as follower_local_hcl_file:
    follower_local_hcl_JsonFile = hcl.load(follower_local_hcl_file)
#open global file
with open(join(followersFolder,"global_hcl_file.txt"),'r') as follower_global_hcl_file:
    follower_global_hcl_JsonFile = hcl.load(follower_global_hcl_file)
   # str = "runTimeMinutes"
  # print follower_global_hcl_JsonFile["Run_details"]["function_parameters"].pop(str)
'''
         API area
'''
'''     LOCAL     API         '''
def getOSName():
    return  follower_local_hcl_JsonFile["Os_name"]

def getBrowserName():
    return  follower_local_hcl_JsonFile["Browser_name"]

def getDBPath():
    return  follower_local_hcl_JsonFile["DB_path"]

def getAplicationName():
    return  follower_local_hcl_JsonFile["Aplication_name"]

def getUserDetails():
    return  getUserName() , getUserPassword()

def getUserName():
    return  follower_local_hcl_JsonFile["User_details"]["userName"]
def getUserPassword():
    return   follower_local_hcl_JsonFile["User_details"]["password"]



def getTsharkPath():
    return  follower_local_hcl_JsonFile["Tshark_parameters"]["Tshark_path"]

def getTsharkNCInterface():
    return  follower_local_hcl_JsonFile["Tshark_parameters"]["NC_interface"] , follower_local_hcl_JsonFile["Tshark_parameters"]["NC_interface_data"]

def getTsharkWriteCommand():
    return  follower_local_hcl_JsonFile["Tshark_parameters"]["write_file_type"]


'''     GLOBAL     API         '''
def getTweetType():
    return  follower_global_hcl_JsonFile["Run_details"]["function_name"]

def getFunctionParameters(i):
    return  follower_global_hcl_JsonFile["Run_details"]["function_parameters"]["param"+`i`]

def getFunctionParametersByKey(key):
 return  follower_global_hcl_JsonFile["Run_details"]["function_parameters"].pop(key)


def paramLength():
    return  len(follower_global_hcl_JsonFile["Run_details"]["function_parameters"])

def getTsharkFileFullCommand():
    return  getTsharkFileCommand() ,getTsharkFileType()

def getTsharkFileCommand():
    return  follower_global_hcl_JsonFile["Run_details"]["Tshark_parameters"]["file_command"]

def getTsharkFileType():
    return  follower_global_hcl_JsonFile["Run_details"]["Tshark_parameters"]["file_type"]

def getTsharkFilterFullCommand():
    return  getTsharkFilterCommand() ,getTsharkFilterType()

def getTsharkFilterCommand():
    return  follower_global_hcl_JsonFile["Run_details"]["Tshark_parameters"]["filter_command"]

def getTsharkFilterType():
    return  follower_global_hcl_JsonFile["Run_details"]["Tshark_parameters"]["filter_type"]

def getFileNameFormat():
    return  follower_global_hcl_JsonFile["Run_details"]["Tshark_parameters"]["filter_type"]

def gettsharkCallNoFileName():
    return  getTsharkPath(),getTsharkFileFullCommand() ,  getTsharkFilterFullCommand() , getTsharkNCInterface(), getTsharkWriteCommand()

def getTsharkParameters():
    return follower_global_hcl_JsonFile["Run_details"]["Tshark_parameters"]
