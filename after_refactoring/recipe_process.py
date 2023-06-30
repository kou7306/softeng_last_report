
from recipe_process_item.create_prompt import CreatePrompt 
from recipe_process_item.display_past_recipe import DisplayPastRecipe
from recipe_process_item.memory_past_recipe import MemoryPastRecipe
from recipe_process_item.output_recipe import OutputRecipe

class RecipeProcess:
    def __init__(self):
        self._create_prompt = CreatePrompt()
        self._display_past_recipe = DisplayPastRecipe()
        self._memory =  MemoryPastRecipe()
        self._output_recipe =  OutputRecipe()
    
    

    
    #1回目のプロンプト作成
    def first_create_prompt(self,searched_ingredients):
        return self._create_prompt.first_create_prompt(searched_ingredients)     
    
    #2回目以降のプロンプト作成
    def after_create_prompt(self,past_recipe_name,searched_ingredients):
        return self._create_prompt.after_create_prompt(past_recipe_name,searched_ingredients)
    
    #過去のレシピを表示
    def display_past_recipe(self):
        self._display_past_recipe.display_past_recipe()
        
    #過去のレシピを記憶
    def memory_recipe(self,responses):
        self._memory.memory_recipe(responses)
        
    #過去のレシピ名を記憶   
    def memory_recipe_name(self,responses):
        self._memory.memory_recipe_name(responses)
        
    #結果出力
    def output_recipe(self,prompt):
        responses = self._output_recipe.output_recipe(prompt)
        return responses