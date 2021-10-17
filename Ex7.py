import requests

print("Part 1.")
response_of_request_without_method = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type")
print("Request without method returns: ", response_of_request_without_method.text)

print("Part 2.")
response_of_unused_method = requests.options("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": "OPTIONS"})
print("Request with unused method returns: ", response_of_unused_method.text)

print("Part 3.")
response_of_correct_method = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params={"method": "GET"})
print("Request with correct method returns: ", response_of_correct_method.text)

print("Part 4.")
tested_methods = ["POST", "GET", "PUT", "DELETE"]

for tested_method in tested_methods:
    response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type",
                             data={"method": tested_method})
    print(f"POST request with tested method '{tested_method}' returns: ", response.text)

    response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type",
                            params={"method": tested_method})
    print(f"GET request with tested method '{tested_method}' returns: ", response.text)

    response = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type",
                            data={"method": tested_method})
    print(f"PUT request with tested method '{tested_method}' returns: ", response.text)

    response = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type",
                            data={"method": tested_method})
    print(f"DELETE request with tested method '{tested_method}' returns: ", response.text)
