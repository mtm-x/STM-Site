from flask import Flask, Response, request
import random
import time
import threading

app = Flask(__name__)

# Shared variable to store the latest numbers
latest_data = {}

def update_numbers():
    """Continuously updates the numbers every 2 seconds"""
    global latest_data
    while True:
        time.sleep(2)
        latest_data = {'numbers': [random.randint(1, 100) for _ in range(5)]}
        # print(latest_data)

# Start the background thread
threading.Thread(target=update_numbers, daemon=True).start()

@app.route('/stream')
def stream():
    """Streams data updates to clients"""
    if request.method == 'GET':
        def event_stream():
            last_data = None
            while True:
                if last_data != latest_data:  # Send update only when data changes
                    last_data = latest_data.copy()
                    yield f"{last_data}\n"
                    print(f"{last_data}\n")
                time.sleep(2)  # Reduce CPU usage

    return Response(event_stream(), mimetype='text/event-stream')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
