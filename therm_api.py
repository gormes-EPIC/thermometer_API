from flask import Flask, jsonify, request
# python3 -m pip install adafruit-circuitpython-dht
import board
import adafruit_dht
dhtDevice = adafruit_dht.DHT11(board.D4, use_pulseio=False)

app = Flask(__name__)

# Example in-memory data
items = [
    {"temp": 1}
]

# GET all items
@app.route('/items', methods=['GET'])
def get_items():
    try:
        temperature_c = dhtDevice.temperature
        temperature_c = float(temperature_c)
        if temperature_c == None:
            temperature_c = 70
        temp = temperature_c * (9 / 5) + 32
        items[0]["temp"] = temp
    except TypeError:
        items[0]["temp"] = 70.5
    except RuntimeError as error:
        time.sleep(0.5)
        items[0]["temp"] = 70.5
    except Exception as error:
        dhtDevice.exit()
        raise error
    return jsonify(items)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
