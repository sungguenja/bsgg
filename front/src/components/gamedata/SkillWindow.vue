<template>
  <div>
    <div class="row">
    <table class="table table-secondary table-hover mb-3">
      <thead>
        <tr>
          <th scope="col" colspan="2">{{name}} - {{button}}</th>
          <th scope="col"></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th scope="row">아이콘</th>
          <th>설명</th>
        </tr>
        <tr>
          <td scope="row">
            <img style="height:80px;" :id="name"><br>
            <img v-if="chname == '하트'" :src="`https://firebasestorage.googleapis.com/v0/b/mhf-fa57c.appspot.com/o/%EC%BA%90%EB%A6%AD%ED%84%B0%2F%EC%8A%A4%ED%82%AC%2F%ED%95%98%ED%8A%B8%2Fafter_${button}.png?alt=media&token=04757cc0-7f4b-4dad-9c03-d680eff3c52e`" alt="" style="height: 80px;">
            <img v-if="chname == '키아라' && button == 'E'" src="https://firebasestorage.googleapis.com/v0/b/mhf-fa57c.appspot.com/o/%EC%BA%90%EB%A6%AD%ED%84%B0%2F%EC%8A%A4%ED%82%AC%2F%ED%82%A4%EC%95%84%EB%9D%BC%2Fafter_E.png?alt=media&token=507fec13-4c9e-4e30-868b-79b8c1261cbd" alt="" style="height:80px;">
            <img v-if="chname == '키아라' && button == 'R'" src="https://firebasestorage.googleapis.com/v0/b/mhf-fa57c.appspot.com/o/%EC%BA%90%EB%A6%AD%ED%84%B0%2F%EC%8A%A4%ED%82%AC%2F%ED%82%A4%EC%95%84%EB%9D%BC%2Fafter_R.png?alt=media&token=5ec7ab88-f6a9-4045-bea0-727e5b0186c5" style="height:80px;">
            <img v-if="chname == '쇼이치' && button == 'Q'" src="https://firebasestorage.googleapis.com/v0/b/mhf-fa57c.appspot.com/o/%EC%BA%90%EB%A6%AD%ED%84%B0%2F%EC%8A%A4%ED%82%AC%2F%EC%87%BC%EC%9D%B4%EC%B9%98%2Fafter_Q.png?alt=media&token=c73811a7-2673-48fa-887a-f32b7bd8f6b2" alt="" style="height:80px;">
            <b-button v-b-toggle="button+button" class="m-1">스킬<br>상세정보</b-button>
          </td>
          <td>
            <img :id="name+'detail'" style="width: 50%;"><br>
            <a v-html="detailText"></a>
          </td>
        </tr>
      </tbody>
    </table>
    </div>
    <b-collapse :id="button+button">
      <b-card class="bg-dark text-light mb-2">
        <div class="row">
        <div v-for="(value,key) in stat" :key="name+key" class="col-4 my-2">
          {{key}}<br>
          <b>{{value}}</b>
        </div>
        </div>
      </b-card>
    </b-collapse>
  </div>
</template>

<script>
import firebase from 'firebase'
export default {
  data() {
    return {
      detailText: null
    }
  },
  props: {
    name: String,
    pk: Number,
    stat: Object,
    detail: String,
    button: String,
    basic: String,
    chname: String
  },
  mounted() {
    this.SetThumbnail()
    this.detailText = this.detail.replaceAll('.', '<br>')
  },
  methods: {
    SetThumbnail() {
      const storage = firebase.storage().ref(`캐릭터/스킬설명/${this.chname}/${this.basic}_${this.button}.gif`)
      const tunmbnailStorage = firebase.storage().ref(`캐릭터/스킬/${this.chname}/${this.basic}_${this.button}.png`)
      var thumnailImg = document.getElementById(`${this.name}`)
      tunmbnailStorage.getDownloadURL().then(url => {thumnailImg.src = url})
      var detailImg = document.getElementById(`${this.name}detail`)
      storage.getDownloadURL().then(url => {detailImg.src = url})
    }
  }
}
</script>

<style>

</style>