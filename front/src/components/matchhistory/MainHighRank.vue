<template>
  <div v-if="character_stat != null" class="d-flex justify-content-around" style="background-color: rgba(211,211,211,0.1); width: 100%; height: 80px; margin-top: 10px; margin-bottom: 10px;">
    <img :src="`https://raw.githubusercontent.com/sungguenja/lumiaimg/master/소형/${character_stat.chr_name}.png`" alt="" style="width: 80px;">
    <span class="highrank_text">평균 순위<br>{{character_stat.avg_win}}</span>
    <span class="highrank_text">최대 킬<br>{{character_stat.max_kill}}</span>
  </div>
</template>

<script>
export default {
  props: {
    character_stat: Object
  }
}
</script>

<style>
.highrank_text {
  font-family: 'SeoulNamsanM';
  font-size: 24px;
  font-weight: normal;
  font-stretch: normal;
  font-style: normal;
  line-height: normal;
  letter-spacing: -1.5px;
  text-align: left;
  color: #bdbdbd;
  margin-top: 15px;
}
</style>