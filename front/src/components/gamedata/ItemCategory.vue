<template>
  <div class="d-flex" style="margin-left: 200px; margin-bottom: 10px;">
    <div class="col-6 row" style="word-break: normal;">
      <SoloItem v-for="(item,index) in items" :key="item.name + index" :item="item" :kind="name"  style="height: 66px; width: 120px;" class="m-2"></SoloItem>
    </div>
    <div class="col-6">
      <h2 class="text-light">{{name}}</h2>
      <ArmorStat v-if="categoryType == 1" :stats="stats" :cat="name"/>
    </div>
    <hr>
  </div>
</template>

<script>
import Axios from 'axios'
import SoloItem from './SoloItem.vue'
import ArmorStat from './ArmorStat.vue'
var SERVER_URL = ''
const check_url = window.location.hostname
if (check_url == 'localhost') {SERVER_URL = 'http://localhost:8000/'}
else if(check_url == 'lumia.kr') {SERVER_URL = 'https://lumia.kr/backapi/'}
else if(check_url == 'xn--2s2b29c91l.kr') {SERVER_URL = 'https://xn--2s2b29c91l.kr/backapi/'}
else if(check_url == '루미아.kr') {SERVER_URL = 'https://루미아.kr/backapi/'}
export default {
  data() {
    return {
      items: [],
      stats: []
    }
  },
  props: {
    itemcat: Number,
    name: String,
    categoryType: Number
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
        this.stats = res.data.stats
      })
      .catch(err => {
        console.log(err)
      })
    }
  },
  components: {
    SoloItem,
    ArmorStat
  }
}
</script>

<style>

</style>