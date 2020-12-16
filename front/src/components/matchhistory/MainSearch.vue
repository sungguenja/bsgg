<template>
  <div class="container">
    <div class="row">
      <h3 class="col-4 text-light">전적 검색</h3>
      <div class="col-4" style="float:left;">
        <img :src="require('../../assets/image/assets/button-refresh-on.png')" style="cursor: pointer;"><br>
        <a class="text-light">최근 전적 갱신 :</a>
      </div>
      <div class="col-4 d-flex justify-content-between">
        <img :src="require('../../assets/image/assets/icon-solo-02.png')" style="cursor: pointer; height: 75%; margin-right:5px;" @click="ChangeMode(0)" class="mode_button">
        <img :src="require('../../assets/image/assets/icon-squad-01.png')" style="cursor: pointer; height: 75%; margin-right:5px;" @click="ChangeMode(1)" class="mode_button">
        <img :src="require('../../assets/image/assets/icon-duo-01.png')" style="cursor: pointer; height: 75%; margin-right:5px;" @click="ChangeMode(2)" class="mode_button">
      </div>
      <form class="col-12 my-2" @submit.prevent="SearchHistory">
        <input type="text" style="width: 100%; border-radius: 3% 3% 3% 3% / 50% 50% 50% 50%; background-color: rgb(206,144,60);" v-model="user_name">
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
        <table class="table table-dark">
          <thead>
            <tr>
              <th scope="col">캐릭터</th>
              <th scope="col">무기</th>
              <th scope="col">순위</th>
              <th scope="col">킬수</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(match,index) in recent_match" :key="index" @click="ShowDetail(index)">
              <th scope="row">{{match.chr_name}}</th>
              <td><img :src="match.weapon_img" style="height:40px"></td>
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
      recent_match: [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    }
  },
  methods: {
    SearchHistory() {
      this.notYet = false
      this.isLoading = true
      this.isError = false
      if(this.user_name == null) {
        alert('닉네임을 입력해주세요')
        return false
      }
      Axios({
        method: "GET",
        url: `${SERVER_URL}matchhistory/search/${this.user_name}/${this.season}/${this.team_mode}`
      })
      .then(res => {
        this.isLoading = false
        if(res.data.success == 0) {this.isError = true}
        else {
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
      var buttons = document.querySelectorAll(".mode_button")
      for(var i=0;i<buttons.length;i++) {
        if(i==n){buttons[i].src = require(`../../assets/image/assets/icon-${this.little_mode[i]}-02.png`)}
        else {buttons[i].src = require(`../../assets/image/assets/icon-${this.little_mode[i]}-01.png`)}
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

</style>