import time
import datetime
import os
import subprocess
import random
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import sys

scrapper_path = os.path.dirname(os.path.dirname(__file__))
utils_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + os.sep + "utils"
import_file_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + os.sep + "ImportFiles"
sys.path.insert(0, scrapper_path)
sys.path.insert(0, utils_path)
sys.path.insert(0, import_file_path)
import TwitterImports as TI
import FollowerImports as FI
import user_info as us
from scrapper import Twitter_scrapper

LOGGER_FORMAT_START = '%(asctime)-15s\t%(levelno)d\t%(levelname)s\t'

"""
Closes the browser, Tshark proc and log file
"""


def end_runing_func(tshark_proc, driver, tw):
    tshark_proc.kill()
    time.sleep(5)
    driver.quit()
    temp = list(tw.log.handlers)
    for i in temp:
        tw.log.removeHandler(i)
        i.flush()
        i.close()


"""
Start and return Tshark process
"""


def createPcap(filename):
    tsharkCall = [TI.getTsharkPath(), TI.getTsharkFileCommand(), TI.getTsharkFileType(), TI.getTsharkFilterCommand(),
                  TI.getTsharkFilterType(), TI.getTsharkNCInterface(), TI.getTsharkNCInterfaceData(),
                  TI.getTsharkWriteCommand(), filename]
    tsharkProc = subprocess.Popen(tsharkCall)
    return tsharkProc


"""
Initialize and return "driver" for the received "browser"
"""


def init_driver(browser):
    webdrv = {'ie': webdriver.Ie, 'chrome': webdriver.Chrome, 'ff': webdriver.Firefox, 'firefox': webdriver.Firefox}

    browser = str.lower(browser)
    if browser not in webdrv.keys():
        return None
    else:
        driver = webdrv[browser]()
        driver.wait = WebDriverWait(driver, 5)
    return driver


"""
Get browser name and root path
Create (if not exist) new folder for every new run
The path format is: "OS NAME AND VERSION_DATE__TIME"
Genarate new log/pcap name:
The file name format: "OS NAME AND VERSION_DATE__TIME"
Return the new run path + new file name as a string
"""


def create_log_name(browser_str, root_path):
    time_str = time.strftime("%m-%d__%H_%M_%S")

    # if not os.path.exists(root_path):
    #     os.makedirs(root_path)

    os_name = us.get_os_name()
    os_version = us.get_os_version(os_name)

    # host_name = platform.node()

    run_path = root_path + os.sep + os_name + os_version + '_' + time_str + os.sep
    if not os.path.exists(run_path):
        os.makedirs(run_path)
    return run_path + os_name + '_' + browser_str + "_" + time_str
    # return root_path + os.sep + os_name + '_' + host_name + '_' + browser_str + "_" + time_str


"""
initialize and return log file, driver and tshark process
"""


def start_driver_and_pcap():
    browser = TI.getBrowserName()
    db_path = TI.getDBPath()
    log_str = create_log_name(browser, db_path)
    # get Web Driver
    driver = init_driver(browser)

    # get TShark recording
    tshark_proc = createPcap(log_str + '.pcap')
    time.sleep(5)
    return log_str, driver, tshark_proc


"""**************************************************************************************************"""

"""
Tweets only text
This function tweets a time string every "num_of_tweet" seconds.
user_name = twitter user name
password= twitter password
num_of_tweet = total number of tweets
time_between_tweets = time between an individual Tweets (in seconds)
num_of_set = after this number of tweets will be a break of "break_time" seconds.
break_time = time to wait between set of tweets. by default "break_time"=60
"""
def tweet_only_text(user_name, password, num_of_tweet, time_between_tweets, num_of_set, break_time , pix_path):
    log_str, driver, tshark_proc = start_driver_and_pcap()

    try:

        # login to Twitter
        tw = Twitter_scrapper(driver, log_str + '.tsv')
        if not tw.login(user_name, password):
            print 'Logging to Twitter account failed'
            return
        dd = datetime.datetime.now()
        twttext = dd.strftime('Now is %Y-%m-%d %H:%M:%S +%f')
        if not tw.make_tweet(user_name+ twttext + '\n'):
                return
        time.sleep(time_between_tweets)
        for tweet_counter in range(num_of_tweet):
            # post tweets
            dd = datetime.datetime.now()
            twttext = dd.strftime('Now is %Y-%m-%d %H:%M:%S +%f')

            if not tw.make_tweet(twttext + '\n'):
                return

            time.sleep(time_between_tweets)
            if tweet_counter % num_of_set == 0:
                time.sleep(break_time - time_between_tweets)

    finally:  # do cleaning anyway
        end_runing_func(tshark_proc, driver, tw)


"""
!!! this function unused for now
Get list of pictures folders paths and run "tweet_only_pic" for each path
"""


def tweet_set_of_pic_by_path(username, password, path_arr, num_of_tweet, time_between_tweets, num_of_set, break_time):
    for op in path_arr:
        tweet_only_pic(username, password, num_of_tweet, time_between_tweets, num_of_set, break_time, op)


