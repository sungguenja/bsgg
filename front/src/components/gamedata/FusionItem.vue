<template>
  <div class="m-2">
    <img :src="img_src" alt="" style="width: 80px;" :class="now_style+' chr_window'" @click="GoPush" v-b-tooltip.hover :title="item.name">
    <div v-if="left!=null | right!=null">
      <div class="d-flex justify-content-center">
        <div v-if="left != null">
          <Fusion :id="left" :key="left"></Fusion>
        </div>
        <hr style="width: 15%;">
        <div v-if="right != null">
          <Fusion :id="right" :key="right"></Fusion>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Axios from 'axios'
const SERVER_URL = `http://${window.location.hostname}:8000/`
const IMG_URL = process.env.VUE_APP_IMG_GIT
export default {
  name: 'Fusion',
  data() {
    return {
      item: [],
      left: null,
      right: null,
      cate: [0,'단검','양손검','도끼','쌍검','권총','돌격 소총','저격총','레이피어','창','망치','방망이','투척','암기','활','석궁','글러브','톤파','기타','쌍절곤','채찍','머리','옷','팔','다리','장식','음식','음료','설치','재료'],
      img_src: null,
      now_style: null
    }
  },
  props: {
    id: Number
  },
  components: {
    'Fusion': this,
  },
  mounted() {
    console.log(IMG_URL)
    this.Detail()
  },
  methods: {
    GoPush() {this.$router.replace({name:'ItemDetail',params:{pk:this.id}})},
    Detail() {
      Axios({
        method: "GET",
        url: SERVER_URL + 'gamedata/only/' + this.id
      })
      .then(res => {
        this.item = res.data[0].fields
        if(this.item.material_left != 0){this.left = this.item.material_left}
        else {this.left = null}
        if(this.item.material_right != 0){this.right = this.item.material_right}
        else {this.right = null}
        this.img_src = IMG_URL+`아이템/${this.cate[this.item.kinds]}/${this.item.name}.png`
        if(this.item.rank == 0) {
          this.now_style = 'noraml'
        } else if (this.item.rank == 1) {this.now_style = 'advanced'}
        else if (this.item.rank == 2) {this.now_style = 'rare'}
        else if (this.item.rank == 3) {this.now_style = 'hero'}
        else {this.now_style = 'legend'}
      })
    }
  },
  watch: {
    id() {
      this.Detail()
    }
  }
}
</script>

<style>

</style>