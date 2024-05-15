import requests
import json
import jsonpath

# GLOBAL (API url, file path...)
URL = "https://thetestingworldapi.com/"
ADDPATH = "api/studentsDetails"
GETPATH = "api/studentsDetails/"
ADD_PATH = 'D:\\Test engineer Learn\\interview\\studentManagement\\studentData\\addStudent.json'

def test_add_new_data():
    global sid
    # Add a student
    # Read input json file
    jf = open(ADD_PATH, 'r')
    json_input = jf.read()
    request_json = json.loads(json_input)
    # Make POST request with Json Input body
    response = requests.post(url=URL + ADDPATH, json=request_json)
    print(response.text)
    sid = jsonpath.jsonpath(response.json(), 'id')
    print(sid[0])
def test_get_details():
    # Fetch student data
    response = requests.get(url=URL + GETPATH + str(sid[0]))
    print(response.text)