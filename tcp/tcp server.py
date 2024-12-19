import socket
import struct
import binascii

def decode_position_packet(data):
    try:
        command, position = struct.unpack('<Bi', data)
        return {
            'command': command,
            'position': position / 1000000.0  # Convert back to degrees
        }
    except struct.error:
        return None

def start_server(host='127.0.0.1', port=8080):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Allow port reuse
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    try:
        server_socket.bind((host, port))
        server_socket.listen(1)
        print(f"Server listening on {host}:{port}")
        
        while True:
            print("\nWaiting for connection...")
            client_socket, address = server_socket.accept()
            print(f"Connection from {address}")
            
            try:
                while True:
                    # Receive exactly 5 bytes (1 byte command + 4 bytes integer)
                    data = client_socket.recv(5)
                    if not data:
                        print("Client disconnected")
                        break
                    
                    # Print raw packet data
                    print("\nReceived packet:")
                    print(f"Raw bytes: {binascii.hexlify(data).decode()}")
                    
                    # Decode and print packet contents
                    packet = decode_position_packet(data)
                    if packet:
                        print(f"Command ID: {packet['command']}")
                        print(f"Position: {packet['position']} degrees")
                    else:
                        print("Failed to decode packet")
                        
            except ConnectionResetError:
                print("Client connection reset")
            finally:
                client_socket.close()
                
    except KeyboardInterrupt:
        print("\nServer shutdown requested")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        server_socket.close()
        print("Server shut down")

if __name__ == "__main__":
    start_server() 