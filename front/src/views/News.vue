<template>
  <div >
    <NewsComponent v-for="(ne, index) in News" :key="index+ne.title" :ne="ne"></NewsComponent>
  </div>
</template>

<script>
import Axios from 'axios'
import NewsComponent from '../components/NewsCompornent.vue'
var SERVER_URL = ''
const check_url = window.location.hostname
if (check_url == 'localhost') {SERVER_URL = 'http://localhost:8000/'}
else if(check_url == 'lumia') {SERVER_URL = 'https://lumia.kr/backapi/'}
else if(check_url == 'xn--2s2b29c91l') {SERVER_URL = 'https://xn--2s2b29c91l.kr/backapi/'}
else if(check_url == '루미아') {SERVER_URL = 'https://루미아.kr/backapi/'}
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