import socket
import struct
import time

COMM_SET_DUTY = 5

def create_data_payload(): # Payload with instruction and data
    payload = bytearray()
    payload.append(COMM_SET_DUTY)

    duty_int = int(0.2 * 100000) # 0 - 100% duty cycle
    # Pack the integer as a 32-bit signed integer (4 bytes)
    payload.extend(struct.pack('>i', duty_int))  # Big-endian format

    return payload

def create_packet(data): # Wraps the data payload in a packet
    start_byte = 2
    length = len(data)
    crc = 0x1234  # Example CRC, replace with actual CRC calculation
    stop_byte = 3

    packet = bytearray()
    packet.append(start_byte)
    packet.append(length)
    packet.extend(data)
    packet.append((crc >> 8) & 0xFF)  # CRC high byte
    packet.append(crc & 0xFF)         # CRC low byte
    packet.append(stop_byte)

    return packet

def send_packet(packet, host='10.13.84.164', port=65102):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        start_time = time.time()
        while time.time() - start_time < 5:
            s.sendall(packet)
            print(f"Sent packet: {packet}")
            time.sleep(0.1)  # Frequency of sending packets

if __name__ == "__main__":
    data_payload = create_data_payload()
    packet = create_packet(data_payload)
    send_packet(packet)