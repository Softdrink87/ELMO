from flask import Flask
import ELMO
import requests,time

app = Flask(__name__)

#mdl = ELMO(tokens="",tokenizer="",max_input_length="",UD_TAGS="")
#mdl 에 있는 초기화 인자들 채워넣자  ! 


@app.route('/POS',methods=['POST'])
def POSpredict():
    received_data = request.get_json()
    received_tokens, received_tokenizer, received_max_input_length, received_UD_TAGS = 
    received_data['token'],received_data['tokenizer'],received_data['max_input_length'],received_data['UD_TAGS']
    mdl = ELMO(received_tokens,received_tokenizer,received_max_input_length,received_UD_TAGS)
    mdl.POSprocess()
    #start = time.time()
    


@app.route('/NSP',methods=['POST'])
def NSPpredict():
    received_data = request.get_json()
    received_sentence, received_tokenized_sentence = received_data['sentence'],received_data['tokenized_sentence']
    mdl.sentence = received_sentence
    mdl.NSPprocess()



if __name__ == '__main__':  # if it's an entry point. then run Flask :O -> if it's not a module call then run Flask :D
    app.run(host='127.0.0.1', port=5000)

