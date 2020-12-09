<template>
  <div>
    <div v-if="isLoading">로딩중</div>
    <div v-else>
      <button @click="SearchHistory">전적 갱신</button>
      <div v-if="isError">
        <h1>없는 닉네임 또는 서버 에러</h1>
      </div>
      <div v-else>
        <div class="d-flex justify-content-center">
          <h1>{{user_name}}</h1>
          <div class="d-flex">
            <div>
              <p>모스트 플레이</p>
              <a><img :src="most_play[0].chr_img" style="height:80px; border-radius: 70%;"> {{most_play[0].chr_name}} 플레이 횟수: {{most_play[0].chr_cont}} 탑3 횟수: {{most_play[0].chr_top3}}</a><br>
              <a><img :src="most_play[1].chr_img" style="height:80px; border-radius: 70%;"> {{most_play[1].chr_name}} 플레이 횟수: {{most_play[1].chr_cont}} 탑3 횟수: {{most_play[1].chr_top3}}</a><br>
              <a><img :src="most_play[2].chr_img" style="height:80px; border-radius: 70%;"> {{most_play[2].chr_name}} 플레이 횟수: {{most_play[2].chr_cont}} 탑3 횟수: {{most_play[2].chr_top3}}</a>
            </div>
            <div>
              <p>평균 순위가 가장 높은 캐릭</p>
              <a><img :src="most_rank[0].chr_img" style="height:80px; border-radius: 70%;"> {{most_rank[0].chr_name}} 평균 순위: {{most_rank[0].avg_win}} 최대 킬수: {{most_rank[0].max_kill}}</a><br>
              <a><img :src="most_rank[1].chr_img" style="height:80px; border-radius: 70%;"> {{most_rank[1].chr_name}} 평균 순위: {{most_rank[1].avg_win}} 최대 킬수: {{most_rank[1].max_kill}}</a><br>
              <a><img :src="most_rank[2].chr_img" style="height:80px; border-radius: 70%;"> {{most_rank[2].chr_name}} 평균 순위: {{most_rank[2].avg_win}} 최대 킬수: {{most_rank[2].max_kill}}</a><br>
            </div>
          </div>
        </div>
        <hr>
        <div class="container">
          <div class="row">
            <div class="col-3">
              <h2>우승 횟수: {{total_stat.win_cnt}}</h2>
              <h2>평균 순위: {{total_stat.avg_win}}</h2>
              <h2>평균 킬수: {{total_stat.avg_kill}}</h2>
            </div>
            <div class="col-9">
              <RecentMatch v-for="(match,i) in recent_match" :match="match" :key="i"></RecentMatch>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Axios from 'axios'
import RecentMatch from '../../components/matchhistory/RecentMatch.vue'
const SERVER_URL = process.env.VUE_APP_SERVER_URL
export default {
  data() {
    return {
      user_name: this.$route.params.user_name,
      season: this.$route.params.season,
      team_mode: this.$route.params.team_mode,
      isLoading: true,
      isError: false,
      most_play: [],
      most_rank: [],
      total_stat: [],
      recent_match: []
    }
  },
  created() {
    this.isLoading = true
    this.isError = false
    this.SearchHistory()
  },
  methods: {
    SearchHistory() {
      this.isLoading = true
      this.isError = false
      Axios({
        method: "GET",
        url: `${SERVER_URL}matchhistory/search/${this.user_name}/${this.season}/${this.team_mode}`
      })
      .then(res => {
        this.isLoading = false
        if(res.data.success == 0) {this.isError = true}
        else {
          this.isError = false
          this.most_play = res.data.most_played
          this.most_rank = res.data.character_statics
          this.recent_match = res.data.recent_match
          this.total_stat = res.data.total_statics
        }
      })
      .catch(err => {
        console.log(err)
      })
    }
  },
  components: {
    RecentMatch
  }
}
</script>

<style>

</style>