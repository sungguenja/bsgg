<template>
  <div class="d-flex flex-wrap">
    <div class="m-3" v-for="(animal,index) in animals" :key="index+animal[0]+index+animal[1]">
      <div class="card chr_window" style="background-color: rgb(51,51,51); width: 10rem;" @click="GoDetail(animal[1])">
        <img :src="`https://raw.githubusercontent.com/sungguenja/lumiaimg/master/동물/${animal[0]}.png`" class="card-img-top" alt="..." style="height:200px;">
        <hr>
        <div class="card-body">
          <p class="card-text text-light">{{animal[0]}}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      animals: [['닭',1],['박쥐',2],['멧돼지',3],['들개',4],['늑대',5],['곰',6],['위클라인',7]]
    }
  },
  methods: {
    GoDetail(n) {this.$router.push({name: 'AnimalDetail',params:{pk:n}})}
  }
}
</script>

<style>

</style>