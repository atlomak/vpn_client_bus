import asyncio
import ssl
import socket

async def tcp_echo_client(message):
    ca_cert = "server_cert.pem"
    context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    context.load_verify_locations(cafile=ca_cert)


    reader, writer = await asyncio.open_connection('127.0.0.1', 8888, ssl=context)

    print(f"Send: {message}")
    writer.write(message.encode())

    data = await reader.read(100)
    print(f"Received: {data.decode()}")

    print("Closing the connection")
    writer.close()

if __name__ == "__main__":
    asyncio.run(tcp_echo_client("Hello VPN!"))
