import requests

url = "http://43.136.92.194:8080/giac"
headers = {
  "Content-Type": "application/json",
}
data={
  "data":"diff(sin(x),x)"
}

response = requests.post(url,json=data,headers=headers)



print(response.content.decode("utf-8"))
