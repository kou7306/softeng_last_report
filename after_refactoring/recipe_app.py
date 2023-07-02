import streamlit as st
from recipe_process import RecipeProcess
from app_design import AppDesign


# タイトル作成
AppDesign().create_title()

# コンテンツ作成
ingredients = AppDesign().create_contents()


#count記憶の作成、検索ボタンが押されたかどうか
if "count" not in st.session_state:
    st.session_state["count"] = 0

# 検索ボタン作成
search_button = AppDesign().create_search_button()

#何も入力されていない場合
if(st.session_state["count"] ==0 and search_button and len(ingredients)==0):
  st.text("食材を入力してください")
  
  
#検索実行、1回目
if(st.session_state["count"] ==0 and search_button and len(ingredients)!=0 ): 
  #ここからの処理をまとめる、2回目以降も
  st.session_state["count"] += 1 #検索フラグセット
  st.session_state["ingredients"] = ingredients #検索している食材情報を記憶
  # プロンプト作成
  prompt = RecipeProcess().first_create_prompt(st.session_state["ingredients"])
  #chatgptに渡して、結果を画面出力
  responses = RecipeProcess().output_recipe(prompt)
  #レシピを記憶
  RecipeProcess().memory_recipe(responses)
  #レシピ名を記憶
  RecipeProcess().memory_recipe_name(responses)



# 2回目以降
if(st.session_state["count"]>1):
  RecipeProcess().display_past_recipe()#過去の料理の出力を表示
  #プロンプト作成
  prompt =  RecipeProcess().after_create_prompt(st.session_state["ingredients"],st.session_state["recipe_name"])
  #chatgptに渡して、結果を画面出力
  responses = RecipeProcess().output_recipe(prompt)
  #レシピを記憶
  RecipeProcess().memory_recipe(responses) 
  #レシピ名を記憶
  RecipeProcess().memory_recipe_name(responses)
  st.session_state["count"] += 1
  if(st.session_state["count"]==4): #4回目で終了
    st.session_state["count"]=0
if(st.session_state["count"]>0):
  if(st.session_state["count"]==1): # もっと見るボタンの表示
    st.session_state["count"] += 1

  # もっと見るボタン作成
  more_button = AppDesign().create_more_button()

