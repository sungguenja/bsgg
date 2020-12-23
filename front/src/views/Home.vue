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
        <RecentMatch :match="ClickedMatch" :pk="ClickedMatch.date"/>
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
      isSearch: false
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
      let mode = ['Solo','Duo','Trio']
      let selected_mode = mode[value.mode_select]
      this.SearchHistory(user_name,selected_mode)
    },
    SearchHistory(name,mode) {
      if(name == null) {
        alert('닉네임을 입력해주세요')
        return false
      }
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
          this.character_statics = res.data.character_statics
          this.most_played = res.data.most_played
          this.total_statics = res.data.total_statics
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
    RecentMatchtable
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