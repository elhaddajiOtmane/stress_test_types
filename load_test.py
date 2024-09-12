import requests
import threading

url = 'http://e-planner.somee.com/'
num_threads = 10
requests_per_thread = 1000

def send_request():
    for _ in range(requests_per_thread):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print("Load Test: Success")
            else:
                print(f"Load Test: Failed with status code {response.status_code}")
        except Exception as e:
            print(f"Load Test: Failed with exception {e}")

def load_test():
    threads = [threading.Thread(target=send_request) for _ in range(num_threads)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    load_test()
