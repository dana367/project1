from quart import Quart, ResponseReturnValue
app = Quart(__name__)

@app.get('/')
async def hello_world():
    return 'Hello, World!!'

