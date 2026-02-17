from flask import Flask
import os

app = Flask(_name_)

@app.route('/')
def hello_world():
    return 'Hello, Render! 部署成功啦！'

if _name_ == '_main_':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
