<template>
  <div class="m-3">
    <div class="card chr_window" style="background-color: rgb(51,51,51); width: 17rem;" @click="GoDetail">
      <img :src="card_img" class="card-img-top" alt="..." style="height:300px;">
      <hr>
      <div class="card-body">
        <p class="card-text text-light">{{character_inform.name}}</p>
      </div>
    </div>
  </div>
</template>

<script>
import firebase from 'firebase'
const IMG_URL = process.env.VUE_APP_IMG_GIT
export default {
  data() {
    return {
      card_img: null,
    }
  },
  props: {
    character_inform: Object
  },
  mounted() {
    this.ChangeImg(this.character_inform.name)
  },
  methods: {
    ChangeImg(name) {
      var storage = firebase.storage().ref(`캐릭터/반신/${name}_full.png`)
      storage.getDownloadURL().then(url => {this.card_img = url})
      .catch(() => {this.card_img = IMG_URL + `반신/${name}.png`})
    },
    GoDetail() {
      this.$router.push({name:'CharacterDetail',params:{pk:this.character_inform.pk}})
    }
  }
}
</script>

<style>
.chr_window {
  -webkit-transform:scale(1);
  -moz-transform:scale(1);
  -ms-transform:scale(1); 
  -o-transform:scale(1);  
  transform:scale(1);
  -webkit-transition:.3s;
  -moz-transition:.3s;
  -ms-transition:.3s;
  -o-transition:.3s;
  transition:.3s;
  cursor: pointer;
}

.chr_window:hover {
  -webkit-transform:scale(1.1);
  -moz-transform:scale(1.1);
  -ms-transform:scale(1.1);   
  -o-transform:scale(1.1);
  transform:scale(1.1);
}
</style>