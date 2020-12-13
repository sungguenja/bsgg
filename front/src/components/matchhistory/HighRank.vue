<template>
  <div class="d-flex mx-3">
    <div>
      <img :src="match.chr_img" style="height:80px; border-radius: 70%;"> <br>
      {{match.chr_name}} 
    </div>
    평균 순위: {{match.avg_win}}
    <br>
    최대 킬 수: {{match.max_kill}}
  </div>
</template>

<script>
export default {
  props: {
    match: Object
  },
  watch: {
    match() {console.log(this.match)}
  }
}
</script>

<style>

</style>