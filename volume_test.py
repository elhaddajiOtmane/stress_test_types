import requests

url = 'http://e-planner.somee.com/'
num_requests = 10000  # Large volume of requests

def send_request():
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("Volume Test: Success")
        else:
            print(f"Volume Test: Failed with status code {response.status_code}")
    except Exception as e:
        print(f"Volume Test: Failed with exception {e}")

def volume_test():
    for _ in range(num_requests):
        send_request()

if __name__ == "__main__":
    volume_test()
