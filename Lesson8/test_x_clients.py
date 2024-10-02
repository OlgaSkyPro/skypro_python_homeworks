import requests
base_url = "https://x-clients-be.onrender.com"

def test_get_workers():
    resp = requests.get(base_url+'/employee')
    body = resp.json()

    assert resp.status_code == 200
    assert len(body) > 0

def get_workers_list(params_to_add = None):
    resp = requests.get(base_url+'/employee', params_to_add)
    return resp.json()

def test_get_active_workers():
    resp = requests.get(base_url+'')
    full_list = resp.json()

    resp = requests.get(base_url+'/employee?active=true')
    filtered_list = resp.json()

    assert len(full_list) > len(filtered_list)

def get_token(user="roxy", password="animal-fairy"):

    creds = {
        "username": user,
        "password": password
    }
    resp = requests.post(base_url + '/auth/login', json=creds)
    return resp.json()["userToken"]

def create_worker(firstname, lastname, middlename, companyid, email, url, phone, birthdate, isactive ):
    
    new_worker = {
        "firstName": firstname,
        "lastName": lastname,
        "middleName": middlename, 
        "companyId": companyid,
        "email": email,
        "url": url,
        "phone": phone,
        "birthdate": birthdate,
        "isActive": isactive

    }
    my_headers = {}
    my_headers["x-client-token"] = get_token()
    resp = requests.post(base_url.url+'/employee', json = new_worker, headers=my_headers)
    return resp.json()

def test_add_new_worker():
    body = get_workers_list()
    len_before = len(body)
        
    firstname = "Иван"
    lastname = "Иванов"
    middlename = "Иванович"
    companyid = 506
    email = "ivan@string.com"
    url = "Ivan@string.ru"
    phone = "+019995055"
    birthdate = "1960-10-02T13:09:21.602Z"
    isactive = True
    
    result = create_worker(firstname,lastname, middlename, companyid, email, url, phone, birthdate, isactive)
    new_id = result["id"]
    
    body = get_workers_list()
    len_after = len(body)

    assert len_after - len_before == 1
    assert body[-1][firstname] == "Иван"
    assert body[-1]["id"] == new_id

def change_worker():
    
    firstname = "Иван"
    lastname = "Иванов"
    middlename = "Иванович"
    companyid = 506
    email = "ivan@string.com"
    url = "Ivan@string.ru"
    phone = "+019995055"
    birthdate = "1960-10-02T13:09:21.602Z"
    isactive = True
    
    result = create_worker(firstname,lastname, middlename, companyid, email, url, phone, birthdate, isactive)
    change_id = result["id"] 
    
    body = get_workers_list()

    resp = requests.patch(base_url.url+'/employee?'+str(change_id))
    
    assert body[-1][firstname] == "Ива"
    
    return resp.json()


