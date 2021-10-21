import requests

class TestMyProject:
    def test_headers(self):
        url = 'https://playground.learnqa.ru/api/homework_header'
        response = requests.get(url)
        response_dict = dict(response.headers)
        print(response_dict)
        expected_header_key = "x-secret-homework-header"
        expected_header_value = "Some secret value"
        assert response.status_code == 200, "Wrong response code"
        assert expected_header_key in response_dict, f"There is no header '{expected_header_key}' in response"
        current_header = response_dict[expected_header_key]
        assert current_header == expected_header_value, "Actual value of header is not correct"
