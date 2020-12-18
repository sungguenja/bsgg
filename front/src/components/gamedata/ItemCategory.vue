<template>
  <div class="container">
    <div class="row">
      <div class="col-6 row" style="word-break: normal;">
        <SoloItem v-for="(item,index) in items" :key="item.name + index" :item="item" :kind="name" class="m-2"></SoloItem>
      </div>
      <div class="col-6">
        <h2 class="text-light">{{name}}</h2>
      </div>
    </div>
    <hr>
  </div>
</template>

<script>
import Axios from 'axios'
import SoloItem from './SoloItem.vue'
const SERVER_URL = `http://${window.location.hostname}:8000/`
export default {
  data() {
    return {
      items: [],
    }
  },
  props: {
    itemcat: Number,
    name: String
  },
  created() {
    this.SearchItems()
  },
  methods: {
    SearchItems() {
      Axios({
        method: "GET",
        url: SERVER_URL + 'gamedata/category/' + this.itemcat
      })
      .then(res => {
        this.items = res.data.items
      })
      .catch(err => {
        console.log(err)
      })
    }
  },
  components: {
    SoloItem
  }
}
</script>

<style>

</style>