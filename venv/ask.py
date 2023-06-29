import os
import openai

openai.api_key = os.environ['OPENAI_API_KEY']

def ask_gpt(prompt):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=100,
        temperature=0.7,
        n=1,
        stop=None,
        # temperature=0.7,
    )
    return response.choices[0].text.strip()

# Chat GPT로 대화하기
user_input = input("사용자: ")
while user_input.lower() != '종료':
    response = ask_gpt(user_input)
    print("ChatGPT:", response)
    user_input = input("사용자: ")
