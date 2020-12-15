<template>
  <div>
    <div>
      <div style="background-color: rgb(51,51,51);">
      <div class="container">
        <div class="row">
          <div class="col-8 d-flex">
            <img :src="chr_thumbnail" alt="" class="m-3">
            <div>
              <h2 class="text-light mx-3 my-4 text-left">{{stats.name}}</h2>
              <div class="text-light py-3 mx-3">
                <a>
                  <img id="Q_detail" :src="Q.thimbnail" class="m-2" style="height:40px;">
                  <img id="W_detail" :src="W.thimbnail" class="m-2" style="height:40px;">
                  <img id="E_detail" :src="E.thimbnail" class="m-2" style="height:40px;">
                  <img id="R_detail" :src="R.thimbnail" class="m-2" style="height:40px;">
                  <img id="passive_detail" :src="passive.thimbnail" class="m-2" style="height:40px;">
                  <b-tooltip target="Q_detail" triggers="hover" placement="bottom" id="art">
                    <a v-html="Q.text"></a>
                  </b-tooltip>
                  <b-tooltip target="W_detail" triggers="hover" placement="bottom" id="art">
                    <a v-html="W.text"></a>
                  </b-tooltip>
                  <b-tooltip target="E_detail" triggers="hover" placement="bottom" id="art">
                    <a v-html="E.text"></a>
                  </b-tooltip>
                  <b-tooltip target="R_detail" triggers="hover" placement="bottom" id="art">
                    <a v-html="R.text"></a>
                  </b-tooltip>
                  <b-tooltip target="passive_detail" triggers="hover" placement="bottom" id="art">
                    <a v-html="passive.text"></a>
                  </b-tooltip>
                </a>
              </div>
            </div>
          </div>
          <div class="col-4 my-3">
            <h2 class="text-light">사용 가능 무기</h2>
            <a v-for="(weapon,i) in weapons" :key="i" class="m-3">
              <img :src="weaponthumbnail[i]" :id="'weapon'+i" style="height:40px;">
              <b-tooltip :target="'weapon'+i" triggers="hover" id="art">
                <a v-html="weapon.skill"></a>
              </b-tooltip>
            </a>
          </div>
        </div>
      </div>
      </div>
      <div class="container">
        <div class="row">
          <hr class="col-12">
          <div class="col-8">
            <SkillWindow v-for="(skill,i) in skills" :key="i" :pk="skill.pk" :name="skill.fields.name" :stat="JSON.parse(skill.fields.stats)" :detail="skill.fields.detail" :basic="skill.fields.is_basic" :button="skill.fields.button" :chname="stats.name"></SkillWindow>
          </div>
          <div class="col-4">
            <div>
              <h1>통계 관련은 추후 제공 ㅠㅠ</h1>
              <h1>api 생기고 구현 예정</h1>
            </div>
            <table class="table table-secondary table-hover" style="width: 100%;">
              <thead>
                <tr>
                  <th scope="col">능력치</th>
                  <th scope="col">시작값</th>
                  <th scope="col">성장값</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <th scope="row">공격력</th>
                  <td>{{stats.attack}}</td>
                  <td>{{stats.attack_growth}}</td>
                </tr>
                <tr>
                  <th scope="row">방어력</th>
                  <td>{{stats.shield}}</td>
                  <td>{{stats.shield_growth}}</td>
                </tr>
                <tr>
                  <th scope="row">체력</th>
                  <td>{{stats.health}}</td>
                  <td>{{stats.health_growth}}</td>
                </tr>
                <tr>
                  <th scope="row">체력 리젠</th>
                  <td>{{stats.health_regen}}</td>
                  <td>{{stats.health_regen_growth}}</td>
                </tr>
                <tr>
                  <th scope="row">스테미너</th>
                  <td>{{stats.stamina}}</td>
                  <td>{{stats.stamina_growth}}</td>
                </tr>
                <tr>
                  <th scope="row">스테미나 리젠</th>
                  <td>{{stats.stamina_regen}}</td>
                  <td>{{stats.stamina_regen_growth}}</td>
                </tr>
                <tr>
                  <th scope="row">공격속도</th>
                  <td>{{stats.attack_speed}}</td>
                  <td>{{stats.attack_speed_growth}}</td>
                </tr>
                <tr>
                  <th scope="row">이동속도</th>
                  <td>{{stats.moving_speed}}</td>
                  <td>{{stats.moving_speed_growth}}</td>
                </tr>
                <tr>
                  <th scope="row">크리티컬</th>
                  <td>{{stats.critical}}</td>
                  <td>{{stats.critical_growth}}</td>
                </tr>
                <tr>
                  <th scope="row">시야</th>
                  <td>{{stats.eyesight}}</td>
                  <td>{{stats.eyesight_growth}}</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Axios from 'axios'
