import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.nn.optim as optim

from torchtext import data
from torchtext.legacy import data
from torchtext.legacy import datasets

from transformers import BertTokenizer, BertModel

import numpy as np

import time,random,functools


SEED = int(input())

random.seed(SEED)
np.random.seed(SEED)
torch.manual_seed(SEED)
torch.backends.cudnn.deterministic = True

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
init_token = tokenizer.cls_token
pad_token = tokenizer.pad_token
unk_token = tokenizer.unk_token

init_token_idx = tokenizer.convert_tokens_to_ids(init_token)
pad_token_idx = tokenizer.convert_tokens_to_ids(pad_token)
unk_token_idx = tokenizer.convert_tokens_to_ids(unk_token)

max_input_length = tokenizer.max_model_input_sizes['bert-base-uncased']

def cut_and_convert_to_id(tokens, tokenizer, max_input_length):
    tokens = tokens[:max_input_length-1] # 자르고
    tokens = tokenizer.convert_tokens_to_ids(tokens) # 토큰을 정수로 변환하기
    return tokens

def cut_to_max_length(tokens,max_input_length):
    tokens = tokens[:max_input_length-1]
    return tokens

text_preprocessor = functools.partial(cut_and_convert_to_id,
                                      tokenizer = tokenizer,
                                      max_input_length = max_input_length
                                      )

tag_preprocessor = functools.partial(cut_to_max_length,max_input_length = max_input_length)

TEXT = data.Field(use_vocab = True,
                  lower=True,
                  init_token=init_token_idx,
                  pad_token=pad_token_idx,
                  unk_token=unk_token_idx)

UD_TAGS = data.Field(unk_token=None,
                    init_token='<pad>'
                    ,preprocessing=tag_preprocessor)


def UD_TAGS_to_KOR:
    for i in range(length(UD_TAGS)):
        UD_TAGS[i] == "NOUN" ? "명사" : "NOUN"
        UD_TAGS[i] == "VERB" ? "동사" : "VERB"
        UD_TAGS[i] == "PRON" ? "발음" : "PRON"
        UD_TAGS[i] == "PUNCT" ? "부호" : "PUNCT"
        UD_TAGS[i] == "ADP" ? "" : ""
        #UD_TAGS[i] == "DET" ? "" : ""
        UD_TAGS[i] == "ADJ" ? "형용사" : "ADJ"
        UD_TAGS[i] == "ADV" ? "부사" : "ADV"
        UD_TAGS[i] == "CCONJ" ? "조정 접속사" : "CCONJ"
        #UD_TAGS[i] == "" ? "" : ""
        #UD_TAGS[i] == "" ? "" : ""
        #UD_TAGS[i] == "" ? "" : ""
        #UD_TAGS[i] == "" ? "" : ""
        #UD_TAGS[i] == "" ? "" : ""

fields = (("TEXT",TEXT),("FIELD",UD_TAGS))

train_data, valid_data, test_data = datasets.UDPOS.splits(fields)

print(vars(train_data.examples[0]))



#BATCH_SIZE = 32

#device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

#train_iterator, valid_iterator, test_iterator = data.BucketIterator.splits(
#    (train_data, valid_data, test_data),
#    batch_size = BATCH_SIZE,
#    device = device)
