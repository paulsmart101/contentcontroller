import requests, base64, json

def gettoken():
    # Production Keys
    # Key: tgwMtl8X09KC-m1VlEgC
    # Secret: AkeMV2oXbhAAz9nXVPXDkzZ2obmT
    
    url = "https://awsacademy.contentcontroller.com/api/public/v1/auth"
    userAndPass = base64.b64encode(b"tgwMtl8X09KC-m1VlEgC:AkeMV2oXbhAAz9nXVPXDkzZ2obmT").decode("ascii")
    payload = "grant_type=client_credentials"
    headers = {
        'Accept': "application/json",
        'Content-Type': "application/x-www-form-urlencoded",
        'Authorization': "Basic " + userAndPass
    }

    r = requests.request("POST", url, data=payload, headers=headers)
    raw = r.json()
    parsed = json.loads(r.text)
    #print(parsed)
    #-- Token is good for 30 minutes
    return parsed['access_token']
    
token = gettoken() #-- Token is good for 30 minutes
    
url = "https://awsacademy.contentcontroller.com/api/public/v1/content/courses"
headers = {
    'Content-Type': "application/json",
    'Accept': "application/json",
    'Authorization': "Bearer " + token
}

r = requests.request("GET", url, headers=headers)
raw = r.json()
parsed = json.loads(r.text)
courses = parsed['courses']

print("All Courses:",len(courses))

counter = 0
for course in courses:
    if course['enabled'] == True:
        #print(course['name'])
        counter += 1
print("Enabled Courses:",counter)
