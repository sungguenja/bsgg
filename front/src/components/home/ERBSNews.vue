<template>
  <div style="margin-left: 61px; margin-top: 48px; width: 610px;">
    <span class="text-light erbs_news_title">블서 뉴스</span>
    <b-carousel
      id="carousel-1"
      v-model="slide"
      :interval="4000"
      controls
      indicators
      background="rgba(171,171,171,0.3)"
      img-width="610px"
      img-height="360px"
      style="text-shadow: 3px 3px 3px black; width: 610px; height:360px;"
      @sliding-start="onSlideStart"
      @sliding-end="onSlideEnd"
    >
    <b-carousel-slide v-for="(nownews,index) in News" :key="index+nownews.title" :img-src="nownews.url" style="height:360px; width:610px;">
        <h2 @click="OpenNews(index)" style="cursor:pointer; background-color: rgba(0,0,0,0.5)">{{nownews.title}}</h2>
      </b-carousel-slide>
    </b-carousel>
    <div class="mt-2">
      <img v-for="(nownews,index) in News" :key="nownews.title" :src="nownews.url" @click="slide=index" class="car_little" style="height:75px; width: 25%; border-style: solid; border-image: linear-gradient(to bottom, grey, black); border-width: 2px; border-image-slice: 1;">
    </div>
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
      slide: 0,
      sliding: null,
      News: [],
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
}
</script>

<style>
.erbs_news_title {
  width: 226px;
  height: 61px;
  margin: 47px 76px 79px 61px;
  font-family: 'SeoulNamsanM';
  font-size: 64px;
  font-weight: normal;
  font-stretch: normal;
  font-style: normal;
  line-height: normal;
  letter-spacing: -4.8px;
  text-align: left;
  color: #bdbdbd;
}
</style>