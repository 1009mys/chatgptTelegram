import copy
import os

class options:
    def __init__(self) -> None:
        self.my_token = os.environ['TOKEN']   #토큰을 변수에 저장합니다.
        self.my_openAI_api_key = os.environ['API_KEY']

        self._default_options = {
            "model": 'gpt-3.5-turbo',
            "messages": []
        }

        self.options = copy.deepcopy(self._default_options)

    def addMessage(self, role: str, message: str):
        self.options["messages"].append({'role': role, 'content' : message})
    
    def printMessage(self):
        print(self.options["messages"])

    def resetOptionAll(self):
        self.options = copy.deepcopy(self._default_options)

    def resetOption(self, option):
        self.options[option] = copy.deepcopy(self._default_options[option])

    def setModel(self, modelName):
        self.options["model"] = modelName