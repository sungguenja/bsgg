<template>
  <div>
    <h2 class="text-light">승률 차트</h2>
    <div class="d-flex" style="height: 450px;">
      <canvas :id="'SoloWin'+ranker"></canvas>
      <canvas :id="'DuoWin'+ranker"></canvas>
      <canvas :id="'SquadWin'+ranker"></canvas>
    </div>
    <h2 class="text-light">픽률 차트</h2>
    <div class="d-flex" style="height: 450px;">
      <canvas :id="'SoloPick'+ranker"></canvas>
      <canvas :id="'DuoPick'+ranker"></canvas>
      <canvas :id="'SquadPick'+ranker"></canvas>
    </div>
    <h2 class="text-light">평균 킬</h2>
    <div class="d-flex" style="height: 450px;">
      <canvas :id="'SoloKill'+ranker"></canvas>
      <canvas :id="'DuoKill'+ranker"></canvas>
      <canvas :id="'SquadKill'+ranker"></canvas>
    </div>
    <h2 class="text-light">평균 순위</h2>
    <div class="d-flex" style="height: 450px;">
      <canvas :id="'SoloRank'+ranker"></canvas>
      <canvas :id="'DuoRank'+ranker"></canvas>
      <canvas :id="'SquadRank'+ranker"></canvas>
    </div>
  </div>
</template>

