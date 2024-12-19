import socket
import struct
import time

# Command ID for SET_POS from VESC firmware
COMM_SET_POS = 9

class VESCTCPClient:
    def __init__(self, host='10.13.84.164', port=65102):
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((host, port))
            print(f"Connected to VESC at {host}:{port}")
        except ConnectionRefusedError:
            print(f"Connection refused - Is the VESC server running at {host}:{port}?")
            raise
        except Exception as e:
            print(f"Failed to connect: {e}")
            raise

    def send_position(self, position):
        try:
            pos_value = int(position * 1000000)
            packet = struct.pack('<Bi', COMM_SET_POS, pos_value)
            self.socket.send(packet)
            print(f"Sent position command: {position} degrees")
        except Exception as e:
            print(f"Error sending position command: {e}")
            raise

    def close(self):
        try:
            self.socket.close()
        except Exception as e:
            print(f"Error closing connection: {e}")

def main():
    vesc = None
    try:
        vesc = VESCTCPClient('10.13.84.164', 65102)

        positions = [30.0, -15.0]
        
        for pos in positions:
            print(f"\nSetting position to {pos} degrees...")
            vesc.send_position(pos)
            time.sleep(2)  # Add a delay to allow position to be reached
            
    except KeyboardInterrupt:
        print("\nProgram interrupted by user")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
    finally:
        if vesc:
            vesc.close()

if __name__ == "__main__":
    main()