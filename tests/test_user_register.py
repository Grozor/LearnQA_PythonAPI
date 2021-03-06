import pytest
import string
import random
import allure

from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions

TEST_CASE_LINK = 'https://github.com/Grozor/LearnQA_PythonAPI/tree/master/tests'
class TestUserRegister(BaseCase):
    exclude_fields = ["password", "username", "firstName", "lastName", "email"]
    huge_firstname = ''.join(random.choice(string.ascii_lowercase) for i in range(251))
    email_without_at = "learnqaexample.com"

    @allure.testcase(TEST_CASE_LINK, 'Test case title')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_user_successfully(self):
        data = self.prepare_registration_data()

        response = MyRequests.post("/user", data=data)
        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")

    @allure.testcase(TEST_CASE_LINK, 'Test case title')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        data = self.prepare_registration_data(email)

        response = MyRequests.post("/user", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode(
            "utf-8") == f"Users with email '{email}' already exists", f"Unexpected response content '{response.content}'"

    @allure.testcase(TEST_CASE_LINK, 'Test case title')
    @allure.severity(allure.severity_level.NORMAL)
    def test_create_user_without_at(self):
        data = self.prepare_registration_data(self.email_without_at)

        response = MyRequests.post("/user", data=data)
        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"Invalid email format"

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize("exclude_field", exclude_fields)
    def test_create_user_without_one_field(self, exclude_field):
        data = {
            'password': '123',
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': 'learnqa@example.com'
        }

        del data[exclude_field]

        response = MyRequests.post("/user", data=data)
        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"The following required params are missed: {exclude_field}"

    @allure.severity(allure.severity_level.NORMAL)
    def test_create_user_with_short_firstname(self):
        data = {
            'password': '123',
            'username': 'learnqa',
            'firstName': 'l',
            'lastName': 'learnqa',
            'email': 'learnqa@example.com'
        }

        response = MyRequests.post("/user", data=data)
        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"The value of 'firstName' field is too short"

    def test_create_user_with_huge_firstname(self):
        data = {
            'password': '123',
            'username': 'learnqa',
            'firstName': self.huge_firstname,
            'lastName': 'learnqa',
            'email': 'learnqa@example.com'
            }

        response = MyRequests.post("/user", data=data)
        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"The value of 'firstName' field is too long"
