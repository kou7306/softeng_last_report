import streamlit as st 

#過去レシピの表示
class DisplayPastRecipe:
  def __init__(self):
    self._line = "-" * 100
    
  @property    
  def line(self):
    return self._line
  
     
  def display_past_recipe(self):
    st.text(st.session_state["recipe"])
    st.text(f"\n\n\n\n\n{self.line}\n\n\n")