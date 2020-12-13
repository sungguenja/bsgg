<template>
  <div class="container m-2" :style="rank">
    <div class="row">
      <div class="col-2">
        <h3 class="my-3" :style="h1_rank">{{match.rank}}위</h3>
      </div>
      <div class="col-2">
        <img :src="match.chr_img" class="my-2" style="height:80px; border-radius: 70%;">
        <br>
        <a>{{match.chr_name}}</a>
      </div>
      <div class="col-4">
        <p class="mt-1">래밸:{{match.level}}</p>
        <p>킬수:{{match.kill_cnt}}</p>
        <p>사냥 수:{{match.animal_cnt}}</p>
      </div>
      <div class="col-4">
        <div class="my-3">
          <div class="d-flex">
            <div :id="'we'+pk" :class="weapon_img"><img :src="match.weapon_img" style="height:40px; width: 72.1px;"></div>
            <div :id="'cl'+pk" :class="cloth_img"><img :src="match.cloth_img" style="height:40px; width: 72.1px;"></div>
            <div :id="'he'+pk" :class="head_img"><img :src="match.head_img" style="height:40px; width: 72.1px;"></div>
            <b-tooltip :target="'we'+pk" triggers="hover" id="wet">
              <a v-html="weapon_text"></a>
            </b-tooltip>
            <b-tooltip :target="'cl'+pk" triggers="hover" id="clt">
              <a v-html="cloth_text"></a>
            </b-tooltip>
            <b-tooltip :target="'he'+pk" triggers="hover" id="het">
              <a v-html="head_text"></a>
            </b-tooltip>
          </div>
          <br>
          <div class="d-flex">
            <div :id="'ar'+pk" :class="arm_img"><img :src="match.arm_img" style="height:40px; width: 72.1px;"></div>
            <div :id="'le'+pk" :class="leg_img"><img :src="match.leg_img" style="height:40px; width: 72.1px;"></div>
            <div :id="'ac'+pk" :class="accessory_img"><img :src="match.accessory_img" style="height:40px; width: 72.1px;"></div>
            <b-tooltip :target="'ar'+pk" triggers="hover" id="art">
              <a v-html="arm_text"></a>
            </b-tooltip>
            <b-tooltip :target="'le'+pk" triggers="hover" id="let">
              <a v-html="leg_text"></a>
            </b-tooltip>
            <b-tooltip :target="'ac'+pk" triggers="hover" id="act">
              <a v-html="accessory_text"></a>
            </b-tooltip>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Axios from 'axios'
