import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect")
redirect_history = response.history
print(f"The count of redirections is: {len(redirect_history)}")
final_url = response.url
print(f"The final URL of redirection is: {final_url}")
