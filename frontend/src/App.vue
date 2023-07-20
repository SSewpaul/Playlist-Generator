<template>
    <div class="search-area">
      <Search id="search-bar" @submit="submitSearch"/>
      <button type="button" @click="showModal">Advanced Filters</button>
      <FilterModal v-show="isModalVisible" id="modal" @close="modalSubmit">
        <template v-slot:header>
          Advanced Filters 
        </template>

        <template v-slot:body>
          <div class="filter-sm">
            <label for="limit">limit: </label>
            <input type="text" id="limit" name="limit" value="10">
          </div>

          <div class="filter-sm">
            <label for="market">market: </label>
            <input type="text" id="market" name="market" value="US">
          </div>

          <div class="filter-lg">
            <label for="seed-artists">Seed artists (comma-separated): </label>
            <input type="text" id="seed-artists" name="seed-artists" value="">
          </div>

          <div class="filter-lg">
            <label for="seed-genres">Seed genres (comma-separated): </label>
            <input type="text" id="seed-genres" name="seed-genres" value="">
          </div>

          <div class="filter-lg">
            <label for="seed-tracks">Seed tracks (comma-separated): </label>
            <input type="text" id="seed-tracks" name="seed-tracks" value="">
          </div>

          <div class="filter-sm">
            <label for="min-acousticness">min-acousticness (0-1): </label>
            <input type="number" id="min-acousticness" name="min-acousticness" value="" min="0" max="1" step=0.1>
          </div>

          <div class="filter-sm">
            <label for="max-acousticness">max-acousticness (0-1): </label>
            <input type="number" id="max-acousticness" name="max-acousticness" value="" min="0" max="1" step=0.1>
          </div>

          <div class="filter-sm">
            <label for="target-acousticness">target-acousticness (0-1): </label>
            <input type="number" id="target-acousticness" name="target-acousticness" value="" min="0" max="1" step=0.1>
          </div>

          <div class="filter-sm">
            <label for="min-danceability">min-danceability (0-1): </label>
            <input type="number" id="min-danceability" name="min-danceability" value="" min="0" max="1" step=0.1>
          </div>

          <div class="filter-sm">
            <label for="max-danceability">max-danceability (0-1): </label>
            <input type="number" id="max-danceability" name="max-danceability" value="" min="0" max="1" step=0.1>
          </div>

          <div class="filter-sm">
            <label for="target-danceability">target-danceability (0-1): </label>
            <input type="number" id="target-danceability" name="target-danceability" value="" min="0" max="1" step=0.1>
          </div>

          <div class="filter-sm">
            <label for="min-duration-ms">min-duration-ms: </label>
            <input type="number" id="min-duration-ms" name="min-duration-ms" value="">
          </div>

          <div class="filter-sm">
            <label for="max-duration-ms">max-duration-ms: </label>
            <input type="number" id="max-duration-ms" name="max-duration-ms" value="">
          </div>

          <div class="filter-sm">
            <label for="target-duration-ms">target-duration-ms: </label>
            <input type="number" id="target-duration-ms" name="target-duration-ms" value="">
          </div>

          <div class="filter-sm">
            <label for="min-energy">min-energy (0-1): </label>
            <input type="number" id="min-energy" name="min-energy" value="" min="0" max="1" step=0.1>
          </div>

          <div class="filter-sm">
            <label for="max-energy">max-energy (0-1): </label>
            <input type="number" id="max-energy" name="max-energy" value="" min="0" max="1" step=0.1>
          </div>

          <div class="filter-sm">
            <label for="target-energy">target-acousticness (0-1): </label>
            <input type="number" id="target-energy" name="target-energy" value="" min="0" max="1" step=0.1>
          </div>

          <div class="filter-sm">
            <label for="min-instrumentalness">min-instrumentalness (0-1): </label>
            <input type="number" id="min-instrumentalness" name="min-instrumentalness" value="" min="0" max="1" step=0.1>
          </div>

          <div class="filter-sm">
            <label for="max-instrumentalness">max-instrumentalness (0-1): </label>
            <input type="number" id="max-instrumentalness" name="max-instrumentalness" value="" min="0" max="1" step=0.1>
          </div>

          <div class="filter-sm">
            <label for="target-instrumentalness">target-instrumentalness (0-1): </label>
            <input type="number" id="target-instrumentalness" name="target-instrumentalness" value="" min="0" max="1" step=0.1>
          </div>

          <div class="filter-sm">
            <label for="min-key">min-key (0-11): </label>
            <input type="number" id="min-key" name="min-key" value="" min="0" max="11" step=1>
          </div>

          <div class="filter-sm">
            <label for="max-key">max-key (0-11): </label>
            <input type="number" id="max-key" name="max-key" value="" min="0" max="11" step=1>
          </div>

          <div class="filter-sm">
            <label for="target-key">target-key (0-11): </label>
            <input type="number" id="target-key" name="target-key" value="" min="0" max="11" step=1>
          </div>

          <div class="filter-sm">
            <label for="min-liveness">min-liveness (0-1): </label>
            <input type="number" id="min-liveness" name="min-liveness" value="" min="0" max="1" step=0.1>
          </div>

          <div class="filter-sm">
            <label for="max-liveness">max-liveness (0-1): </label>
            <input type="number" id="max-liveness" name="max-liveness" value="" min="0" max="1" step=0.1>
          </div>

          <div class="filter-sm">
            <label for="target-liveness">target-liveness (0-1): </label>
            <input type="number" id="target-liveness" name="target-liveness" value="" min="0" max="1" step=0.1>
          </div>

          <div class="filter-sm">
            <label for="min-loudness">min-loudness: </label>
            <input type="number" id="min-loudness" name="min-loudness" value="" step="0.1">
          </div>

          <div class="filter-sm">
            <label for="max-loudness">max-loudness: </label>
            <input type="number" id="max-loudness" name="max-loudness" value="" step="0.1">
          </div>

          <div class="filter-sm">
            <label for="target-loudness">target-loudness: </label>
            <input type="number" id="target-loudness" name="target-loudness" value="" step="0.1">
          </div>

          <div class="filter-sm">
            <label for="min-mode">min-mode (0-1): </label>
            <input type="number" id="min-mode" name="min-mode" value="" min="0" max="1" step=0.1>
          </div>

          <div class="filter-sm">
            <label for="max-mode">max-mode (0-1): </label>
            <input type="number" id="max-mode" name="max-mode" value="" min="0" max="1" step=0.1>
          </div>

          <div class="filter-sm">
            <label for="target-mode">target-mode (0-1): </label>
            <input type="number" id="target-mode" name="target-mode" value="" min="0" max="1" step=0.1>
          </div>

          <div class="filter-sm">
            <label for="min-popularity">min-popularity (0-100): </label>
            <input type="number" id="min-popularity" name="min-popularity" value="" min="0" max="100" step=1>
          </div>

          <div class="filter-sm">
            <label for="max-popularity">max-popularity (0-100): </label>
            <input type="number" id="max-popularity" name="max-popularity" value="" min="0" max="100" step=1>
          </div>

          <div class="filter-sm">
            <label for="target-popularity">target-popularity (0-100): </label>
            <input type="number" id="target-popularity" name="target-popularity" value="" min="0" max="100" step=1>
          </div>

          <div class="filter-sm">
            <label for="min-speechiness">min-speechiness (0-1): </label>
            <input type="number" id="min-speechiness" name="min-speechiness" value="" min="0" max="1" step=0.1>
          </div>

          <div class="filter-sm">
            <label for="max-speechiness">max-speechiness (0-1): </label>
            <input type="number" id="max-speechiness" name="max-speechiness" value="" min="0" max="1" step=0.1>
          </div>

          <div class="filter-sm">
            <label for="target-speechiness">target-speechiness (0-1): </label>
            <input type="number" id="target-speechiness" name="target-speechiness" value="" min="0" max="1" step=0.1>
          </div>

          <div class="filter-sm">
            <label for="min-tempo">min-tempo(BPM): </label>
            <input type="number" id="min-tempo" name="min-tempo" value="">
          </div>

          <div class="filter-sm">
            <label for="max-tempo">max-tempo(BPM): </label>
            <input type="number" id="max-tempo" name="max-tempo" value="">
          </div>

          <div class="filter-sm">
            <label for="target-tempo">target-tempo(BPM): </label>
            <input type="number" id="target-tempo" name="target-tempo" value="">
          </div>

          <div class="filter-sm">
            <label for="min-time-signature">min-time-signature (0-11): </label>
            <input type="number" id="min-time-signature" name="min-time-signature" value="" min="0" max="11" step=1>
          </div>

          <div class="filter-sm">
            <label for="max-time-signature">max-time-signature (0-11): </label>
            <input type="number" id="max-time-signature" name="max-time-signature" value="" min="0" max="11" step=1>
          </div>

          <div class="filter-sm">
            <label for="target-time-signature">target-time-signature (0-11): </label>
            <input type="number" id="target-time-signature" name="target-time-signature" value="" min="0" max="11" step=1>
          </div>

          <div class="filter-sm">
            <label for="min-valence">min-valence (0-1): </label>
            <input type="number" id="min-valence" name="min-valence" value="" min="0" max="1" step=0.1>
          </div>

          <div class="filter-sm">
            <label for="max-valence">max-valence (0-1): </label>
            <input type="number" id="max-valence" name="max-valence" value="" min="0" max="1" step=0.1>
          </div>

          <div class="filter-sm">
            <label for="target-valence">target-valence (0-1): </label>
            <input type="number" id="target-valence" name="target-valence" value="" min="0" max="1" step=0.1>
          </div>
        </template>

      </FilterModal>
    </div>
    <FooterSection id="footer-section"/>
