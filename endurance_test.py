import requests
import threading
import time

url = 'http://e-planner.somee.com/'
num_threads = 10

def send_request():
    while True:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print("Endurance Test: Success")
            else:
                print(f"Endurance Test: Failed with status code {response.status_code}")
        except Exception as e:
            print(f"Endurance Test: Failed with exception {e}")
        time.sleep(1)

def endurance_test():
    threads = [threading.Thread(target=send_request) for _ in range(num_threads)]
    for thread in threads:
        thread.start()
    time.sleep(86400)  # Run for 24 hours
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    endurance_test()
