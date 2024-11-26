<template>
  <div class="video-container" v-if="videoId">
    <iframe
      width="100%"
      height="100%"
      :src="`https://www.youtube.com/embed/${videoId}?autoplay=1`"
      frameborder="0"
      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
      allowfullscreen
    ></iframe>
  </div>
  <div v-else>
    <p>Loading video...</p>
  </div>
</template>

<script>
export default {
  name: 'TrailerPlayer',
  props: {
    videoId: {
      type: String,
      required: true,
    },
  },
};
</script>

<style scoped>
.video-container {
  width: 100%;
  max-width: 600px;
  height: 80vh;
  background-color: black;
}
</style>
