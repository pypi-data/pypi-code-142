# ╔══════════════════════════════════════════════════════════════════════════╗
# ║ Copyright 2022. quinn.7@foxmail.com All rights reserved.                 ║
# ║                                                                          ║
# ║ Licensed under the Apache License, Version 2.0 (the "License");          ║
# ║ you may not use this file except in compliance with the License.         ║
# ║ You may obtain a copy of the License at                                  ║
# ║                                                                          ║
# ║ http://www.apache.org/licenses/LICENSE-2.0                               ║
# ║                                                                          ║
# ║ Unless required by applicable law or agreed to in writing, software      ║
# ║ distributed under the License is distributed on an "AS IS" BASIS,        ║
# ║ WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. ║
# ║ See the License for the specific language governing permissions and      ║
# ║ limitations under the License.                                           ║
# ╚══════════════════════════════════════════════════════════════════════════╝
"""
[ Awaken Web Socket ]

"""
import asyncio
import websockets
import websockets_routes

# 初始化一个router对象
router = websockets_routes.Router()

tl = []
from random import randint
for _ in range(0, 100):
    tl.append(str(randint(1, 1000)))


@router.route("/awaken/{path}")
async def awaken_router(websocket, path):
    async for _ in websocket:
        if (path.params['path'] == 'test'):
            if len(tl) > 0:
                el = tl[0]
                del  tl[0]
                await websocket.send(f'信息:{el}')


async def main():
    async with websockets.serve(lambda x, y: router(x, y), "localhost", 8765):
        await  asyncio.Future()
