# Multi-Agent Recipe Generator

- This Python application demonstrates a multi-agent system for generating recipes using various APIs and services.   
- Create a team of AI agents that work together to generate a personalized recipe based on user preferences.


## Project Overview

### Design:   
- **Ingredient Scout Agent**: Scans databases and user input to gather a list of available ingredients.
- **Recipe Curator Agent**: Filters and selects recipes that match the user's dietary preferences and available ingredients.
- **Instruction Writer Agent**: Crafts clear, step-by-step cooking instructions.
- **Nutrition Analyzer Agent**: Analyzes the nutritional content of the recipe.
- **Presentation Designer Agent**: Provides plating and presentation suggestions.
- **Final Recipe Compiler Agent**: Compiles the recipe and presentation into a user-friendly format.

### Frameworks and APIs:

 - **LangGraph**:
 1. Utilize the LangGraph framework to design and manage the workflow of AI agents.
 2. Agents will interact and pass information in a cyclical manner, ensuring iterative improvement and refinement.

 - **Tabily API**:
 1. Use the Tavily API for reliable data retrieval and integration of external recipe databases.
 2. Incorporate RAG to enhance the reliability and quality of recipe suggestions.
   

## Installation

1. Clone the repository:
   git clone https://github.com/your_username/your_repository.git   
   cd your_repository
   
2. Set up environment variables:
   - Create a .env file in the root directory.
   - Add your API keys:   
     TAVILY_API_KEY=your_tavily_api_key   
     OPENAI_API_KEY=your_openai_api_key

## Usage
- Input your dietary preferences and available ingredients.
- Receive a personalized recipe with detailed instructions and nutritional analysis.

## Contribution
- Fork the repository and create a pull request.
- Report issues or suggest features.

## Conclusion
- This project demonstrates the potential of multi-agent systems in creating personalized culinary experiences. The collaboration of specialized agents ensures a high-quality, user-friendly output.

## Future Work
- Expand the agent capabilities to include more complex culinary tasks.
- Integrate more external databases for diverse recipe suggestions.
- Improve the user interface for a better experience.
