
### Backend (FastAPI)

1. **Install Required Packages:**
   First, ensure you have the necessary packages installed for WebSocket support in FastAPI.

   ```bash
   pip install fastapi uvicorn websockets
   ```

2. **Create a WebSocket Endpoint:**

   Create a new Python file (e.g., `main.py`) and define a WebSocket endpoint.

   ```python
   from fastapi import FastAPI, WebSocket, WebSocketDisconnect

   app = FastAPI()

   active_connections: list[WebSocket] = []

   @app.websocket("/ws")
   async def websocket_endpoint(websocket: WebSocket):
       await websocket.accept()
       active_connections.append(websocket)

       try:
           while True:
               data = await websocket.receive_text()
               # Broadcast the message to all connected clients
               await broadcast(data)
       except WebSocketDisconnect:
           active_connections.remove(websocket)

   async def broadcast(message: str):
       for connection in active_connections:
           if connection.client_state == 1:
               await connection.send_text(message)
   ```

3. **Run the FastAPI Server:**

   Start your FastAPI server using Uvicorn.

   ```bash
   uvicorn main:app --reload
   ```

### Frontend (Flutter)

1. **Add Dependencies:**
   Add the `web_socket_channel` package to your Flutter app's `pubspec.yaml`.

   ```yaml
   dependencies:
     flutter:
       sdk: flutter
     web_socket_channel: ^2.1.0
   ```

2. **Create a WebSocket Service:**

   Create a new Dart file (e.g., `websocket_service.dart`) to manage WebSocket connections.

   ```dart
   import 'package:flutter/material.dart';
   import 'package:web_socket_channel/web_socket_channel.dart';

   class WebSocketService {
     final _channel = WebSocketChannel.connect(
       Uri.parse('ws://<your-fastapi-backend-url>/ws'),
     );

     Stream<String> get stream => _channel.stream.map((event) => event as String);

     void sendMessage(String message) {
       _channel.sink.add(message);
     }

     void dispose() {
       _channel.sink.close();
     }
   }
   ```

3. **Integrate WebSocket in Your App:**

   Use the `WebSocketService` to handle real-time messages in your Flutter app.

   ```dart
   import 'package:flutter/material.dart';
   import 'websocket_service.dart';

   void main() {
     runApp(MyApp());
   }

   class MyApp extends StatelessWidget {
     @override
     Widget build(BuildContext context) {
       return MaterialApp(
         home: ChatScreen(),
       );
     }
   }

   class ChatScreen extends StatefulWidget {
     @override
     _ChatScreenState createState() => _ChatScreenState();
   }

   class _ChatScreenState extends State<ChatScreen> {
     final TextEditingController _controller = TextEditingController();
     WebSocketService _webSocketService = WebSocketService();

     List<String> _messages = [];

     @override
     void initState() {
       super.initState();
       _webSocketService.stream.listen((message) {
         setState(() {
           _messages.add(message);
         });
       });
     }

     @override
     void dispose() {
       _controller.dispose();
       _webSocketService.dispose();
       super.dispose();
     }

     @override
     Widget build(BuildContext context) {
       return Scaffold(
         appBar: AppBar(title: Text('Real-Time Chat')),
         body: Column(
           children: [
             Expanded(
               child: ListView.builder(
                 reverse: true,
                 itemCount: _messages.length,
                 itemBuilder: (context, index) {
                   return ListTile(
                     title: Text(_messages[index]),
                   );
                 },
               ),
             ),
             TextField(
               controller: _controller,
               onSubmitted: (value) {
                 _webSocketService.sendMessage(value);
                 _controller.clear();
               },
             ),
           ],
         ),
       );
     }
   }
   ```

### Self-Hosting

To ensure self-hosting, you can use open-source solutions like Nginx or Apache to proxy WebSocket connections.
Here's a simple example using Nginx:

1. **Install Nginx:**

   ```bash
   sudo apt update
   sudo apt install nginx
   ```

2. **Configure Nginx:**

   Create a new configuration file in `/etc/nginx/sites-available/` (e.g., `myapp`) and link it to
`sites-enabled`.

   ```nginx
   server {
       listen 80;
       server_name yourdomain.com;

       location /ws {
           proxy_pass http://localhost:8000; # Replace with your FastAPI port
           proxy_http_version 1.1;
           proxy_set_header Upgrade $http_upgrade;
           proxy_set_header Connection "upgrade";
       }
   }

   sudo ln -s /etc/nginx/sites-available/myapp /etc/nginx/sites-enabled/
   sudo nginx -t
   sudo systemctl restart nginx
   ```

By following these steps, you can implement a real-time chat feature in your Flutter app using FastAPI with
open-source and self-hosted solutions.