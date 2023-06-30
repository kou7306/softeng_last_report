import streamlit as st

# 検索ボタンの作成
class CreateSearchButton:
  def create_search_button(self):
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
    return search_button