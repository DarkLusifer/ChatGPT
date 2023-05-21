import openai

openai.api_key = "OPENAI_API_KEY"

print(" Hi! I'm a AIChatbot... Ask me anything : )\n   \n    ")

q = input("Ask Q : ")
completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": q}])
print (completion.choices[0].message.content)
