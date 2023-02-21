
import os
import openai
import json

class Chatbot :

    openai.organization = "org-Yj4ad5DTjY2lJ33mWITLHsUr"
    openai.api_key = "YOUR-API-KEY"
    # openai.FineTune.create(id="cmpl-6lQi3AckW8rrPcmPKBlTmasrKsdbh")
    

    def __init__(self,question):
        self.question = question
        self.ask()
        

    def ask(self):
        self.ask = askgpt
        prompt = self.question
        
        if prompt == "9" :
            self.Continue = False
        
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            max_tokens=300,
            temperature=0
            )
        print(response)
        text = response["choices"][0]["text"]
        # self.savingResponse(text)
        self.displayResponse(text)



    def displayResponse(self,text):
        self.text = text 
        print("\nChatBot:" ,self.text.strip())

    def savingResponse(self,text):
        pass
    
qNumber = 1
while True :
    question = input(f"\n{qNumber}-Question (To exit please enter '9') : ")
    qNumber += 1
    if question == "9" :
        print("\nChatbot is over.")
        break
    else :
        askgpt = (question)
        Chatbot(askgpt)

    
    
        

        


