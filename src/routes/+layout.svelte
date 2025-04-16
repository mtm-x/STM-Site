<script lang="ts">
  import "../app.css";
  import logo from "$lib/stmicon.webp";

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
  class="fixed w-[100%] z-99 top-0 bg-violet-950 p-3 flex items-center justify-between gap-3"
>
  <h3 class="text-white font-bold text-xl md:text-2xl">
    Smart Traffic Management
  </h3>
  <nav class="flex flex-col">
    <div class="block md:flex gap-3 items-center">
      <button aria-label="nav-toggle" class="nav-toggle" onclick={toggleNav}>
        <i class="ri-menu-fill"></i>
      </button>
      <div class="hidden md:flex gap-3">
        <a href="/" class="nav-links">
          <i class="ri-home-6-line font-normal"></i> Home
        </a>
        <a href="/live" class="nav-links">
          <i class="ri-live-line font-normal"></i> View Live Feed
        </a>
        <a href="/density" class="nav-links">
          <i class="ri-bar-chart-line font-normal"></i> View Traffic Density
        </a>
        <a href="/hospitals" class="nav-links">
          <i class="ri-hospital-line font-normal"></i> Nearby Hospitals
        </a>
        <a href="/about" class="nav-links">
          <i class="ri-information-line font-normal"></i> About
        </a>
      </div>

      <div class="mobile-nav" class:block={show} class:hidden={!show}>
        <a href="/" class="nav-links" onclick={toggleNav}>
          <i class="ri-home-6-line font-normal"></i> Home
        </a>
        <a href="/live" class="nav-links" onclick={toggleNav}>
          <i class="ri-live-line font-normal"></i> View Live Feed
        </a>
        <a href="/" class="nav-links" onclick={toggleNav}>
          <i class="ri-bar-chart-line font-normal"></i> View Traffic Density
        </a>
        <a href="/hospitals" class="nav-links">
          <i class="ri-hospital-line font-normal"></i> Nearby Hospitals
        </a>
        <a href="/about" class="nav-links" onclick={toggleNav}>
          <i class="ri-information-line font-normal"></i> About
        </a>
      </div>
    </div>
  </nav>
</header>

{@render children()}

<footer class="relative bottom-0 mt-28 bg-violet-950 p-5">
  <div class="block sm:flex text-center sm:text-left items-center gap-4">
    <img
      src={logo}
      class="w-[150px] h-[150px] mx-auto sm:mx-0 rounded-full border-4 border-violet-500"
      alt=""
    />
    <div>
      <h2 class="text-2xl text-white font-bold mt-3 sm:mt-0">
        Smart Traffic Management
      </h2>
      <ul class="text-white">
        <li>Thamaraimanalan M</li>
        <li>Jeyapranov</li>
        <li>Jaswin Kumar N R</li>
        <li>Navamohan M</li>
      </ul>
    </div>
  </div>
</footer>

<style>
  @import url("https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap");
</style>
