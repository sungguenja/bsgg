<template>
  <div class="m-2 text-light" :style="rank" v-if="isView">
    <div class="">
      <div class="d-flex justify-content-around">
        <div class="">
          <b>{{date}}</b><br>
          <img :src="match.chr_img" class="my-2" style="height:80px; border-radius: 70%;">
          <br>
          <a>{{match.chr_name}}</a>
        </div>
        <div class="">
          <h3 class="my-3" :style="h1_rank">{{match.rank}} 위</h3>
        </div>
        <div class="">
          <h3 class="mt-1">래밸:{{match.level}}</h3>
          <h3>킬수:{{match.kill_cnt}}</h3>
          <h3>사냥 수:{{match.animal_cnt}}</h3>
        </div>
      </div>
      <div class="">
        <div class="my-3 d-flex">
          <div class="d-flex" style="width:50%;">
            <div :id="'we'+pk" :class="weapon_img"><img :src="match.weapon_img" style="width: 100%; height:100%;" @click="GoDetail(0)" v-if="match.weapon_img!=null"></div>
            <div :id="'cl'+pk" :class="cloth_img"><img :src="match.cloth_img" style="width: 100%; height: 100%;" @click="GoDetail(1)" v-if="match.cloth_img!=null"></div>
            <div :id="'he'+pk" :class="head_img"><img :src="match.head_img" style="width: 100%; height: 100%;" @click="GoDetail(2)" v-if="match.head_img!=null"></div>
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
          <div class="d-flex" style="width:50%;">
            <div :id="'ar'+pk" :class="arm_img"><img :src="match.arm_img" style="width: 100%; height: 100%" @click="GoDetail(3)" v-if="match.arm_img!=null"></div>
            <div :id="'le'+pk" :class="leg_img"><img :src="match.leg_img" style="width: 100%; height: 100%" @click="GoDetail(4)" v-if="match.leg_img!=null"></div>
            <div :id="'ac'+pk" :class="accessory_img"><img :src="match.accessory_img" style="width: 100%; height: 100%" @click="GoDetail(5)" v-if="match.accessory_img!=null"></div>
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
var SERVER_URL = ''
const check_url = window.location.hostname
if (check_url == 'localhost') {SERVER_URL = 'http://localhost:8000/'}
else if(check_url == 'lumia.kr') {SERVER_URL = 'https://lumia.kr/backapi/'}
else if(check_url == 'xn--2s2b29c91l.kr') {SERVER_URL = 'https://xn--2s2b29c91l.kr/backapi/'}
else if(check_url == '루미아.kr') {SERVER_URL = 'https://루미아.kr/backapi/'}
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
      item_color: ['noraml mx-1','advanced mx-1','rare mx-1','hero mx-1','legend mx-1'],
      weapon_text: null,
      cloth_text: null,
      head_text: null,
      arm_text: null,
      leg_text: null,
      accessory_text: null,
      pk_list: [null,null,null,null,null,null],
      date: null,
      isView: false
    }
  },
  props: {
    match: Object,
    pk: String
  },
  mounted() {
    if(this.match.rank == 1) {
      this.rank = '{border-radius: 10%; border-left: 1rem solid #ffd700; background-color: rgba(211,211,211,0.1);}'
      this.h1_rank = '{color: #ffd700;}'
    } else if (this.match.rank == 2) {
      this.rank = '{border-radius: 10%; border-left: 1rem solid #7c7c7c; background-color: rgba(211,211,211,0.1);}'
      this.h1_rank = '{color: #7c7c7c;}'
    } else if (this.match.rank == 3) {
      this.rank = '{border-radius: 10%; border-left: 1rem solid #624637; background-color: rgba(211,211,211,0.1);}'
      this.h1_rank = '{color: #624637;}'
    } else {
      this.rank = '{border-radius: 10%; border-left: 1rem solid #ffffff; background-color: rgba(211,211,211,0.1);}'
      this.h1_rank = '{color: white;}'
    }
    this.date = this.match.date
    if(this.date != null) {this.isView = true}
    this.ChangeColor(this.match.arm,'ar')
    this.ChangeColor(this.match.cloth,'cl')
    this.ChangeColor(this.match.head,'he')
    this.ChangeColor(this.match.leg,'le')
    this.ChangeColor(this.match.weapon,'we')
    this.ChangeColor(this.match.accessory,'ac')
  },
  methods: {
    ChangeColor(name,id_name) {
      if(name == null) {
        if(id_name == 'ar') {
          this.arm_img = 'mx-1'
          this.arm_text = ''
          this.pk_list[3] = null
        } else if(id_name == 'we') {
          this.weapon_img = 'mx-1'
          this.weapon_text = ''
          this.pk_list[0] = null
        } else if(id_name == 'cl') {
          this.cloth_img = 'mx-1'
          this.cloth_text = ''
          this.pk_list[1] = null
        } else if(id_name == 'he') {
          this.head_img = 'mx-1'
          this.head_text = ''
          this.pk_list[2] = null
        } else if(id_name == 'ac') {
          this.accessory_img = 'mx-1'
          this.accessory_text = ''
          this.pk_list[5] = null
        } else if(id_name == 'le') {
          this.leg_img = 'mx-1'
          this.leg_text = ''
          this.pk_list[4] = null
        }
        return false
      }
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
          this.pk_list[3] = res.data.pk
        }
        else if(id_name == 'we') {
          this.weapon_img=this.item_color[res.data.kind]
          for(key in res.data.stat) {
            text += `${key}: ${res.data.stat[key]} <br>`
          }
          this.weapon_text = text
          this.pk_list[0] = res.data.pk
        }
        else if(id_name == 'cl') {
          this.cloth_img=this.item_color[res.data.kind]
          for(key in res.data.stat) {
            text += `${key}: ${res.data.stat[key]} <br>`
          }
          this.cloth_text = text
          this.pk_list[1] = res.data.pk
        }
        else if(id_name == 'he') {
          this.head_img=this.item_color[res.data.kind]
          for(key in res.data.stat) {
            text += `${key}: ${res.data.stat[key]} <br>`
          }
          this.head_text = text
          this.pk_list[2] = res.data.pk
        }
        else if(id_name == 'le') {
          this.leg_img=this.item_color[res.data.kind]
          for(key in res.data.stat) {
            text += `${key}: ${res.data.stat[key]} <br>`
          }
          this.leg_text = text
          this.pk_list[4] = res.data.pk
        }
        else if(id_name == 'ac') {
          this.accessory_img=this.item_color[res.data.kind]
          for(key in res.data.stat) {
            text += `${key}: ${res.data.stat[key]} <br>`
          }
          this.accessory_text = text
          this.pk_list[5] = res.data.pk
        }
      })
      .catch(err => {
        console.log(err)
      })
    },
    GoDetail(n) {
      if(this.pk_list[n] == null) {
        alert('없는 아이템을 클릭하셨어요')
        return false
      }
      this.$router.push({name:'ItemDetail',params:{pk:this.pk_list[n]}})
    }
  },
  watch: {
    pk() {
      this.date = this.match.date
      this.isView = true
      if(this.match.rank == 1) {
        this.rank = '{border-radius: 10%; border-left: 1rem solid #ffd700; background-color: rgba(211,211,211,0.1);}'
        this.h1_rank = '{color: #ffd700;}'
      } else if (this.match.rank == 2) {
        this.rank = '{border-radius: 10%; border-left: 1rem solid #AC58FA; background-color: rgba(211,211,211,0.1);}'
        this.h1_rank = '{color: #7c7c7c;}'
      } else if (this.match.rank == 3) {
        this.rank = '{border-radius: 10%; border-left: 1rem solid #00498c; background-color: rgba(211,211,211,0.1);}'
        this.h1_rank = '{color: #624637;}'
      } else {
        this.rank = '{border-radius: 10%; border-left: 1rem solid #808080; background-color: rgba(211,211,211,0.1);}'
        this.h1_rank = '{color: white;}'
      }
      this.ChangeColor(this.match.arm,'ar')
      this.ChangeColor(this.match.cloth,'cl')
      this.ChangeColor(this.match.head,'he')
      this.ChangeColor(this.match.leg,'le')
      this.ChangeColor(this.match.weapon,'we')
      this.ChangeColor(this.match.accessory,'ac')
    }
  }
}
</script>

<style>
.noraml {
  border: solid #808080;
  border-radius: 5px;
  width: 30%;
  cursor: pointer;
}

.advanced {
  border: solid #3eb489;
  border-radius: 5px;
  width: 30%;
  cursor: pointer;
}

.rare {
  border: solid #00498c;
  border-radius: 5px;
  width: 30%;
  cursor: pointer;
}

.hero {
  border: solid #AC58FA;
  border-radius: 5px;
  width: 30%;
  cursor: pointer;
}

.legend {
  border: solid #ffd700;
  border-radius: 5px;
  width: 30%;
  cursor: pointer;
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