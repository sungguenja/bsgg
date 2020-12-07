<template>
  <div id="main">
    
  </div>
</template>

<script>
import Axios from 'axios'
const SERVER_URL = process.env.VUE_APP_SERVER_URL
export default {
  data() {
    return {
      user_name: this.$route.params.user_name,
      season: this.$route.params.season,
      team_mode: this.$route.params.team_mode
    }
  },
  created() {
    Axios({
      method: "GET",
      url: `${SERVER_URL}matchhistory/search/${this.user_name}/${this.season}/${this.team_mode}`
    })
    .then(res => {
      var Main = document.getElementById('main')
      console.log(res)
      Main.innerHTML = res.data.output
    })
    .catch(err => {
      console.log(err)
    })
  },
}
</script>

<style>

</style>