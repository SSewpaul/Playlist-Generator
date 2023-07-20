<script setup lang="ts">
import { ref } from 'vue';
</script>

<template>
    <div class="search_box">
        <input type="text" id="search-text" v-model="search_val" placeholder="Type of music" v-on:keyup.enter = "submitSearch"/>
        <button type="submit" v-on:click="submitSearch">
        <img src="../assets/search-interface-symbol.png" alt="search" >
    </button>
    </div>
</template>

<script lang="ts">
let search_val = ref("");

export default {
    name: "Search",
    methods: {
        submitSearch() {
            this.$emit('submit', document.querySelector('#search-text').value);
        }
    }
};
</script>

<style>
@import '../assets/base.css';

.search_box
{
    margin-top: 20%;
    display: flex;
    justify-content: center;
    min-width: 25px;
    min-height: 25px;
    width: 50%;
    height: 10%;
    max-width: 60vw;
    max-height: 6vh;
}

.search_box input{
    width: 100%;
    height: 100%;
}

.search_box button{
    min-width: 25px;
    min-height: 25px;
    width: 10%;
    background-color: white; 
    border: 1px solid white;
    border-radius: 25%;
    display: flex;
    justify-content: center;
    align-items: center;
}

.search_box button img{
    width: 80%;
    height: 80%;
}

input {
    background-color: var(--vt-c-black);
    border-bottom: 1% solid white;
    border-left: 0px;
    border-right: 0px;
    border-top: 0px;
    color: white;
    font: 16pt sans-serif;
}
</style>