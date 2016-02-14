'''
Created on 27 dec 2015

@author: M
'''
import FollowerImports as FI

if __name__ == '__main__':
    
   
    
    print("OS:\t\t " + FI.getOSName())
    print("Browser:\t " + FI.getBrowserName())
    print("App:\t\t " + FI.getAplicationName())
    print("DBPath:\t\t " + FI.getDBPath())
    
  #  for users in range(0 , FI.getNumOfUsers()):
   #    a,b =FI.getUserDetails(users)
    #    print("twitter users \n userName"+`users`+":\t " + a+"\n password"+`users`+":\t"+b)
   
    
    #print("User Details name  \n user:\t\t " + a+"\n pass:\t\t " + b)
    
    print("TsharkPath:\t " + FI.getTsharkPath())
    a,b =FI.getTsharkNCInterface()
    print("Tshark Network Card \n interface:\t %s" + a+"\n number:\t"+b)
    print("Tshark Write Command: \t %s" % FI.getTsharkWriteCommand())
    #tsharkCall = [FI.gettsharkCallNoFileName()]
   # for param in range(0 , FI.paramLength()):
    #    print("function param "+`param`+":\t " +  FI.getFunctionParameters(param))
    
    str = "runTimeMinutes"
   # str = 
    print("function integer TestRunTimeSeconds:\t %s " % FI.getFunctionParametersByKey(str))   
   # print( follower_global_hcl_JsonFile["Run_details"]["function_parameters"].pop("TestRunTimeSeconds"))
    pass