<template>
  <div class="" style="margin-left: 50px;">
    <div class="d-flex">
      <div class="" style="width: 30%; margin-right: 100px;">
        <Fusion :id="pk"></Fusion>
      </div>
      <div class="">
        <table class="table table-secondary table-hover">
          <tbody>
            <tr>
              <th colspan="2">{{item.item.name}}</th>
            </tr>
            <tr>
              <th colspan="2"><img :src="img_src" alt="" style="width: 50%;"></th>
            </tr>
            <tr>
              <th colspan="2" style="background-color: rgba(255,127,0,0.5)"><br></th>
            </tr>
            <tr>
              <td>종류</td>
              <td>{{cate[item.item.kinds]}}</td>
            </tr>
            <tr>
              <td>등급</td>
              <td>{{ranks[item.item.rank]}}</td>
            </tr>
            <tr>
              <td>능력치</td>
              <td>
                <b v-for="(value,key) in stats" :key="key+value">{{key}} : {{value}} <br> </b>
              </td>
            </tr>
            <tr>
              <td>드랍 장소</td>
              <td>
                <b v-for="(value,index) in item.area" :key="value.pk+value.quantity+index+value.name"><span @click="GoAreaDetail(value.pk)" style="cursor: pointer;">{{value.name}} : {{value.quantity}} 개 </span><br> </b>
              </td>
            </tr>
            <tr>
              <td>드랍 동물</td>
              <td>
                <b v-for="(value,index) in item.animal" :key="value.pk+index+value.name"><span @click="GoAnimalDetail(value.pk)" style="cursor: pointer;"><img :src="`https://raw.githubusercontent.com/sungguenja/lumiaimg/master/동물/${value.name}.png`" alt="" style="height: 40px"><br>{{value.name}}</span><br></b>
              </td>
            </tr>
          </tbody>
        </table>
        <button class="btn btn-dark" @click="GoBack">아이템 목록으로</button>
      </div>
    </div>
    <div class="">
      <b class="text-light" style="float: left;">상위템</b>
      <div class="d-flex" style="float: left;">
        <SoloItem v-for="(item,index) in item.upper" :key="item.name + index" :item="item" :kind="cate[item.kinds]" class="m-2" style="float: left; height: 66px; width: 120px;"></SoloItem>
      </div>
    </div>
  </div>
</template>

<script>
import Axios from 'axios'
import SoloItem from '../../components/gamedata/SoloItem.vue'
import Fusion from '../../components/gamedata/FusionItem.vue'
var SERVER_URL = ''
const check_url = window.location.hostname
if (check_url == 'localhost') {SERVER_URL = 'http://localhost:8000/'}
else if(check_url == 'lumia.kr') {SERVER_URL = 'https://lumia.kr/backapi/'}
else if(check_url == 'xn--2s2b29c91l.kr') {SERVER_URL = 'https://xn--2s2b29c91l.kr/backapi/'}
else if(check_url == '루미아.kr') {SERVER_URL = 'https://루미아.kr/backapi/'}
const IMG_URL = process.env.VUE_APP_IMG_GIT
export default {
  data() {
    return {
      pk: this.$route.params.pk,
      item: null,
      cate: [0,'단검','양손검','도끼','쌍검','권총','돌격 소총','저격총','레이피어','창','망치','방망이','투척','암기','활','석궁','글러브','톤파','기타','쌍절곤','채찍','머리','옷','팔','다리','장식','음식','음료','설치','재료'],
      ranks: ['일반','고급','희귀','영웅','전설'],
      img_src: null,
      stats: null,
    }
  },
  created() {
    this.SearchDetail()
  },
  components: {
    SoloItem,
    Fusion
  },
  methods: {
    SearchDetail() {
      this.pk = this.$route.params.pk
      Axios({
        method: "GET",
        url: SERVER_URL + 'gamedata/detail/' + this.pk
      })
      .then(res => {
        this.item = res.data
        this.img_src = IMG_URL + `아이템/${this.cate[this.item.item.kinds]}/${this.item.item.name}.png`
        this.stats = JSON.parse(this.item.item.stats)
      })
      .catch(err => {console.log(err)})
    },
    GoBack() {
      if(this.item.item.kinds<=20) {
        this.$router.push({name: 'WeaponCategory'})
      }
      else if(this.item.item.kinds<=25) {
        this.$router.push({name: 'Category',params:{'category':1}})
      } else {this.$router.push({name: 'Category',params:{'category':2}})}
    },
    GoAreaDetail(pk) {
      this.$router.push({name: 'MapDetail',params:{'pk':pk}})
    },
    GoAnimalDetail(pk) {
      this.$router.push({name: 'AnimalDetail',params:{'pk':pk}})
    }
  },
  watch: {
    $route(to,from) {
      this.pk = from.params.pk
      this.pk = to.params.pk
      this.SearchDetail()
    }
  }
}
</script>

<style>

</style>