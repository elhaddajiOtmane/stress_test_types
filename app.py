import requests
import threading

# URL of the website you want to send traffic to
url = 'http://e-planner.somee.com/'

# Number of requests to send
total_requests = 200000

# Number of threads to use
num_threads = 10

# Define the headers with a User-Agent
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Cookie': 'ASP.NET_SessionId=5yw2viasdasuyh405usdasdm0145azpj0w;b=b'
}

# Counter to keep track of the number of completed requests
lock = threading.Lock()
requests_sent = 0

def send_request():
    global requests_sent
    while True:
        with lock:
            if requests_sent >= total_requests:
                break
            request_num = requests_sent + 1
            requests_sent += 1
        
        try:
            # Make the request with the User-Agent header
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                print(f"Request {request_num}: Success")
            else:
                print(f"Request {request_num}: Failed with status code {response.status_code}")
        except Exception as e:
            print(f"Request {request_num}: Failed with exception {e}")

def simulate_traffic():
    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=send_request)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    simulate_traffic()
