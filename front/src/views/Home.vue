<template>
  <div class="home" style="height: 1080px;">
    <img alt="Vue logo" :src="'../image/logo_white.png'">
    <Search/>
  </div>
</template>

<script>
// @ is an alias to /src
import Search from '../components/matchhistory/Search.vue'

export default {
  name: 'Home',
  components: {
    Search
  }
}
</script>
