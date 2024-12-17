from concurrent.futures import ThreadPoolExecutor 
#Allows ability to execute concurrent tasks
#Thread pool executor does the asynchronous execution with threads 
import socket
#Libray for working with socets. Used to form TCP conenction. 
import time

MAX_WORKERS = 10000 #Max number of threads working at once 

def generate_port_chunks(port_range): 
    #Gets the min/max port numbers from port range
    port_ranges = port_range.split('-')
    port_chunks = []
    #Divides port range into chunks 
    chunks_size = int((int(port_ranges[1])- int(port_ranges[0]))/MAX_WORKERS)
    #Creates nested list of port chunks to be handled by each worker

    for i in range(MAX_WORKERS):
        start = int(port_ranges[0]) + (chunks_size * i)
        end = start + chunks_size
        port_chunks.append([start, end])
    return port_chunks

def scan(ip_address,port_chunk):
    print(f"[-] Scanning {ip_address} from {port_chunk[0]} to {port_chunk[1]}.")
    #Loop through min/max port chunks 
    for port in range(int(port_chunk[0]), int(port_chunk[1])):
        #Attempt a TCP IPv4 connection to provided port and IP address
        try: 
            scan_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            scan_socket.settimeout(2)
            scan_socket.connect((ip_address,port))
            print(f"[!] Port {port} is open")
            #If port is closed an exception will be thrown, capture it here 
        except:
            None

def main():
    ip_address = "31.220.55.159"
    port_range = '0-10000'

    port_chunks = generate_port_chunks(port_range)

    start_time = time.time()
    #Submit tasks to be executed by thead pool using map
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor: 
        executor.map(scan, [ip_address] * len(port_chunks), port_chunks)

        end_time = time.time()

        print(f"Scanned {port_range[1]} ports in {end_time - start_time} seconds.")

if __name__ == '__main__':
    main()