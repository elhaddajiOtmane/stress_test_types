import requests
import threading
import time

url = 'http://e-planner.somee.com/'

def send_request():
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("Spike Test: Success")
        else:
            print(f"Spike Test: Failed with status code {response.status_code}")
    except Exception as e:
        print(f"Spike Test: Failed with exception {e}")

def spike_test():
    # Initial load
    for _ in range(50):
        threading.Thread(target=send_request).start()

    # Spike load
    time.sleep(10)
    for _ in range(200):
        threading.Thread(target=send_request).start()

if __name__ == "__main__":
    spike_test()
