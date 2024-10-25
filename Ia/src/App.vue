<template>
  <!--nav>
    <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link>
  </nav-->
  <router-view/>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}

.boton {
  background-color: #322458;
  color: cyan;
  width: 200px;
  height: 75px;
  font-size: 18px;
  font-weight: bold;
  border-radius: 15px;
}

.urlArchivo{
  height: 54vh;
  width: 90vw;
}
</style>
