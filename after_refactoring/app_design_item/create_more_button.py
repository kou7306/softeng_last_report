import streamlit as st

# もっと見るボタンの作成
class CreateMoreButton:
  def create_more_button(self):
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
    
    return more_button