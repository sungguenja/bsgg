<template>
  <div class="d-flex mx-3">
    <div>
      <img :src="match.chr_img" style="height:80px; border-radius: 70%;"> <br>
      {{match.chr_name}} 
    </div>
    플레이 횟수: {{match.chr_cont}}
    <br>
    탑3 횟수: {{match.chr_top3}} 회
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