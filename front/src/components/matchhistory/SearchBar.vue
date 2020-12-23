<template>
  <div>
    <div class="d-flex justify-content-between" style="width: 752px;">
      <div class="d-flex">
        <span class="text-light search_text">전적 검색</span>
        <div class="d-flex flex-column-reverse">
          <b class="text-light recent_search" style="">최근 전적 갱신: {{search_time}}</b>
        </div>
      </div>
      <div class="d-flex justify-content-between" style="width: 289px; height: 35px;">
        <img v-for="(stat,index) in button_stat" :key="button_on[index][stat]" :src="button_on[index][stat]" alt="" style="cursor: pointer;" class="chr_window" @click="ChangeMode(index)">
      </div>
    </div>
    <form class="mt-1" @submit.prevent="SearchMatch">
      <input type="text" style="width: 80%; background-color: rgb(206,144,60); padding: 0 10px 0 10px; margin-right: 1%; height: 40px;" v-model="user_name" placeholder="아이디를 검색해보세요." class="search_bar">
      <button type="submit" class="btn" style="width: 9%; margin-right: 1%; padding: 0 0 0 0; height: 40px;"><img :src="require('../../assets/image/assets/button-search-01-on.png')" style="width: 100%; height: 100%;"></button>
      <button type="submit" class="btn" style="width: 9%; padding: 0 0 0 0; height: 40px;"><img :src="require('../../assets/image/assets/button-refresh-on.png')" style="width: 100%; height: 100%;"> </button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      user_name: null,
      mode_select: 0,
      button_on: [[require('../../assets/image/assets/button-solo-on.png'),require('../../assets/image/assets/button-solo-off.png')],
      [require('../../assets/image/assets/button-duo-on.png'),require('../../assets/image/assets/button-duo-off.png')],
      [require('../../assets/image/assets/button-squad-on.png'),require('../../assets/image/assets/button-squad-off.png')]],
      button_stat: [1,0,0]
    }
  },
  props: {
    search_time: String
  },
  methods: {
    ChangeMode(n) {
      if(n==this.mode_select) {return false}
      this.mode_select = n
      for(var i=0; i<3; i++) {
        this.ChangeModeButton(i)
      }
      if(this.user_name != null) {this.SearchMatch()}
    },
    ChangeModeButton(n) {
      if(n==this.mode_select) {this.button_stat[n] = 1}
      else {this.button_stat[n] = 0}
      this.button_stat.push(0)
      this.button_stat.pop()
    },
    SearchMatch() {
      if(this.user_name == null) {
        alert('닉네임을 입력해주세요')
        return false
      }
      this.$emit('startsearch',{'user_name':this.user_name,'mode_select':this.mode_select})
    }
  }
}
</script>

<style>
.search_text {
  width: 200px;
  height: 50px;
  font-family: 'SeoulNamsanM';
  font-size: 48px;
  font-weight: normal;
  font-stretch: normal;
  font-style: normal;
  line-height: normal;
  text-align: left;
  color: #bdbdbd;
}

.recent_search {
  height: 16px;
  font-family: 'SeoulNamsanM';
  font-size: 16px;
  font-weight: normal;
  font-stretch: normal;
  font-style: normal;
  line-height: normal;
  letter-spacing: -1.2px;
  text-align: left;
  color: #bdbdbd;
}
</style>