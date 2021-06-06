# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 13:11:35 2021

@author: dingzeyu
"""
import requests

# definate a function for keyword extraction 
def keywordExtraction (input_Sentence):
    headers = {
    'Content-Type': 'application/json;charset=UTF-8',
    'Authorization': 'Bearer '+access_token, # access_token is valid only for 24 hours
    }

    data = '{\
        "document":"' +input_Sentence+'",\
        "type": "default","do_segment":true,"max_keyword_num":5}'

    response = requests.post('https://api.ce-cotoha.com/api/dev/nlp/v1/keyword', headers=headers, data=data.encode('utf-8'))
    
    print(response.json())
    
    
# get access to COTOHA webAPI
headers = {
    'Content-Type': 'application/json',
}


data = '{\
            "grantType": "client_credentials", \
            "clientId": "riuM1I4OQ1SsoVGA7GDjMyDo1U0sR8VR", \
            "clientSecret": "e7YGKz5u9vWVVcRG"\
        }'
    
response = requests.post('https://api.ce-cotoha.com/v1/oauth/accesstokens', headers=headers, data=data)

print(response.json()) # JSON files about access information
access_token = response.json()['access_token']

# receive sentence from external 
input_Sentence = "普段は公園に行ったりですとか、子供とよく遊んでいます"

# invoke keyword extraction Function
keywordExtraction (input_Sentence)

input_Sentence = "近くに駐車場とレストランがありますか"
keywordExtraction (input_Sentence)