<script>
import Chart from 'chart.js'
export default {
  data() {
    return {
      type: 'bar',
      SoloData: {
        labels: [],
        datasets: [{
          barPercentage: 0.5,
          barThickness: 50,
          maxBarThickness: 50,
          backgroundColor: ['rgba(255,255,255,1)','rgba(0,0,0,1)','rgba(255,127,0,1)','rgba(139,0,255,1)','rgba(62,180,137,1)'],
          data: []
        }]
      },
      DuoData: {
        labels: [],
        datasets: [{
          barPercentage: 0.5,
          barThickness: 50,
          maxBarThickness: 50,
          backgroundColor: ['rgba(255,255,255,1)','rgba(0,0,0,1)','rgba(255,127,0,1)','rgba(139,0,255,1)','rgba(62,180,137,1)'],
          data: []
        }]
      },
      SquadData: {
        labels: [],
        datasets: [{
          barPercentage: 0.5,
          barThickness: 50,
          maxBarThickness: 50,
          backgroundColor: ['rgba(255,255,255,1)','rgba(0,0,0,1)','rgba(255,127,0,1)','rgba(139,0,255,1)','rgba(62,180,137,1)'],
          data: []
        }]
      },
      SoloPickData: {
        labels: [],
        datasets: [{
          barPercentage: 0.5,
          barThickness: 50,
          maxBarThickness: 50,
          backgroundColor: ['rgba(255,255,255,1)','rgba(0,0,0,1)','rgba(255,127,0,1)','rgba(139,0,255,1)','rgba(62,180,137,1)'],
          data: []
        }]
      },
      DuoPickData: {
        labels: [],
        datasets: [{
          barPercentage: 0.5,
          barThickness: 50,
          maxBarThickness: 50,
          backgroundColor: ['rgba(255,255,255,1)','rgba(0,0,0,1)','rgba(255,127,0,1)','rgba(139,0,255,1)','rgba(62,180,137,1)'],
          data: []
        }]
      },
      SquadPickData: {
        labels: [],
        datasets: [{
          barPercentage: 0.5,
          barThickness: 50,
          maxBarThickness: 50,
          backgroundColor: ['rgba(255,255,255,1)','rgba(0,0,0,1)','rgba(255,127,0,1)','rgba(139,0,255,1)','rgba(62,180,137,1)'],
          data: []
        }]
      },
      SoloKillData: {
        labels: [],
        datasets: [{
          barPercentage: 0.5,
          barThickness: 50,
          maxBarThickness: 50,
          backgroundColor: ['rgba(255,255,255,1)','rgba(0,0,0,1)','rgba(255,127,0,1)','rgba(139,0,255,1)','rgba(62,180,137,1)'],
          data: []
        }]
      },
      DuoKillData: {
        labels: [],
        datasets: [{
          barPercentage: 0.5,
          barThickness: 50,
          maxBarThickness: 50,
          backgroundColor: ['rgba(255,255,255,1)','rgba(0,0,0,1)','rgba(255,127,0,1)','rgba(139,0,255,1)','rgba(62,180,137,1)'],
          data: []
        }]
      },
      SquadKillData: {
        labels: [],
        datasets: [{
          barPercentage: 0.5,
          barThickness: 50,
          maxBarThickness: 50,
          backgroundColor: ['rgba(255,255,255,1)','rgba(0,0,0,1)','rgba(255,127,0,1)','rgba(139,0,255,1)','rgba(62,180,137,1)'],
          data: []
        }]
      },
      SoloRankData: {
        labels: [],
        datasets: [{
          barPercentage: 0.5,
          barThickness: 50,
          maxBarThickness: 50,
          backgroundColor: ['rgba(255,255,255,1)','rgba(0,0,0,1)','rgba(255,127,0,1)','rgba(139,0,255,1)','rgba(62,180,137,1)'],
          data: []
        }]
      },
      DuoRankData: {
        labels: [],
        datasets: [{
          barPercentage: 0.5,
          barThickness: 50,
          maxBarThickness: 50,
          backgroundColor: ['rgba(255,255,255,1)','rgba(0,0,0,1)','rgba(255,127,0,1)','rgba(139,0,255,1)','rgba(62,180,137,1)'],
          data: []
        }]
      },
      SquadRankData: {
        labels: [],
        datasets: [{
          barPercentage: 0.5,
          barThickness: 50,
          maxBarThickness: 50,
          backgroundColor: ['rgba(255,255,255,1)','rgba(0,0,0,1)','rgba(255,127,0,1)','rgba(139,0,255,1)','rgba(62,180,137,1)'],
          data: []
        }]
      },
      options: {
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
    all_stat: Object,
    stat: Array,
    ranker: Boolean
  },
  methods: {
    createChart() {
      const SoloWinCanvas = document.getElementById('SoloWin'+this.ranker).getContext('2d')
      const SoloWinChart = new Chart(SoloWinCanvas, {
        type: this.type,
        data: this.SoloData,
        options: this.options,
      })
      const DuoWinCanvas = document.getElementById('DuoWin'+this.ranker).getContext('2d')
      const DuoWinChart = new Chart(DuoWinCanvas, {
        type: this.type,
        data: this.DuoData,
        options: this.options,
      })
      const SquadWinCanvas = document.getElementById('SquadWin'+this.ranker).getContext('2d')
      const SquadWinChart = new Chart(SquadWinCanvas, {
        type: this.type,
        data: this.SquadData,
        options: this.options,
      })
      const SoloPickCanvas = document.getElementById('SoloPick'+this.ranker).getContext('2d')
      const SoloPickChart = new Chart(SoloPickCanvas, {
        type: this.type,
        data: this.SoloPickData,
        options: this.options,
      })
      const DuoPickCanvas = document.getElementById('DuoPick'+this.ranker).getContext('2d')
      const DuoPickChart = new Chart(DuoPickCanvas, {
        type: this.type,
        data: this.DuoPickData,
        options: this.options,
      })
      const SquadPickCanvas = document.getElementById('SquadPick'+this.ranker).getContext('2d')
      const SquadPickChart = new Chart(SquadPickCanvas, {
        type: this.type,
        data: this.SquadPickData,
        options: this.options,
      })

      const SoloKillCanvas = document.getElementById('SoloKill'+this.ranker).getContext('2d')
      const SoloKillChart = new Chart(SoloKillCanvas, {
        type: this.type,
        data: this.SoloKillData,
        options: this.options,
      })
      const DuoKillCanvas = document.getElementById('DuoKill'+this.ranker).getContext('2d')
      const DuoKillChart = new Chart(DuoKillCanvas, {
        type: this.type,
        data: this.DuoKillData,
        options: this.options,
      })
      const SquadKillCanvas = document.getElementById('SquadKill'+this.ranker).getContext('2d')
      const SquadKillChart = new Chart(SquadKillCanvas, {
        type: this.type,
        data: this.SquadKillData,
        options: this.options,
      })
      const SoloRankCanvas = document.getElementById('SoloRank'+this.ranker).getContext('2d')
      const SoloRankChart = new Chart(SoloRankCanvas, {
        type: this.type,
        data: this.SoloRankData,
        options: this.options,
      })
      const DuoRankCanvas = document.getElementById('DuoRank'+this.ranker).getContext('2d')
      const DuoRankChart = new Chart(DuoRankCanvas, {
        type: this.type,
        data: this.DuoRankData,
        options: this.options,
      })
      const SquadRankCanvas = document.getElementById('SquadRank'+this.ranker).getContext('2d')
      const SquadRankChart = new Chart(SquadRankCanvas, {
        type: this.type,
        data: this.SquadRankData,
        options: this.options,
      })

      console.log(SoloWinChart,DuoWinChart,SquadWinChart,SoloPickChart,DuoPickChart,SquadPickChart,SoloKillChart,DuoKillChart,SquadKillChart,SoloRankChart,DuoRankChart,SquadRankChart)
    },
    startFunction() {
      if(this.ranker) {
        this.SoloData.labels = ['Ranker']
        this.SoloKillData.labels = ['Ranker']
        this.SoloRankData.labels = ['Ranker']
        this.SoloPickData.labels = ['Ranker']
        this.SoloData.datasets[0].data = [this.all_stat.solo_avg_win.toFixed(2)]
        this.SoloPickData.datasets[0].data = [this.all_stat.solo_avg_pick.toFixed(2)]
        this.SoloKillData.datasets[0].data = [this.all_stat.solo_avg_kill.toFixed(2)]
        this.SoloRankData.datasets[0].data = [this.all_stat.solo_avg_rank.toFixed(2)]
        this.DuoData.labels = ['Ranker']
        this.DuoKillData.labels = ['Ranker']
        this.DuoRankData.labels = ['Ranker']
        this.DuoPickData.labels = ['Ranker']
        this.DuoData.datasets[0].data = [this.all_stat.duo_avg_win.toFixed(2)]
        this.DuoPickData.datasets[0].data = [this.all_stat.duo_avg_pick.toFixed(2)]
        this.DuoKillData.datasets[0].data = [this.all_stat.duo_avg_kill.toFixed(2)]
        this.DuoRankData.datasets[0].data = [this.all_stat.duo_avg_rank.toFixed(2)]
        this.SquadData.labels = ['Ranker']
        this.SquadKillData.labels = ['Ranker']
        this.SquadRankData.labels = ['Ranker']
        this.SquadPickData.labels = ['Ranker']
        this.SquadData.datasets[0].data = [this.all_stat.squad_avg_win.toFixed(2)]
        this.SquadPickData.datasets[0].data = [this.all_stat.squad_avg_pick.toFixed(2)]
        this.SquadKillData.datasets[0].data = [this.all_stat.squad_avg_kill.toFixed(2)]
        this.SquadRankData.datasets[0].data = [this.all_stat.squad_avg_rank.toFixed(2)]
      } else {
        this.SoloData.labels = ['All']
        this.SoloKillData.labels = ['All']
        this.SoloRankData.labels = ['All']
        this.SoloPickData.labels = ['All']
        this.SoloData.datasets[0].data = [this.all_stat.solo_avg_win.toFixed(2)]
        this.SoloPickData.datasets[0].data = [this.all_stat.solo_avg_pick.toFixed(2)]
        this.SoloKillData.datasets[0].data = [this.all_stat.solo_avg_kill.toFixed(2)]
        this.SoloRankData.datasets[0].data = [this.all_stat.solo_avg_rank.toFixed(2)]
        this.DuoData.labels = ['All']
        this.DuoKillData.labels = ['All']
        this.DuoRankData.labels = ['All']
        this.DuoPickData.labels = ['All']
        this.DuoData.datasets[0].data = [this.all_stat.duo_avg_win.toFixed(2)]
        this.DuoPickData.datasets[0].data = [this.all_stat.duo_avg_pick.toFixed(2)]
        this.DuoKillData.datasets[0].data = [this.all_stat.duo_avg_kill.toFixed(2)]
        this.DuoRankData.datasets[0].data = [this.all_stat.duo_avg_rank.toFixed(2)]
        this.SquadData.labels = ['All']
        this.SquadKillData.labels = ['All']
        this.SquadRankData.labels = ['All']
        this.SquadPickData.labels = ['All']
        this.SquadData.datasets[0].data = [this.all_stat.squad_avg_win.toFixed(2)]
        this.SquadPickData.datasets[0].data = [this.all_stat.squad_avg_pick.toFixed(2)]
        this.SquadKillData.datasets[0].data = [this.all_stat.squad_avg_kill.toFixed(2)]
        this.SquadRankData.datasets[0].data = [this.all_stat.squad_avg_rank.toFixed(2)]
      }
      for(var i=0; i<this.stat.length; i++){
        if(this.stat[i].is_ranker != this.ranker) {continue}
        if(this.stat[i].mode == 'Solo') {
          this.SoloData.labels.push(`${this.stat[i].cate} ${this.stat[i].win_rate_rank}등`)
          this.SoloPickData.labels.push(`${this.stat[i].cate} ${this.stat[i].pick_rate_rank}등`)
          this.SoloKillData.labels.push(`${this.stat[i].cate} ${this.stat[i].avg_kill_rank}등`)
          this.SoloRankData.labels.push(`${this.stat[i].cate} ${this.stat[i].avg_rank_rank}등`)
          this.SoloData.datasets[0].data.push(this.stat[i].win_rate)
          this.SoloPickData.datasets[0].data.push(this.stat[i].pick_rate)
          this.SoloKillData.datasets[0].data.push(this.stat[i].avg_kill)
          this.SoloRankData.datasets[0].data.push(this.stat[i].avg_rank)
        } else if(this.stat[i].mode == 'Duo') {
          this.DuoData.labels.push(`${this.stat[i].cate} ${this.stat[i].win_rate_rank}등`)
          this.DuoPickData.labels.push(`${this.stat[i].cate} ${this.stat[i].pick_rate_rank}등`)
          this.DuoKillData.labels.push(`${this.stat[i].cate} ${this.stat[i].avg_kill_rank}등`)
          this.DuoRankData.labels.push(`${this.stat[i].cate} ${this.stat[i].avg_rank_rank}등`)
          this.DuoData.datasets[0].data.push(this.stat[i].win_rate)
          this.DuoPickData.datasets[0].data.push(this.stat[i].pick_rate)
          this.DuoKillData.datasets[0].data.push(this.stat[i].avg_kill)
          this.DuoRankData.datasets[0].data.push(this.stat[i].avg_rank)
        } else {
          this.SquadData.labels.push(`${this.stat[i].cate} ${this.stat[i].win_rate_rank}등`)
          this.SquadPickData.labels.push(`${this.stat[i].cate} ${this.stat[i].pick_rate_rank}등`)
          this.SquadKillData.labels.push(`${this.stat[i].cate} ${this.stat[i].avg_kill_rank}등`)
          this.SquadRankData.labels.push(`${this.stat[i].cate} ${this.stat[i].avg_rank_rank}등`)
          this.SquadData.datasets[0].data.push(this.stat[i].win_rate)
          this.SquadPickData.datasets[0].data.push(this.stat[i].pick_rate)
          this.SquadKillData.datasets[0].data.push(this.stat[i].avg_kill)
          this.SquadRankData.datasets[0].data.push(this.stat[i].avg_rank)
        }
      }
      this.createChart()
    }
  },
  watch: {
    stat() {
      this.startFunction()
    }
  },
}
</script>

<style>

</style>