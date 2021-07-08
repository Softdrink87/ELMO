import POSmatching 
import protoNSP
from datetime import datetime
import time 
import jsonify

class ELMO:

    def __init__(self,tokens,tokenizer,max_input_length,UD_TAGS,sentence,text):
        self.tokens = tokens
        self.tokenizer = tokenizer
        self.max_input_length = max_input_length
        self.UD_TAGS = UD_TAGS
        self.sentence = sentence
        self.text = text

    def POSprocess(self):
        startS = time.time()
        self.tokens = POSmatching.cut_and_convert_to_id(self.tokens,self.tokenizer,self.max_input_length)
        self.tokens = POSmatching.cut_to_max_length(self.tokens,self.max_input_length)
        self.TEXT,self.UD_TAGS = POSmatching.init(5000)

        UD_TAGS_to_KOR(self.UD_TAGS)

        text,output = POSmatching.result(self.TEXT,self.UD_TAGS)
        endS = time.time()

        return jsonify(
            output = output,
            version = datetime.today(),
            time = str(endS-startS)
        )







    # ----------------- POSmatching.py ------------------------------
    def NSPprocess(self):
        startS = time.time()
        tokenized_sentence = protoNSP.tokenizing(self.sentence)
        endS = time.time()
        output = protoNSP.process(tokenized_sentence)

        return jsonify (
            output = output,
            version = datetime.today,
            time = str(endS - startS)
        )


 # ----------------- protoNSP.py ------------------------------

    

    


