#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      suresh.kumar
#
# Created:     07-10-2017
# Copyright:   (c) suresh.kumar 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import requests
import json
import unittest
import time

class ReopentenderusingRESTAPIclass(unittest.TestCase):
      def test_authunticateAPI(self):
            time.sleep(1)
            #APIDetails = DataDriver()

##            Username =APIDetails.readfromXML(folder_path+'\Data\APIdetailsStaging.xml','eTender','username')
##            Password =APIDetails.readfromXML(folder_path+'\Data\APIdetailsStaging.xml','eTender','password')
##
##            env = APIDetails.readfromXML(folder_path+'\Env\Setup.xml','eTender','env')
##            print env
            url = 'http://bg-etender-ser:8080/tenderservices/api/signin'


            Login = {'email':'Estimator@etender.com','password':'Estimator'}
            #Login = {'email':'nagendra@etender.com','password':'nag'}

            headers = {'Content-type': 'application/x-www-form-urlencoded'}

            response = requests.post(url,data=Login,headers=headers)

            #print response.text

            accesstoken = response.text
            code = response.status_code
            print code
            print url
            print accesstoken
            time.sleep(1)
            time.sleep(1)
            #return accesstoken





