import streamlit as st 
from recipe_process_item.chatgpt_handler import ChatGPTHandler

#結果の出力
class OutputRecipe:
  def __init__(self):
    self._timeholder = st.empty()
    self._responses = [""]
  
  @property    
  def timeholder(self):
    return self._timeholder 
  
  @property    
  def responses(self):
    return self._responses   
  
  def output_recipe(self,prompt):
    answer = ChatGPTHandler().ans_chat_gpt(prompt,self.responses)
    #リアルタイム出力
    for talk in answer:
      self.timeholder.text(talk)
    return self.responses