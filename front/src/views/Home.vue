<template>
  <div class="home" style="width: 1400px; margin-top: 50px; margin-left: 250px;">
    <div style="min-width: 100%; min-height: 600px;" class="d-none">
      <h1>루트창</h1>
    </div>
    <div class="d-flex flex-wrap"> 
      <SearchBar @startsearch="GoSearch" :search_time="search_time"/>
      <!-- <LumiaNews/> -->
      <div style="min-width: 100px;"></div> 
      <div class="mb-2">
        <UserStat :stat="total_statics" :notYet="notYet" :isError="isError" :isLoading="isLoading"/>
        <MainMost :most_played="most_played" :notYet="notYet" :isError="isError" :isLoading="isLoading"/>
      </div>
      <ERBSNews/>
      <div style="width: 396px;" v-show="isSearch">
        <span class="main_high_rank_text" style="float: left;">캐릭터별 평균 순위</span>
        <MainHighRank v-for="(stat,index) in character_statics" :key="stat.avg_win+stat.chr_name+index" :character_stat="stat"/>
        <button @click="whatlook = !whatlook" v-show="showButton">다른 내용</button>
        <RecentMatch :match="ClickedMatch" :pk="ClickedMatch.date" v-show="whatlook & showButton"/>
        <MatchInfo :info="ClickedMatchDetail" v-show="!whatlook & showButton"/>
      </div>
      <div style="width: 895px; margin-left: 52px;" v-show="isSearch">
        <span class="recent_match_text" style="float: left;">최근 매치</span>
        <RecentMatchtable :recent_match="recent_match" @clickshow="ShowDetail"/>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import Axios from 'axios'
