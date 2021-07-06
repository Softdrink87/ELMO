import POSmatching
import protoNSP

class ELMO:

    def __init__:
        self.tokens = tokens
        self.tokenizer = tokenizer
        self.max_input_length = max_input_length
        self.UD_TAGS = UD_TAGS
        self.sentence = sentence
        self.text = text

    def POSprocess:
        
        def cut_and_convert_to_id(POSmatching.tokens, POSmatching.tokenizer, POSmatching.max_input_length):
        #return POSmatching.cut_and_convert_to_id(POSmatching.tokens,POSmatching.tokenizer,POSmatching.max_input_length)
            tokens = POSmatching.cut_and_convert_to_id(tokens,tokenizer,max_input_length)

        def cut_to_max_length(tokens,max_input_length):
        #return POSmatching.cut_to_max_length(POSmatching.tokens,POSmatching.max_input_length)
            tokens = POSmatching.cut_to_max_length(tokens,max_input_length)

        def UD_TAGS_to_KOR():
            POSmatching.UD_TAGS_to_KOR(UD_TAGS)

        def result(TEXT,UD_TAGS):
            return POSmatching.result(TEXT, UD_TAGS)

    # ----------------- POSmatching.py ------------------------------
    def NSPprocess:
        
        def tokenizing():
        #return protoNSP.tokenizing(protoNSP.sentence)
            tokenized_sentence = protoNSP.tokenizing(sentence)
    
        def process(tokenized_sentence):
        #return protoNSP.process(protoNSP.tokenized_sentence)
            return protoNSP.process(tokenized_sentence)

 # ----------------- protoNSP.py ------------------------------

    

    


