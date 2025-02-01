#!/usr/bin/env python

import asyncio
import json
import itertools

from websockets.asyncio.server import serve
from websockets.exceptions import ConnectionClosedOK

from connect4 import PLAYER1, PLAYER2, Connect4


# async def handler(websocket):
    # while True:
    #     try:
    #         message = await websocket.recv()
    #     except ConnectionClosedOK:
    #         print("Connection Closed.")
    #         break
    #     print(message)
    # async for message in websocket:
    #     print(message)

    # for player, column, row in [
    #     (PLAYER1, 3, 0),
    #     (PLAYER1, 3, 1),
    #     (PLAYER1, 4, 0),
    #     (PLAYER1, 4, 1),
    #     (PLAYER1, 2, 0),
    #     (PLAYER1, 1, 0),
    #     (PLAYER1, 5, 0),
    # ]:
    #     event = {
    #         'type': 'play',
    #         'player': player,
    #         'column': column,
    #         'row': row
    #     }
    #     await websocket.send(json.dumps(event))
    #     await asyncio.sleep(0.9);
    # event = {
    #     "type": "win",
    #     "player": PLAYER1,
    # }
    # await websocket.send(json.dumps(event))


async def handler(websocket):
    game = Connect4()

    turns = itertools.cycle([ PLAYER1, PLAYER2 ])
    player = next(turns)
    column = -1

    #  msg = json.loads(await websocket.recv()) -> inside while loop
    async for msg in websocket:

        try:
            msg = json.loads(msg)
            assert msg['type'] == 'play'
            column = msg['column']
        except ConnectionClosedOK:
            print("Client Connection closed.")
            break
        except AssertionError or TypeError as e:
            print(e)
            await websocket.send(json.dumps({
                "type": 'error',
                "message": "Event type must be 'play' or Message not valid."
            }))

        try:
            row = game.play(player, column)
        except ValueError as e:
            print(str(e))
            await websocket.send(json.dumps({
                'type': 'error',
                'message' : str(e),
            }));
            continue

        if game.winner:
            await websocket.send(json.dumps({
                'type': 'win',
                'player' : game.winner,
                'column': column,
                'row' : row
            }))

        await websocket.send(json.dumps({
            'type': 'play',
            'player': player,
            'column': column,
            'row' : row
        }))

        player = next(turns)


async def main():
    async with serve(handler, "", 8001):
        await asyncio.get_running_loop().create_future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())