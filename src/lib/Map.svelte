<script lang="ts">
  import { onMount } from "svelte";

  let container: HTMLElement;
  let map: google.maps.Map;
  let zoom = 17;
  let center = { lat: 12.98436555105405, lng: 77.59269938491829 };

  let fromPac;
  let toPac;
  let fromPacElement: HTMLDivElement;
  let toPacElement: HTMLDivElement;
  let selectedPlaceInfo: HTMLParagraphElement;
  let nearbyHospitals: LatLon[] = [];

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

    fromPac = new google.maps.places.PlaceAutocompleteElement({
      componentRestrictions: {
        country: "in",
      },
    });

    toPac = new google.maps.places.PlaceAutocompleteElement({
      componentRestrictions: {
        country: "in",
      },
    });

    fromPacElement.appendChild(fromPac);
    toPacElement.appendChild(toPac);

    // @ts-ignore
    fromPac.addEventListener("gmp-select", async ({ placePrediction }) => {
      const place = placePrediction.toPlace();
      await place.fetchFields({
        fields: ["displayName", "formattedAddress", "location"],
      });

      let fromLocation: LatLon = {
        lat: place.toJSON().location.lat,
        lon: place.toJSON().location.lng,
      };

      selectedPlaceInfo.textContent = `${fromLocation.lat.toString()}, ${fromLocation.lon.toString()}`;
    });

    // @ts-ignore
    toPac.addEventListener("gmp-select", async ({ placePrediction }) => {
      const place = placePrediction.toPlace();
      await place.fetchFields({
        fields: ["displayName", "formattedAddress", "location"],
      });
      selectedPlaceInfo.textContent = JSON.stringify(place.toJSON());
    });
    map = new google.maps.Map(container, {
      zoom,
      center,
      mapId: "5d80ad85e18e2eaf",
    });

    function displayJunction(lat: number, lon: number) {
      const marker = new AdvancedMarkerElement({
        position: { lat: lat, lng: lon },
        map: map,
        title: "Junction",
      });
      const infoWindow = new google.maps.InfoWindow({
        ariaLabel: "Junction 1",
        content: `<h1 class="font-bold text-xl">Traffic Junction</h1>`,
      });

      marker.addListener("gmp-click", () => {
        infoWindow.open(map, marker);
      });
    }

    displayJunction(center.lat, center.lng);

    const hospitalsRequest = {
      // required parameters
      fields: ["displayName", "location", "businessStatus"],
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
        let hospitalMarker = new AdvancedMarkerElement({
          map,
          position: place.location,
          title: place.displayName,
        });

        // @ts-ignore
        nearbyHospitals.push(place);
        console.log(place);
      });

      // map.fitBounds(bounds);
    } else {
      console.log("No results");
    }
  });
</script>

<div>
  <div class="p-3 flex flex-col gap-3">
    <h3 class="font-bold">Find Directions</h3>
    <div class=" items-center w-full gap-3">
      <p class="my-3">From</p>

      <!-- <input
        type="text"
        class="bg-violet-100 w-[100%] p-3 m-2 outline-0 focus:bg-violet-200"
      /> -->

      <div bind:this={fromPacElement}></div>

      <div class="autocomplete">
        <p bind:this={selectedPlaceInfo}></p>
      </div>

      <p class="my-3">To</p>

      <div bind:this={toPacElement} class="w-full"></div>
    </div>
    <div class="flex justify-center">
      <button
        class="bg-violet-800 text-white w-100 cursor-pointer hover:bg-violet-700 transition-all ease-in-out rounded-lg font-bold p-4 text-center outline-0"
        >Go</button
      >
    </div>
  </div>
  <div bind:this={container} class="min-h-[500px]"></div>
</div>
