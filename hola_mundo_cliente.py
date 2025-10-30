import asyncio
from fastmcp import Client

async def main():
    async with Client("hola_mundo_server.py") as client:
        response = await client.call_tool("say_hello", {"name": "Juan"})
        print(response)

if __name__ == "__main__":
    asyncio.run(main())