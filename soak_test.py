import requests
import threading
import time

url = 'http://e-planner.somee.com/'
num_threads = 10  # Moderate number for continuous load

def send_request():
    while True:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print("Soak Test: Success")
            else:
                print(f"Soak Test: Failed with status code {response.status_code}")
        except Exception as e:
            print(f"Soak Test: Failed with exception {e}")
        time.sleep(1)

def soak_test():
    threads = [threading.Thread(target=send_request) for _ in range(num_threads)]
    for thread in threads:
        thread.start()
    time.sleep(3600)  # Run for 1 hour
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    soak_test()
