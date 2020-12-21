<template>
  <div class="d-flex" style="margin-left: 200px; margin-bottom: 10px;">
    <div class="col-6 row" style="word-break: normal;">
      <SoloItem v-for="(item,index) in items" :key="item.name + index" :item="item" :kind="name"  style="height: 66px; width: 120px;" class="m-2"></SoloItem>
    </div>
    <div class="col-6">
      <h2 class="text-light">{{name}}</h2>
    </div>
    <hr>
  </div>
</template>

<script>
import Axios from 'axios'
import SoloItem from './SoloItem.vue'
const SERVER_URL = `${process.env.VUE_APP_BACK_HTTP}${window.location.hostname}:8000/`
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