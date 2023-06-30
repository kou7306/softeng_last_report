from app_design_item.create_title import CreateTitle
from app_design_item.create_contents import CreateContents
from app_design_item.create_search_button import CreateSearchButton
from app_design_item.create_more_button import CreateMoreButton

class AppDesign:
  def __init__(self):
    self._create_title = CreateTitle()
    self._create_contents = CreateContents()
    self._create_search_button = CreateSearchButton()
    self._create_more_button = CreateMoreButton()

  # タイトル作成
  def create_title(self):
    self._create_title.create_title()
   
  # コンテンツ作成 
  def create_contents(self):
    return self._create_contents.create_contents()
  
  # 検索ボタンの作成
  def create_search_button(self):
    return self._create_search_button.create_search_button()
  
  # もっと見るボタンの作成
  def create_more_button(self):
    return self._create_more_button.create_more_button()