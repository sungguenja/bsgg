<template>
  <div :class="now_style+' chr_window'" @click="GoPush">
    <img src="" alt="" :id="item.name+kind" style="height: 100%; margin: auto;" v-b-tooltip.hover :title="item.name">
  </div>
</template>

<script>
const IMG_URL = process.env.VUE_APP_IMG_GIT
export default {
  data() {
    return {
      now_style: ''
    }
  },
  props: {
    item: Object,
    kind: String
  },
  mounted() {
    const ImgTag = document.getElementById(this.item.name + this.kind)
    ImgTag.src = IMG_URL + `아이템/${this.kind}/${this.item.name}.png`
    if(this.item.rank == 0) {
      this.now_style = 'noraml'
    } else if (this.item.rank == 1) {this.now_style = 'advanced'}
    else if (this.item.rank == 2) {this.now_style = 'rare'}
    else if (this.item.rank == 3) {this.now_style = 'hero'}
    else {this.now_style = 'legend'}
  },
  methods: {
    GoPush() {this.$router.push({name:'ItemDetail',params:{pk:this.item.pk}})}
  }
}
</script>

<style>

</style>