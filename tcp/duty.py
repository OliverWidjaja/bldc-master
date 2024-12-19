import socket
import struct
import time

VESC_IP = '10.13.84.164'
VESC_PORT = 65102
COMM_SET_DUTY = 5

def send_set_duty(duty, duration):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        sock.connect((VESC_IP, VESC_PORT))
        print(f"Connected to VESC at {VESC_IP}:{VESC_PORT}")

        end_time = time.time() + duration

        while time.time() < end_time:
            packet = bytearray()
            packet.append(COMM_SET_DUTY)

            duty_int = int(duty * 100000)
            # Pack the integer as a 32-bit signed integer (4 bytes)
            packet.extend(struct.pack('>i', duty_int))  # Big-endian format

            sock.sendall(packet)
            print(f"Sent COMM_SET_DUTY command with duty: {duty}")
            print(packet)

            time.sleep(0.01)

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        sock.close()
        print("Connection closed.")

if __name__ == "__main__":
    target_duty = 0.5  # duty cycle (0.0 to 1.0)
    duration = 5
    send_set_duty(target_duty, duration)