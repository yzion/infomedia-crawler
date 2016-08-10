import os
from os.path import join
import hcl
import requests
import sys


"""   loading local config file from local comp """
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

with open(join(BASE_DIR,"local_hcl_file.txt"),'r') as follower_local_hcl_file:
    follower_local_hcl_JsonFile = hcl.load(follower_local_hcl_file)

'''    ******     GLOBAL    FOLLOWER    FILE     ******   '''

# """    working online import settings file from benamika GitHub's account """
r = requests.get('https://raw.githubusercontent.com/yzion/infomedia-crawler/dev/CrawlerAPInew/newCrawler/follower/global_hcl_file.txt?token=AG6lb4JimkeElmqI5OTZwKNiq51yKaloks5XtDOJwA%3D%3D' ,auth=('infomediaTeamCrawler', 'CrawlerTeam16'))
follower_global_hcl_JsonFile = hcl.api.loads(r.text )

"""    working offline on local comp """
# with open(join(BASE_DIR,"CrawlerAPInew/newCrawler/follower/global_hcl_file.txt"),'r') as follower_global_hcl_file:
#    follower_global_hcl_JsonFile = hcl.load(follower_global_hcl_file)



'''        API AREA    '''
    
'''     GLOBAL     API         '''
def check_new_tweets_every_X_minutes():
    return follower_global_hcl_JsonFile["Run_details"]["check_new_tweets_every_X_minutes"]

def run_time_X_minutes():
    return follower_global_hcl_JsonFile["Run_details"]["runTimeMinutes"]

def getCiphersString():
    return str(follower_global_hcl_JsonFile["Run_details"]["cipherString"])
 
'''     LOCAL     API         '''
def getOSName():
    return  follower_local_hcl_JsonFile["Os_name"]

def getBrowserName():
    return  str(follower_local_hcl_JsonFile["Browser_name"])

def getDBPath():
    return str(follower_local_hcl_JsonFile["DB_path"])

def getUserDetails():
    return  str(getUserName()) , str(getUserPassword())

def getUserName():
    return  follower_local_hcl_JsonFile["User_details"]["userName"]
def getUserPassword():
    return   follower_local_hcl_JsonFile["User_details"]["password"]

'''    TSHARK settings    '''
def getTsharkPath():
    return  str(follower_local_hcl_JsonFile["Tshark_parameters"]["Tshark_path"])

def getTsharkFileCommand():
    return  str(follower_local_hcl_JsonFile["Tshark_parameters"]["file_command"])

def getTsharkFileType():
    return str(follower_local_hcl_JsonFile["Tshark_parameters"]["file_type"])

def getTsharkFilterCommand():
    return  str(follower_local_hcl_JsonFile["Tshark_parameters"]["filter_command"])

def getTsharkFilterType():
    return  str(follower_local_hcl_JsonFile["Tshark_parameters"]["filter_type"])

def getTsharkNCInterface():
    return  str(follower_local_hcl_JsonFile["Tshark_parameters"]["NC_interface"] )

def getTsharkNCInterfaceData():
    return  str(follower_local_hcl_JsonFile["Tshark_parameters"]["NC_interface_data"])

def getTsharkWriteCommand():
    return  str(follower_local_hcl_JsonFile["Tshark_parameters"]["write_file_type"])

'''    LOGFILE settings    '''
def getDefaultLogFilePath():
    return  follower_local_hcl_JsonFile["Log_settings"]["logName"]