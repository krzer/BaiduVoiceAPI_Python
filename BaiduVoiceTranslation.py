#coding:utf-8

import json
import base64
import os
import urllib2

class BaiduVoiceHttpClient():
    apiKey = ""
    secretKey = ""
    

    def __init__(self,apiKey,secretKey):
        self.apiKey = apiKey;
        self.secretKey = secretKey;

    def __getToken(self):
        auth_url = "https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id=%s&client_secret=%s" % (self.apiKey, self.secretKey);
        response = self.__request(auth_url,'');
        return response['access_token'];

    def VocieTranslation(self,Language,Channel,audioFile,Format,Rate):

        Token = self.__getToken();
        cuid = Token[Token.index("-") + 1:];
        API_url = "http://vop.baidu.com/server_api";
        
        audioFileLen = os.path.getsize(audioFile);
        audio = open(audioFile,'rb');
        base_data = base64.b64encode(audio.read());
        audio.close();
        
        Postdata = {'format':Format,'rate':Rate,'channel':Channel,'lan':Language,'token':Token,'cuid':cuid,'len':audioFileLen,'speech':base_data};

        response = self.__request(API_url,Postdata);
        if (response['err_no'] == 0):
            return response['result'][0];
        else:
            return response['err_msg'];
    


    def __request(self,url,data):
        try:
            res =  urllib2.urlopen(url = url,data=json.dumps(data));
            json_data = json.loads(res.read());
            return json_data;
        except Exception, e:
            print e;


apiKey = "r6S4Wf6daGimwzsQWtsbQqXp"                                            #这里输入自己的key
secretKey = "60d0b8f3a83bdf31da3fa1387b6c7feb"                                         #这里输入自己的secretKey
audioFile = '6.wav'  				     #生成并解析的语音路径+文件名 默认在当前程序所在目录
Language = "zh"                         			            #默认zh 支持中文(zh) 英文(en) 粤语(ct)                         					 		
Rate = 16000                          				             #采样率，支持8000和16000
Channel = 1                             			            #声道，目前baidu只支持单声道
Format = 'wav'                                         #语音格式，支持wav pcm opus speex amr x-flac


VoiceTranslation = BaiduVoiceHttpClient(apiKey,secretKey)

VoiceRespone = VoiceTranslation.VocieTranslation(Language,Channel,audioFile,Format,Rate)

print VoiceRespone
