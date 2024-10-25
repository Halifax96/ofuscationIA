<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <Portada msg="Welcome to Your Vue.js App"/>
  </div>
</template>

<script>
// @ is an alias to /src
import Portada from '@/components/Portada.vue'

export default {
  name: 'PortadaView',
  components: {
    Portada
  }
}
</script>

<style scoped>
  .home{
    text-align: center;
  }
</style>
