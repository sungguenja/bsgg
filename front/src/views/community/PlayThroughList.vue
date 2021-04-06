<template>
  <div class="d-flex">
    <div style="width: 25%;" class="m-3 mx-5 d-flex flex-wrap">
      <CharacterWindow v-for="(character,i) in chr_list" :key="character.name+i+'playthrough'" :character_inform="character" @click="getPlayThroughList(character.pk)"></CharacterWindow>
    </div>
    <div style="width: 60%;" class="m-3">
      <table class="table text-light" style="width: 100%;">
        <thead>
          <tr>
            <th scope="col">#</th>
            <th scope="col">제목</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(playthrough,i) in playthrough_list" :key="playthrough.title + playthrough.pk + i">
            <td scope="row">{{playthrough.pk}}</td>
            <td>{{playthrough.title}}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import Axios from 'axios'
import CharacterWindow from '../../components/community/CharacterWindow.vue'
var SERVER_URL = ''
const check_url = window.location.hostname
if (check_url == 'localhost') {SERVER_URL = 'http://localhost:8000/'}
else if(check_url == 'lumia.kr') {SERVER_URL = 'https://lumia.kr/backapi/'}
else if(check_url == 'xn--2s2b29c91l.kr') {SERVER_URL = 'https://xn--2s2b29c91l.kr/backapi/'}
else if(check_url == '루미아.kr') {SERVER_URL = 'https://루미아.kr/backapi/'}
export default {
  data() {
    return {
      chr_list: [],
      playthrough_list: [],
    }
  },
  methods: {
    getCharacterList() {
      Axios({
        method: "GET",
        url: `${SERVER_URL}characters/`
      })
      .then(res => {this.chr_list = res.data})
      .catch(err => {
        console.log(err)
        alert("데이터를 가져오는 데 에러가 일어났습니다.")
      })
    },
    getPlayThroughList(id) {
      console.log(id)
      Axios({
        method: "GET",
        url: `${SERVER_URL}community/${id}`
      })
      .then(res => {
        this.playthrough_list = res.data
      })
      .catch(err => {
        console.log(err)
        alert("공략글을 가져오는 데 에러가 일어났습니다.")
      })
    }
  },
  created() {
    this.getCharacterList()
    this.getPlayThroughList(0)
  },
  components: {
    CharacterWindow
  }
}
</script>

<style>

</style>