const SERVER_URL = process.env.VUE_APP_SERVER_URL
export default {
  data() {
    return {
      rank: '{border-radius: 30px; border-left: 1rem solid #ffffff;}',
      h1_rank: '{color: white;}',
      weapon_img: 'normal mx-1',
      cloth_img: 'normal mx-1',
      head_img: 'normal mx-1',
      arm_img: 'normal mx-1',
      leg_img: 'normal mx-1',
      accessory_img: 'normal mx-1',
      item_color: ['normal mx-1','advanced mx-1','rare mx-1','hero mx-1','legend mx-1'],
      weapon_text: null,
      cloth_text: null,
      head_text: null,
      arm_text: null,
      leg_text: null,
      accessory_text: null,
    }
  },
  props: {
    match: Object,
    pk: Number
  },
  mounted() {
    if(this.match.rank == 1) {
      this.rank = '{border-radius: 10%; border-left: 1rem solid #ffd700;}'
      this.h1_rank = '{color: #ffd700;}'
    } else if (this.match.rank == 2) {
      this.rank = '{border-radius: 10%; border-left: 1rem solid #7c7c7c;}'
      this.h1_rank = '{color: #7c7c7c;}'
    } else if (this.match.rank == 3) {
      this.rank = '{border-radius: 10%; border-left: 1rem solid #624637;}'
      this.h1_rank = '{color: #624637;}'
    }
    this.ChangeColor(this.match.arm,'ar')
    this.ChangeColor(this.match.cloth,'cl')
    this.ChangeColor(this.match.head,'he')
    this.ChangeColor(this.match.leg,'le')
    this.ChangeColor(this.match.weapon,'we')
    this.ChangeColor(this.match.accessory,'ac')
  },
  methods: {
    ChangeColor(name,id_name) {
      if(name == null) {return false}
      var key = 0
      var text = `${name} <br>`
      Axios({
        method: 'GET',
        url: `${SERVER_URL}gamedata/search/${name}`
      })
      .then(res => {
        if(id_name == 'ar') {
          this.arm_img=this.item_color[res.data.kind]
          for(key in res.data.stat) {
            text += `${key}: ${res.data.stat[key]} <br>`
          }
          this.arm_text = text
        }
        else if(id_name == 'we') {
          this.weapon_img=this.item_color[res.data.kind]
          for(key in res.data.stat) {
            text += `${key}: ${res.data.stat[key]} <br>`
          }
          this.weapon_text = text
        }
        else if(id_name == 'cl') {
          this.cloth_img=this.item_color[res.data.kind]
          for(key in res.data.stat) {
            text += `${key}: ${res.data.stat[key]} <br>`
          }
          this.cloth_text = text
        }
        else if(id_name == 'he') {
          this.head_img=this.item_color[res.data.kind]
          for(key in res.data.stat) {
            text += `${key}: ${res.data.stat[key]} <br>`
          }
          this.head_text = text
        }
        else if(id_name == 'le') {
          this.leg_img=this.item_color[res.data.kind]
          for(key in res.data.stat) {
            text += `${key}: ${res.data.stat[key]} <br>`
          }
          this.leg_text = text
        }
        else if(id_name == 'ac') {
          this.accessory_img=this.item_color[res.data.kind]
          for(key in res.data.stat) {
            text += `${key}: ${res.data.stat[key]} <br>`
          }
          this.accessory_text = text
        }
      })
      .catch(err => {
        console.log(err)
      })
    }
  }
}
</script>

<style>
.noraml {
  background-color: #808080;
  height: 40px;
  width: 72.12px;
}

.advanced {
  background-color: #3eb489;
  height: 40px;
  width: 72.12px;
}

.rare {
  background-color: #00498c;
  height: 40px;
  width: 72.12px;
}

.hero {
  background-color: #8b00ff;
  height: 40px;
  width: 72.12px;
}

.legend {
  background-color: #ffd700;
  height: 40px;
  width: 72.12px;
}

[data-tooltip-text]:hover {
  position: relative;
}

[data-tooltip-text]:after {
	-webkit-transition: bottom .3s ease-in-out, opacity .3s ease-in-out;
	-moz-transition: bottom .3s ease-in-out, opacity .3s ease-in-out;
	transition: bottom .3s ease-in-out, opacity .3s ease-in-out;

	background-color: rgba(0, 0, 0, 0.8);

  -webkit-box-shadow: 0px 0px 3px 1px rgba(50, 50, 50, 0.4);
	-moz-box-shadow: 0px 0px 3px 1px rgba(50, 50, 50, 0.4);
	box-shadow: 0px 0px 3px 1px rgba(50, 50, 50, 0.4);
	
  -webkit-border-radius: 5px;
	-moz-border-radius: 5px;
	border-radius: 5px;
	
  color: #FFFFFF;
	font-size: 12px;
	margin-bottom: 10px;
	padding: 7px 12px;
	position: absolute;
	width: auto;
	min-width: 50px;
	max-width: 300px;
	word-wrap: break-word;

	z-index: 9999;

	opacity: 0;
	left: -9999px;
  top: 90%;
	
	content: attr(data-tooltip-text);
}

[data-tooltip-text]:hover:after {
	top: 130%;
	left: 0;
	opacity: 1;
}
</style>