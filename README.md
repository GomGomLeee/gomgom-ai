# gomgom-ai
똑똑한 곰곰이 만들기

<br>

<h3>1. 가상환경 설정</h3>

<br>

가상환경 만들 위치로 이동

```shell
cd '가상환경을 만들 위치'
```

<br>

가상환경 만들기

```shell
python3 -m venv '가상환경 이름'
```

<br>

가상환경 접속
```shell
source '가상환경 이름/bin/activate'
```

<br>

--- 

<br>

<h3>2. Open API 키 가져오기</h3>

<br>

openai.com 에서 가입하고 API 키 생성

<br>

---

<br>

<h3>3. OpenAI Python 라이브러리 설치</h3>

<br>

터미널 혹은 명령 프롬프트에서 다음 명령 실행
```shell
pip3 install openai
```

<br>

---

<br>

<h3>4. API 키 설정</h3>

<br>

API 키를 설정해야 파이썬 코드에서 사용 가능
터미널에서 다음 명령어 실행, 이 세션은 해당 터미널에서만 유효

```shell
export OPENAI_API_KEY="KEY"
```

<br>

---

<br>

<h3>5. 파이썬 코드 작성 및 실행</h3>

<br>

```python
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
```

__실행 시 run code가 아니라 run python__