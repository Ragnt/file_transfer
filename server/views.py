from aiohttp import web
import os


async def index(request):
    return web.Response(text='Hello Aiohttp!')

async def store_pcapng_parts(request):
    print(f"File Upload Started from {request.host}")
    reader = await request.multipart()
    file_part = await reader.next()
    filename = file_part.filename

    # You cannot rely on Content-Length if transfer is chunked.
    size = 0
    file = os.path.join('C:/Users/RSB/PycharmProjects/shark/tests', filename)
    with open(file, 'wb') as f:
        while True:
            chunk = await file_part.read_chunk()  # 8192 bytes by default.
            if not chunk:
                break
            size += len(chunk)
            f.write(chunk)
    text = f'{filename} with size of {size} successfully stored at {file}'
    print(text)
    return web.Response(text=text)