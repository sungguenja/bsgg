<template>
  <div class="home" style="min-height: 1080px;">
    <div class="container">
      <div class="row">
        <div class="col-6 py-3">
          <MainSearch @clickshow="ShowDetail"></MainSearch>
        </div>
        <div class="col-6 py-3"> 
          <h2 class="text-light">블서 뉴스</h2>
          <b-carousel
            id="carousel-1"
            v-model="slide"
            :interval="4000"
            controls
            indicators
            background="#ababab"
            img-width="1024"
            img-height="480"
            style="text-shadow: 1px 1px 2px #333;"
            @sliding-start="onSlideStart"
            @sliding-end="onSlideEnd"
          >
            <b-carousel-slide v-for="(nownews,index) in News" :key="index" :img-src="nownews.url" style="height:303px;">
              <h1 @click="OpenNews(index)" style="cursor:pointer;">{{nownews.title}}</h1>
            </b-carousel-slide>
          </b-carousel>
          <img v-for="(nownews,index) in News" :key="nownews.title" :src="nownews.url" @click="slide=index" class="car_little col-3 my-1" style="height:59px;">
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import Axios from 'axios'
import MainSearch from '../components/matchhistory/MainSearch.vue'
const SERVER_URL = `http://${window.location.hostname}:8000/`
export default {
  name: 'Home',
  data() {
    return {
      slide: 0,
      sliding: null,
      News: []
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
      console.log(value)
    }
  },
  created() {
    Axios({
      method: "GET",
      url: SERVER_URL+'matchhistory/steam/'
    })
    .then(res => {
      this.News = res.data.response
    })
    .catch(err => {console.log(err)})
  },
  components: {
    MainSearch
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