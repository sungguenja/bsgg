<template>
  <div class="container">
    <h2 class="text-light">{{name}}</h2>
    <div class="row">
      <div class="col-6 row" style="word-break: normal;">
        <SoloItem v-for="(item,index) in items" :key="item.name + index" :item="item" :kind="name" class="m-2"></SoloItem>
      </div>
      <div class="col-6">
        <h2 class="text-light">클릭시 아이템 상세정보 조회</h2>
        <div v-if="1<=itemcat<=20" @click="is_tab = !is_tab">
          <b class="text-light">클릭시 설명 전환</b>
          <table class="table table-secondary table-hover" v-if="is_tab">
            <thead>
              <tr>
                <th scope="col">숙련도별</th>
                <th scope="col">기본치</th>
                <th scope="col">성장치</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <th scope="row">추가 데미지</th>
                <td>{{weapon_stat.additional_damage}}</td>
                <td>{{weapon_stat.additional_damage_growth}}</td>
              </tr>
              <tr>
                <th scope="row">스킬 증폭</th>
                <td>{{weapon_stat.amplify_skill_damage}}</td>
                <td>{{weapon_stat.amplify_skill_damage}}</td>
              </tr>
              <tr>
                <th scope="row">추가 공속</th>
                <td>{{weapon_stat.attack_speed}}</td>
                <td>{{weapon_stat.attack_speed}}</td>
              </tr>
            </tbody>
          </table>
          <table class="table table-secondary table-hover" v-if="!is_tab">
            <thead>
              <tr>
                <th scope="col">스킬 사용 예</th>
                <th scope="col">스킬 설명</th>
              </tr>
            </thead>
            <tbody>
              <th scope="row"><img :src="weapon_skill" style="width: 350px;"></th>
              <th>{{weapon_stat.skill_detail}}</th>
            </tbody>
          </table>
        </div>
      </div>
    </div>
    <hr>
  </div>
</template>

<script>
import Axios from 'axios'
import SoloItem from './SoloItem.vue'
const SERVER_URL = `http://${window.location.hostname}:8000/`
const IMG_URL = process.env.VUE_APP_IMG_GIT
export default {
  data() {
    return {
      items: [],
      weapon_stat: null,
      is_tab: true,
      weapon_skill: null
    }
  },
  props: {
    itemcat: Number,
    name: String
  },
  created() {
    this.SearchItems()
  },
  methods: {
    SearchItems() {
      Axios({
        method: "GET",
        url: SERVER_URL + 'gamedata/category/' + this.itemcat
      })
      .then(res => {
        this.items = res.data.items
      })
      .catch(err => {
        console.log(err)
      })
      if(1<=this.itemcat<=20) {
        Axios({
          method: "GET",
          url: SERVER_URL + 'characters/weapon/' + this.itemcat
        })
        .then(res => {
          this.weapon_stat = res.data[0].fields
          this.weapon_stat.skill_detail = this.weapon_stat.skill_detail.replace(/\\n/g, ' ')
          this.weapon_stat.skill_detail = this.weapon_stat.skill_detail.replace(/\n/g, ' ')
          this.weapon_skill = IMG_URL + '스킬설명/무기 스킬/' + this.name + '.gif'
        })
        .catch(err => {console.log(err)})
      }
    }
  },
  components: {
    SoloItem
  }
}
</script>

<style>

</style>