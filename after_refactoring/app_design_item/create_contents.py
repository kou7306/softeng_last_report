import streamlit as st

# コンテンツの作成
class CreateContents:
  def create_contents(self):
    # サブタイトル
    contents = """
    余った食材で料理を作ろう！！
    """
    st.markdown(contents)
    
    # テキストボックス
    ingredients = st.text_input('食材を句読点（、）で区切って入力')
    return ingredients