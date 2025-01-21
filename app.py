from flask import Flask, jsonify
import pymongo

app = Flask(__name__)

@app.route('/run-script', methods=['GET'])
def run_script():
    # Connect to MongoDB
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["twitter_data"]
    collection = db["trending_topics"]

    # Fetch the latest record
    latest_record = collection.find().sort([("_id", -1)]).limit(1)
    data = list(latest_record)[0] if latest_record else {}

    # Format response
    response = {
        "datetime": data.get("timestamp"),
        "trend1": data.get("trend1"),
        "trend2": data.get("trend2"),
        "trend3": data.get("trend3"),
        "trend4": data.get("trend4"),
        "trend5": data.get("trend5"),
        "ip": data.get("ip_address"),
        "record": data
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(port=5000)
