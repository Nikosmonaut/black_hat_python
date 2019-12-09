import socket

target_host = 'localhost'
target_port = 4000

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client.sendto(b'AAABBBCCC', (target_host, target_port))

data = bytearray(4096)
nbytes, sender = client.recvfrom_into(data, 4096)

print(data)
