<template>
  <div>
    <div style="background-color: rgb(51,51,51); width: 100%;">
      <div>
        <div class="d-flex">
          <div class="d-flex" style="margin-left: 250px;">
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
          <div class="m-5">
            <h3 class="text-light">사용 가능 무기</h3>
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
    <hr>
    <div class="" style="margin-left: 90px;">
      <div class="d-flex" style="margin-left: 150px;">
        <button @click="ChangeMode(0)" class="m-3">스킬 정보</button>
        <button @click="ChangeMode(1)" class="m-3">통계 정보</button>
        <button @click="ChangeMode(2)" class="m-3">능력치</button>
      </div>
      <div class="d-flex" style="margin-left: 150px;">
        <div class="m-3" style="width: 50%;" v-show="now_mode === 0">
          <SkillWindow v-for="(skill,i) in skills" :key="skill.fields.name+i" :pk="skill.pk" :name="skill.fields.name" :stat="JSON.parse(skill.fields.stats)" :detail="skill.fields.detail" :basic="skill.fields.is_basic" :button="skill.fields.button" :chname="stats.name"></SkillWindow>
        </div>
        <div class="" style="width: 25%;">
          <div v-show="now_mode === 1">
            <div class="d-flex">
              <button @click="ChangeState">통계 집단 바꾸기</button>
              <div v-if="view_rank==0"><b class="text-light ml-3">전체</b></div>
              <div v-if='view_rank==1'><b class="text-light ml-3">상위 랭커</b></div>
              <div v-if='view_rank==2'><b class="text-light ml-3">무기 통계</b></div>
            </div>
            <CharStatChart :all_stat="all_state" :stat="stat" :ranker="false" v-show="view_rank == 0"/>
            <CharStatChart :all_stat="all_state" :stat="stat" :ranker="true" v-show="view_rank == 1"/>
            <div v-show="view_rank == 2" v-for="(statsz, index) in weapon_state" :key="index+statsz[0].name+index+statsz[0].cate+statsz.length" >
              <button @click="ChangeWeaponStat" v-show="index == WeaponShow">{{weapons[WeaponShow].name}}</button>
              <WeaponChart :stat="statsz" v-show="index == WeaponShow"/>
            </div>
          </div>
          <div v-show="now_mode === 2">
            <div style="display: flex;">
              <div>
                <h3 class="text-light">능력치</h3>
                <table class="table table-secondary table-hover mx-3" style="width: 450px;">
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
              <div style="width: 800px;">
                <h3 class="text-light text-center" style="width: 100%;">모드별 변동</h3>
                <table class="table table-secondary table-hover" style="width: 800px;">
                  <thead>
                    <tr>
                      <th scope="col">무기</th>
                      <th scope="col">솔로 받는 데미지</th>
                      <th scope="col">솔로 주는 데미지</th>
                      <th scope="col">듀오 받는 데미지</th>
                      <th scope="col">듀오 주는 데미지</th>
                      <th scope="col">스쿼드 받는 데미지</th>
                      <th scope="col">스쿼드 주는 데미지</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="(amp,index) in ampli" :key="index+amp.weapon_type+amp.DuoDamageGive+amp.DuoDamageTaken+amp.SoloDamageGive+amp.SoloDamageTaken+amp.SquadDamageGive+amp.SquadDamageTaken">
                      <th scope="row">{{amp.weapon_type}}</th>
                      <td>{{100+amp.SoloDamageTaken}}%</td>
                      <td>{{100+amp.SoloDamageGive}}%</td>
                      <td>{{100+amp.DuoDamageTaken}}%</td>
                      <td>{{100+amp.DuoDamageGive}}%</td>
                      <td>{{100+amp.SquadDamageTaken}}%</td>
                      <td>{{100+amp.SquadDamageGive}}%</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
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
import CharStatChart from '../../components/gamedata/CharStatChart.vue'
import WeaponChart from '../../components/gamedata/WeaponChart.vue'
var SERVER_URL = ''
const check_url = window.location.hostname
if (check_url == 'localhost') {SERVER_URL = 'http://localhost:8000/'}
else if(check_url == 'lumia.kr') {SERVER_URL = 'https://lumia.kr/backapi/'}
else if(check_url == 'xn--2s2b29c91l.kr') {SERVER_URL = 'https://xn--2s2b29c91l.kr/backapi/'}
else if(check_url == '루미아.kr') {SERVER_URL = 'https://루미아.kr/backapi/'}
const IMG_URL = process.env.VUE_APP_IMG_GIT
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
      weaponthumbnail: [],
      ampli: [],
      now_mode: 0,
      all_state: {},
      ranker_state: [],
      stat: [],
      view_rank: false,
      weapon_state: [],
      WeaponShow: 0
    }
  },
  created() {
    this.pk = this.$route.params.pk
    this.SearchDetail()
  },
  methods: {
    SearchDetail() {
      Axios({
        method: "GET",
        url: `${SERVER_URL}characters/detail/${this.pk}`
      })
      .then(res => {
        this.all_state = res.data.all_state
        this.ranker_state = res.data.ranker_state
        this.stat = res.data.stat
        this.stats = res.data.character[0].fields
        this.skills = res.data.skills
        this.weapons = res.data.weapons
        this.chr_thumbnail = IMG_URL + `소형/${this.stats.name}.png`
        this.ampli = res.data.ampli
        var storage = firebase.storage().ref(`캐릭터/소형/${this.stats.name}.png`)
        for(var i=0;i<this.skills.length;i++) {
          if(this.skills[i].fields.button == 'Q') {
            this.Q.text += `${this.skills[i].fields.name}: ` + this.skills[i].fields.detail + '<br>'
            if(this.skills[i].fields.is_basic == 'basic') {
              var skillstorageQ = firebase.storage().ref(`캐릭터/스킬/${this.stats.name}/basic_Q.png`)
              skillstorageQ.getDownloadURL().then(url => {this.Q.thimbnail = url})
              .catch(() => {this.Q.thimbnail = IMG_URL + `스킬/${this.stats.name}/basic_Q.png`})
            }
          }
          if(this.skills[i].fields.button == 'W') {
            this.W.text += `${this.skills[i].fields.name}: ` + this.skills[i].fields.detail + '<br>'
            if(this.skills[i].fields.is_basic == 'basic') {
              var skillstorageW = firebase.storage().ref(`캐릭터/스킬/${this.stats.name}/basic_W.png`)
              skillstorageW.getDownloadURL().then(url => {this.W.thimbnail = url})
              .catch(() => {this.W.thimbnail = IMG_URL + `스킬/${this.stats.name}/basic_W.png`})
            }
          }
          if(this.skills[i].fields.button == 'E') {
            this.E.text += `${this.skills[i].fields.name}: ` + this.skills[i].fields.detail + '<br>'
            if(this.skills[i].fields.is_basic == 'basic') {
              var skillstorageE = firebase.storage().ref(`캐릭터/스킬/${this.stats.name}/basic_E.png`)
              skillstorageE.getDownloadURL().then(url => {this.E.thimbnail = url})
              .catch(() => {this.E.thimbnail = IMG_URL + `스킬/${this.stats.name}/basic_E.png`})
            }
          }
          if(this.skills[i].fields.button == 'R') {
            this.R.text += `${this.skills[i].fields.name}: ` + this.skills[i].fields.detail + '<br>'
            if(this.skills[i].fields.is_basic == 'basic') {
              var skillstorageR = firebase.storage().ref(`캐릭터/스킬/${this.stats.name}/basic_R.png`)
              skillstorageR.getDownloadURL().then(url => {this.R.thimbnail = url})
              .catch(() => {this.R.thimbnail = IMG_URL + `스킬/${this.stats.name}/basic_R.png`})
            }
          }
          if(this.skills[i].fields.button == '패시브') {
            this.passive.text += `${this.skills[i].fields.name}: ` + this.skills[i].fields.detail + '<br>'
            if(this.skills[i].fields.is_basic == 'basic') {
              var skillstorageT = firebase.storage().ref(`캐릭터/스킬/${this.stats.name}/basic_패시브.png`)
              skillstorageT.getDownloadURL().then(url => {this.passive.thimbnail = url})
              .catch(() => {this.passive.thimbnail = IMG_URL + `스킬/${this.stats.name}/basic_패시브.png`})
            }
          }
        }
        storage.getDownloadURL().then(url => {this.chr_thumbnail = url})
        for(var j=0; j<this.weapons.length; j++) {
          this.weapons[j].skill = this.weapons[j].skill.replace(/\\n/g, '<br>')
          this.weapons[j].skill = this.weapons[j].skill.replace(/\n/g, '<br>')
          this.weaponthumbnail.push(IMG_URL+`스킬/무기 스킬/${this.weapons[j].name}.png`)
        }
        this.weapon_state = []
        for(j=0;j<this.weapons.length;j++) {
          this.weapon_state.push([])
        }
        for(i=0;i<res.data.weapon_each_stat.length;i++) {
          for(j=0;j<this.weapons.length;j++) {
            if(res.data.weapon_each_stat[i].cate == this.weapons[j].name) {
              this.weapon_state[j].push(res.data.weapon_each_stat[i])
            }
          }
        }
        if(res.data.stat.length == 0) {
          this.weapon_state = []
        }
      })
      .catch(err => {console.log(err)})
    },
    ChangeMode(n) {
      this.now_mode = n
    },
    ChangeState() {
      this.view_rank += 1
      this.view_rank = this.view_rank%3
    },
    ChangeWeaponStat() {
      this.WeaponShow += 1
      this.WeaponShow = this.WeaponShow%this.weapon_state.length
    }
  },
  components: {
    SkillWindow,
    CharStatChart,
    WeaponChart
  },
}
</script>

<style>

</style>