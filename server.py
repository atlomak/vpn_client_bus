import asyncio
import ssl
import socket

async def handle_client(reader, writer):
    data = await reader.read(1000)
    message = data.decode()
    addr = writer.get_extra_info("peername")

    print(f"Received {message} from {addr}")

    print(f"Send: {message}")
    writer.write(data)
    await writer.drain()

    print("Closing the connection")
    writer.close()

async def main():
    server_cert = "server_cert.pem"
    server_key = "server_key.pem"

    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile=server_cert, keyfile=server_key)


    server = await asyncio.start_server(handle_client, '127.0.0.1', 8888, ssl=context)

    addr = server.sockets[0].getsockname()
    print(f"Serving on {addr}")

    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())
