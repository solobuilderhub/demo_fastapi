import aiohttp
import asyncio
from datetime import datetime

url = "https://www.reddit.com/r/all/new/.json"
headers = {'User-agent': 'Mozilla/5.0'}

async def send_request(session):
    async with session.get(url, headers=headers) as response:
        print(f"{datetime.now()} --- Status: {response.status}")
        print(f"Headers: {response.headers}")

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [send_request(session) for _ in range(100)]
        await asyncio.gather(*tasks)

# Run the main function
asyncio.run(main())