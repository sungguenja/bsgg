<template>
  <div class="d-flex" style="margin-left: 50px; margin-top: 30px;">
    <div style="width: 30%;">
      <table class="table table-secondary table-hover" >
        <thead>
          <tr>
            <th scope="col"></th>
            <th scope="col">{{animal.name}}</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <th scope="row">사진</th>
            <td><img :src="`https://raw.githubusercontent.com/sungguenja/lumiaimg/master/동물/${animal.name}.png`" alt=""></td>
          </tr>
          <tr>
            <th scope="row">첫 등장 시간</th>
            <td>{{animal.first_appear}} 초</td>
          </tr>
          <tr>
            <th scope="row">리젠 시간</th>
            <td>{{animal.respon_time}} 초</td>
          </tr>
          <tr>
            <th scope="row">스킬</th>
            <td>
              <b v-for="(value,key) in animal.skill" :key="key+animal.name+value"><span>{{key}} : {{value}}</span><br> </b>
            </td>
          </tr>
        </tbody>
      </table>
      <img :src="`https://raw.githubusercontent.com/sungguenja/lumiaimg/master/동물/${animal.name}_respon.png`" alt="">
    </div>
    <div style="width: 40%;">
      <div>
        <h2 class="text-light">드랍 아이템</h2>
        <div class="d-flex flex-wrap">
          <a v-for="(item,index) in items" :key="item.name + index + item.pk + item.name" >
            <SoloItem :item="item" :kind="cate[item.kinds]"  style="height: 66px; width: 120px;" class="m-2"></SoloItem>
            <b class="text-light">{{item.name}}:{{item.percentage}}% <br>{{item.socket}}번 자리</b>
          </a>
        </div>
        <h2 class="text-light">등장 지역</h2>
        <b v-for="(value,index) in areas" :key="index+value.name+value.pk+value.respon"><span class="text-light" @click="GoMapDetail(value.pk)" style="cursor: pointer;">{{value.name}}: {{value.respon}}마리 리스폰</span><br> </b>
      </div>
      <hr>
    </div>
  </div>
</template>

<script>
import Axios from 'axios'
import SoloItem from '../../components/gamedata/SoloItem.vue'
var SERVER_URL = ''
const check_url = window.location.hostname
if (check_url == 'localhost') {SERVER_URL = 'http://localhost:8000/'}
else if(check_url == 'lumia.kr') {SERVER_URL = 'https://lumia.kr/backapi/'}
else if(check_url == 'xn--2s2b29c91l.kr') {SERVER_URL = 'https://xn--2s2b29c91l.kr/backapi/'}
else if(check_url == '루미아.kr') {SERVER_URL = 'https://루미아.kr/backapi/'}
export default {
  data() {
    return {
      pk: this.$route.params.pk,
      animal: [],
      items: [],
      areas: [],
      cate: [0,'단검','양손검','도끼','쌍검','권총','돌격 소총','저격총','레이피어','창','망치','방망이','투척','암기','활','석궁','글러브','톤파','기타','쌍절곤','채찍','머리','옷','팔','다리','장식','음식','음료','설치','재료']
    }
  },
  created() {
    this.pk = this.$route.params.pk
    this.CheckDetail()
  },
  methods: {
    CheckDetail() {
      Axios({
        method: "GET",
        url: SERVER_URL + 'gamedata/animal/' + this.pk
      })
      .then(res => {
        this.animal = res.data.animal
        this.items = res.data.items
        this.areas = res.data.areas
        this.animal.skill = JSON.parse(this.animal.skill)
        console.log(this.animal.skill)
      })
      .catch(err => {console.log(err)})
    },
    GoMapDetail(pk) {this.$router.push({name:'MapDetail',params:{pk:pk}})},
  },
  components: {
    SoloItem
  }
}
</script>

<style>

</style>