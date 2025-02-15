<script lang="ts">

  import { onMount } from "svelte";
  import ApexCharts from "apexcharts";

  let { options } = $props();

  let chartContainer: HTMLElement;
  let chart: ApexCharts;

  onMount(() => {
    chart = new ApexCharts(chartContainer, options);
    chart.render();
    return () => chart.destroy();
  });
</script>

<div bind:this={chartContainer}></div>