"""
Tweets only pictures
num_of_tweet = total number of tweets
time_between_tweets = time between an individual Tweets (in seconds)
num_of_set = after this number of tweets will be a break of "break_time" seconds.
break_time = time to wait between set of tweets. by default "break_time"=60
pix_path = the path into the pictures folder. by default "pix_path"= r'D:\TwitterDB\diff_pic'
"""


def tweet_only_pic(user_name, password, num_of_tweet, time_between_tweets, num_of_set, break_time, pix_path):
    log_str, driver, tshark_proc = start_driver_and_pcap()

    try:
        # login to Twitter
        tw = Twitter_scrapper(driver, log_str + '.tsv')
        if not tw.login(user_name, password):
            print 'Logging to Tweeter account failed'
            return

        # get list of photos
        pix_names = []
        for filename in os.listdir(pix_path):
            if filename.lower().endswith('.jpg') or filename.lower().endswith('.png'):
                pix_names.append(pix_path + os.sep + filename)

        pic_cnt = 0
        for tweet_counter in range(0, num_of_tweet):
            pic = pix_names[pic_cnt]
            pic_cnt += 1
            if pic_cnt >= len(pix_names):
                pic_cnt = 0;

            if not tw.make_tweet('', pic):
                return
            print pic
            if Twitter_scrapper.tweets_number >= 300:
                break
            time.sleep(time_between_tweets)
            if tweet_counter % num_of_set == 0:
                time.sleep(break_time - time_between_tweets)


    finally:  # do cleaning anyway
        end_runing_func(tshark_proc, driver, tw)


"""
Tweets pictures with text
user_name = twitter user name
password= twitter password
num_of_tweet = total number of tweets
time_between_tweets = time between an individual Tweets (in seconds)
num_of_set = after this number of tweets will be a break of "break_time" seconds.
break_time = time to wait between set of tweets.
pix_path = the path into the pictures folder. by default "pix_path"= r'D:\TwitterDB\diff_pic'
"""


def tweet_pic_with_text(user_name, password, num_of_tweet, time_between_tweets, num_of_set, break_time, pix_path):
    log_str, driver, tshark_proc = start_driver_and_pcap()

    try:
        # login to Twitter
        tw = Twitter_scrapper(driver, log_str + '.tsv')
        if not tw.login(user_name, password):
            print 'Logging to Tweeter account failed'
            return
        # get list of photos
        pix_names = []
        for filename in os.listdir(pix_path):
            if filename.lower().endswith('.jpg') or filename.lower().endswith('.png'):
                pix_names.append(pix_path + os.sep + filename)

        # first tweet with user name
        dd = datetime.datetime.now()
        twttext = dd.strftime('Now is %Y-%m-%d %H:%M:%S +%f')
        pic = pix_names[0]
        if not tw.make_tweet(user_name + ' ' + twttext + '\n', pic):
            return
        time.sleep(time_between_tweets)
        pic_cnt = 0
        for tweet_counter in range(0, num_of_tweet):
            # picture part
            pic = pix_names[pic_cnt]
            pic_cnt += 1
            if pic_cnt >= len(pix_names):
                pic_cnt = 0;
            # text part
            dd = datetime.datetime.now()
            twttext = dd.strftime('Now is %Y-%m-%d %H:%M:%S +%f')

            if not tw.make_tweet(twttext + '\n', pic):
                return
            print pic
            if Twitter_scrapper.tweets_number >= 700:
                break
            time.sleep(time_between_tweets)
            if tweet_counter % num_of_set == 0:
                time.sleep(break_time - time_between_tweets)


    finally:  # do cleaning anyway
        end_runing_func(tshark_proc, driver, tw)


"""
    ### random tweets ###
    tweet any tweets(only random pic/only random text/random text+random pic)
    user_name = twitter user name
    password = twitter password
    path_list =
    num_of_tweet = total number of tweets. by default "num_of_tweet" = 3000.
    min_time_between_tweets = min time between an individual Tweets (in seconds) by default == 180
    max_time_between_tweets = max time between an individual Tweets (in seconds) by default == 300

"""


