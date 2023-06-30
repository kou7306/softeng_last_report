import streamlit as st

#記憶関連
class MemoryPastRecipe:
  def __init__(self):
    self._line = "-" * 100
  
  @property    
  def line(self):
    return self._line 
   
  #過去レシピを記憶
  def memory_recipe(self,responses): 
    if "recipe" not in st.session_state:
      st.session_state["recipe"] = responses[0]
    else:
      st.session_state["recipe"] = st.session_state["recipe"] + "\n\n\n\n\n" + self.line + "\n\n\n" +  responses[0]
      
  #過去の料理名に記憶
  def memory_recipe_name(self, responses):
    target = '::'
    idx = responses[0].find(target)
    recipe_name = responses[0][:idx].strip() if idx != -1 else ""
    if "recipe_name" not in st.session_state:  # 1回目
        st.session_state["recipe_name"] = recipe_name
    else:  # 2回目以降
        st.session_state["recipe_name"] += "," + recipe_name

