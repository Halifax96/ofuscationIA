<template>
  <div class="portada">
    <button class="boton" @click="entrada">Aquí empieza todo</button>
  </div>
</template>

<script>
export default {
  name: "PortadaVue",
  methods: {
    entrada() {
      this.$router.push("/principalia")
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .portada{
    text-align: center;
  }
</style>
