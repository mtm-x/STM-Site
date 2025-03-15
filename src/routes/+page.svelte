<script lang="ts">
  import Chart from "$lib/Chart.svelte";
  import { density, accidents, hospitals } from "$lib/sampledata.json";

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

  // Accidents Chart

  let accidentsData = {
    chart: {
      type: "bar",
      width: "100%",
    },
    title: {
      text: "Accidents in the Past Month",
      style: {
        fontSize: "16px",
        align: "center",
      },
    },
    colors: ["#8d42f5"],
    stroke: {
      curve: "smooth",
    },
    xaxis: {
      categories: accidents.map((data) => data.date),
    },
    series: [
      {
        name: "Traffic Density",
        data: accidents.map((data) => data.count),
      },
    ],
  };

  fetch("http://127.0.0.1:5000/stream")
    .then((response) => {
      if (!response.ok) {
        throw new Error(`Error Retrieving Data: ${response.status}`);
      }
      return response.json();
    })
    .then((data) => console.log(data))
    .catch((error) => console.error(`Error Fetching Data ${error}`));
</script>

<main class="relative top-[5rem]">
  <div class="outer-container">
    <div
      id="charts"
      class="flex flex-col md:flex-row gap-3 justify-center items-center"
    >
      <div class="border border-gray-400 rounded-md max-h-[100%] max-w-[60%] flex-1 w-90 p-3">
        <Chart options={densityData} />
      </div>
    </div>

    <div id="hospitals" class="flex mt-4">
      <div class="flex-1 w-100 overflow-x-auto">
        <table
          id="hospitals-table"
          class="table-auto bg-violet-200 rounded-xl w-[100%] text-center"
        >
          <caption
            class="caption-top bg-violet-800 text-white rounded-tr-xl rounded-tl-xl p-3 font-bold border-b border-violet-300"
          >
            Hospitals Nearby
          </caption>
          <thead>
            <tr class="bg-violet-800 text-white">
              <th>S. No</th>
              <th>Hospital Name</th>
              <th>Address</th>
              <th>Directions</th>
            </tr>
          </thead>
          <tbody>
            {#each hospitals as hospital, i}
              <tr
                class="hover:bg-violet-400 hover:text-white transition-all ease-in-out"
              >
                <td class="rounded-bl-xl">{i + 1}</td>
                <td>{hospital.name}</td>
                <td>{hospital.address}</td>
                <td class="rounded-br-xl">View Map</td>
              </tr>
            {/each}
          </tbody>
        </table>
      </div>
    </div>
  </div>
</main>

<style lang="scss">
  #hospitals-table {
    font-size: 1rem;
    th {
      padding: 1rem;
    }
    td {
      padding: 1rem;
    }
  }
</style>
