import os
import anthropic
from reflectionEX import *


# Generate API KEY from OPENAI website and define as a variable.
os.environ["ANTHROPIC_API_KEY"] = "YOUR_API_KEY" # Replace with your actual API key

# Model Name
MODEL_NAME = "claude-3-5-sonnet-20240620"

# Defind the maximum tokens for the model
MAX_TOKENS = 1000


# Question to be asked
QUERY = "What is the potential impact of Chinese price war on Thailand economy?"

# Role of Respondent
ROLE_1 = """You are expert economist.'"""

# Details to be checked in the response
REFLECTION_CONTENT1 = """You are expert editor and expert economist.
                        Your role is reading user's input and finding the perspective that not in user's input.
                        You can write more about your opinion in the perspective that you found.
                        In the parts, that you are agree with, you can follow the same content.
                        In the parts, that you are not agree with, you can edit it.
                        Then, write it all again"""

# Final Adjustment Content
FINAL_REFLECTION_CONTENT = """You are expert editor and expert economist.
                             rewrite it with fluent language."""




# Create the language model
LLM1 = anthropic.Anthropic()

# Call the economist function with the query and model
RESPONSE_ECONOMIST= economist(query=QUERY, max_tokens=MAX_TOKENS, llm=LLM1, model_name=MODEL_NAME, role=ROLE_1)
# Reflect on the response from the economist
REFLECYION_RESPONSE_ECONOMIST = reflection(query=RESPONSE_ECONOMIST, max_tokens=MAX_TOKENS, llm=LLM1, model_name=MODEL_NAME, reflection_content=REFLECTION_CONTENT1)
# Make the sentence fluent and easy to read
FINAL_RESPONSE = final_reflection(query=REFLECYION_RESPONSE_ECONOMIST,llm=LLM1, max_tokens=MAX_TOKENS, model_name=MODEL_NAME, reflection_content=FINAL_REFLECTION_CONTENT)


# Print the final response
print(FINAL_RESPONSE)