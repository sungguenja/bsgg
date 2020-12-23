<template>
  <div class="d-flex justify-content-center text-light flex-wrap">
    <b-card
      title="Card Title"
      img-src="https://raw.githubusercontent.com/sungguenja/lumiaimg/master/weapon.png"
      img-alt="Image"
      img-top
      tag="article"
      style="max-width: 20rem; cursor: pointer; background-color: rgb(51,51,51); width: 17rem;"
      
      class="m-3 chr_window col-3"
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
      style="max-width: 20rem; cursor: pointer; background-color: rgb(51,51,51); width: 17rem;"
      
      class="m-3 chr_window col-3"
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
      style="max-width: 20rem; cursor: pointer; background-color: rgb(51,51,51); width: 17rem;"
      
      class="m-3 chr_window col-3"
      @click="GoPush(2)"
    >
      <b-card-text>
        그 이외 아이템
      </b-card-text>
    </b-card>
    <b-card
      title="Card Title"
      :img-src="require('../../assets/image/game/BlankMap.png')"
      img-alt="Image"
      img-top
      tag="article"
      style="max-width: 20rem; cursor: pointer; background-color: rgb(51,51,51); width: 17rem;"
      img-height="300"
      class="m-3 chr_window col-3"
      @click="GoPush(3)"
    >
      <b-card-text>
        맵 정보
      </b-card-text>
    </b-card>
    <b-card
      title="Card Title"
      img-src="https://raw.githubusercontent.com/sungguenja/lumiaimg/master/동물/위클라인.png"
      img-alt="Image"
      img-top
      tag="article"
      style="max-width: 20rem; cursor: pointer; background-color: rgb(51,51,51); width: 17rem;"
      img-height="300"
      class="m-3 chr_window col-3"
      @click="GoPush(4)"
    >
      <b-card-text>
        야생동물 정보
      </b-card-text>
    </b-card>
    <b-card
      title="Card Title"
      img-src="https://steamcdn-a.akamaihd.net/steamcommunity/public/images/clans/34875433/ecf7b911c55b1c86de0e8dd06473c1f942775b0b.png"
      img-alt="Image"
      img-top
      tag="article"
      style="max-width: 20rem; cursor: pointer; background-color: rgb(51,51,51); width: 17rem;"
      img-height="300"
      class="m-3 chr_window col-3"
      @click="GoPush(5)"
    >
      <b-card-text>
        랭커 보기
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
      if(n==3) {
        this.$router.push({name: 'mapdata'})
        return false
      }
      if(n==4) {
        this.$router.push({name: 'AnimalList'})
        return false
      }
      if(n==5) {
        this.$router.push({name: 'Ranking'})
        return false
      }
      this.$router.push({name: 'Category',params:{category:n}})
    }
  }
}
</script>

<style>

</style>