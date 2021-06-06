import socket
import time
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
    
    
class SpeechRecognitionController(object):
    def __init__(self, ip, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((ip, port))

    def disconnect(self):
        self.sock.close()

    def send_command(self,command):
        command_ln = command + "\n"
        self.sock.send(command_ln.encode('utf-8'))

    def sppech_get(self):
        msg_dec = ""
        while msg_dec.startswith('result:') == False:
            msg = self.sock.recv(1024)
            msg_dec = msg.decode("utf-8")
            if msg_dec.startswith('result:') == True:
                return msg_dec
                break
            time.sleep(0.5)

if __name__ == "__main__":
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
    
    while True:
    #各システムに接続
        robot_SpeechRecognition_controller = SpeechRecognitionController("150.65.239.80", 8888)
        
    #テストで色々試してみる（言ったことばをそのまま返す）-------
    #Speech Recognition Serever より音声メッセージを受信
        msg_d = robot_SpeechRecognition_controller.sppech_get()
        
        if msg_d.splitlines()[0] == 'result:終わり':
            break
        print("msg_d:" + msg_d)
        keywordExtraction (msg_d.splitlines()[0][7:])
        print('\n')


#各システム切断
    robot_SpeechRecognition_controller.disconnect()
    print('\nEnd')

