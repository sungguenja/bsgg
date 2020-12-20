<template>
  <div style="">
    <img :src="require('../../assets/image/game/BlankMap.png')" alt="BlackMap" usemap="#BlackMap">
    <map name="BlackMap" id="BlackMap">
      <area shape="poly" coords="189,118,261,45,278,61,293,47,317,70,327,61,380,115,380,137,366,151,331,121,259,188" @click="ClickMap(0)" style="cursor: pointer;">
      <area shape="poly" coords="379,137,366,151,395,180,382,193,413,223,421,215,464,255,504,215,490,189,436,137" @click="ClickMap(1)" style="cursor: pointer;">
      <area shape="poly" coords="330,120,394,181,383,194,398,209,364,241,358,236,308,288,275,252,257,272,240,256,282,213,259,189" @click="ClickMap(2)" style="cursor: pointer;">
      <area shape="poly" coords="398,210,412,224,422,216,472,265,426,311,432,317,387,362,327,312,331,307,310,288,357,235,365,240" @click="ClickMap(3)" style="cursor: pointer;">
      <area shape="poly" coords="473,265,513,329,447,394,441,387,431,395,392,358" @click="ClickMap(4)" style="cursor: pointer;">
      <area shape="poly" coords="189,118,219,150,191,179,201,192,159,234,119,204,120,176,155,135" @click="ClickMap(5)" style="cursor: pointer;">
      <area shape="poly" coords="219,151,282,212,211,284,160,234,202,191,191,179" @click="ClickMap(6)" style="cursor: pointer;">
      <area shape="poly" coords="327,312,387,362,392,359,430,396,382,443,346,405,336,414,279,359" @click="ClickMap(7)" style="cursor: pointer;">
      <area shape="poly" coords="441,389,503,455,466,493,406,523,376,501,351,477" @click="ClickMap(8)" style="cursor: pointer;">
      <area shape="poly" coords="119,204,136,222,209,285,150,343,122,324,115,330,62,264" @click="ClickMap(9)" style="cursor: pointer;">
      <area shape="poly" coords="240,257,257,273,219,307,293,374,246,422,158,336" @click="ClickMap(10)" style="cursor: pointer;">
      <area shape="poly" coords="295,376,383,442,330,496,271,437,246,422" @click="ClickMap(11)" style="cursor: pointer;">
      <area shape="poly" coords="90,307,115,330,150,344,158,338,194,371,140,423,45,344" @click="ClickMap(12)" style="cursor: pointer;">
      <area shape="poly" coords="194,372,249,428,280,445,186,530,111,448" @click="ClickMap(13)" style="cursor: pointer;">
      <area shape="poly" coords="280,447,331,496,351,477,441,567,147,568,222,506" @click="ClickMap(14)" style="cursor: pointer;">
      <area shape="poly" coords="276,251,330,306,276,363,219,306" @click="ClickMap(15)" style="cursor: pointer;">
    </map>
  </div>
</template>

<script>
export default {
  data() {
    return {
      DataList: [['골목길',1],['절',2],['번화가',3],['연못',4],['병원',5],['양궁장',6],['학교',7],['묘지',8],['공장',9],['호텔',10],['숲',11],['성당',12],['모래사장',13],['고급 주택가',14],['항구',15],['연구소',16]]
    }
  },
  methods: {
    ClickMap(n) {
      this.$emit('clickdetail',this.DataList[n])
    }
  }
}
</script>

<style>

</style>