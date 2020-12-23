<template>
  <div style="margin-left: 270px; width: 50%;">
    <div class="d-flex justify-content-around my-3">
      <button @click="ChangeMode(1)">솔로</button>
      <button @click="ChangeMode(2)">듀오</button>
      <button @click="ChangeMode(3)">스쿼드</button>
    </div>
    <div v-if="ranker.length == 0">
      <h1 class="text-light">로딩중입니다</h1>
    </div>
    <table class="table table-striped table-dark text-light">
      <thead style="background-color: black;">
        <tr>
          <th scope="col">등수</th>
          <th scope="col">닉네임</th>
          <th scope="col">mmr</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(value,index) in ranker.topRanks" :key="index+value.mmr+value.nickname">
          <th scope="row">{{value.rank}}</th>
          <td><b @click="GoRanker(value.nickname)" style="cursor: pointer;">{{value.nickname}}</b></td>
          <td>{{value.mmr}}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
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
      ranker: [],
      now_mode: 1,
      mode: [0,'Solo','Duo','Trio']
    }
  },
  created() {
    this.GetRanker()
  },
  methods: {
    GetRanker() {
      Axios({
        method: "GET",
        url: SERVER_URL + 'matchhistory/rank/' + this.now_mode
      })
      .then(res => {this.ranker = res.data})
      .catch(err => {console.log(err)})
    },
    GoRanker(name) {this.$router.push({name:'MatchHistory',params:{'user_name':name,'season':'OPEN','team_mode':this.mode[this.now_mode]}})},
    ChangeMode(n) {
      this.ranker = []
      this.now_mode = n
      this.GetRanker()
    }
  }
}
</script>

<style>

</style>