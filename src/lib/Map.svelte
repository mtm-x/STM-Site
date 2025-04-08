<script lang="ts">
  import { onMount } from "svelte";

  let container: HTMLElement;
  let map;
  let zoom = 8;
  let center = { lat: 11.397, lng: 76.644 };

  onMount(async () => {
    map = new google.maps.Map(container, {
      zoom,
      center,
      // @ts-ignore
      //   styles: mapStyles, // optional
    });
  });
</script>

<div>
  <div class="p-3 flex flex-col gap-3">
    <h3 class="font-bold">Find Directions</h3>
    <div class="md:flex block items-center w-100 gap-3">
      <p>From</p>
      <input type="text" class="bg-violet-100 p-3 m-2 md:w-40 w-[100%] outline-0 focus:bg-violet-200" />
      <p>To</p>
      <input type="text" class="bg-violet-100 p-3 m-2 md:w-40 w-[100%] outline-0 focus:bg-violet-200" />
    </div>
  </div>
  <div bind:this={container} class="min-h-[360px]"></div>
</div>
