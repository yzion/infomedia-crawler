import os
from os.path import join 

import hcl
import requests

BASE_DIR = os.getcwd()
twitterFolder = BASE_DIR+"/newCrawler/twitter"


r = requests.get('https://raw.githubusercontent.com/infomediaTeamCrawler/infomedia-crawler/dev/CrawlerAPInew/newCrawler/twitter/global_hcl_file.txt?token=AQtyeAl1nGZB55RL4BJ8t1Nxs9rMdHrDks5W3CyKwA%3D%3D' ,auth=('infomediaTeamCrawler', 'CrawlerTeam16'))

twitter_global_hcl_JsonFile = hcl.api.loads(r.text )
#print twitter_global_hcl_JsonFile
#keyWord = "P200"
#print twitter_global_hcl_JsonFile["Pictures_path"][keyWord]
#open local file 
##with open(join(twitterFolder,"local_hcl_file.txt"),'r') as twitter_local_hcl_file:
#  twitter_local_hcl_JsonFile = hcl.load(twitter_local_hcl_file)
#open global file  
#with open(join(twitterFolder,"global_hcl_file.txt"),'r') as twitter_global_hcl_file:
#    twitter_global_hcl_JsonFile = hcl.load(twitter_global_hcl_file)

  

'''
         API area
'''  
'''     GLOBAL     API         '''
def getPictures_path(keyWord):
    return  str(twitter_global_hcl_JsonFile["Pictures_path"][keyWord])

def getCountOfUsers():
    return  len(twitter_global_hcl_JsonFile["User_details"])/2

def getUserName(i):
    return  str(twitter_global_hcl_JsonFile["User_details"]["userName"+`i`]) 

def getUserPassword(i):
    return   str(twitter_global_hcl_JsonFile["User_details"]["password"+`i`])

def getTweetType():
    return  str(twitter_global_hcl_JsonFile["Run_details"]["type_of_tweet"])

def getTweetTypeRestrictions():
    return  twitter_global_hcl_JsonFile["Run_details"]["type_restriction"]

def getFunctionParameters(keyWord):
    return  str(twitter_global_hcl_JsonFile["Run_details"]["tweet_parameters"][keyWord])










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


def paramLength():
    return  len(twitter_global_hcl_JsonFile["Run_details"]["function_parameters"])

