<template>
  <div class="container">
    <div class="row">
      <CharacterCard v-for="(character,i) in chr_list" :key="i" :character_inform="character"></CharacterCard>
    </div>
  </div>
</template>

<script>
import Axios from 'axios'
import CharacterCard from '../../components/gamedata/CharacterWindow.vue'
const SERVER_URL = process.env.VUE_APP_SERVER_URL
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