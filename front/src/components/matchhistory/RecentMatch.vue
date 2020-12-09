<template>
  <div class="d-flex">
    <div style="border-right:solid; width: 10%;">
      <h3>{{match.rank}}위</h3>
    </div>
    <div class="ml-1" style="border-right:solid;">
      <img :src="match.chr_img" style="height:80px; border-radius: 70%;">
      <br>
      <a>{{match.chr_name}}</a>
    </div>
    <div style="border-right:solid; width: 10%;">
      <p>래밸:{{match.level}}</p>
      <p>킬수:{{match.kill_cnt}}</p>
      <p>사냥 수:{{match.animal_cnt}}</p>
    </div>
    <div>
      <a><img :src="match.weapon_img" style="height:40px;"></a>
      <a><img :src="match.cloth_img" style="height:40px;"></a>
      <a><img :src="match.head_img" style="height:40px;"></a>
      <br>
      <a><img :src="match.arm_img" style="height:40px;"></a>
      <a><img :src="match.leg_img" style="height:40px;"></a>
      <a><img :src="match.accessory_img" style="height:40px;"></a>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    match: Object
  }
}
</script>

<style>

</style>