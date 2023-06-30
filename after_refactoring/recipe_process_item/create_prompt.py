# プロンプト作成
class CreatePrompt:
  # 1回目のプロンプト作成
  def first_create_prompt(self,searched_ingredients):
    
    prompt = f"""
    {searched_ingredients}だけを使った料理のレシピを1個表示して。ただし、最初にその料理名を書き、料理名の直後に"":""と書いた後、改行し、材料とその量を箇条書きにしてから、作り方を書いて。
    例
    カレー::
    
        材料:
        
        -人参:20グラム
        -豚肉:100グラム
        
        
        作り方:
        
        1. フライパンにバターとオリーブオイルを加えて、中火にかける。
        2. 玉ねぎを加えて、柔らかくなるまで約30分間煮込む。
    """
    return prompt
  
  # 2回目以降のプロンプト作成
  def after_create_prompt(self,past_recipe_name,searched_ingredients):
    prompt = f"""
    {past_recipe_name}といったこれらの料理以外で、{searched_ingredients}だけを使った料理のレシピを1個表示して。ただし、最初にその料理名を書き、料理名の直後に"":""と書いた後、改行し、材料とその量を箇条書きにしてから、作り方を書いて。
    例
    カレー::
    
        材料:
        
        -人参:20グラム
        -豚肉:100グラム
        
        
        作り方:
        
        1. フライパンにバターとオリーブオイルを加えて、中火にかける。
        2. 玉ねぎを加えて、柔らかくなるまで約30分間煮込む。
    """
    
    return prompt