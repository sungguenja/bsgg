<template>
  <div class="col-12">
    <table class="table table-striped text-light" style="font-size: 16px; background-color: rgba(211,211,211,0.1);">
      <thead style="background-color: black;">
        <tr>
          <th scope="col">캐릭터</th>
          <th scope="col">아이템</th>
          <th scope="col">순위</th>
          <th scope="col">킬수</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(match,index) in recent_match" :key="index" @click="ShowDetail(index)">
          <th scope="row" style="font-size: 20px;">{{match.chr_name}}</th>
            <td>
              <img :src="match.weapon_img" style="height: 40px;">
              <img :src="match.cloth_img" style="height: 40px;">
              <img :src="match.head_img" style="height: 40px;">
              <img :src="match.arm_img" style="height: 40px;">
              <img :src="match.leg_img" style="height: 40px;">
              <img :src="match.accessory_img" style="height: 40px;">
            </td>
            <td style="font-size: 20px; background-color: #ffd700;;" v-if="match.rank==1"><b>{{match.rank}}</b></td>
            <td style="font-size: 20px; background-color: #AC58FA;" v-if="match.rank==2"><b>{{match.rank}}</b></td>
            <td style="font-size: 20px; background-color: #00498c;" v-if="match.rank==3"><b>{{match.rank}}</b></td>
            <td style="font-size: 20px; color: white;" v-if="match.rank>3"><b>{{match.rank}}</b></td>
            <td style="font-size: 20px;"><b>{{match.kill_cnt}}</b></td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  props: {
    recent_match: Object
  },
  methods: {
    ShowDetail(n) {
      if(this.recent_match[n] == 0) {return false}
      this.$emit('clickshow',this.recent_match[n])
    }
  }
}
</script>

<style>

</style>