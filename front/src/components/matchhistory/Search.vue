<template>
  <div>
    <form @submit.prevent="SearchMatch" class="d-flex justify-content-center">
      <input type="text" v-model="nickname" class="form-control mx-2" style="width:50%;">
      <select class="from-select mx-2" v-model="mode">
        <option disabled value="">모드 선택</option>
        <option value="Solo">솔로</option>
        <option value="Duo">듀오</option>
        <option value="Trio">스쿼드</option>
      </select>
      <button class="byn btn-secondary mx-2">검색</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      nickname: null,
      mode: '',
    }
  },
  methods: {
    SearchMatch() {
      if(this.mode == '') {
        this.mode = 'Solo'
      }
      this.$router.push({
        name: 'MatchHistory',
        params: {
          user_name:this.nickname,
          season: 'OPEN',
          team_mode: this.mode
        }
      })
    }
  }
}
</script>

<style>

</style>