<template>
  <div>
    <WeaponItemCategory v-for="(value,index) in items" :key="index+cate[value]" :itemcat="value" :name="cate[value]"></WeaponItemCategory>
  </div>
</template>

<script>
import WeaponItemCategory from '../../components/gamedata/WeaponItemCategory.vue'
export default {
  data() {
    return {
      cate: [0,'단검','양손검','도끼','쌍검','권총','돌격 소총','저격총','레이피어','창','망치','방망이','투척','암기','활','석궁','글러브','톤파','기타','쌍절곤','채찍','머리','옷','팔','다리','장식','음식','음료','설치','재료'],
      items: []
    }
  },
  created() {
    this.items = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
  },
  methods: {
  },
  components: {
    WeaponItemCategory
  }
}
</script>

<style>

</style>