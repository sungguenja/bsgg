<template>
  <div>
    <h1 class="my-2">로딩중</h1>
    <div class="pb-5">
      <b-carousel
        id="carousel-fade"
        style="text-shadow: 0px 0px 2px #000"
        fade
        indicators
        img-width="1024"
        img-height="480"
        :interval="350"
      >
        <b-carousel-slide
          caption="First slide"
          :img-src="img1"
        >
        </b-carousel-slide>
        <b-carousel-slide
          caption="Second Slide"
          :img-src="img2"
        >
        </b-carousel-slide>
        <b-carousel-slide
          caption="Third Slide"
          :img-src="img3"
        >
        </b-carousel-slide>
      </b-carousel>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      img1: '../../../../image/loading1.png',
      img2: '../../../../image/loading2.jpg',
      img3: '../../../../image/loading3.jpg'
    }
  }
}
</script>

<style>

</style>