import os
import time
from openai import OpenAI
from dotenv import load_dotenv
import requests
load_dotenv()

tavily_api_key = os.getenv('TAVILY_API_KEY')
openai_api_key = os.getenv('OPENAI_API_KEY')

class IngredientScoutAgent:
    def __init__(self, api_key):
        self.api_key = api_key

    def run(self, data):
        query = data.get('query')
        url = f'https://api.tavily.com/ingredients?query={query}&api_key={self.api_key}'
        response = requests.get(url)
        ingredients = response.json()
        return ingredients

class RecipeCuratorAgent:
    def __init__(self, api_key):
        self.api_key = api_key

    def run(self, data):
        ingredients = data.get('ingredients')
        cuisine = data.get('cuisine')
        # Example using Tavily API to search for recipes
        url = f'https://api.tavily.com/recipes?ingredients={ingredients}&cuisine={cuisine}&api_key={self.api_key}'
        response = requests.get(url)
        recipes = response.json()
        return recipes


class InstructionWriterAgent:
    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key)

    def run(self, data):
        recipe_id = data.get('recipe_id')
        time.sleep(1)
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that generates cooking instructions."},
                {"role": "user", "content": f"Generate cooking instructions for recipe ID {recipe_id}"}
            ]
        )
        instructions = response.choices[0].message.content.strip()
        return instructions



class NutritionAnalyzerAgent:
    def __init__(self, api_key):
        self.api_key = api_key

    def run(self, data):
        recipe_id = data.get('recipe_id')
        # Example using Tavily API to get nutritional information for the recipe
        url = f'https://api.tavily.com/nutrition?recipe_id={recipe_id}&api_key={self.api_key}'
        response = requests.get(url)
        nutrition_info = response.json()
        return nutrition_info

class PresentationDesignerAgent:
    def __init__(self, output_dir):
        self.output_dir = output_dir

    def run(self, data):
        recipes = data.get('recipes')
        # Example: Implement logic to create a presentation document
        # For example, using a library like ReportLab for PDF generation
        # or HTML templates for web-based presentation
        # This example shows a basic placeholder for PDF generation:
        from reportlab.lib.pagesizes import letter
        from reportlab.pdfgen import canvas

        pdf_filename = f'{self.output_dir}/recipes_presentation.pdf'
        c = canvas.Canvas(pdf_filename, pagesize=letter)
        c.drawString(100, 750, "Recipes Presentation")
        y_position = 700
        for recipe in recipes:
            y_position -= 20
            c.drawString(100, y_position, f"Recipe: {recipe['title']}")
            c.drawString(100, y_position - 10, f"Ingredients: {', '.join(recipe['ingredients'])}")
            c.drawString(100, y_position - 20, f"Instructions: {recipe['instructions']}")
            y_position -= 30
        c.save()
        return pdf_filename

class FinalRecipeCompilerAgent:
    def __init__(self, output_dir):
        self.output_dir = output_dir

    def run(self, data):
        recipes = data.get('recipes')
        # Example: Compile recipes into a markdown document
        markdown_content = "# Recipes Compilation\n\n"
        for recipe in recipes:
            markdown_content += f"## {recipe['title']}\n\n"
            markdown_content += f"### Ingredients:\n"
            for ingredient in recipe['ingredients']:
                markdown_content += f"- {ingredient}\n"
            markdown_content += f"\n### Instructions:\n{recipe['instructions']}\n\n"

        markdown_filename = f'{self.output_dir}/recipes_compilation.md'
        with open(markdown_filename, 'w') as f:
            f.write(markdown_content)
        return markdown_filename


