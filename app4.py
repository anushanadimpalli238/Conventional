import ollama 
print("AI chatbot")
lis=[]
while True:
    you=input("you:")
    if(you.lower()=="exit"):
        print("Good bye")
        break 
    lis.append({"role":"user",
                    "content":you})

    response=ollama.chat(
        model="llama3.2",
        messages=lis
                 ) 
    ai_response=response["message"]["content"]
    print("bot:",ai_response)

    lis.append({"role":"assistant",
                "content":ai_response}) 
for i in lis:
    if lis["role"]=="user":
        print("you:",lis["content"])
    else:
        print("bot:",lis["content"])
    
