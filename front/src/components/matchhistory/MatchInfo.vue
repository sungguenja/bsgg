<template>
  <div class="my-2" :style="rank">
    <div class="d-flex flex-wrap px-2">
      <b class="text-light mx-2" v-for="(value,key) in info.mastery" :key="`${info.name} ${key} ${value}`">{{key}} : {{value}} </b>
    </div>
    <h3 class="text-light">스킬 순서</h3>
    <div class="d-flex flex-wrap px-2">
      <a v-for="(value,key) in info.skill_pick" :key="info.name + key + value + 'button'" class="text-light mx-1">
        <img :src="`https://raw.githubusercontent.com/sungguenja/lumiaimg/master/스킬/${info.name}/basic_${value}.png`" alt="" style="width: 50px;" v-if="value != '무기스킬'">
        <img :src="`https://raw.githubusercontent.com/sungguenja/lumiaimg/master/소형/${info.name}.png`" alt="" style="width: 50px; height: 50px;" v-else> -> 
        <br>
        {{key}}
      </a>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      rank: ''
    }
  },
  props: {
    info: Object
  },
  methods: {
    InfoFunction() {
      console.log(this.info)
      if(this.info.rank == 1) {
        this.rank = '{border-radius: 10%; border-left: 1rem solid #ffd700; background-color: rgba(211,211,211,0.1);}'
      } else if (this.info.rank == 2) {
        this.rank = '{border-radius: 10%; border-left: 1rem solid #AC58FA; background-color: rgba(211,211,211,0.1);}'
      } else if (this.info.rank == 3) {
        this.rank = '{border-radius: 10%; border-left: 1rem solid #00498c; background-color: rgba(211,211,211,0.1);}'
      } else {
        this.rank = '{border-radius: 10%; border-left: 1rem solid #808080; background-color: rgba(211,211,211,0.1);}'
      }
    }
  },
  watch: {
    info() {this.InfoFunction()}
  }
}
</script>

<style>

</style>