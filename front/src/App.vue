<template>
  <div id="app" :style="`background-image: url( ${backgroundImg}); min-width:1900px; min-height: ${user_height}px; background-repeat: repeat;'`">
    <div class="d-flex" style="height: 6%;">
      <img :src="require('./assets/image/assets/button-home.png')" style="cursor: pointer;" alt="" @click="GoPush(2)">
      <img :src="require('./assets/image/assets/menu-top.png')" style="position: absolute; left: 235px; z-index: 1; overflow: auto;" alt="">
      <img :src="require('./assets/image/assets/menu-top_side.png')" style="position: absolute; top: -4px;left: 1902px; z-index: 0; overflow: auto;" v-if="BigDisplay" alt="">
      <div style="width: 90%; height: 100%;" class="d-flex justify-content-between">
        <div class="my-3 d-flex justify-content-around" style="margin-left: 4%; width: 40%; z-index: 2;">
          <span class="nav_button_text" @click="GoPush(0)">News</span>
          <span class="nav_button_text" @click="GoPush(1)">캐릭터 정보</span>
          <span class="nav_button_text" @click="GoPush(3)">게임 정보</span>
          <span class="nav_button_text" @click="GoPush(4)">공략</span>
          <span class="nav_button_text" @click="GoPush(5)">Help</span>
        </div>
        <div style="width:40%;"></div>
        <form @submit.prevent="Search" class="my-2" style="width: 20%; z-index: 1;">
          <input type="text" style="width: 80%; border-radius: 3% 0 0 3% / 50% 50% 50% 50%; background-color: rgb(0,0,0); padding: 0 10px 0 10px; color: rgb(255,255,255);" v-model="search_text" placeholder="여긴 아직 미구현입니다" class="search_bar">
          <img :src="require('./assets/image/assets/button-search-all-on.png')" style="width: 20%;">
        </form>
      </div>
    </div>
    <div>
      <router-view class="py-2"/>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      backgroundImg: require('./assets/image/assets/bg.jpg'),
      can_go: ['News','CharacterList','Home','SelectCategory',"PlayThroughList",'NotFoundPage'],
      user_height: screen.height,
      search_text: null,
      BigDisplay: false
    }
  },
  created() {
    document.title = 'Lumia'
    if(window.outerWidth > 2000) {this.BigDisplay = true}
  },
  methods: {
    GoPush(n) {
      this.$router.push({name: this.can_go[n]})
    },
    Search() {
      console.log('됨')
    }
  },
}
</script>

<style>
#app {
  font-family: 'SeoulNamsanM', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#app::after {
  background-repeat: repeat;
}

.menu_image_home {
  width: 243px;
  margin: 0 74px 52px 0;
  padding: 28px 87px 0 0;
  object-fit: contain;
}

.button_home {
  width: 104px;
  height: 28px;
  object-fit: contain;
}

.inner-shadow {
  width: 156px;
  height: 62px;
  padding: 18px 3px 33px 20px;
  top:0%;
  position: absolute;
}

@font-face {
  font-family: 'SeoulNamsanM';
  src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_two@1.0/SeoulNamsanM.woff') format('woff');
  font-weight: normal;
  font-style: normal;
}

.nav_button {
  margin: 1px 62px 23px 0;
  cursor: pointer;
}

.nav_button_text {
  color: #bdbdbd;
  font-family: 'SeoulNamsanM';
  font-size: 25px;
  font-weight: normal;
  font-stretch: normal;
  font-style: normal;
  line-height: normal;
  letter-spacing: -1.88px;
  text-align: center;
  cursor: pointer;
  text-shadow: 2px 2px 2px #2e2c2a;
}

.nav_button_text:hover {
  color: orange;
}

.search_bar::placeholder {
  color: white;
  font-size: 13px;
}
</style>
