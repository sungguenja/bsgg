<template>
  <div class="container">
    <div class="row">
      <div class="col-12 d-flex justify-content-between">
        <div class="d-flex">
          <span class="text-light search_text">전적 검색</span>
          <div style="float: left;">
            <img :src="require('../../assets/image/assets/button-refresh-on.png')" style="cursor: pointer; float:left; width: 100%;" @click="SearchHistory"><br>
            <span class="text-light ml-2" style="float: left; font-size: 0.8vw;">최근 전적 갱신<br> {{search_time}}</span>
          </div>
        </div>
        <div class="d-flex justify-content-between">
          <span class="mode_text mx-3 clicked_mode" @click="ChangeMode(0)">Solo</span>
          <span class="mode_text mx-3" @click="ChangeMode(1)">Duo</span>
          <span class="mode_text mx-3" @click="ChangeMode(2)">Squad</span>
        </div>
      </div>
      <form class="col-12 my-2" @submit.prevent="SearchHistory">
        <input type="text" style="width: 90%; background-color: rgb(206,144,60); padding: 0 10px 0 10px; margin-right: 1%;" v-model="user_name" placeholder="아이디를 검색해보세요." class="search_bar">
        <img :src="require('../../assets/image/assets/button-search-01-on.png')" style="width: 9%; cursor:pointer;" @click="SearchHistory">
      </form>
      <div class="col-12">
        <div v-show="notYet" style="background-color: rgba(0,0,0,0.5); height:100%; z-index: 1; width: 94.5%; position: absolute;">
          <h1 class="mt-5">아직 전적 검색을 <br>안하셨어요!</h1>
        </div>
        <div v-show="!notYet & isLoading" style="background-color: rgba(0,0,0,0.5); height:100%; z-index: 1; width: 94.5%; position: absolute;">
          <b-spinner style="width: 3rem; height: 3rem;" label="Large Spinner" type="grow" variant="light"></b-spinner>
        </div>
        <div v-show="!notYet & isError" style="background-color: rgba(0,0,0,0.5); height:100%; z-index: 1; width: 94.5%; position: absolute;">
          <h1 class="my-5 text-light">서버가 에러를 일으켰거나 <br> 없는 닉네임입니다!</h1>
        </div>
        <table class="table table-dark" style="font-size: 0.8vw;">
          <thead>
            <tr>
              <th scope="col">캐릭터</th>
              <th scope="col">아이템</th>
              <th scope="col">순위</th>
              <th scope="col">킬수</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(match,index) in recent_match" :key="index" @click="ShowDetail(index)">
              <th scope="row">{{match.chr_name}}</th>
              <td>
                <img :src="match.weapon_img" style="height: 40px;">
                <img :src="match.cloth_img" style="height: 40px;">
                <img :src="match.head_img" style="height: 40px;">
                <img :src="match.arm_img" style="height: 40px;">
                <img :src="match.leg_img" style="height: 40px;">
                <img :src="match.accessory_img" style="height: 40px;">
              </td>
              <td>{{match.rank}}</td>
              <td>{{match.kill_cnt}}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import Axios from 'axios'
const SERVER_URL = `http://${window.location.hostname}:8000/`
export default {
  data() {
    return {
      user_name: null,
      season: 'OPEN',
      team_mode: 'Solo',
      mode: ['Solo','Duo','Trio'],
      little_mode: ['solo','squad','duo'],
      isLoading: false,
      isError: false,
      notYet: true,
      recent_match: [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      search_time: null
    }
  },
  methods: {
    SearchHistory() {
      if(this.user_name == null) {
        alert('닉네임을 입력해주세요')
        return false
      }
      this.notYet = false
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
          let today = new Date()
          this.search_time = `${today.getFullYear()}/${today.getMonth()}/${today.getDate()}/${today.getHours()}:${today.getMinutes()}:${today.getSeconds()}`
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
    ChangeMode(n) {
      this.team_mode = this.mode[n]
      var ModeButtons = document.querySelectorAll('.mode_text')
      for(var i=0;i<ModeButtons.length;i++) {
        if(i==n){ModeButtons[i].className = 'mode_text mx-3 clicked_mode'}
        else {ModeButtons[i].className = 'mode_text mx-3'}
      }
      if(this.user_name != null) {
        this.SearchHistory()
      }
    },
    ShowDetail(n) {
      if(this.recent_match[n] == 0) {return false}
      this.$emit('clickshow',this.recent_match[n])
    }
  }
}
</script>

<style>
.search_text {
  font-family: 'SeoulNamsanB';
  font-size: 35px;
  font-weight: normal;
  font-stretch: normal;
  font-style: normal;
  line-height: normal;
  letter-spacing: -3.9px;
  text-align: left;
  color: #bdbdbd;
  text-shadow: 4px 4px 4px black;
}

.mode_text {
  font-family: 'SeoulNamsanB';
  font-size: 25px;
  font-weight: normal;
  font-stretch: normal;
  font-style: normal;
  line-height: normal;
  letter-spacing: -3.9px;
  text-align: left;
  color: #bdbdbd;
  text-shadow: 4px 4px 4px black;
  cursor: pointer;
}

.mode_text:hover {
  color: orange;
}

.clicked_mode {
  color: orange;
}
</style>