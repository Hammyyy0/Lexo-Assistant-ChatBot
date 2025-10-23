import openai

while True:
    
    
    client = openai.OpenAI(api_key="YOUR_API_KEY")
    prompt = input("You: ")
   

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    if prompt == "Goodbye".strip().lower() or prompt == "break".strip().lower():
        print(f"Lexo:", 'Goodbye')
        break
    else:
        print()
        print(f"Lexo:",response.choices[0].message.content)
        
      
        continue