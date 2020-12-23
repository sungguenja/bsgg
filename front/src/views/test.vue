<template>
  <div>
    {{respon}}
  </div>
</template>

<script>
import Axios from 'axios'
export default {
  data() {
    return {
      respon: null
    }
  },
  created() {
    Axios({
      method: "GET",
      url: "http://localhost:8000/matchhistory/text",
    })
    .then(res => {this.respon = res})
    .catch(err => {this.respon = err})
  }
}
</script>

<style>

</style>