</template>

<script lang="ts">
import Search from "./components/Search.vue";
import FooterSection from "./components/Footer.vue"
import FilterModal from "./components/Modal.vue"
import axios from 'axios'

export default{
  name: 'App',
  components: {
    Search,
    FooterSection,
    FilterModal
  },
  data() {
    return {
      isModalVisible: false,
      filters : {
        limit: 10,
        market: 'US'
      },
      body: {}
    };
  },
  methods: {
    showModal() {
      this.isModalVisible = true;
    },
    closeModal() {
      this.isModalVisible = false;
    },
    modalSubmit() {
      
      this.filters = {
        limit: parseFloat(document.querySelector("#limit").value),
        market: document.querySelector("#market").value,
        seed_artist: document.querySelector("#seed-artists").value,
        seed_genres: document.querySelector("#seed-genres").value,
        seed_tracks: document.querySelector("#seed-tracks").value,
        min_acousticness:parseFloat(document.querySelector("#min-acousticness").value),
        max_acousticness:parseFloat(document.querySelector("#max-acousticness").value),
        target_acousticness:parseFloat(document.querySelector("#target-acousticness").value),
        min_danceability:parseFloat(document.querySelector("#min-danceability").value),
        max_danceability:parseFloat(document.querySelector("#max-danceability").value),
        target_danceability:parseFloat(document.querySelector("#target-danceability").value),
        min_duration_ms:parseFloat(document.querySelector("#min-duration-ms").value),
        max_duration_ms:parseFloat(document.querySelector("#max-duration-ms").value),
        target_duration_ms:parseFloat(document.querySelector("#target-duration-ms").value),
        min_energy:parseFloat(document.querySelector("#min-energy").value),
        max_energy:parseFloat(document.querySelector("#max-energy").value),
        target_energy:parseFloat(document.querySelector("#target-energy").value),
        min_instumentalness:parseFloat(document.querySelector("#min-instrumentalness").value),
        max_instumentalness:parseFloat(document.querySelector("#max-instrumentalness").value),
        target_instumentalness:parseFloat(document.querySelector("#target-instrumentalness").value),
        min_key: parseFloat(document.querySelector("#min-key").value),
        max_key: parseFloat(document.querySelector("#max-key").value),
        target_key: parseFloat(document.querySelector("#target-key").value),
        min_liveness: parseFloat(document.querySelector("#min-liveness").value),
        max_liveness: parseFloat(document.querySelector("#max-liveness").value),
        target_liveness: parseFloat(document.querySelector("#target-liveness").value),
        min_loudness: parseFloat(document.querySelector("#min-loudness").value),
        max_loudness: parseFloat(document.querySelector("#max-loudness").value),
        target_loudness: parseFloat(document.querySelector("#target-loudness").value),
        min_mode: parseFloat(document.querySelector("#min-mode").value),
        max_mode: parseFloat(document.querySelector("#max-mode").value),
        target_mode: parseFloat(document.querySelector("#target-mode").value),
        min_popularity: parseFloat(document.querySelector("#min-popularity").value),
        max_popularity: parseFloat(document.querySelector("#max-popularity").value),
        target_popularity: parseFloat(document.querySelector("#target-popularity").value),
        min_speechiness: parseFloat(document.querySelector("#min-speechiness").value),
        max_speechiness: parseFloat(document.querySelector("#max-speechiness").value),
        target_speechiness: parseFloat(document.querySelector("#target-speechiness").value),
        min_tempo: parseFloat(document.querySelector("#min-tempo").value),
        max_tempo: parseFloat(document.querySelector("#max-tempo").value),
        target_tempo: parseFloat(document.querySelector("#target-tempo").value),
        min_time_signature: parseFloat(document.querySelector("#min-time-signature").value),
        max_time_signature: parseFloat(document.querySelector("#max-time-signature").value),
        target_time_signature: parseFloat(document.querySelector("#target-time-signature").value),
        min_valence: parseFloat(document.querySelector("#min-valence").value),
        max_valence: parseFloat(document.querySelector("#max-valence").value),
        target_valence: parseFloat(document.querySelector("#target-valence").value),
      };

      this.isModalVisible = false;
    },
    submitSearch(value){

      
      let body = {};
      for (const param in this.filters) {
        if (this.filters[param]){
          body[param] = this.filters[param];
        }
      }
      
      return axios.post('http://localhost/filter/', body, {
        headers: { "Content-Type": "application/json; charset=UTF-8" },
        params: { search_words: value }
      })
      
    }
  }
};
</script>

<style scoped>
.search-area{
  height: 95%;
  margin: 0 10% 0 10%;
}

#search-bar{
  width: 100%;
  height: 100%;
}

#footer-section {
  height: 5%;
}

.filter-sm{
  margin-top: 5%;
}
.filter-lg{
  margin-top: 5%;
}

.filter-sm input{
  max-width: 20%;
  text-align: center;
}

</style>
