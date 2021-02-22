<template>
  <div>
    <div class="" style="width: 100%;">
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
            <img v-if="chname == '하트'" :src="`https://raw.githubusercontent.com/sungguenja/lumiaimg/master/스킬/하트/after_${button}.png`" alt="" style="height: 80px;">
            <img v-if="chname == '키아라' && button == 'E'" src="https://raw.githubusercontent.com/sungguenja/lumiaimg/master/스킬/키아라/after_E.png" alt="" style="height:80px;">
            <img v-if="chname == '키아라' && button == 'R'" src="https://raw.githubusercontent.com/sungguenja/lumiaimg/master/스킬/키아라/after_R.png" style="height:80px;">
            <img v-if="chname == '쇼이치' && button == 'Q'" src="https://raw.githubusercontent.com/sungguenja/lumiaimg/master/스킬/쇼이치/after_Q.png" alt="" style="height:80px;">
            <img v-if="chname == '루크' && button == 'Q'" src="https://raw.githubusercontent.com/sungguenja/lumiaimg/master/스킬/루크/after_Q.png" alt="" style="height:80px;">
            <br><b-button v-b-toggle="button+button" class="m-1">스킬<br>상세정보</b-button>
          </td>
          <td>
            <img :id="name+'detail'" style="width: 50%;"><br>
            <div v-if="chname == '엠마' && button == 'Q'">
              <img style="width: 50%;" src="https://raw.githubusercontent.com/sungguenja/lumiaimg/master/스킬설명/엠마/advance_Q.gif"><br>
            </div>
            <div v-if="chname == '엠마' && button == 'R'">
              <img style="width: 50%;" src="https://raw.githubusercontent.com/sungguenja/lumiaimg/master/스킬설명/엠마/hat_R.gif"><br>
              <img style="width: 50%;" src="https://raw.githubusercontent.com/sungguenja/lumiaimg/master/스킬설명/엠마/rabbit_R.gif"><br>
            </div>
            <div v-if="chname == '레녹스' && button =='패시브'">
              <img style="width: 50%;" src="https://raw.githubusercontent.com/sungguenja/lumiaimg/master/스킬설명/레녹스/basic_패시브2.gif">
            </div>
            <div v-if="chname == '루크' && button =='패시브'">
              <img style="width: 50%;" src="https://raw.githubusercontent.com/sungguenja/lumiaimg/master/스킬설명/루크/basic_패시브2.gif">
            </div>
            <div v-if="chname == '루크' && button =='Q'">
              <img style="width: 50%;" src="https://raw.githubusercontent.com/sungguenja/lumiaimg/master/스킬설명/루크/after_Q.gif">
            </div>
            <div v-if="chname == '캐시' && button =='R'">
              <img style="width: 50%;" src="https://raw.githubusercontent.com/sungguenja/lumiaimg/master/스킬설명/캐시/basic_R2.gif">
            </div>
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
const IMG_URL = process.env.VUE_APP_IMG_GIT
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
      .catch(() => {thumnailImg.src = IMG_URL+`스킬/${this.chname}/${this.basic}_${this.button}.png`})
      var detailImg = document.getElementById(`${this.name}detail`)
      storage.getDownloadURL().then(url => {detailImg.src = url})
      .catch(() => {detailImg.src = IMG_URL+`스킬설명/${this.chname}/${this.basic}_${this.button}.gif`})
    }
  }
}
</script>

<style>

</style>