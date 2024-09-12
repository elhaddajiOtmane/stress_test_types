import requests
import threading

url = 'http://e-planner.somee.com/'
num_threads = 20  # Number of concurrent requests

def send_request():
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("Concurrency Test: Success")
        else:
            print(f"Concurrency Test: Failed with status code {response.status_code}")
    except Exception as e:
        print(f"Concurrency Test: Failed with exception {e}")

def concurrency_test():
    threads = [threading.Thread(target=send_request) for _ in range(num_threads)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    concurrency_test()
