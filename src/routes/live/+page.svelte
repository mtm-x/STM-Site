<script lang="ts">
  import { onMount } from "svelte";
  let imageUrl = "";

  async function fetchLatestImage() {
    imageUrl = `https://poultry-winston-reviewer-faqs.trycloudflare.com/latest-image?timestamp=${new Date().getTime()}`;
  }

  onMount(() => {
    fetchLatestImage();
    const interval = setInterval(fetchLatestImage, 5000); // Refresh every 5 seconds
    return () => clearInterval(interval);
  });

  let canvas: HTMLCanvasElement; // Bind the canvas element
  let context: any;
  let websocket: WebSocket;
  let img: HTMLImageElement;

  onMount(() => {
    context = canvas.getContext("2d");
    websocket = new WebSocket("ws://127.0.0.1:8765");
    img = new Image();

    websocket.onmessage = (event) => {
      img.onload = () => {
        context.drawImage(img, 0, 0, canvas.width, canvas.height);
      };
      img.src = "data:image/jpeg;base64," + event.data;
    };

    websocket.onerror = (error) => {
      console.error("WebSocket Error:", error);
    };

    websocket.onclose = () => {
      console.log("WebSocket connection closed");
    };
  });
</script>

<main>
  <div class="outer-container">
    <div class="grid grid-cols-1 md:grid-cols-2 gap-5">
      <div>
        <h2 class="text-xl font-bold text-gray-600 mb-3">Traffic Junction 1</h2>
        <div class="feed-canvas bg-gray-200 w-[100%] h-100 rounded">
          <img
            src={imageUrl}
            alt="Latest Detection"
            on:error={() => (imageUrl = "")}
            style="max-width: 100%; height: auto;"
          />
        </div>
      </div>
      <div>
        <h2 class="text-xl font-bold text-gray-600 mb-3">Traffic Junction 2</h2>
        <div class="feed-canvas bg-gray-200 w-[100%] h-100 rounded">
          <canvas
            bind:this={canvas}
            style="border: 1px solid black;"
            class="w-[100%] h-[100%]"
          ></canvas>
        </div>
      </div>
    </div>
  </div>
</main>
