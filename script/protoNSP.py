from torch.nn.functional import softmax
from transformers import BertForNextSentencePrediction, BertToknizer


class NSP:

    BATCH_SIZE = 16
    model = BertForNextSentencePrediction.from_pretrained('bert-base-cased')
    toknizer = BertToknizer.from_pretrained('bert-base-cased')

    def toknizing(sentence):

        return toknizer.encode_plus(
        sentence,
        return_attention_mask=True,
        return_tensors='pt',
        )



    def process(tokenized_sentence):

        seq_relationship_logits = model(**toknized_sentence[0])
        probs = softmax(seq_relationship_logits,dim=1)

        return probs


#if __name__ == "__main__":
#    toknizing(sentence)
#    process(toknized_sentence)
