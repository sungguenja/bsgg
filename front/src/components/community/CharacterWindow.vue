<template>
  <div class="mx-auto play_window" style="margin-bottom: 8px;">
    <img :src="card_img" class="img-thumbnail" alt="...">
  </div>
</template>

<script>
import firebase from 'firebase'
const IMG_URL = process.env.VUE_APP_IMG_GIT

export default {
  data() {
    return {
      card_img: null
    }
  },
  props: {
    character_inform: Object
  },
  methods: {
    changeCardImg(name) {
      var storage = firebase.storage().ref(`캐릭터/소형/${name}_full.png`)
      storage.getDownloadURL().then(url => {this.card_img = url})
      .catch(() => {this.card_img = IMG_URL + `소형/${name}.png`})
    }
  },
  mounted() {
    this.changeCardImg(this.character_inform.name)
  }
}
</script>

<style>
.play_window {
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

.play_window:hover {
  -webkit-transform:scale(1.1);
  -moz-transform:scale(1.1);
  -ms-transform:scale(1.1);   
  -o-transform:scale(1.1);
  transform:scale(1.1);
}
</style>