from flask import Flask
import ELMO
import requests,time
import jsonify
import googletrans

app = Flask(__name__)

#mdl = ELMO(tokens="",tokenizer="",max_input_length="",UD_TAGS="",sentence="",text="")
mdl = predict()

@app.route('/QA',methods=['POST'])
def POSpredict():   
    received_data = requests.get_json()
    received_theme , received_sentence = received_data['theme'], received_data['sentence']
#   received_tokens, received_tokenizer, received_max_input_length, received_UD_TAGS = received_data['token'],received_data['tokenizer'],received_data['max_input_length'],received_data['UD_TAGS']
    #mdl = ELMO(received_tokens,received_tokenizer,received_max_input_length,received_UD_TAGS)
    mdl.predict(received_theme, received_sentence)


#@app.route('/NSP',methods=['POST'])
#def NSPpredict():
    #received_data = requests.get_json()
    #received_sentence = received_data['sentence']
    #mdl.sentence = received_sentence
    #mdl.NSPprocess()



if __name__ == '__main__':  # if it's an entry point. then run Flask :O -> if it's not a module call then run Flask :D
    app.run(host='0.0.0.0', port=5000,debug=True)

