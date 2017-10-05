import requests
import json

data = json.dumps({
"id" : "204",
"nodes" : "{4,8}",
"edges":"{48}",
})

#print(data)

headers = {'Content-Type':'application/json', 'Accept':'application/json'}
#res = requests.post("http://127.0.0.1:5000/api/graphs/insert/",data = data, headers = headers)
#data = res.json()
#print (data['idx'])

d = json.dumps({
"idx":"204",
})
res = requests.get("http://127.0.0.1:5000/api/graphs/select/", data=d, headers=headers)
print(res)

data = res.json()
print(data)

data = json.dumps({
"update_id" : "204",
"nodes" : "{3,8}",
"edges":"{38}",
})
res = requests.get("http://127.0.0.1:5000/api/graphs/update/", data=data, headers=headers)
print(res, res.json())

data = json.dumps({
"delete_id" : "4",
})
res = requests.get("http://127.0.0.1:5000/api/graphs/delete/", data=data, headers=headers)
print(res, res.json())
