from config import *


class openAI():
    def __init__(self) -> None:
        self.header = ""
        self.url = ""
        
    def requestModels(self):
        
        self.header = {
            "Authorization": f"Bearer {OPENAI_API_KEY}"
        }

        self.url = "https://api.openai.com/v1/models"
        request = requests.get(self.url, headers=self.header)

        if request.status_code == 200:
            models = request.json()
            display(models)
        else:
            print(request)
    
    def requestingAI(self):
        self.url = "https://api.openai.com/v1/chat/completions"

    
        with open("output.txt", "r", encoding='latin-1') as f:
            file = f.read()
        
        self.header = {
            "Authorization": f"Bearer {OPENAI_API_KEY}",
            "Content-Type": "application/json"
        }

        body_message ={ 
            "model": "gpt-3.5-turbo",
            "messages": [{"role": "user", "content": f"Quais bancos de dados relacionais são mais requisitados nas vagas?: {file} "}]
        }

        retorno = requests.post(self.url, headers=self.header, data=json.dumps(body_message))

        if retorno.status_code == 200:
            chat_gpt = retorno.json()
            print(chat_gpt['choices'][0]['message']['content'])
        else:
            print(retorno.status_code)
            print(retorno.text)