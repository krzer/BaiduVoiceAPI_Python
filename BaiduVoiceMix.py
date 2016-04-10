#coding:utf-8

import json
import urllib2


class BaiduVoiceHttpClient():
    apiKey = ""
    secretKey = ""

    def __init__(self,client_id,client_secret):
        self.apiKey = apiKey;
        self.secretKey = secretKey;

    def __getToken(self):
        auth_url = "https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id=%s&client_secret=%s" % (self.apiKey, self.secretKey);
        response = self.__request(auth_url);
        return response['access_token'];

    def VoiceMix(self,tex,lan,ctp):
        tok = self.__getToken();
        cuid = tok[tok.index("-") + 1:];
        
        text = open(textFile,'rb');
        tex = text.read()
        text.close()
        
        API_url = "http://tsn.baidu.com/text2audio?tex=%s&lan=zh&cuid=%s&ctp=1&tok=%s" % (tex,cuid,tok);

        response = self.__request1(API_url)

        return response

    def __request(self,url):
        try:

            res =  urllib2.urlopen(url);
            json_data = json.loads(res.read());
            return json_data;
        except Exception, e:
            print e;

    def __request1(self,url):
        try:

            res =  urllib2.urlopen(url);
            request_data = res.read();
            return request_data;
        except Exception, e:
            print e;

apiKey = "r6S4Wf6daGimwzsQWtsbQqXp"                                            
secretKey = "60d0b8f3a83bdf31da3fa1387b6c7feb"                                        
textFile = 'yuyin.txt'  			#必须采用UTF-8 无BOM格式编码	     
lan = "zh"                         			                                   					 		
ctp = 1                          				            

Voicemix = BaiduVoiceHttpClient(apiKey,secretKey)

VoiceRespone = Voicemix.VoiceMix(textFile,lan,ctp)

#print VoiceRespone


fo = open("yuyin.mp3", "wb")
fo.write(VoiceRespone)
fo.close()


