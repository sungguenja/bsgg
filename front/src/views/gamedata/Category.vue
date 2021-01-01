<template>
  <div>
    <ItemCategory v-for="(value,index) in items" :key="index+cate[value]" :itemcat="value" :name="cate[value]" :categoryType="categoryType"></ItemCategory>
  </div>
</template>

<script>
import ItemCategory from '../../components/gamedata/ItemCategory.vue'
export default {
  data() {
    return {
      categoryType: this.$route.params.category,
      cate: [0,'단검','양손검','도끼','쌍검','권총','돌격 소총','저격총','레이피어','창','망치','방망이','투척','암기','활','석궁','글러브','톤파','기타','쌍절곤','채찍','머리','옷','팔','다리','장식','음식','음료','설치','재료'],
      items: []
    }
  },
  created() {
    this.categoryType = this.$route.params.category
    if(this.categoryType == 0) {
      this.items = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    } else if (this.categoryType == 1) {this.items = [21,22,23,24,25]}
    else {this.items = [26,27,28,29]}
  },
  methods: {
  },
  components: {
    ItemCategory
  }
}
</script>

<style>

</style>