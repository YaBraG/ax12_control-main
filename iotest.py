import socketio

sio = socketio.Client()


@sio.event
def connect():
    print('connection established')


@sio.event
def my_message(data):
    print('message received with ', data)
    sio.emit('my response', {'response': 'my response'})


@sio.event
def disconnect():
    print('disconnected from server')


@sio.on('mouse-order')
def on_message(data):
    print(data)


sio.connect('http://192.168.2.12:3000')
sio.wait()
