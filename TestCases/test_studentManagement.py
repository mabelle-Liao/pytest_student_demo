import requests
import json
import jsonpath

# GLOBAL (API url, file path...)
URL = "https://thetestingworldapi.com/"
ADDPATH = "api/studentsDetails"
GETPATH = "api/studentsDetails/10277608"
PUTPATH = "api/studentsDetails/10277609"
DELPATH = "api/studentsDetails/10277612"
ADD_FILE_PATH = 'D:\\Test engineer Learn\\interview\\studentManagement\\studentData\\studentData.json'
UPDATE_FILE_PATH = 'D:\\Test engineer Learn\\interview\\studentManagement\\studentData\\studentData-u.json'


def test_add_student_data():
    # Read input json file
    j_file = open(ADD_FILE_PATH, 'r')
    json_input = j_file.read()
    request_json = json.loads(json_input)
    # Make POST request with Json Input body
    response = requests.post(url=URL + ADDPATH, json=request_json)
    print(response.text)
    assert response.status_code == 201

def test_fetch_student_details():
    # Send Get Requests
    response = requests.get(URL+GETPATH)
    json_response = response.json()
    sid = jsonpath.jsonpath(json_response,'data.id')
    assert sid[0] == 10277608

def test_update_student_data():
    # Read input json file
    j_file = open(UPDATE_FILE_PATH, 'r')
    json_input = j_file.read()
    request_json = json.loads(json_input)
    # Make POST request with Json Input body
    response = requests.put(url=URL + PUTPATH, json=request_json)
    print(response.text)
    assert response.status_code == 200

def test_delete_student():
    response = requests.delete(URL+DELPATH)
    # Fetch Response Code
    print(response.text)
    assert response.status_code == 200