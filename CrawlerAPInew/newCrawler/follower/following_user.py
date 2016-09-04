import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import logging.handlers
import os
import platform
import subprocess
import random
import sys

""" 07/08/16
adding to path of platform the located file
way around bugs. to import files
"""
local_folder = os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + os.sep + "ImportFiles"
print local_folder
sys.path.insert(0, local_folder)

globalCountOfPcap = 0
<<<<<<< 9c8d831b8fc198ef3c488cf8c353ad009a57bf03
import FollowerImports as FI
=======

>>>>>>> partly sepereted functoins of follower
# import TwitterImports as TI
from Twitter_scrapper_for_follower import Twitter_scrapper

LOGGER_FORMAT_START = '%(asctime)-15s\t%(levelno)d\t%(levelname)s\t'

def createPcap(filename):
    
    tsharkCall = [FI.getTsharkPath(),FI.getTsharkFileCommand(), FI.getTsharkFileType(), FI.getTsharkFilterCommand(), FI.getTsharkFilterType(), FI.getTsharkNCInterface(), FI.getTsharkNCInterfaceData(), FI.getTsharkWriteCommand(), str(filename)]
    
    tsharkProc = subprocess.Popen(tsharkCall)
    
    return tsharkProc


"""
Initial the chrome option to ignore the ciphers in "ciphers_string"
If cipher string is empty then nothing happend.
Return chrome options
"""

def change_chrome_ciphers(ciphers_string):
    chrome_options = Options()
    if ciphers_string == "":
        return chrome_options
    chrome_options.add_argument(ciphers_string)
    return chrome_options

def init_driver(browser):
    webdrv = {'ie': webdriver.Ie, 'chrome': webdriver.Chrome, 'ff': webdriver.Firefox, 'firefox': webdriver.Firefox}
    browser = str.lower(browser)
    if browser not in webdrv.keys():
        return None
    else:
        if browser == 'chrome':
            ciphers_string = FI.getCiphersString()
            chrome_options = change_chrome_ciphers(ciphers_string)
            driver = webdrv[browser](chrome_options=chrome_options)
            driver.wait = WebDriverWait(driver, 5)
        else:
            # TODO: add firefox handling
            driver = webdrv[browser]()
            driver.wait = WebDriverWait(driver, 5)
    return driver

def create_log_name(browser_str, root_path):
    time_str = time.strftime("%m-%d__%H_%M_%S")

    if not os.path.exists(root_path):
        os.makedirs(root_path)

    os_name = platform.system()[0]
    host_name = platform.node()
    return root_path + os.sep + os_name + '_' + host_name + '_' + browser_str + "_" + time_str

"""
initialize and return log file, driver and tshark process
"""


def start_driver_and_pcap():
    browser = FI.getBrowserName()

    db_path = FI.getDBPath()

    log_str = create_log_name(browser, db_path)

    # get Web Driver
    driver = init_driver(browser)
    # get TShark recording
    tshark_proc = createPcap(log_str + '.pcap')
    time.sleep(5)
    return log_str, driver, tshark_proc

def end_runing_func(tshark_proc,driver,tw):
    tshark_proc.kill()
    time.sleep(5)
    driver.quit()
    temp = list(tw.log.handlers)
    for i in temp:
        tw.log.removeHandler(i)
        i.flush()
        i.close()

"""
follow and captures Tweets
Follows on updates on twitter for "timeout" minutes
timeout = time to capture in minutes. by default "timeout" = 60.
"""
def follows_and_captures_Tweets_complete(timeout = 60):
    log_str, driver, tshark_proc = start_driver_and_pcap()
    try:
        # login to Twitter
        tw = Twitter_scrapper(driver, log_str + '.tsv')

        if not tw.login(FI.getUserName() , FI.getUserPassword()):
            print 'Logging to Twitter account failed'
            return
        tw.consume(timeout)



    finally:    # do cleaning anyway
        end_runing_func(tshark_proc,driver,tw)

<<<<<<< 9c8d831b8fc198ef3c488cf8c353ad009a57bf03

def follows_and_captures_Tweets_pcap_first(timeout = 60):
   
    browser = FI.getBrowserName()
    db_path =  FI.getDBPath()
    log_str = create_log_name(browser, db_path)
    log_str_by_time = log_str
    t = time.time()
    while (time.time()-t)/60 < timeout:      
        # get Web Driver
        try:
            tshark_proc = createPcap(log_str_by_time +"_pcap_first_" +  "_pcap_count_"+str(globalCountOfPcap) + '.pcap')
            time.sleep(5)
        
            driver = init_driver(browser)
        
       
           
            # login to Twitter
            tw = Twitter_scrapper(driver, log_str + '.tsv')
            
            if not tw.login(FI.getUserName() , FI.getUserPassword()):
                print 'Logging to Twitter account failed'
                return
            
            
            # get TShark recording
            
            tw.consume(timeout)
           
        finally:    # do cleaning anyway
            end_runing_func(tshark_proc,driver,tw)
            globalCountOfPcapPP() 
            
