<template>
  <div class="container d-flex justify-content-around">
    <b-card
      title="Card Title"
      img-src="https://raw.githubusercontent.com/sungguenja/lumiaimg/master/weapon.png"
      img-alt="Image"
      img-top
      tag="article"
      style="max-width: 20rem; cursor: pointer;"
      class="mx-2 chr_window"
      @click="GoPush(0)"
    >
      <b-card-text>
        무기 정보
      </b-card-text>
    </b-card>
    <b-card
      title="Card Title"
      img-src="https://raw.githubusercontent.com/sungguenja/lumiaimg/master/cloth.png"
      img-alt="Image"
      img-top
      tag="article"
      style="max-width: 20rem; cursor: pointer;"
      class="mx-2 chr_window"
      @click="GoPush(1)"
    >
      <b-card-text>
        방어구 정보
      </b-card-text>
    </b-card>
    <b-card
      title="Card Title"
      img-src="https://raw.githubusercontent.com/sungguenja/lumiaimg/master/etc.jpg"
      img-alt="Image"
      img-top
      tag="article"
      style="max-width: 20rem; cursor: pointer;"
      class="mx-2 chr_window"
      @click="GoPush(2)"
    >
      <b-card-text>
        그 이외 아이템
      </b-card-text>
    </b-card>
  </div>
</template>

<script>
export default {
  methods: {
    GoPush(n) {
      if(n==0) {
        this.$router.push({name: 'WeaponCategory'})
        return false
      }
      this.$router.push({name: 'Category',params:{category:n}})
    }
  }
}
</script>

<style>

</style>