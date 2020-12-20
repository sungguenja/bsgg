<template>
  <div class="d-flex m-3" >
    <img :src="ne.url" alt="" style="width:50%; cursor: pointer;" @click="GoNews">
    <div class="d-flex mx-5">
      <h1 style="margin: auto; cursor: pointer;" class="text-light" @click="GoNews">{{ne.title}}</h1>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    ne: Object
  },
  methods: {
    GoNews() {
      window.open(this.ne.click,'_blank')
    }
  }
}
</script>

<style>

</style>