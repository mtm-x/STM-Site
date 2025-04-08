import cv2
import asyncio
import websockets
import base64
import numpy as np

async def webcam_feed(websocket):
    """Sends webcam feed over WebSocket."""

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Error: Could not read frame.")
                break

            # Encode the frame as a JPEG image.
            _, buffer = cv2.imencode('.jpg', frame)
            # Convert the buffer to base64.
            encoded_image = base64.b64encode(buffer).decode('utf-8')

            # Send the encoded image over WebSocket.
            await websocket.send(encoded_image)
            await asyncio.sleep(0.03)  # Adjust for desired frame rate.

    except websockets.exceptions.ConnectionClosedOK:
        print("WebSocket connection closed gracefully.")
    except websockets.exceptions.ConnectionClosedError:
        print("WebSocket connection closed with error.")
    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        cap.release()
        print("Webcam released.")

async def main():
    async with websockets.serve(webcam_feed, "localhost", 8765):
        print("WebSocket server started at ws://localhost:8765")
        await asyncio.Future()  # Run forever

if __name__ == "__main__":
    asyncio.run(main())