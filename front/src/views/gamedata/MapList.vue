<template>
  <div class="container">
    <div class="d-flex justify-content-around">
      <div>
        <h2 class="text-light">맵 목록</h2>
        <ul>
          <li v-for="(data,index) in MapListData" :key="index+data.name+data.pk" @click="GoDetail(index+1)" style="cursor: pointer; color: white;">{{data.name}}</li>
        </ul>
      </div>
      <MapComponent @clickdetail="MapClick"></MapComponent>
    </div>
  </div>
</template>

<script>
import MapComponent from '../../components/gamedata/MapComponent.vue'
import Axios from 'axios'
const SERVER_URL = `http://${window.location.hostname}:8000/`
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