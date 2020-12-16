<template>
  <div id="app" :style="`background-image: url( ${backgroundImg}); min-height:`+user_height+'px; background-repeat: repeat-y;'">
    <div class="d-flex">
    <div style="width: 10%; height:62px; cursor: pointer;" @click="GoPush(2)">
      <img :src="require('./assets/image/assets/menu-image-home.png')" style="width:100%; height:100%; z-index:1;" alt="">
      <div class="inner-shadow">
        <img :src="require('./assets/image/assets/button-home.png')" 
        :srcset="require('./assets/image/assets/button-home@2x.png')+' 2x,'+require('./assets/image/assets/button-home@3x.png')+' 3x'"
        class="button_home">
      </div>
    </div>
    <div style="width: 90%; height: 62px;">
      <img :src="require('./assets/image/assets/menu-top.png')" style="height:75%; width:100%; transform:scaleY(-1); z-index:1; position: relative; top:0; left:0;" alt="">
      <div style="z-index:2; position: absolute; top:10px; left:20%;">
        <img id="search_button" :src="require('./assets/image/assets/button-pvp-log-off.png')" alt="" :onmouseover="`this.src='${require('./assets/image/assets/button-pvp-log-on.png')}'`" :onmouseout="`this.src='${require('./assets/image/assets/button-pvp-log-off.png')}'`" class="nav_button" @click="GoPush(0)">
        <img id="search_button" :src="require('./assets/image/assets/button-cha-info-off.png')" alt="" :onmouseover="`this.src='${require('./assets/image/assets/button-cha-info-on.png')}'`" :onmouseout="`this.src='${require('./assets/image/assets/button-cha-info-off.png')}'`" class="nav_button" @click="GoPush(1)">
        <img id="search_button" :src="require('./assets/image/assets/button-walkthrough-off.png')" alt="" :onmouseover="`this.src='${require('./assets/image/assets/button-walkthrough-on.png')}'`" :onmouseout="`this.src='${require('./assets/image/assets/button-walkthrough-off.png')}'`" class="nav_button" @click="GoPush(3)">
        <img id="search_button" :src="require('./assets/image/assets/button-contact-off.png')" alt="" :onmouseover="`this.src='${require('./assets/image/assets/button-contact-on.png')}'`" :onmouseout="`this.src='${require('./assets/image/assets/button-contact-off.png')}'`" class="nav_button" @click="GoPush(3)">
      </div>
    </div>
    </div>
    <router-view class="py-2"/>
  </div>
</template>

<script>
export default {
  data() {
    return {
      nickname: null,
      mode: '',
      backgroundImg: require('./assets/image/assets/bg.jpg'),
      can_go: ['SearchHistory','CharacterList','Home','NotFoundPage'],
      user_height: screen.height
    }
  },
  methods: {
    SearchMatch() {
      if(this.mode == '') {
        this.mode = 'Solo'
      }
      this.$router.push({
        name: 'MatchHistory',
        params: {
          user_name:this.nickname,
          season: 'OPEN',
          team_mode: this.mode
        }
      })
    },
    GoPush(n) {
      this.$router.push({name: this.can_go[n]})
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
</style>
