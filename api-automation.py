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
  response = requests.post(url="", data=user_info.data)
  user_info.data = response.json()
  assert (response.status_code == 201), "Status code is not 201. Rather found: " + str(response.status_code)
  assert user_info.data['name'] == "Simon", "User created with wrong name. \
     Expected: Simon, but found: " + str(user_info.data['name'])
  assert user_info.data['job'] == "QA", "User created with wrong job. \
     Expected: QA, but found: " + str(user_info.data['job'])
                                                    
def test_create_user():
  response = requests.post(url, json=user_info.new_data)
  assert response.status_code == 201
  user_info.data = response.json()
  assert "id" in user_info.data
  assert user_info.data['first_name'] == user_info.new_data['first_name']
  assert user_info.data['last_name'] == user_info.mew_data['last_name']
  
def test_update_user():
  user_id = 1
  response = requests.put(f"{url}/{user_id}", json=updated_data)
  assert response.status_code == 200
  user_info.data = response.json()
  assert user_info.data['first_name'] == user_info.updated_data['first_name']
  assert user_info.data['last_name'] == user_info.updated_data['last_name']
  
def test_delete_user()
  user_id = 1
  response = requests.delete(f"{url}/{user_id}")
  assert response.status_code == 204
  get_response = requests.get(f"{url}/{user_id}")
  assert get_responss.status_code == 404