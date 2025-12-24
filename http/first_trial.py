import requests

response = requests.get('https://chat.deepseek.com/a/chat/s/0bcc234f-5e06-49e8-b90b-8be681bc9193')
print(response.status_code)
print(response.text)
