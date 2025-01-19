# Port Scanner with Thread Pool Executor

This program is a multithreaded port scanner that scans a given range of ports on a specified IP address to identify open ports. It uses Python's `concurrent.futures.ThreadPoolExecutor` for concurrent execution and the `socket` library to attempt TCP connections.

## Features

- Scans a specified range of ports on a given IP address.
- Utilizes multithreading for fast and efficient scanning.
- Prints open ports to the console.
- Handles connection timeouts gracefully.

## Prerequisites

- Python 3.6 or later.
- Internet connection to reach the target IP address.

## Installation

1. Clone or download this repository.
2. Ensure Python 3 is installed on your system.
3. (Optional) Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Linux/Mac
   venv\Scripts\activate     # On Windows
   ```

## Usage

1. Open the script file and modify the following variables in the `main()` function:
   - `ip_address`: The target IP address to scan.
   - `port_range`: The range of ports to scan (e.g., `'0-10000'`).

2. Run the script:
   ```bash
   python port_scanner.py
   ```

3. The program will:
   - Divide the port range into chunks for efficient processing.
   - Create up to 10,000 threads to scan ports concurrently.
   - Display open ports in the console.

### Example Output

```
[-] Scanning 31.220.55.159 from 0 to 100.
[-] Scanning 31.220.55.159 from 100 to 200.
[!] Port 80 is open
[!] Port 443 is open
Scanned 10000 ports in 12.34 seconds.
```

## Program Structure

### Functions

1. **`generate_port_chunks(port_range)`**
   - Splits the specified port range into manageable chunks.
   - Returns a list of port chunks for workers.

2. **`scan(ip_address, port_chunk)`**
   - Attempts to connect to each port in the chunk.
   - Prints open ports to the console.

3. **`main()`**
   - Defines the IP address and port range.
   - Divides the work among threads using `ThreadPoolExecutor`.

## Customization

- **Change Maximum Workers**: Modify the `MAX_WORKERS` variable to adjust the number of threads.
- **Timeout**: Adjust the timeout value in the `scan()` function by modifying `scan_socket.settimeout()`.



[Your Name]
```

Feel free to replace `[Your Name]` with your name and adapt the file as needed!
