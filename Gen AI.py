import ollama
model_name='deepseek-r1:1.5b'
messages=[{"role":"system","content":"hello what i can do for you "},
          {"role":"user","content":"hello"}]
response=ollama.chat(model=model_name,messages=messages)
print("Bot",response.message.content)

while True:
    user_input=input("you:")
    if not user_input:
        break
    messages.append({"role":"user","content":user_input})
    response=ollama.chat(model=model_name,messages=messages)
    answer=response.message.content
    print("bot:",answer)
    messages.append({"role":"assistant","content":answer})
