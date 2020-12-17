<template>
  <div id="app" :style="`background-image: url( ${backgroundImg}); min-height:`+user_height+'px; background-repeat: repeat;'">
    <div class="d-flex" style="height: 6%;">
      <img :src="require('./assets/image/assets/button-home.png')" style="width: 10%; height: 100%; cursor: pointer;" alt="" @click="GoPush(2)">
      <div :style="`width: 90%; height: 100%; background-image: url(${require('./assets/image/assets/menu-top.png')}); background-size: cover;`" class="d-flex justify-content-between">
        <div class="my-2" style="margin-left: 4%;">
          <span class="nav_button_text" @click="GoPush(0)">전적 검색</span>
          <span class="nav_button_text" @click="GoPush(1)">캐릭터 정보</span>
          <span class="nav_button_text" @click="GoPush(3)">아이템 정보</span>
          <span class="nav_button_text" @click="GoPush(3)">공략</span>
          <span class="nav_button_text" @click="GoPush(3)">Contact</span>
        </div>
        <form @submit.prevent="Search" class="my-2" style="width: 20%; margin-right: 4%;">
          <input type="text" style="width: 100%; border-radius: 3% 3% 3% 3% / 50% 50% 50% 50%; background-color: rgb(0,0,0); padding: 0 10px 0 10px; color: rgb(255,255,255);" v-model="search_text" placeholder="검색을 해보아요">
        </form>
      </div>
    </div>
    <router-view class="py-2"/>
  </div>
</template>

<script>
export default {
  data() {
    return {
      backgroundImg: require('./assets/image/assets/bg.jpg'),
      can_go: ['SearchHistory','CharacterList','Home','NotFoundPage'],
      user_height: screen.height,
      search_text: null,
    }
  },
  created() {
    document.title = 'Lumia'
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
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

.menu_image_home {
  width: 243px;
  height: 90px;
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
  margin: 19px 81px 26px 0;
  font-family: 'SeoulNamsanM';
  font-size: 3vh;
  font-weight: normal;
  font-stretch: normal;
  font-style: normal;
  line-height: normal;
  letter-spacing: -1.88px;
  text-align: center;
  cursor: pointer;
  text-shadow: 4px 4px 4px black;
}

.nav_button_text:hover {
  color: orange;
}
</style>
