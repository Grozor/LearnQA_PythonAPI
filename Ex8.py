import json

import requests
import time
status_of_running_job = "Job is NOT ready"
status_of_ended_job = "Job is ready"

started_job = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
token = started_job.json()['token']
print(f"The job has been created with token '{token}'")
time_to_end_of_job = started_job.json()['seconds']
print("Time to end of the job =", time_to_end_of_job)
running_job = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token": token})
status_of_current_job = running_job.json()['status']
assert status_of_current_job == status_of_running_job, print("Panic! Status of current job is not correspond to running")
print()
print(f"Status: '{status_of_current_job}'. This status is correct for a task that is still in progress.")
print()
print(f"Waiting for {time_to_end_of_job} seconds...")
print()
time.sleep(time_to_end_of_job)
print("Request for status and job result:")
ended_job = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token": token})
status_of_current_job = ended_job.json()['status']
result_of_ended_job = ended_job.json()['result']
assert status_of_current_job == status_of_ended_job, print("Panic! Status of current job is not correspond to ended.")
print(f"Status:'{status_of_current_job}'. This status is correct for a task that has been completed.")
assert result_of_ended_job is not None
print(f"Result: {result_of_ended_job}")
