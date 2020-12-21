<template>
  <div class="d-flex flex-wrap">
    <CharacterCard v-for="(character,i) in chr_list" :key="character.name+i" :character_inform="character"></CharacterCard>
  </div>
</template>

<script>
import Axios from 'axios'
import CharacterCard from '../../components/gamedata/CharacterWindow.vue'
var SERVER_URL = ''
const check_url = window.location.hostname
if (check_url == 'localhost') {SERVER_URL = 'http://localhost:8000/'}
else if(check_url == 'lumia') {SERVER_URL = 'https://lumia.kr/backapi/'}
else if(check_url == 'xn--2s2b29c91l') {SERVER_URL = 'https://xn--2s2b29c91l.kr/backapi/'}
else if(check_url == '루미아') {SERVER_URL = 'https://루미아.kr/backapi/'}
export default {
  data() {
    return {
      chr_list: []
    }
  },
  created() {
    this.AllCharacters()
  },
  methods: {
    AllCharacters() {
      Axios({
        method: "GET",
        url: `${SERVER_URL}characters/`
      })
      .then(res => {this.chr_list = res.data})
      .catch(err => {console.log(err)})
    }
  },
  components: {
    CharacterCard,
  }
}
</script>

<style>

</style>