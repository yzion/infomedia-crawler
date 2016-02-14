'''
Created on 3 jun 2016

@author: M
'''
import FollowerImports as FI
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import logging
import logging.handlers
import os
import platform
import subprocess


LOGGER_FORMAT_START = '%(asctime)-15s\t%(levelno)d\t%(levelname)s\t'

def create_log_name(browser_str, root_path):
    if not os.path.exists(root_path):
        os.makedirs(root_path)
    pass 

def createPcap():
    tsharkProc = subprocess.Popen(TsharkCall)
    return tsharkProc

def init_driver():
    webdrv = {'ie':webdriver.Ie, 'chrome':webdriver.Chrome, 'ff':webdriver.Firefox, 'firefox':webdriver.Firefox}
     
    if BrowserName not in webdrv.keys():
        return None
    else:
        driver = webdrv[BrowserName]()
        driver.wait = WebDriverWait(driver, 5)
    return driver
    pass

def initVarsScraper():
         
    global TestRunTimeSeconds , RunTimeMinutes , OsName , BrowserName ,DBPath , log_str ,fileName ,TsharkCall ,TsharkProc
    
    str = "TestRunTimeSeconds"
    TestRunTimeSeconds = int(FI.getFunctionParametersByKey(str))
   
    str = "runTimeMinutes"
    RunTimeMinutes = int(FI.getFunctionParametersByKey(str))
    OsName      = FI.getOSName()
    BrowserName = FI.getBrowserName()
    DBPath      = FI.getDBPath() 
    
    time_str = time.strftime("%m-%d__%H_%M_%S")
    host_name = platform.node()
    
    fileName = DBPath + os.sep + OsName + '_' + host_name + '_' + BrowserName + "_" + time_str
   
    path                         = FI.getTsharkPath()
    fileCommand  , fileType      = FI.getTsharkFileFullCommand()
    filterCommand ,filterType    = FI.getTsharkFilterFullCommand()
    NCInterface ,NCInterfaceType = FI.getTsharkNCInterface()
  
    
    WirtFileCommand  = FI.getTsharkWriteCommand()
    TsharkCall  = [ path, fileCommand, fileType, filterCommand, filterType, NCInterface, NCInterfaceType, WirtFileCommand, fileName+"."+fileType ] 
    
    
    
    pass

def initOperationsScrape():
    create_log_name(BrowserName,DBPath)
   # init_driver()
   # print "hii" + TsharkProc
    createPcap()
    print "hii" + TsharkProc
    
    pass

if __name__ == "__main__":
    initVarsScraper()
    initOperationsScrape()
    
    pass
