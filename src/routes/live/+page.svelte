<script lang="ts">
  import { onMount } from 'svelte';
  let imageUrl = '';

  async function fetchLatestImage() {
    imageUrl = `https://return-attribute-march-mixture.trycloudflare.com/latest-image?timestamp=${new Date().getTime()}`;
  }

  onMount(() => {
    fetchLatestImage();
    const interval = setInterval(fetchLatestImage, 5000); // Refresh every 5 seconds
    return () => clearInterval(interval);
  });
</script>

<main class="relative top-[5rem]">
  <div class="outer-container">
    <div class="grid grid-cols-1 md:grid-cols-2 gap-5">
      <div>
        <h2 class="text-xl font-bold text-gray-600 mb-3">Traffic Junction 1</h2>
        <div class="feed-canvas bg-gray-200 w-[100%] h-100 rounded">
          <img src={imageUrl} alt="Latest Detection" on:error={() => imageUrl = ''} style="max-width: 100%; height: auto;" />
        </div>
      </div>
      <div>
        <h2 class="text-xl font-bold text-gray-600 mb-3">Traffic Junction 2</h2>
        <div class="feed-canvas bg-gray-200 w-[100%] h-100 rounded"></div>
      </div>
      <div>
        <h2 class="text-xl font-bold text-gray-600 mb-3">Traffic Junction 3</h2>
        <div class="feed-canvas bg-gray-200 w-[100%] h-100 rounded"></div>
      </div>
      <div>
        <h2 class="text-xl font-bold text-gray-600 mb-3">Traffic Junction 4</h2>
        <div class="feed-canvas bg-gray-200 w-[100%] h-100 rounded"></div>
      </div>
    </div>
  </div>
</main>
