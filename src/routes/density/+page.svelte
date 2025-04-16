<script lang="ts">
  import Chart from "$lib/Chart.svelte";
  import { density } from "$lib/sampledata.json";

  let densityTimes = $state(density.map((data) => data.time));
  let densityNums = $state(density.map((data) => data.count));

  // Density Chart
  let densityData = {
    chart: {
      type: "line",
      width: "100%",
    },
    title: {
      text: "Traffic Density (Past 5 Hours)",
      style: {
        fontSize: "16px",
        align: "center",
      },
    },
    stroke: {
      curve: "smooth",
    },
    xaxis: {
      categories: densityTimes,
    },
    series: [
      {
        name: "Traffic Density",
        data: densityNums,
      },
    ],
  };
</script>

<main>
  <div class="flex justify-center">
    <div class="border border-gray-400 rounded-md p-3 w-[80%]">
      <Chart options={densityData} />
    </div>
  </div>
</main>
