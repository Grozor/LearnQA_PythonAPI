import requests
import pytest


class TestMyProject:
    data_sets = [
        {"header": {'User-Agent': 'Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'}, 'platform': 'Mobile', 'browser': 'No', 'device': 'Android'},
        {"header": {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1'}, 'platform': 'Mobile', 'browser': 'Chrome', 'device': 'iOS'},
        {"header": {'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}, 'platform': 'Googlebot', 'browser': 'Unknown', 'device': 'Unknown'},
        {"header": {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0'}, 'platform': 'Web', 'browser': 'Chrome', 'device': 'No'},
        {"header": {'User-Agent': 'Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'}, 'platform': 'Mobile', 'browser': 'No', 'device': 'iPhone'}
    ]

    def setup(self):
        self.url = "https://playground.learnqa.ru/ajax/api/user_agent_check"

    @pytest.mark.parametrize('data', data_sets)
    def test_user_agent(self, data):
        response = requests.get(self.url, headers=data["header"])
        parsed_response = response.json()
        print(response.text)
        assert parsed_response["platform"] == data["platform"], "There is an incorrect answer for 'platform'"
        assert parsed_response["browser"] == data["browser"], "There is an incorrect answer for 'browser'"
        assert parsed_response["device"] == data["device"], "There is an incorrect answer for 'device'"
