import requests
url = 'http://localhost/garage_door/webpage/api/set_state.php?d1=1&d2=1'
response = requests.get(url)