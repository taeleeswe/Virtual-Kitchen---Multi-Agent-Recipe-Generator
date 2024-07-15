import os
import time
from concurrent.futures import ThreadPoolExecutor
from langgraph.graph import Graph
from dotenv import load_dotenv
import sys
from agents import (
    IngredientScoutAgent,
    RecipeCuratorAgent,
    InstructionWriterAgent,
    NutritionAnalyzerAgent,
    PresentationDesignerAgent,
    FinalRecipeCompilerAgent
)

load_dotenv()
sys.path.append('/path/to/your/langchain')

class RecipeMasterAgent:
    def __init__(self):
        self.output_dir = f"outputs/run_{int(time.time())}"
        os.makedirs(self.output_dir, exist_ok=True)

    def run(self, queries: list):
        # Initialize agents with API keys
        ingredient_agent = IngredientScoutAgent(api_key=os.getenv('TAVILY_API_KEY'))
        recipe_agent = RecipeCuratorAgent(api_key=os.getenv('TAVILY_API_KEY'))
        instruction_agent = InstructionWriterAgent(api_key=os.getenv('OPENAI_API_KEY'))
        nutrition_agent = NutritionAnalyzerAgent(api_key=os.getenv('TAVILY_API_KEY'))
        presentation_agent = PresentationDesignerAgent(output_dir=self.output_dir)
        compiler_agent = FinalRecipeCompilerAgent(output_dir=self.output_dir)

        # Define Langchain graph
        workflow = Graph()

        # Add nodes for each agent
        workflow.add_node("ingredient_scout", ingredient_agent.run)
        workflow.add_node("recipe_curator", recipe_agent.run)
        workflow.add_node("instruction_writer", instruction_agent.run)
        workflow.add_node("nutrition_analyzer", nutrition_agent.run)
        workflow.add_node("presentation_designer", presentation_agent.run)
        workflow.add_node("final_compiler", compiler_agent.run)

        # Define edges
        workflow.add_edge('ingredient_scout', 'recipe_curator')
        workflow.add_edge('recipe_curator', 'instruction_writer')
        workflow.add_edge('instruction_writer', 'nutrition_analyzer')
        workflow.add_edge('nutrition_analyzer', 'presentation_designer')
        workflow.add_edge('presentation_designer', 'final_compiler')

        # Set entry and finish points
        workflow.set_entry_point("ingredient_scout")
        workflow.set_finish_point("final_compiler")

        # Compile the graph
        chain = workflow.compile()

        # Execute the chain in parallel for each query
        with ThreadPoolExecutor() as executor:
            results = list(executor.map(lambda q: chain.invoke({'query': q}), queries))

        # Example result handling (modify as per your application's needs)
        return results

if __name__ == "__main__":
    # Example usage:
    queries = ["chicken", "pasta", "cake"]
    master_agent = RecipeMasterAgent()
    results = master_agent.run(queries)
    print("Results:", results)