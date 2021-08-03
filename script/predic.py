# -*- coding: utf-8 -*-
"""Untitled28.ipynb

Automatically generated by Colaboratory.

Original file is located at®
    https://colab.research.google.com/drive/1Lj2wEZlXqBqIvBg4yO_UskbhPUvO2gLJ
"""
from googletrans import Translator
from transformers import pipeline
from parser import Parser

translator = Translator()


class Predict:
  def __init__(self):
    self.question_answer = pipeline('question-answering')


  @staticmethod
  def predict(self,subject,sentence,link):
    parser = Parser(link)
    print("loading...")
    if len(parser.saveParser()) != 0 and len(sentence) == 0:
     sentence = parser.saveParser()
    elif len(parser.saveParser()) == 0:
      pass
    result = translator.translate(subject,dest='en')
    translated_input = result.text
    if float(self.question_answer({'question':translated_input,'context':sentence})['score']) < 0.2:
      return "the score is under 20%! be careful to crawl the data what you get!!\n" + "   result : " + str(self.question_answer({'question': translated_input,'context':sentence})['answer']) + "    percentage : " + str(round(self.question_answer({'question': translated_input,'context':sentence})['score'] * 100,1)) + "%"
    return "result : "  +  str(self.question_answer({'question': translated_input,'context':sentence})['answer']) + "    percentage : " + str(round(self.question_answer({'question': translated_input,'context':sentence})['score'] * 100,1)) + "%"