import firebase from 'firebase'
import SkillWindow from '../../components/gamedata/SkillWindow.vue'
const SERVER_URL = process.env.VUE_APP_SERVER_URL
export default {
  data() {
    return {
      pk: this.$route.params.pk,
      stats: [],
      skills: [],
      weapons: [],
      chr_thumbnail: null,
      Q: {
        text: '',
        thimbnail: null
      },
      W: {
        text: '',
        thimbnail: null
      },
      E: {
        text: '',
        thimbnail: null
      },
      R: {
        text: '',
        thimbnail: null
      },
      passive: {
        text: '',
        thimbnail: null
      },
      weaponthumbnail: []
    }
  },
  created() {
    this.pk = this.$route.params.pk
    this.SearchDetail()
    console.log(this.skills)
  },
  methods: {
    SearchDetail() {
      Axios({
        method: "GET",
        url: `${SERVER_URL}characters/detail/${this.pk}`
      })
      .then(res => {
        this.stats = res.data.character[0].fields
        this.skills = res.data.skills
        this.weapons = res.data.weapons
        var storage = firebase.storage().ref(`캐릭터/소형/${this.stats.name}.png`)
        for(var i=0;i<this.skills.length;i++) {
          if(this.skills[i].fields.button == 'Q') {
            this.Q.text += `${this.skills[i].fields.name}: ` + this.skills[i].fields.detail + '<br>'
            if(this.skills[i].fields.is_basic == 'basic') {
              var skillstorageQ = firebase.storage().ref(`캐릭터/스킬/${this.stats.name}/basic_Q.png`)
              skillstorageQ.getDownloadURL().then(url => {this.Q.thimbnail = url})
            }
          }
          if(this.skills[i].fields.button == 'W') {
            this.W.text += `${this.skills[i].fields.name}: ` + this.skills[i].fields.detail + '<br>'
            if(this.skills[i].fields.is_basic == 'basic') {
              var skillstorageW = firebase.storage().ref(`캐릭터/스킬/${this.stats.name}/basic_W.png`)
              skillstorageW.getDownloadURL().then(url => {this.W.thimbnail = url})
            }
          }
          if(this.skills[i].fields.button == 'E') {
            this.E.text += `${this.skills[i].fields.name}: ` + this.skills[i].fields.detail + '<br>'
            if(this.skills[i].fields.is_basic == 'basic') {
              var skillstorageE = firebase.storage().ref(`캐릭터/스킬/${this.stats.name}/basic_E.png`)
              skillstorageE.getDownloadURL().then(url => {this.E.thimbnail = url})
            }
          }
          if(this.skills[i].fields.button == 'R') {
            this.R.text += `${this.skills[i].fields.name}: ` + this.skills[i].fields.detail + '<br>'
            if(this.skills[i].fields.is_basic == 'basic') {
              var skillstorageR = firebase.storage().ref(`캐릭터/스킬/${this.stats.name}/basic_R.png`)
              skillstorageR.getDownloadURL().then(url => {this.R.thimbnail = url})
            }
          }
          if(this.skills[i].fields.button == '패시브') {
            this.passive.text += `${this.skills[i].fields.name}: ` + this.skills[i].fields.detail + '<br>'
            if(this.skills[i].fields.is_basic == 'basic') {
              var skillstorageT = firebase.storage().ref(`캐릭터/스킬/${this.stats.name}/basic_패시브.png`)
              skillstorageT.getDownloadURL().then(url => {this.passive.thimbnail = url})
            }
          }
        }
        storage.getDownloadURL().then(url => {this.chr_thumbnail = url})
        var weaponStorage = null
        for(var j=0; j<this.weapons.length; j++) {
          this.weapons[j].skill = this.weapons[j].skill.replace(/\\n/g, '<br>')
          this.weapons[j].skill = this.weapons[j].skill.replace(/\n/g, '<br>')
          weaponStorage = null
          weaponStorage = firebase.storage().ref(`캐릭터/스킬/무기스킬/${this.weapons[j].name}.png`)
          weaponStorage.getDownloadURL().then(url => {
            this.weaponthumbnail.push(url)
          })
        }
      })
      .catch(err => {console.log(err)})
    }
  },
  components: {
    SkillWindow,
  }
}
</script>

<style>

</style>