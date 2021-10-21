import requests

class TestMyProject:
    def test_cookies(self):
        url = 'https://playground.learnqa.ru/api/homework_cookie'
        expected_cookie = "hw_value"
        response = requests.get(url)
        response_dict = dict(response.cookies)
        print(response_dict)
        assert response.status_code == 200, "Wrong response code"
        assert "HomeWork" in response_dict, "There is no cookie 'HomeWork' in response"
        current_cookie = response_dict["HomeWork"]
        assert current_cookie == expected_cookie, "Actual value of cookie is not correct"