def follows_and_captures_Tweets_web_first(timeout = 60):
<<<<<<< 186264576f60ab9161268d746b08fc991b5a9a10
=======
def follows_and_captures_Tweets_parts(timeout = 60):
>>>>>>> partly sepereted functoins of follower
=======
>>>>>>> 0.5
    
    browser = FI.getBrowserName()
    db_path =  FI.getDBPath()
    log_str = create_log_name(browser, db_path)
    log_str_by_time = log_str
<<<<<<< 186264576f60ab9161268d746b08fc991b5a9a10
<<<<<<< 9c8d831b8fc198ef3c488cf8c353ad009a57bf03
    t = time.time()
    while (time.time()-t)/60 < timeout: 
=======
    while True: # TODO: fix to reasonable amount of time
>>>>>>> partly sepereted functoins of follower
=======
    t = time.time()
    while (time.time()-t)/60 < timeout: 
>>>>>>> 0.5
        
        # get Web Driver
        driver = init_driver(browser)
        
        try:
           
            # login to Twitter
            tw = Twitter_scrapper(driver, log_str + '.tsv')
            
            if not tw.login(FI.getUserName() , FI.getUserPassword()):
                print 'Logging to Twitter account failed'
                return
            
<<<<<<< 186264576f60ab9161268d746b08fc991b5a9a10
<<<<<<< 9c8d831b8fc198ef3c488cf8c353ad009a57bf03
            
            # get TShark recording
            tshark_proc = createPcap(log_str_by_time +"_web_first_" +  "_pcap_count_"+str(globalCountOfPcap) + '.pcap')
=======
           
            # get TShark recording
            tshark_proc = createPcap(log_str_by_time +  "_pcap_count_"+str(globalCountOfPcap) + '.pcap')
>>>>>>> partly sepereted functoins of follower
=======
            
            # get TShark recording
            tshark_proc = createPcap(log_str_by_time +"_web_first_" +  "_pcap_count_"+str(globalCountOfPcap) + '.pcap')
>>>>>>> 0.5
            time.sleep(5)
            tw.consume(timeout)
           
        finally:    # do cleaning anyway
            end_runing_func(tshark_proc,driver,tw)
<<<<<<< 186264576f60ab9161268d746b08fc991b5a9a10
<<<<<<< 9c8d831b8fc198ef3c488cf8c353ad009a57bf03
            globalCountOfPcapPP() 
=======
            globalCountOfPcap++
>>>>>>> partly sepereted functoins of follower
=======
            globalCountOfPcapPP() 
>>>>>>> 0.5
"""
follow and captures Tweets by time
Follows on updates on twitter for "timeout" minutes
make refresh after "refresh_time" minutes
timeout = time to capture in minutes. by default "timeout" = 60.
"""
<<<<<<< 186264576f60ab9161268d746b08fc991b5a9a10

def follows_and_captures_Tweets_by_time(timeout=60, refrash_time=30):
=======
def follows_and_captures_Tweets_by_time(timeout = 60, refrash_time = 30):
>>>>>>> 0.5
    log_str, driver, tshark_proc = start_driver_and_pcap()

    try:
        # login to Twitter
        tw = Twitter_scrapper(driver, log_str + '.tsv')
        if not tw.login(FI.getUserName(), FI.getUserPassword()):
            print 'Logging to Twitter account failed'
            return
        tw.consume_by_time(timeout, refrash_time)



<<<<<<< 186264576f60ab9161268d746b08fc991b5a9a10
    finally:  # do cleaning anyway
        end_runing_func(tshark_proc, driver, tw)
=======
    finally:    # do cleaning anyway
        end_runing_func(tshark_proc,driver,tw)
>>>>>>> 0.5

def globalCountOfPcapPP():
    global globalCountOfPcap
    globalCountOfPcap = globalCountOfPcap+1

if __name__ == "__main__":

   
    runTimeMinutes = FI.run_time_X_minutes()
    checkNewTweetsInXTime = FI.check_new_tweets_every_X_minutes()
    followType = FI.get_follow_type()
    
    possibles = globals().copy()
    possibles.update(locals())
    method = possibles.get(followType)
<<<<<<< 186264576f60ab9161268d746b08fc991b5a9a10
<<<<<<< 9c8d831b8fc198ef3c488cf8c353ad009a57bf03
    #global globalCountOfPcap
=======
>>>>>>> partly sepereted functoins of follower
=======
    #global globalCountOfPcap
>>>>>>> 0.5
    if not method:
        raise NotImplementedError("Method %s not implemented" % followType)
    
    # follows_and_captures_Tweets_complete(60*runTimeMinutes)
    method(60*runTimeMinutes)
#     refresh_time = 30
#     follows_and_captures_Tweets_by_time(runTimeMinutes, refresh_time)
