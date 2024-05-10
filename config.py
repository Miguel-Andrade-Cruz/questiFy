from pathlib import Path
import hashlib
import google.generativeai as genai

MODEL = ""

# -------------------------------------
# ---------DEFAULT SETTINGS------------
# -------------------------------------
generation_config = {
    "temperature": 0.9,
    "top_p": 0.95,
    "top_k": 32,
    "max_output_tokens": 1024,
}


safety_settings = [
    {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
]


model_name = "models/gemini-pro"
# -----------------------------------
# -----------------------------------
# -----------------------------------

def insertKey(key):
    genai.configure(api_key = key)


def chooseModel(model_name = model_name, generation_config = generation_config, safety_settings = safety_settings):
    model = genai.GenerativeModel(
        model_name=model_name,
        generation_config=generation_config,
        safety_settings=safety_settings
    )

    return model



def sendSimplePrompt(message: str, attach: (list | str) = False):
    
    if(not attach):
        return MODEL.generate_content([message]).text

    elif(type(attach) == list):
        print(attach + message)
        return MODEL.generate_content(attach + message).text
    


    return MODEL.generate_content([message, attach]).text




def prepareFile(path: str):
    return genai.upload_file(path)


def chatSession(prompt):
    chat = MODEL.start_chat()

    response = chat.send_message(prompt)

    return response.text