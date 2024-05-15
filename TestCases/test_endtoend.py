import requests
import json
import jsonpath

# GLOBAL (API url, file path...)
URL = "https://thetestingworldapi.com/"
ADDSPATH = "api/studentsDetails"
ADDTPATH = "api/technicalskills"
ADDAPATH = "api/addresses"
GETSDETAIL = "api/FinalStudentDetails/"
ADD_S_PATH = 'D:\\Test engineer Learn\\interview\\studentManagement\\studentData\\studentData.json'
ADD_T_PATH = 'D:\\Test engineer Learn\\interview\\studentManagement\\studentData\\techData.json'
ADD_A_PATH = 'D:\\Test engineer Learn\\interview\\studentManagement\\studentData\\addressData.json'


def test_add_new_data():
    # Add a student
    # Read input json file
    jf = open(ADD_S_PATH, 'r')
    json_input = jf.read()
    request_json = json.loads(json_input)
    # Make POST request with Json Input body
    response = requests.post(url=URL + ADDSPATH, json=request_json)
    print(response.text)
    sid = jsonpath.jsonpath(response.json(), 'id')
    print(sid[0])

    # Add a technical
    # Read input json file
    jf = open(ADD_T_PATH, 'r')
    json_input = jf.read()
    request_json = json.loads(json_input)
    request_json['id'] = int(sid[0])
    request_json['st_id'] = str(sid[0])
    # Make POST request with Json Input body
    response = requests.post(url=URL + ADDTPATH, json=request_json)
    print(response.text)

    # Add a Address
    # Read input json file
    jf = open(ADD_A_PATH, 'r')
    json_input = jf.read()
    request_json = json.loads(json_input)
    request_json['stId'] = str(sid[0])
    # Make POST request with Json Input body
    response = requests.post(url=URL + ADDAPATH, json=request_json)
    print(response.text)

    # Fetch student final data
    response = requests.get(url=URL + GETSDETAIL + str(sid[0]))
    print(response.text)
    # assert response.status_code == 201
