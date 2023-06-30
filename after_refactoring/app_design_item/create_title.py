import streamlit as st

# タイトルの作成
class CreateTitle:
  
  def create_title(self):
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