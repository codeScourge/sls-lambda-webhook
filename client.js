let websocket = null;

document.getElementById('start-btn').addEventListener('click', () => {
        const URL = 'enter your URL here'; // wss:... endpoint from API Gateway
        websocket = new WebSocket(URL);
        
        
        // this will happen once connection is established
        websocket.onopen = () => {
            websocket.send(JSON.stringify({"action": "default"}))
        }
        
        websocket.onmessage = (e) => {
            document.getElementById('output').innerHTML = e.data
        }

        websocket.onerror = (e) => {
            console.log(e)
        }
    }
)

document.getElementById('stop-btn').addEventListener('click', () => {
    if (websocket != null) {
        websocket.close();
    }
})

