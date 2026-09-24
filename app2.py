
import ollama
print("AI CHATBOT")
print("Type exit if you want to stop the process") 
while True:
    you=input("you:")
    if you.lower()=="exit":
        print("good bye")
        break
    response=ollama.chat(
            model="llama3.2",
            messages=[{"role":"user",
                       "content":you}]) 
    print("bot:",response["message"]["content"]) 
 
