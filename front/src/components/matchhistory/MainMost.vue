<template>
  <div class="d-flex" style="margin-top: 45px; background-color: rgba(39,37,41,0.8); width: 657px; height: 352px;" v-if="!notYet & !isError & !isLoading">
    <div style="width: 50%; margin-left: 3%;">
      <img :src="`https://raw.githubusercontent.com/sungguenja/lumiaimg/master/반신/${most_played[0].characterCode}.png`" alt="" style="width: 100%; height: 90%;">
      <span class="text-light">{{most_played[0].characterCode}} / 플레이횟수: {{most_played[0].totalGames}} / 탑3횟수: {{most_played[0].top3}}</span>
    </div>
    <div>
      <div v-for="(data,index) in search_data" :key="index+data.chr_name+index" class="d-flex" style="height: 23%; background-color: rgba(211,211,211,0.1); margin-top: 1%; margin-bottom: 1%;">
        <img :src="`https://raw.githubusercontent.com/sungguenja/lumiaimg/master/소형/${data.characterCode}.png`" alt="" style="height:100%;">
        <span class="text-light">{{data.chr_name}} / 플레이횟수: {{data.totalGames}} / 탑3횟수: {{data.top3}}</span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      search_data: []
    }
  },
  props: {
    most_played: Array,
    notYet: Boolean,
    isError: Boolean,
    isLoading: Boolean
  },
  watch: {
    most_played() {
      this.search_data = []
      for(var i=1; i<this.most_played.length; i++) {
        this.search_data.push(this.most_played[i])
      }
    }
  }
}
</script>

<style>

</style>