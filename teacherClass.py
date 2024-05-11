import config as cfg
import metadata as mtdt
from typing import Union


#-------------------CLASS TEACHER-----------------------
class Teacher:
    def __init__(this, name: str, theme: str):
        this.name = name
        this.theme = theme



    def simpleAsk(this, message: str, attach: Union[str, list, bool] = False):
        prompt = f"Lembrando que sou um professor de {this.theme}, {message}"
        
        if(not attach):
            return cfg.sendSimplePrompt(prompt)
        
        response = cfg.sendSimplePrompt(prompt, attach)
        
        
        return response


    def requestQuestions(this, content: str, questions_quantity: str, question_type: str) -> str:
        
        prompt = [
            f"Matéria: {this.theme}",
            f"Conteúdo: {content}",
            f"recursos: {questions_quantity} questões, {question_type}"
        ]

        prompt = mtdt.data + prompt

        response = cfg.sendPrompt(prompt)

        return response


#--------------------------------------------------------




def addNewTeacher(name, theme):
    return Teacher(name, theme)