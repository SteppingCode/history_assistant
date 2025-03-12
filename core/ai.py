from ollama import chat


def get_ai_response(question: str):
    response = chat(model='llama3.2:3b', messages=[
        {
            'role': 'user',
            'content': question
        }
    ])
    return response.message.content