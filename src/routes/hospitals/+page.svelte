<script lang="ts">
  import { onMount } from "svelte";

  let center = { lat: 12.98436555105405, lng: 77.59269938491829 };
  var nearbyHospitals: any = [];
  let loadingHospitals = true;

  interface LatLon {
    lat: Number;
    lon: Number;
  }
  onMount(async () => {
    // Markers Library
    const { AdvancedMarkerElement } = (await google.maps.importLibrary(
      "marker"
    )) as google.maps.MarkerLibrary;

    // Places Library
    const { Place, SearchNearbyRankPreference } =
      (await google.maps.importLibrary("places")) as google.maps.PlacesLibrary;

    const hospitalsRequest = {
      // required parameters
      fields: ["displayName", "location", "formattedAddress"],
      locationRestriction: {
        center: center,
        radius: 5000,
      },
      // optional parameters
      includedPrimaryTypes: ["hospital"],
      maxResultCount: 5,
      rankPreference: SearchNearbyRankPreference.DISTANCE,
      language: "en-US",
      region: "us",
    };

    const { places } = await Place.searchNearby(hospitalsRequest);
    if (places.length) {
      console.log(places);

      // Loop through and get all the results.
      places.forEach((place) => {
        // @ts-ignore
        nearbyHospitals.push(place);
        console.log(place);
      });

      console.log(nearbyHospitals);
      loadingHospitals = false;
    } else {
      console.log("No results");
    }
  });
</script>

<main>
  <div id="hospitals" class="flex mt-4 p-4">
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
        {#if loadingHospitals}
          <tbody> </tbody>
        {:else}
          <tbody>
            {#each nearbyHospitals as hospital, i}
              <tr
                class="hover:bg-violet-400 hover:text-white transition-all ease-in-out"
              >
                <td class="rounded-bl-xl">{i + 1}</td>
                <td>{hospital.displayName}</td>
                <td>{hospital.formattedAddress}</td>
                <td class="rounded-br-xl">View Map</td>
              </tr>
            {/each}
          </tbody>
        {/if}
      </table>
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
