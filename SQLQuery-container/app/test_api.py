import requests

try:
    resp_oro = requests.get("http://127.0.0.1:8000/oro")
    print("ORENDA /oro:", resp_oro.json())
except Exception as e:
    print("Error /oro:", e)

try:
    resp_plata = requests.get("http://127.0.0.1:8000/plata")
    print("ORENDA /plata:", resp_plata.json())
except Exception as e:
    print("Error /plata:", e)
