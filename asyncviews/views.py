import asyncio
import httpx
from django.http import HttpResponse

async def http_call_async():
    for num in range(1, 6):
        await asyncio.sleep(1)
        print(num)
    async with httpx.AsyncClient() as client:
        r = await client.get("https://httpbin.org/get")
        print(r.text)

def http_call_sync():
    import time
    import requests
    
    for num in range(1, 6):
        time.sleep(1)
        print(num)
    r = requests.get("https://httpbin.org/get")
    print(r.text)

async def async_view(request):
    asyncio.create_task(http_call_async())
    return HttpResponse("Non-blocking HTTP request")

def sync_view(request):
    http_call_sync()
    return HttpResponse("Blocking HTTP request")
