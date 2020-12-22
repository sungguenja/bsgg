<template>
  <div class="">
    <h1 class="my-3 text-light">{{name}}</h1>
    <div class="d-flex justify-content-around">
      <div style="width:30%;" class="d-flex flex-wrap">
        <div class="" v-for="(item,index) in items" :key="item.name+pk+index+item.quantity">
          <a class="text-light" style="cursor: pointer;" @click="GoItem(item.pk)"><img :src="`https://raw.githubusercontent.com/sungguenja/lumiaimg/master/아이템/${cate[item.kinds]}/${item.name}.png`" alt=""><br>{{item.name}}:{{item.quantity}} 개</a>
        </div>
      </div>
      <div style="width: 30%;">
        <h1 class="text-light">동물 리스폰</h1>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col" class="text-light">동물</th>
              <th scope="col" class="text-light">리스폰 양</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(animal,index) in animals" :key="animal.name+pk+index+animal.respon">
              <th scope="row"><b class="text-light" @click="GoAnimalDetail(animal.pk)" style="cursor: pointer;"><img :src="`https://raw.githubusercontent.com/sungguenja/lumiaimg/master/동물/${animal.name}.png`" alt=""><br>{{animal.name}}</b></th>
              <td class="text-light">{{animal.respon}}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import Axios from 'axios'
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
      items: [],
      animals: [],
      name: null,
      cate: [0,'단검','양손검','도끼','쌍검','권총','돌격 소총','저격총','레이피어','창','망치','방망이','투척','암기','활','석궁','글러브','톤파','기타','쌍절곤','채찍','머리','옷','팔','다리','장식','음식','음료','설치','재료']
    }
  },
  created() {
    this.pk = this.$route.params.pk
    this.GetData()
  },
  methods: {
    GetData() {
      Axios({
        method: "GET",
        url: SERVER_URL + 'gamedata/area/' + this.pk
      })
      .then(res => {
        console.log(res)
        this.items = res.data.items
        this.animals = res.data.animal
        this.name = res.data.name
      })
      .catch(err => {console.log(err)})
    },
    GoItem(pk) {
      this.$router.push({name: 'ItemDetail',params:{pk:pk}})
    },
    GoAnimalDetail(pk) {
      this.$router.push({name: 'AnimalDetail',params:{'pk':pk}})
    }
  }
}
</script>

<style>

</style>