from pyrogram import Client
from pyrogram.api import functions, types

# get from my.telegram.org
app = Client(
    "session_file",
    api_id="YOUR_APP_ID",
    api_hash="YOUR_API_HASH")

@app.on_message(None)
def hello(client, message):
    app.send(
            functions.messages.SetTyping(
                peer=app.resolve_peer(message.chat.id),
                action=types.SendMessageTypingAction()
            )
        )
        
app.run()
