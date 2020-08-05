import aiohttp # download
import aiofiles # download
import asyncio
import os
from itertools import chain, islice
from pathlib import Path
import math

def split_file2(file_name):
    folder = "C:/Users/XXX/Documents/Videos/"
    split_folder = "C:/Users/XXX/Documents/Videos/Split/"
    CHUNK_SIZE = 10000000
    file_number = 0
    with open(folder+file_name, "rb") as f:
        chunk = f.read(CHUNK_SIZE)
        while chunk:
            file_number += 1
            with open(f"{split_folder}{file_name}.{file_number}", "wb") as chunk_file:
                chunk_file.write(chunk)
            chunk = f.read(CHUNK_SIZE)
    print(f'{file_name} split in {file_number} files.')

if __name__ == "__main__":
    folder = "C:/Users/XXX/Documents/Videos/"
    files = os.listdir(folder)
    for file_name in files:
        if os.path.isfile(folder+file_name):
            split_file2(file_name)

'''

THIS CODE IS FOR SENDING / RECIEVING, BUT YOU NEED A SERVER...

async def file_sender(file_name=None):
    async with aiofiles.open(file_name, 'rb') as f:
        chunk = await f.read(64 * 1024)
        while chunk:
            yield chunk
            chunk = await f.read(64 * 1024)

async def req(file_name):
    source = "/root/recordings/complete/exfil/"
    async with aiohttp.ClientSession() as session:
        data = aiohttp.FormData()
        data.add_field('file', file_sender(file_name=source+file_name), filename=f"{file_name}", content_type='application'
                                                                                                       '/octet-stream')
        resp = await session.post('http://192.168.0.14:8080/upload', data=data)
        return await resp.text()

'''

