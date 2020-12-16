<template>
  <div class="text-light">
    <div v-show="isLoading" style="height:1080px;">
      <Loading></Loading>
    </div>
    <div v-show="!isLoading">
      <div v-if="isError" style="height: 1080px;">
        <button @click="SearchHistory" class="m-3 btn btn-secondary">전적 갱신</button>
        <h1>없는 닉네임 또는 서버 에러</h1>
      </div>
      <div v-else>
        <div class="py-3 d-flex justify-content-center" style="background-color: rgb(51,51,51);">
          <div style="background-color: rgb(51,51,51);">
            <h1 class="m-3">{{user_name}}</h1>
            <button @click="SearchHistory" class="m-3 btn btn-secondary">전적 갱신</button>
          </div>
          <div class="d-flex" style="background-color: rgb(51,51,51);">
            <div>
              <p>모스트 플레이</p>
              <MostPlay v-for="(match,i) in most_play" :match="match" :key="i"></MostPlay>
            </div>
            <div>
              <p>평균 순위가 가장 높은 캐릭</p>
              <HighRank v-for="(match,i) in most_rank" :match="match" :key="i"></HighRank>
            </div>
          </div>
        </div>
        <hr>
        <div class="container">
          <div class="row">
            <div class="col-3">
              <div style="background-color: rgb(51,51,51);">
                <h2>우승 횟수: {{total_stat.win_cnt}}</h2>
                <h2>평균 순위: {{total_stat.avg_win}}</h2>
                <h2>평균 킬수: {{total_stat.avg_kill}}</h2>
              </div>
            </div>
            <div class="col-9">
              <RecentMatch v-for="(match,i) in recent_match" :match="match" :key="i" :pk="i" style="background-color: rgb(51,51,51); border-radius: 10px;"></RecentMatch>
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
import MostPlay from '../../components/matchhistory/MostPlay.vue'
import HighRank from '../../components/matchhistory/HighRank.vue'
import Loading from '../../components/varies/Loading.vue'
const SERVER_URL = `http://${window.location.hostname}:8000/`
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
  watch: {
    $route(to,from) {
      this.user_name = from.params.user_name
      this.user_name = to.params.user_name
      this.isLoading = true
      this.isError = false
      this.SearchHistory()
    }
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
          while(this.most_play.length > 3) {
            this.most_play.pop()
          }
          const now_rank = res.data.character_statics
          this.most_rank = [now_rank[0],now_rank[1],now_rank[2]]
          this.recent_match = res.data.recent_match
          this.total_stat = res.data.total_statics
        }
      })
      .catch(err => {
        this.isLoading = false
        this.isError = false
        console.log(err)
      })
    }
  },
  components: {
    RecentMatch,
    MostPlay,
    HighRank,
    Loading
  }
}
</script>

<style>

</style>