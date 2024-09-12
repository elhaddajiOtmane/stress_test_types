import requests
import threading

url = 'http://e-planner.somee.com/'
num_threads = 5000000000000000000000  # Gradually increase to find capacity

def send_request():
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("Capacity Test: Success")
        else:
            print(f"Capacity Test: Failed with status code {response.status_code}")
    except Exception as e:
        print(f"Capacity Test: Failed with exception {e}")

def capacity_test():
    threads = [threading.Thread(target=send_request) for _ in range(num_threads)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    capacity_test()
