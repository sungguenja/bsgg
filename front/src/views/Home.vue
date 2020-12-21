<template>
  <div class="home d-flex" style="min-height: 1080px;">
    <div class="py-3 m-5" style="width: 800px;">
      <MainSearch @clickshow="ShowDetail"></MainSearch>
    </div>
    <div class="py-3 m-5" style="width: 800px;"> 
      <h2 class="text-light">블서 뉴스</h2>
      <b-carousel
        id="carousel-1"
        v-model="slide"
        :interval="4000"
        controls
        indicators
        background="#ababab"
        img-width="1280"
        img-height="720"
        style="text-shadow: 3px 3px 3px black;"
        @sliding-start="onSlideStart"
        @sliding-end="onSlideEnd"
      >
        <b-carousel-slide v-for="(nownews,index) in News" :key="index" :img-src="nownews.url" style="height:450px;">
          <h2 @click="OpenNews(index)" style="cursor:pointer;">{{nownews.title}}</h2>
        </b-carousel-slide>
      </b-carousel>
      <div>
        <img v-for="(nownews,index) in News" :key="nownews.title" :src="nownews.url" @click="slide=index" class="car_little m-3" style="height:75px; width: 20%;">
      </div>
      <div class="py-3">
        <h1 v-show="!isClick" class="text-light">전적 클릭하시면 <br> 세부정보를 보여드립니다</h1>
        <div v-show="isClick">
          <div class="d-flex justify-content-between">
            <img src="" alt="" id="click_chr">
            <h2 class="text-light" id="click_name"></h2>
            <div id="click_stat">
            </div>
          </div>
          <div class="d-flex" id="click_item">
            <RecentMatch :match="ClickedMatch" :pk="pkpk" style="background-color: rgb(51,51,51); border-radius: 10px; min-width: 100%;"></RecentMatch>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import Axios from 'axios'
import MainSearch from '../components/matchhistory/MainSearch.vue'
import RecentMatch from '../components/matchhistory/RecentMatch.vue'
var SERVER_URL = ''
const check_url = window.location.hostname
if (check_url == 'localhost') {SERVER_URL = 'http://localhost:8000/'}
else if(check_url == 'lumia') {SERVER_URL = 'https://lumia.kr/backapi/'}
else if(check_url == 'xn--2s2b29c91l') {SERVER_URL = 'https://xn--2s2b29c91l.kr/backapi/'}
else if(check_url == '루미아') {SERVER_URL = 'https://루미아.kr/backapi/'}
// const IMG_URL = process.env.VUE_APP_IMG_GIT
export default {
  name: 'Home',
  data() {
    return {
      slide: 0,
      sliding: null,
      News: [],
      isClick: false,
      ClickedMatch: {},
      pkpk: 'aksdfkjdnn'
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
    ShowDetail(value) {
      this.ClickedMatch = value
      this.pkpk = this.slide+value.chr_name+value.level+value.rank
      this.isClick = true
      // console.log(value)
      // var selectWindow = document.getElementById('click_chr')
      // selectWindow.src = `${IMG_URL}소형/${value.chr_name}.png`
      // selectWindow = document.getElementById('click_name')
      // selectWindow.innerText = value.chr_name
      // selectWindow = document.getElementById('click_stat')
      // selectWindow.innerHTML = `<b class="text-light">순위:${value.rank}위</b><br><b class="text-light">사냥수:${value.animal_cnt}</b><br><b class="text-light">킬수:${value.kill_cnt}</b>`
      // selectWindow = document.getElementById('click_item')
      // selectWindow.innerHTML = `<img src="${value.weapon_img}" style="height:40px;"> <img src="${value.cloth_img}" style="height:40px;"> <img src="${value.head_img}" style="height:40px;"> <img src="${value.arm_img}" style="height:40px;"> <img src="${value.leg_img}" style="height:40px;"> <img src="${value.accessory_img}" style="height:40px;">`
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
    MainSearch,
    RecentMatch
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
</style>