import RecentMatch from '../components/matchhistory/RecentMatch.vue'
import SearchBar from '../components/matchhistory/SearchBar.vue'
// import LumiaNews from '../components/home/LumiaNews.vue'
import UserStat from '../components/matchhistory/UserStat.vue'
import ERBSNews from '../components/home/ERBSNews.vue'
import MainMost from '../components/matchhistory/MainMost.vue'
import MainHighRank from '../components/matchhistory/MainHighRank.vue'
import RecentMatchtable from '../components/matchhistory/RecentMatchTable'
import MatchInfo from '../components/matchhistory/MatchInfo.vue'
var SERVER_URL = ''
const check_url = window.location.hostname
if (check_url == 'localhost') {SERVER_URL = 'http://localhost:8000/'}
else if(check_url == 'lumia.kr') {SERVER_URL = 'https://lumia.kr/backapi/'}
else if(check_url == 'xn--2s2b29c91l.kr') {SERVER_URL = 'https://xn--2s2b29c91l.kr/backapi/'}
else if(check_url == '루미아.kr') {SERVER_URL = 'https://루미아.kr/backapi/'}
// const IMG_URL = process.env.VUE_APP_IMG_GIT
export default {
  name: 'Home',
  data() {
    return {
      recent_match: [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      isClick: false,
      ClickedMatch: {},
      pkpk: 'aksdfkjdnn',
      notYet: true,
      isLoading: false,
      isError: false,
      season: 'OPEN',
      total_statics: {},
      most_played: [0,0,0,0,0],
      character_statics: [],
      search_time: '',
      isSearch: false,
      whatlook: true,
      showButton: false,
      ClickedMatchDetail: {}
    }
  },
  methods: {
    onSlideStart(slide) {
      this.sliding = true
      console.log(slide)
    },
    onSlideEnd(slide) {
      this.sliding = false
      console.log(slide)
    },
    OpenNews(n) {
      window.open(this.News[n].click,'_blank')
    },
    GoSearch(value) {
      let user_name = value.user_name
      this.SearchHistory(user_name,value.mode_select+1)
    },
    SearchHistory(name,mode) {
      if(name == null) {
        alert('닉네임을 입력해주세요')
        return false
      }
      this.character_statics = []
      this.recent_match = []
      this.ClickedMatch = {}
      this.ClickedMatchDetail = {}
      this.showButton = false
      this.notYet = false
      this.isLoading = true
      this.isError = false
      Axios({
        method: "GET",
        url: `${SERVER_URL}matchhistory/search/${name}/${this.season}/${mode}`
      })
      .then(res => {
        this.isLoading = false
        this.isSearch = true
        if(res.data.success == 0) {this.isError = true}
        else {
          var chst = []
          if('character_statistics' in res.data.most_played.normal) {
            for(var i=0; i<res.data.most_played.normal.character_statistics.length; i++) {chst.push(res.data.most_played.normal.character_statistics[i])}
          }
          var j = 0
          var cnt = 0
          if('character_statistics' in res.data.most_played.rank) {
            for(i=0; i<res.data.most_played.rank.character_statistics.length; i++) {
              cnt = 0
              for(j=0; j<chst.length; j++){
                if(res.data.most_played.rank.character_statistics[i].characterCode == chst[j].characterCode){
                  chst[j].totalGames += res.data.most_played.rank.character_statistics[i].totalGames
                  chst[j].top3 += res.data.most_played.rank.character_statistics[i].top3
                  chst[j].wins += res.data.most_played.rank.character_statistics[i].wins
                  chst[j].maxKillings = Math.max(chst[j].maxKillings,res.data.most_played.rank.character_statistics[i].maxKillings)
                }
                else {cnt += 1}
              }
              if(cnt == chst.length) {
                chst.push(res.data.most_played.rank.character_statistics[i])
              }
            }
          }
          this.character_statics = chst
          this.most_played = []
          var whe = -1
          for(i=0;i<chst.length;i++){
            if(this.most_played.length<5){
              this.most_played.push(chst[i])
            }
            else {
              cnt = -1
              whe = -1
              for(j=0; j<this.most_played.length; j++) {
                if(this.most_played[j].totalGames < chst[i].totalGames) {
                  if(cnt == -1){
                    cnt = this.most_played[j].totalGames
                    whe = j
                  } else {
                    if(cnt > this.most_played[j].totalGames) {
                      cnt = this.most_played[j].totalGames
                      whe = j
                    }
                  }
                }
              }
              if(whe != -1) {this.most_played[whe] = chst[i]}
            }
          }
          if(!this.isEmpty(res.data.most_played.normal) & !this.isEmpty(res.data.most_played.rank)){
            this.total_statics = {
              'win_cnt': res.data.most_played.normal.total_win + res.data.most_played.rank.total_win,
              'avg_win': ((res.data.most_played.normal.avg_rank*res.data.most_played.normal.total_play+res.data.most_played.rank.avg_rank*res.data.most_played.rank.total_play)/(res.data.most_played.normal.total_play+res.data.most_played.rank.total_play)).toFixed(2) ,
              'avg_kill': ((res.data.most_played.normal.avg_kill*res.data.most_played.normal.total_play+res.data.most_played.rank.avg_kill*res.data.most_played.rank.total_play)/(res.data.most_played.normal.total_play+res.data.most_played.rank.total_play)).toFixed(2) 
            }
          } else if(!this.isEmpty(res.data.most_played.normal) & this.isEmpty(res.data.most_played.rank)) {
            this.total_statics = {
              'win_cnt': res.data.most_played.normal.total_win,
              'avg_win': res.data.most_played.normal.avg_rank,
              'avg_kill': res.data.most_played.normal.avg_kill
            }
          } else if(this.isEmpty(res.data.most_played.normal) & !this.isEmpty(res.data.most_played.rank)) {
            this.total_statics = {
              'win_cnt': res.data.most_played.rank.total_win,
              'avg_win': res.data.most_played.rank.avg_rank,
              'avg_kill': res.data.most_played.rank.avg_kill
            }
          } else {
            this.total_statics = {
              'win_cnt': 0,
              'avg_win': 0,
              'avg_kill': 0
            }
          }
          
          this.total_statics.name = name
          let today = new Date()
          this.search_time = `${today.getFullYear()}/${today.getMonth()+1}/${today.getDate()}/${today.getHours()}:${today.getMinutes()}:${today.getSeconds()}`
          this.isError = false
          this.recent_match = res.data.recent_match
        }
      })
      .catch(err => {
        this.isLoading = false
        this.isError = true
        console.log(err)
      })
    },
    ShowDetail(value) {
      this.ClickedMatch = value
      var now = {}
      now.mastery = value.mastery
      now.skill_pick = value.skill_pick
      now.rank = value.rank
      now.name = value.chr_name
      this.ClickedMatchDetail = now
      this.showButton = true
    },
    isEmpty(param) {
      return Object.keys(param).length === 0
    }
  },
  created() {
    Axios({
      method: "GET",
      url: SERVER_URL+'matchhistory/steam/4'
    })
    .then(res => {
      this.News = res.data.response
    })
    .catch(err => {console.log(err)})
  },
  components: {
    RecentMatch,
    SearchBar,
    // LumiaNews,
    UserStat,
    ERBSNews,
    MainMost,
    MainHighRank,
    RecentMatchtable,
    MatchInfo
  }
}
</script>

<style>
.car_little {
  -webkit-transform:scale(1);
  -moz-transform:scale(1);
  -ms-transform:scale(1); 
  -o-transform:scale(1);  
  transform:scale(1);
  -webkit-transition:.3s;
  -moz-transition:.3s;
  -ms-transition:.3s;
  -o-transition:.3s;
  transition:.3s;
}

.car_little:hover {
  -webkit-transform:scale(1.2);
  -moz-transform:scale(1.2);
  -ms-transform:scale(1.2);   
  -o-transform:scale(1.2);
  transform:scale(1.2);
}

.main_high_rank_text {
  height: 31px;
  font-family: 'SeoulNamsanM';
  font-size: 32px;
  font-weight: normal;
  font-stretch: normal;
  font-style: normal;
  line-height: normal;
  letter-spacing: -2.4px;
  text-align: left;
  color: #bdbdbd;
}

.recent_match_text {
  height: 30px;
  font-family: 'SeoulNamsanM';
  margin-left: 16px;
  margin-bottom: 8px;;
  font-size: 32px;
  font-weight: normal;
  font-stretch: normal;
  font-style: normal;
  line-height: normal;
  letter-spacing: -2.4px;
  text-align: left;
  color: #bdbdbd;
}
</style>