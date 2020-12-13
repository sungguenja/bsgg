<template>
  <div id="app" style="background-color: #808080;">
    <b-navbar toggleable="lg" type="dark" variant="dark">
      <b-navbar-brand href="#">NavBar</b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item href="#">Link</b-nav-item>
          <b-nav-item href="#" disabled>Disabled</b-nav-item>
        </b-navbar-nav>

        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">
          <b-nav-form @submit.prevent="">
            <b-form-input size="sm" class="mr-sm-2" placeholder="검색할 닉네임" v-model="nickname"></b-form-input>
            <b-button size="sm" class="my-2 my-sm-0" type="submit" variant="light">전적 검색</b-button>
          </b-nav-form>
          <!-- 다중 언어 구현하게 되면
          <b-nav-item-dropdown text="Lang" right>
            <b-dropdown-item href="#">EN</b-dropdown-item>
            <b-dropdown-item href="#">ES</b-dropdown-item>
            <b-dropdown-item href="#">RU</b-dropdown-item>
            <b-dropdown-item href="#">FA</b-dropdown-item>
          </b-nav-item-dropdown> -->

          <!-- 회원으로 뭔갈 할 생각이 생기면
          <b-nav-item-dropdown right> -->
            <!-- Using 'button-content' slot  요건 주석 둬야함-->
            <!-- <template #button-content>
              <em>User</em>
            </template>
            <b-dropdown-item href="#">Profile</b-dropdown-item>
            <b-dropdown-item href="#">Sign Out</b-dropdown-item>
          </b-nav-item-dropdown> -->
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
    <router-view/>
  </div>
</template>

<script>
export default {
  data() {
    return {
      nickname: null,
      mode: ''
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
    },
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
