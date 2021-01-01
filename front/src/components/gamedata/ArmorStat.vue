<template>
  <div style="height: 300px;">
    <button @click="ChangeModeButton">{{Mode[ModeButton]}} 승률</button>
    <canvas :id="'SoloWin'+cat" v-show="ModeButton == 0"></canvas>
    <canvas :id="'DuoWin'+cat" v-show="ModeButton == 1"></canvas>
    <canvas :id="'SquadWin'+cat" v-show="ModeButton == 2"></canvas>
  </div>
</template>

<script>
import Chart from 'chart.js'
export default {
  data() {
    return {
      ModeButton: 0,
      barType: 'bar',
      Mode: ['솔로','듀오','스쿼드'],
      SoloBarData: {
        labels: [],
        datasets: [{
          barPercentage: 0.5,
          barThickness: 50,
          maxBarThickness: 50,
          backgroundColor: ['rgba(255,255,255,1)','rgba(0,0,0,1)','rgba(255,127,0,1)','rgba(139,0,255,1)','rgba(62,180,137,1)','rgba(0,73,140,1)','rgba(1,168,96,1)','rgba(166,18,106,1)','rgba(180,224,75,1)','rgba(1,173,185,1)','rgba(255,0,0,1)','rgba(0,255,0,1)','rgba(0,0,255,1)','rgba(255,255,0,1)','rgba(255,0,255,1)','rgba(0,255,255,1)'],
          data: []
        }]
      },
      DuoBarData: {
        labels: [],
        datasets: [{
          barPercentage: 0.5,
          barThickness: 50,
          maxBarThickness: 50,
          backgroundColor: ['rgba(255,255,255,1)','rgba(0,0,0,1)','rgba(255,127,0,1)','rgba(139,0,255,1)','rgba(62,180,137,1)','rgba(0,73,140,1)','rgba(1,168,96,1)','rgba(166,18,106,1)','rgba(180,224,75,1)','rgba(1,173,185,1)','rgba(255,0,0,1)','rgba(0,255,0,1)','rgba(0,0,255,1)','rgba(255,255,0,1)','rgba(255,0,255,1)','rgba(0,255,255,1)'],
          data: []
        }]
      },
      SquadBarData: {
        labels: [],
        datasets: [{
          barPercentage: 0.5,
          barThickness: 50,
          maxBarThickness: 50,
          backgroundColor: ['rgba(255,255,255,1)','rgba(0,0,0,1)','rgba(255,127,0,1)','rgba(139,0,255,1)','rgba(62,180,137,1)','rgba(0,73,140,1)','rgba(1,168,96,1)','rgba(166,18,106,1)','rgba(180,224,75,1)','rgba(1,173,185,1)','rgba(255,0,0,1)','rgba(0,255,0,1)','rgba(0,0,255,1)','rgba(255,255,0,1)','rgba(255,0,255,1)','rgba(0,255,255,1)'],
          data: []
        }]
      },
      BarOptions: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          yAxes: [{
            ticks: {
              beginAtZero: true,
              stepSize: 0.2
            }
          }]
        },
        legend: {
          labels: {
            fontColor: 'black'
          }
        },
      }
    }
  },
  props: {
    stats: Array,
    cat: String
  },
  methods: {
    ChangeModeButton() {
      this.ModeButton += 1
      this.ModeButton = this.ModeButton%3
    },
    CreateChart() {
      const SoloWinCanvas = document.getElementById('SoloWin'+this.cat).getContext('2d')
      const SoloWinChart = new Chart(SoloWinCanvas, {
        type: this.barType,
        data: this.SoloBarData,
        options: this.BarOptions,
      })
      const DuoWinCanvas = document.getElementById('DuoWin'+this.cat).getContext('2d')
      const DuoWinChart = new Chart(DuoWinCanvas, {
        type: this.barType,
        data: this.DuoBarData,
        options: this.BarOptions,
      })
      const SquadWinCanvas = document.getElementById('SquadWin'+this.cat).getContext('2d')
      const SquadWinChart = new Chart(SquadWinCanvas, {
        type: this.barType,
        data: this.SquadBarData,
        options: this.BarOptions,
      })
      console.log(SoloWinChart,DuoWinChart,SquadWinChart)
    },
    MountFunction() {
      this.SoloBarData.labels = []
      this.SoloBarData.datasets[0].data = []
      this.DuoBarData.labels = []
      this.DuoBarData.datasets[0].data = []
      this.SquadBarData.labels = []
      this.SquadBarData.datasets[0].data = []
      for(var i=0; i<this.stats.length; i++) {
        this.SoloBarData.labels.push(this.stats[i].name)
        this.DuoBarData.labels.push(this.stats[i].name)
        this.SquadBarData.labels.push(this.stats[i].name)
        this.SoloBarData.datasets[0].data.push(this.stats[i].solo)
        this.DuoBarData.datasets[0].data.push(this.stats[i].duo)
        this.SquadBarData.datasets[0].data.push(this.stats[i].squad)
      }
      this.CreateChart()
    }
  },
  watch: {
    stats() {this.MountFunction()}
  }
}
</script>

<style>

</style>