from flask import Flask,Response,render_template
from flask_redis import FlaskRedis
import json

app = Flask(__name__)
app.config["DEBUG"] = False

#ReidsConfig
app.config['REDIS_URL']='redis://@35.234.14.146:6379'
redisClient=FlaskRedis(app)


@app.route('/', methods=['GET'])
def home():
    returnData=[str(redisClient.get('testChat'),encoding="utf-8")]
    return Response(json.dumps(returnData),mimetype='application/json')

if(__name__)=="__main__":
    app.run()