def random_tweet(user_name, password, path_list, num_of_tweet, min_time_between_tweets, max_time_between_tweets):
    log_str, driver, tshark_proc = start_driver_and_pcap()
    try:
        # login to Twitter
        tw = Twitter_scrapper(driver, log_str + '.tsv')
        if not tw.login(user_name, password):
            print 'Logging to Tweeter account failed'
            return
        # get list of photos
        pix_names = []
        paths(path_list, pix_names)

        # first tweet with user name
        time_between_tweets = random.randint(min_time_between_tweets, max_time_between_tweets)
        tw.log.info('time between tweets: %i' % (time_between_tweets), extra=tw.log_extra)
        dd = datetime.datetime.now()
        twttext = dd.strftime('Now is %Y-%m-%d %H:%M:%S +%f')
        rand_pic = random.randint(0, len(pix_names))
        pic = pix_names[rand_pic]
        if not tw.make_tweet(user_name + ' ' + twttext + '\n', pic):
            return
        time.sleep(time_between_tweets)
        for tweet_counter in range(0, num_of_tweet):
            pic_cnt = random.randint(0, len(pix_names))
            # choose random team between the tweets
            time_between_tweets = random.randint(min_time_between_tweets, max_time_between_tweets)
            tw.log.info('time between tweets: %i' % (time_between_tweets), extra=tw.log_extra)
            # choose random tweet. 1==only text, 2== only pic, 3== pic+text
            which_tweet = random.randint(1, 3)
            if which_tweet == 1:  # only text
                # post tweets
                dd = datetime.datetime.now()
                twttext = dd.strftime('Now is %Y-%m-%d %H:%M:%S +%f')
                if not tw.make_tweet(twttext + '\n'):
                    return
            elif which_tweet == 2:  # only pic
                pic = pix_names[pic_cnt]
                if not tw.make_tweet('', pic):
                    return
                print pic

            elif which_tweet == 3:  # pic+text
                # picture part
                pic = pix_names[pic_cnt]
                # text part
                dd = datetime.datetime.now()
                twttext = dd.strftime('Now is %Y-%m-%d %H:%M:%S +%f')

                if not tw.make_tweet(twttext + '\n', pic):
                    return
                print pic

            if Twitter_scrapper.tweets_number >= 10:
                break
            time.sleep(time_between_tweets)


    finally:  # do cleaning anyway
        end_runing_func(tshark_proc, driver, tw)


def paths(path_list, pix_names):
    for i in range(3):
        pix_path = path_list[i]
        for filename in os.listdir(pix_path):
            if filename.lower().endswith('.jpg') or filename.lower().endswith('.png'):
                pix_names.append(pix_path + os.sep + filename)


if __name__ == "__main__":

    """ path list for pictures folders """
    path_list = [TI.getPictures_path("P200"), TI.getPictures_path("P1000"), TI.getPictures_path("P2000")]

    """ list of useres for the crawler """
    twitter_users = []
    for index in range(TI.getCountOfUsers()):
        twitter_users.append(TI.getUserName(index))
    twitter_passwords = []
    for index in range(TI.getCountOfUsers()):
        twitter_passwords.append(TI.getUserPassword(index))

    """ variable list """
    num_of_all_tweets = TI.getFunctionParameters("num_of_all_tweets")  # 200
    num_of_tweet = TI.getFunctionParameters("num_of_tweet")  # 200
    time_between_tweets = float(TI.getFunctionParameters("time_between_tweets"))  # 180 #time in seconds between tweets
    num_of_set = TI.getFunctionParameters("num_of_set")  # 100
    break_time = TI.getFunctionParameters("break_time")  # 300

    # vlues for random tweets
    min_time_between_tweets = TI.getFunctionParameters("min_time_between_tweets")  # 180
    max_time_between_tweets = TI.getFunctionParameters("max_time_between_tweets")  # 300

    tweetType = TI.getTweetType()

    if (tweetType == "tweet_only_text"):
        tweetRestrictions = 0
    elif (tweetType == "random_tweet"):
        # random_tweet()
        print("random_tweet needs implementation changing to tweet_only_text")
        tweetType = "tweet_only_text"
    else:
        tweetRestrictions = TI.getTweetTypeRestrictions()

    possibles = globals().copy()
    possibles.update(locals())
    method = possibles.get(tweetType)
    if not method:
        raise NotImplementedError("Method %s not implemented" % tweetType)

    """ run for tweet_only_text AND tweet_only_pic AND tweet_pic_with_text """
    pics_recurser = 1
    if (tweetRestrictions == 1):
        pics_recurser = len(path_list)
    i = 0
    for j in range(0, pics_recurser):
        # print "random_tweet j=",j
        if (tweetRestrictions == 1):
            pix_path = path_list[j]
        elif (tweetRestrictions == 200 and tweetType != "tweet_only_text"):
            pix_path = path_list[0]
        elif (tweetRestrictions == 1000 and tweetType != "tweet_only_text"):
            pix_path = path_list[1]
        elif (tweetRestrictions == 2000 and tweetType != "tweet_only_text"):
            pix_path = path_list[2]
        else:
            pix_path = ""
        while i < (len(twitter_users) * 4):
            username = twitter_users[i % len(twitter_users)]
            password = twitter_passwords[i % len(twitter_users)]
            method(username, password, num_of_tweet, time_between_tweets, num_of_set, break_time, pix_path)
            i += 1
            if (Twitter_scrapper.tweets_number >= num_of_all_tweets):
                Twitter_scrapper.tweets_number = 0
                break
        time.sleep(60)

    """ run for random_tweet"""


    #     subprocess.call('C:\port_closer\cports.exe /close * * * * chrome.exe', shell=True)
    #     subprocess.call('cports.exe /close * * * * chrome.exe' ,shell = True)
