import requests
import pytest
import user_info

#URL link of API
url = ""

def test_api_request():
  response = requests.get(url)
  assert (url.status_code == 200), "Status code is not 200. Rather found: " + str(url.status_code)
  for record in url.json()['data']:
    if record['id'] == 4:
      assert record['first_name'] == "Eve",\
         "Data not matched! Expected: Eve, but found: " + str(record['first_name'])
      assert record['last_name'] == "Holt",\
         "Data not matched! Expected: Holt, but found: " + str(record['last_name'])

def test_api_response():
  response = requests.post(url="",data=user_info.data)
  user_info.data = response.json()
  assert (response.status_code == 201), "Status code is not 201. Rather found: " + str(response.status_code)
  assert user_info.data['name'] == "Simon", "User created with wrong name. \
     Expected: Simon, but found: " + str(user_info.data['name'])
  assert user_info.data['job'] == "QA", "User created with wrong job. \
     Expected: QA, but found: " + str(user_info.data['job'])
                                                    
