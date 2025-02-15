<script lang="ts">
  import "../app.css";
  let { children } = $props();

  let show = $state(false);
  function toggleNav() {
    show = !show;
  }
</script>

<head>
  <link
    href="https://cdn.jsdelivr.net/npm/remixicon@4.6.0/fonts/remixicon.css"
    rel="stylesheet"
  />
</head>

<header
  class="fixed w-[100vw] z-99 top-0 bg-violet-950 p-5 flex items-center justify-between gap-3"
>
  <h3 class="text-white font-bold text-2xl">Smart Traffic Management</h3>
  <nav>
    <div class="block md:flex gap-3 items-center">
      <button aria-label="nav-toggle" class="nav-toggle" onclick={toggleNav}>
        <i class="ri-menu-fill"></i>
      </button>
      <div class="hidden md:flex gap-3">
        <a href="/" class="nav-links"
          ><i class="ri-home-6-line font-normal"></i> Home</a
        >
        <a href="/live" class="nav-links"
          ><i class="ri-live-line font-normal"></i> View Live Feed</a
        >
        <a href="/" class="nav-links"
          ><i class="ri-bar-chart-line font-normal"></i> View Traffic Density</a
        >
        <a href="/" class="nav-links"
          ><i class="ri-hospital-line font-normal"></i> Emergency Vehicle Detection</a
        >
      </div>
    </div>

    <div
      class="mobile-nav absolute bg-violet-950 top-[5rem] left-0 w-[100%] md:hidden"
      class:block={show}
      class:hidden={!show}
    >
      <a href="/" class="nav-links"
        ><i class="ri-home-6-line font-normal"></i> Home</a
      >
      <a href="/live" class="nav-links"
        ><i class="ri-live-line font-normal"></i> View Live Feed</a
      >
      <a href="/" class="nav-links"
        ><i class="ri-bar-chart-line font-normal"></i> View Traffic Density</a
      >
      <a href="/" class="nav-links"
        ><i class="ri-hospital-line font-normal"></i> Emergency Vehicle Detection</a
      >
    </div>
  </nav>
</header>

{@render children()}

<style>
  @import url("https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap");
</style>
