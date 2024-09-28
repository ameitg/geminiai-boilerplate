import google
import google.generativeai as genai


from dotenv import load_dotenv
load_dotenv()
import os
from getTextFromUrl import getTextFromUrl

genai.configure(api_key=os.environ['GEMINI_API_KEY'])

# Function to load the text and pass it to the model
def getAnswerFromText(text, question):
    # Prepare prompt with text content
    prompt = f"""
    You are provided with the following text:
    '{text}'
    
    Based on this text, answer the following question: {question}
    """
    
    # Use gemini's completion API to get an answer based on the text
    model = genai.GenerativeModel("gemini-1.5-flash")
        
    response = model.generate_content([question,text])
    
    # Return the answer
    return response
webpage_text = getTextFromUrl("https://profile.amitg.pro")
response=getAnswerFromText(webpage_text, "Show skills related to Technical project manager  with employer name")
print(response.text)

print("Answer:", response)
