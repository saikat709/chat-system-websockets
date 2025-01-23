## What is [Connect Four](https://en.wikipedia.org/wiki/Connect_Four)?
Connect Four (also known as Connect 4, Four Up, Plot Four, Find Four, Captain's Mistress, Four in a Row, Drop Four, and Gravitrips in the Soviet Union) is a game in which the players choose a color and then take turns dropping colored tokens into a six-row, seven-column vertically suspended grid. The pieces fall straight down, occupying the lowest available space within the column. The objective of the game is to be the first to form a horizontal, vertical, or diagonal line of four of one's own tokens. It is therefore a type of m,n,k-game (7, 6, 4) with restricted piece placement. Connect Four is a solved game. The first player can always win by playing the right moves.

![Amimation or connect Four](https://upload.wikimedia.org/wikipedia/commons/a/ad/Connect_Four.gif)

## Tools Used
1. Python
2. Python Websockets
3. html, css, js
---
## Steps to run ( Linux )
```bash
python3 -m venv env  // create virtual environment named 'env'
pip install -r requiments.txt
python -m websockets --version  // version of websockets

# serve the html - index.html ( using http server without any framework, or static server )
python -m http.server

# run the file containing websocket. ( no new file needed in flask. Just run before the app.run() )
python app.py

# test cinnection
python -m websockets ws://localhost:8001/
# this means `new  WebSocket('ws://localhost:8001/')` of js.

```

### Visualization:
Branch 1: **send_receive**  - Full Setup ( But play from single laptop )
[![Video That shows the first Step code result.](https://github.com/saikat709/chat-system-websockets/blob/main/github_readme_assets/c4.png?raw=true)](https://github.com/saikat709/chat-system-websockets/blob/main/github_readme_assets/sr_1.webm?raw=true)


# About app.py
If we are serving our website using static server method then We dont need  a differebt server code to handle the connections. But If we are serving using dynamic framework i.e server we can integrate the connection handling into that framework somehow. Thus we wont need an extra server to handle connection.
Not that:
    - websites are served using http method which can not handle connections directly because it only sends reponse based on the request. Not a continuos connection.
    - websocket maybe uses 'ws' method.
___