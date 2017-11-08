import lights


def on():
    try:
        requests.get('http://192.168.42.10:5000/light/on', timeout=0.1)
    except (requests.exceptions.Timeout, requests.ConnectionError):
        pass


def off():
    try:
        requests.get('http://192.168.42.10:5000/light/off', timeout=0.1)
    except (requests.exceptions.Timeout, requests.ConnectionError):
        pass
