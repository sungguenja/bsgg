<template>
  <div class="d-flex" style="margin-left: 200px;">
    <div style="margin-right: 30px;">
      <h2 class="text-light">맵 목록</h2>
      <ul>
        <li v-for="(data,index) in MapListData" :key="index+data.name+data.pk" @click="GoDetail(index+1)" style="cursor: pointer; color: white;">{{data.name}}</li>
      </ul>
    </div>
    <MapComponent @clickdetail="MapClick"></MapComponent>
  </div>
</template>

<script>
import MapComponent from '../../components/gamedata/MapComponent.vue'
import Axios from 'axios'
var SERVER_URL = ''
const check_url = window.location.hostname
if (check_url == 'localhost') {SERVER_URL = 'http://localhost:8000/'}
else if(check_url == 'lumia.kr') {SERVER_URL = 'https://lumia.kr/backapi/'}
else if(check_url == 'xn--2s2b29c91l.kr') {SERVER_URL = 'https://xn--2s2b29c91l.kr/backapi/'}
else if(check_url == '루미아.kr') {SERVER_URL = 'https://루미아.kr/backapi/'}
export default {
  data() {
    return {
      MapListData: []
    }
  },
  created() {
    this.GetData()
  },
  methods: {
    GetData() {
      Axios({
        method: "GET",
        url: SERVER_URL + 'gamedata/area/0'
      })
      .then(res => {
        this.MapListData = res.data
      })
      .catch(err => {console.log(err)})
    },
    GoDetail(n) {
      this.$router.push({name: 'MapDetail',params:{pk:n}})
    },
    MapClick(value) {
      console.log(value)
      this.GoDetail(value[1])
    }
  },
  components: {
    MapComponent
  }
}
</script>

<style>
li:hover {
  background-color: blue;
}
</style>