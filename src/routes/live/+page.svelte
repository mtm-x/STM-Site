<script lang="ts">
  import { onDestroy, onMount } from "svelte";

  let imageUrl = "";

  async function fetchLatestImage() {
    let imgTimestamp = new Date().getTime();
    imageUrl = `http://192.168.213.22:5000/latest-image?timestamp=${imgTimestamp}`;
  }

  onMount(() => {
    // Static Image Retrieval
    fetchLatestImage();
    setInterval(fetchLatestImage, 5000); // Refresh every 5 seconds
  });
</script>

<main>
  <div class="outer-container mb-10">
    <div class="grid grid-cols-1 md:grid-cols-2 gap-8 md:gap-4">
      <div>
        <h2 class="text-xl font-bold text-gray-600 mb-3">Traffic Junction 1</h2>
        <div class="feed-canvas bg-gray-200 w-full rounded">
          <img
            src={imageUrl}
            alt="Latest Detection"
            on:error={() => (imageUrl = "")}
            class="w-full"
          />
        </div>
      </div>

      <div>
        <h2 class="text-xl font-bold text-gray-600 mb-3">Traffic Junction 2</h2>
        <div class="feed-canvas bg-gray-200 rounded-lg">
          <!-- <img
            src={imageUrl}
            alt="Latest Detection"
            on:error={() => (imageUrl = "")}
            class="w-full"
          /> -->
        </div>
      </div>
    </div>
  </div>
</main>
