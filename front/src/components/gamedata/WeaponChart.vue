<template>
  <div class="my-2">
    <h2 class="text-light">솔로</h2>
    <div style="height: 450px;" class="d-flex">
      <canvas :id='"SoloWin"+stat[0].cate'></canvas>
      <canvas :id='"SoloPick"+stat[0].cate'></canvas>
    </div>
    <h2 class="text-light">듀오</h2>
    <div style="height: 450px;" class="d-flex">
      <canvas :id='"DuoWin"+stat[0].cate'></canvas>
      <canvas :id='"DuoPick"+stat[0].cate'></canvas>
    </div>
    <h2 class="text-light">스쿼드</h2>
    <div style="height: 450px;" class="d-flex">
      <canvas :id='"SquadWin"+stat[0].cate'></canvas>
      <canvas :id='"SquadPick"+stat[0].cate'></canvas>
    </div>
  </div>
</template>

<script>
import Chart from 'chart.js'
export default {
  data() {
    return {
      barType: 'bar',
      DoughnutType: 'doughnut',
      SoloBarData: {
        labels: [],
        datasets: [{
          barPercentage: 0.5,
          barThickness: 50,
          maxBarThickness: 50,
          backgroundColor: ['rgba(255,255,255,1)','rgba(0,0,0,1)','rgba(255,127,0,1)','rgba(139,0,255,1)','rgba(62,180,137,1)','rgba(0,73,140,1)','rgba(1,168,96,1)','rgba(166,18,106,1)','rgba(180,224,75,1)','rgba(1,173,185,1)'],
          data: []
        }]
      },
      DuoBarData: {
        labels: [],
        datasets: [{
          barPercentage: 0.5,
          barThickness: 50,
          maxBarThickness: 50,
          backgroundColor: ['rgba(255,255,255,1)','rgba(0,0,0,1)','rgba(255,127,0,1)','rgba(139,0,255,1)','rgba(62,180,137,1)','rgba(0,73,140,1)','rgba(1,168,96,1)','rgba(166,18,106,1)','rgba(180,224,75,1)','rgba(1,173,185,1)'],
          data: []
        }]
      },
      SquadBarData: {
        labels: [],
        datasets: [{
          barPercentage: 0.5,
          barThickness: 50,
          maxBarThickness: 50,
          backgroundColor: ['rgba(255,255,255,1)','rgba(0,0,0,1)','rgba(255,127,0,1)','rgba(139,0,255,1)','rgba(62,180,137,1)','rgba(0,73,140,1)','rgba(1,168,96,1)','rgba(166,18,106,1)','rgba(180,224,75,1)','rgba(1,173,185,1)'],
          data: []
        }]
      },
      SoloPieData: {
        labels: [],
        datasets: [{
          barPercentage: 0.5,
          barThickness: 50,
          maxBarThickness: 50,
          backgroundColor: ['rgba(255,255,255,1)','rgba(0,0,0,1)','rgba(255,127,0,1)','rgba(139,0,255,1)','rgba(62,180,137,1)','rgba(0,73,140,1)','rgba(1,168,96,1)','rgba(166,18,106,1)','rgba(180,224,75,1)','rgba(1,173,185,1)'],
          data: []
        }]
      },
      DuoPieData: {
        labels: [],
        datasets: [{
          barPercentage: 0.5,
          barThickness: 50,
          maxBarThickness: 50,
          backgroundColor: ['rgba(255,255,255,1)','rgba(0,0,0,1)','rgba(255,127,0,1)','rgba(139,0,255,1)','rgba(62,180,137,1)','rgba(0,73,140,1)','rgba(1,168,96,1)','rgba(166,18,106,1)','rgba(180,224,75,1)','rgba(1,173,185,1)'],
          data: []
        }]
      },
      SquadPieData: {
        labels: [],
        datasets: [{
          barPercentage: 0.5,
          barThickness: 50,
          maxBarThickness: 50,
          backgroundColor: ['rgba(255,255,255,1)','rgba(0,0,0,1)','rgba(255,127,0,1)','rgba(139,0,255,1)','rgba(62,180,137,1)','rgba(0,73,140,1)','rgba(1,168,96,1)','rgba(166,18,106,1)','rgba(180,224,75,1)','rgba(1,173,185,1)'],
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
    stat: Array
  },
  methods: {
    MakeChart() {
      const SoloWinCanvas = document.getElementById('SoloWin'+this.stat[0].cate).getContext('2d')
      const SoloWinChart = new Chart(SoloWinCanvas, {
        type: this.barType,
        data: this.SoloBarData,
        options: this.BarOptions,
      })
      const DuoWinCanvas = document.getElementById('DuoWin'+this.stat[0].cate).getContext('2d')
      const DuoWinChart = new Chart(DuoWinCanvas, {
        type: this.barType,
        data: this.DuoBarData,
        options: this.BarOptions,
      })
      const SquadWinCanvas = document.getElementById('SquadWin'+this.stat[0].cate).getContext('2d')
      const SquadWinChart = new Chart(SquadWinCanvas, {
        type: this.barType,
        data: this.SquadBarData,
        options: this.BarOptions,
      })

      const SoloPickCanvas = document.getElementById('SoloPick'+this.stat[0].cate).getContext('2d')
      const SoloPickChart = new Chart(SoloPickCanvas, {
        type: this.DoughnutType,
        data: this.SoloPieData,
        options: {},
      })
      const DuoPickCanvas = document.getElementById('DuoPick'+this.stat[0].cate).getContext('2d')
      const DuoPickChart = new Chart(DuoPickCanvas, {
        type: this.DoughnutType,
        data: this.DuoPieData,
        options: {},
      })
      const SquadPickCanvas = document.getElementById('SquadPick'+this.stat[0].cate).getContext('2d')
      const SquadPickChart = new Chart(SquadPickCanvas, {
        type: this.DoughnutType,
        data: this.SquadPieData,
        options: {},
      })
      console.log(SoloWinChart,DuoWinChart,SquadWinChart,SoloPickChart,DuoPickChart,SquadPickChart)
    },
    WatchFunction() {
      this.SoloBarData.labels = []
      this.SoloBarData.datasets[0].data = []
      this.DuoBarData.labels = []
      this.DuoBarData.datasets[0].data = []
      this.SquadBarData.labels = []
      this.SquadBarData.datasets[0].data = []
      this.SoloPieData.labels = []
      this.SoloPieData.datasets[0].data = []
      this.DuoPieData.labels = []
      this.DuoPieData.datasets[0].data = []
      this.SquadPieData.labels = []
      this.SquadPieData.datasets[0].data = []
      for(var i=0; i<this.stat.length; i++) {
        if(this.stat[i].mode == '솔로') {
          this.SoloBarData.labels.push(this.stat[i].name)
          this.SoloBarData.datasets[0].data.push(this.stat[i].win_rate)
          this.SoloPieData.labels.push(this.stat[i].name)
          this.SoloPieData.datasets[0].data.push(this.stat[i].pick_rate)
        } else if(this.stat[i].mode == '듀오') {
          this.DuoBarData.labels.push(this.stat[i].name)
          this.DuoBarData.datasets[0].data.push(this.stat[i].win_rate)
          this.DuoPieData.labels.push(this.stat[i].name)
          this.DuoPieData.datasets[0].data.push(this.stat[i].pick_rate)
        } else if(this.stat[i].mode == '스쿼드') {
          this.SquadBarData.labels.push(this.stat[i].name)
          this.SquadBarData.datasets[0].data.push(this.stat[i].win_rate)
          this.SquadPieData.labels.push(this.stat[i].name)
          this.SquadPieData.datasets[0].data.push(this.stat[i].pick_rate)
        }
      }
      this.MakeChart()
    }
  },
  watch: {
    stat() {
      this.WatchFunction()
    }
  },
  mounted() {
    this.WatchFunction()
  }
}
</script>

<style>

</style>