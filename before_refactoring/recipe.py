import streamlit as st
import openai
import json

# キーの読み取り
with open('secret.json') as f:
  secret = json.load(f)
KEY = secret['KEY']
openai.api_key = KEY


responses = [""]
r = ""

# API応答に関して
def Ans_ChatGPT(question,responses):
  completion = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": "You are a cooking professional"},
      {"role" : "user","content" : question}  
    ],
    stream = True
  )
  # responseに出力していく
  # response = completion.choices[0].message.content
  response = ""
  for chunk in completion:
    if chunk:
      content = chunk['choices'][0]['delta'].get('content')
      if content:
        response += content
        responses[0] += content
        yield response



# タイトルの装飾用のCSSスタイル
title_style = """
    <style>
    .title {
        color: #3366ff;
        font-size: 32px;
        text-align: center;
        border-bottom: 2px solid #3366ff;
        padding-bottom: 10px;
        margin-bottom: 20px;
    }
    </style>
"""

# タイトルの表示と装飾
st.markdown(title_style, unsafe_allow_html=True)
st.markdown("<h1 class='title'>レシピ検索</h1>", unsafe_allow_html=True)  



comment = """
余った食材で料理を作ろう！！
"""
st.markdown(comment)


ingredients = st.text_input('食材を句読点（、）で区切って入力')

#flag記憶の作成、検索ボタンが押されたかどうか
if "flag" not in st.session_state:
    st.session_state["flag"] = 0


# "検索" ボタンの装飾用のCSSスタイル
search_button_style = f"""
    <style>
      div.stButton > button:first-child  {{
        font-weight  : bold                ;/* 文字：太字                   */
        border       :  5px solid blue     ;/* 枠線：ピンク色で5ピクセルの実線 */
        border-radius: 10px 10px 10px 10px ;/* 枠線：半径10ピクセルの角丸     */
        background   : #ddd                ;/* 背景色：薄いグレー            */
      }}
    </style>
    """
# "検索" ボタンの表示と装飾
st.markdown(search_button_style, unsafe_allow_html=True)
search_button = st.button("レシピ検索")





# 区切り線
line = "-" * 100 



if(st.session_state["flag"] ==0 and search_button and len(ingredients)==0): #何も入力されていない
  st.text("食材を入力してください")
if(st.session_state["flag"] ==0 and search_button and len(ingredients)!=0 ): #検索実行、1回目
  
  st.session_state["flag"] += 1 #検索フラグセット
  timeHolder = st.empty()
  st.session_state["ingredients"] = ingredients #検索している食材情報を記憶
  a = st.session_state["ingredients"]
  # プロンプト作成
  question = f"""
  {a}だけを使った料理のレシピを1個表示して。ただし、最初にその料理名を書き、料理名の直後に""::""と書いた後、改行し、材料とその量を箇条書きにしてから、作り方を書いて。
  例
  カレー:
  
      材料:
      
      -人参:20グラム
      -豚肉:100グラム
      
      
      作り方:
      
      1. フライパンにバターとオリーブオイルを加えて、中火にかける。
      2. 玉ねぎを加えて、柔らかくなるまで約30分間煮込む。
  """
  ans = Ans_ChatGPT(question,responses)
  #リアルタイム出力
  for talk in ans:
    timeHolder.text(talk)
  
  
  st.session_state["recipe"] = responses[0] #料理のレシピを記憶
  
  target = '::'
  idx = responses[0].find(target)
  r+=responses[0][:idx]
  st.session_state["ans_except"]=r #過去の料理名に記憶
  
# 2回目以降
if(st.session_state["flag"]>1):
  
  #過去の料理の出力を表示
  st.text(st.session_state["recipe"])
  # st.text(st.session_state["ans_except"])
  st.text(f"\n\n\n\n\n{line}\n\n\n")
  timeHolder = st.empty()
  a = st.session_state["ingredients"] #材料
  b= st.session_state["ans_except"]
  #プロンプト作成
  question = f"""
  {b}といったこれらの料理以外で、{a}だけを使った料理のレシピを1個表示して。ただし、最初にその料理名を書き、料理名の直後に""::""と書いた後、改行し、材料とその量を箇条書きにしてから、作り方を書いて。
  例
  カレー:
  
      材料:
      
      -人参:20グラム
      -豚肉:100グラム
      
      
      作り方:
      
      1. フライパンにバターとオリーブオイルを加えて、中火にかける。
      2. 玉ねぎを加えて、柔らかくなるまで約30分間煮込む。
  """
  ans = Ans_ChatGPT(question,responses)
  # リアルタイム出力
  for talk in ans:
    timeHolder.text(talk)
  #過去レシピに追加
  st.session_state["recipe"] = st.session_state["recipe"] + "\n\n\n\n\n" + line + "\n\n\n" +  responses[0]
  #料理名を記憶
  target = '::'
  idx = responses[0].find(target)
  r+=responses[0][:idx]
  st.session_state["ans_except"] = st.session_state["ans_except"] + "," + r #過去の料理名に追加
  st.session_state["flag"] += 1
  if(st.session_state["flag"]==4): #4回目で終了
    st.session_state["flag"]=0
if(st.session_state["flag"]>0):
  if(st.session_state["flag"]==1):
    st.session_state["flag"] += 1
    #もっと見るボタン
  more_button_style = f"""
    <style>
      div.stButton > button:first-child + button  {{
        font-weight  : bold                ;/* 文字：太字                   */
        border       :  3px solid black     ;/* 枠線：ピンク色で5ピクセルの実線 */
        border-radius: 10px 10px 10px 10px ;/* 枠線：半径10ピクセルの角丸     */
        background   : #ddd                ;/* 背景色：薄いグレー            */
      }}
    </style>
    """

    # "もっと見る" ボタンの表示と装飾
  st.markdown(more_button_style, unsafe_allow_html=True)
  more_button = st.button("もっと見る")



