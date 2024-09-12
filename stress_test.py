import requests
import threading

url = 'http://e-planner.somee.com/'
num_threads = 100  # High number to stress the system

def send_request():
    while True:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print("Stress Test: Success")
            else:
                print(f"Stress Test: Failed with status code {response.status_code}")
        except Exception as e:
            print(f"Stress Test: Failed with exception {e}")

def stress_test():
    threads = [threading.Thread(target=send_request) for _ in range(num_threads)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    stress_test()
