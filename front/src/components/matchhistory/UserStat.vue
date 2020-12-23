<template>
  <div style="margin-top: 45px; background-color: rgba(39,37,41,0.8); min-width: 657px; min-height: 130px;">
    <div v-if="notYet">
      <h1 class="text-light" style="margin-top: 30px;">전적 검색을 이용해 보세요!</h1>
    </div>
    <div v-if="!notYet & isLoading">
      <b-spinner style="width: 3rem; height: 3rem;" label="Large Spinner" type="grow" variant="light"></b-spinner>
    </div>
    <div v-if="!notYet & !isLoading & isError">
      <h1 class="text-light mt-3">서버에서 에러가 났거나 없는 닉네임입니다</h1>
    </div>
    <div v-if="!notYet & !isLoading & !isError">
      <span class="main_name">{{stat.name}}</span>
      <div class="d-flex justify-content-between">
        <div class="d-flex" style="margin-left: 16px; margin-right: 16px;">
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" class="bi bi-trophy-fill text-light mr-2" viewBox="0 0 16 16">
            <path fill-rule="evenodd" d="M2.5.5A.5.5 0 0 1 3 0h10a.5.5 0 0 1 .5.5c0 .538-.012 1.05-.034 1.536a3 3 0 1 1-1.133 5.89c-.79 1.865-1.878 2.777-2.833 3.011v2.173l1.425.356c.194.048.377.135.537.255L13.3 15.1a.5.5 0 0 1-.3.9H3a.5.5 0 0 1-.3-.9l1.838-1.379c.16-.12.343-.207.537-.255L6.5 13.11v-2.173c-.955-.234-2.043-1.146-2.833-3.012a3 3 0 1 1-1.132-5.89A33.076 33.076 0 0 1 2.5.5zm.099 2.54a2 2 0 0 0 .72 3.935c-.333-1.05-.588-2.346-.72-3.935zm10.083 3.935a2 2 0 0 0 .72-3.935c-.133 1.59-.388 2.885-.72 3.935z"/>
          </svg>
          <div>
            <span class="inner_stat_text">최종우승횟수</span><br>
            <span class="inner_stat_number">{{stat.win_cnt}}</span>
          </div>
        </div>
        <div class="d-flex" style="margin-left: 16px; margin-right: 16px;">
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" class="bi bi-bar-chart-line-fill text-light mr-2" viewBox="0 0 16 16">
            <path fill-rule="evenodd" d="M11 2a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v12h.5a.5.5 0 0 1 0 1H.5a.5.5 0 0 1 0-1H1v-3a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v3h1V7a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v7h1V2z"/>
          </svg>
          <div>
            <span class="inner_stat_text">평균 순위</span><br>
            <span class="inner_stat_number">{{stat.avg_win}}</span>
          </div>
        </div>
        <div class="d-flex" style="margin-left: 16px; margin-right: 16px;">
          <span style="font-size:24px">&#128128;</span>
          <div>
            <span class="inner_stat_text">평균 킬</span><br>
            <span class="inner_stat_number">{{stat.avg_kill}}</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    stat: Object,
    notYet: Boolean,
    isError: Boolean,
    isLoading: Boolean
  }
}
</script>

<style>
.main_name {
  font-family: 'SeoulNamsanM';
  font-size: 40px;
  font-weight: normal;
  font-stretch: normal;
  font-style: normal;
  line-height: normal;
  letter-spacing: -3px;
  text-align: left;
  color: #bdbdbd;
}

.inner_stat_text {
  font-family: 'SeoulNamsanM';
  font-size: 16px;
  font-weight: normal;
  font-stretch: normal;
  font-style: normal;
  line-height: normal;
  letter-spacing: normal;
  text-align: left;
  color: #bdbdbd;
}

.inner_stat_number {
  font-family: 'SeoulNamsanM';
  font-size: 24px;
  font-weight: normal;
  font-stretch: normal;
  font-style: normal;
  line-height: normal;
  letter-spacing: normal;
  text-align: left;
  color: #bdbdbd;
}
</style>