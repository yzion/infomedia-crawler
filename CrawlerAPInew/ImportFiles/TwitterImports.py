import os
from os.path import join 

import hcl
import requests

"""    working offline on mika's comp """
#twitterFolder = r"C:\Users\Mika\Python\infomedia-sourceTree\CrawlerAPInew\newCrawler\twitter"
#with open(join(twitterFolder,"global_hcl_file.txt"),'r') as twitter_global_hcl_file:
#    twitter_global_hcl_JsonFile = hcl.load(twitter_global_hcl_file)
#print(twitter_global_hcl_JsonFile["DB_path"])

"""    working online import settins file from benamika GitHub's account """
r = requests.get('https://raw.githubusercontent.com/benamika/infomedia-crawler/dev/CrawlerAPInew/newCrawler/twitter/global_hcl_file.txt?token=AGd2fy20HgZaKixDaxSJdT0o5GJB_K8Qks5W6xsKwA%3D%3D' ,auth=('infomediaTeamCrawler', 'CrawlerTeam16'))
twitter_global_hcl_JsonFile = hcl.api.loads(r.text )

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


'''    TSHARK settings    '''
def getTsharkPath():
    return  twitter_global_hcl_JsonFile["Tshark_parameters"]["Tshark_path"]

def getTsharkFileCommand():
    return  twitter_global_hcl_JsonFile["Tshark_parameters"]["file_command"]

def getTsharkFileType():
    return  twitter_global_hcl_JsonFile["Tshark_parameters"]["file_type"]

def getTsharkFilterCommand():
    return  twitter_global_hcl_JsonFile["Tshark_parameters"]["filter_command"]

def getTsharkFilterType():
    return  twitter_global_hcl_JsonFile["Tshark_parameters"]["filter_type"]

def getTsharkNCInterface():
    return  twitter_global_hcl_JsonFile["Tshark_parameters"]["NC_interface"] 

def getTsharkNCInterfaceData():
    return  twitter_global_hcl_JsonFile["Tshark_parameters"]["NC_interface_data"]

def getTsharkWriteCommand():
    return  twitter_global_hcl_JsonFile["Tshark_parameters"]["write_file_type"]

def getBrowserName():
    return  twitter_global_hcl_JsonFile["Browser_name"]

def getDBPath():
    return  twitter_global_hcl_JsonFile["DB_path"]


""" NOT in use yet """

def getOSName():
    return  twitter_global_hcl_JsonFile["Os_name"]

def getAplicationName():
    return  twitter_global_hcl_JsonFile["Aplication_name"]

def getUserDetails(i):
    return  getUserName(i) , getUserPassword(i)

def getNumOfUsers():
    return  len(twitter_global_hcl_JsonFile["User_details"])/2

