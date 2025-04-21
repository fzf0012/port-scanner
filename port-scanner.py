import socket

def banner_grab(ip, port):
    try:
        with socket.create_connection((ip, port), timeout=2) as s:
            s.sendall(b"HEAD / HTTP/1.0\r\n\r\n")
            return s.recv(1024).decode(errors="ignore")
    except Exception:
        return "No banner"

def scan_ports(target, ports):
    open_ports = {}
    for port in ports:
        try:
            with socket.create_connection((target, port), timeout=1):
                banner = banner_grab(target, port)
                open_ports[port] = banner.strip()
        except:
            continue
    return open_ports

result = scan_ports("192.168.1.1", range(1, 1025))
for port, banner in result.items():
    print(f"Port {port} open: {banner}")

