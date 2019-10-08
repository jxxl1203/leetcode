import websocket, ssl



# ws = websocket.WebSocket()
# ws.connect("ws://ngrok.jxjjxl.cn/gamecenter/ws")


ws = websocket.WebSocket(sslopt={"cert_reqs": ssl.CERT_NONE})
ws.connect("wss://ngrok.jxjjxl.cn/ws")

ws.send("aaaaaaaaaaaaaaaaaaaaaa")