<template>
  <div class="container">
    <div class="row">
      <NewsComponent v-for="(ne, index) in News" :key="index+ne.title" :ne="ne"></NewsComponent>
    </div>
  </div>
</template>

<script>
import Axios from 'axios'
import NewsComponent from '../components/NewsCompornent.vue'
const SERVER_URL = `http://${window.location.hostname}:8000/`
export default {
  data() {
    return {
      News: null
    }
  },
  created() {
    Axios({
      method: "GET",
      url: SERVER_URL+'matchhistory/steam/20'
    })
    .then(res => {
      this.News = res.data.response
    })
    .catch(err => {console.log(err)})
  },
  components: {
    NewsComponent
  }
}
</script>

<style>

</style>