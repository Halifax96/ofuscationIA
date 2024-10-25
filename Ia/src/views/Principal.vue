<template>
  <div class="principal">
    <div class="menu">
      <div class="h4" @click="mostrar(1)">
        <h4 >Insertar texto</h4>
      </div>
      <div class="h4" @click="mostrar(2)">
        <h4 >Cargar desde archivo</h4>
      </div>
      <div class="h4" @click="mostrar(3)">
        <h4>Analizar URL</h4>
      </div>
      <div class="vboton">
        <v-btn class="vbtn" @click="analizar">Analizar</v-btn>
      </div>
      <div class="pie">
        <h5>Todos los derechos reservados</h5>
        <h5>®Esteban Salazar Peña</h5>
      </div>
    </div>
    <div>
      <Texto v-show="ver == 1" ref="txt" @envia="tratar"></Texto>
    </div>
    <div>
      <Archivo v-show="ver == 2" ref="arc" @envia="tratar"></Archivo>
    </div>
    <div>
      <Url v-show="ver == 3" ref="url" @envia="tratar"></Url>
    </div>
    <div>
      <Estadisticas v-show="ver == 4" :texto="this.original" :resultados="this.resultado" :ofuscacion="porcentajes" :ver="hayOfuscacion"></Estadisticas>
    </div>
  </div>
  
</template>

<script>
import Texto from "@/components/Cuadro.vue";
import Archivo from "@/components/Archivo.vue";
import Url from "@/components/Url.vue"
import Estadisticas from "@/components/Estadisticas.vue";
import VBtn from "vuetify/lib";
import axios from "axios";
export default {
  name: "PrinCipal",
  components: {
    Texto,
    Archivo,
    Url,
    Estadisticas,
    VBtn
  },
  data: ()=>{
    return{
    ver: 0,
    original: "",
    resultado: {},
    porcentajes: "",
    hayOfuscacion: -1,
    }
  },
  methods:{
    mostrar(codigo){
      this.ver = codigo;
    },
    analizar(){
      var txt = "";
      switch(this.ver){
        case 1: this.$refs.txt.getText(txt); break;
        case 2: this.$refs.arc.getText(txt); break;
        case 3: this.$refs.url.getText(txt); break;
      }
    },
    tratar(texto){
      this.original = texto;
        axios.get("http://127.0.0.1:8000/detecta/",{
            params:{
                "texto": texto,
            }
        }).then(response => {
          this.estadisticas(response.data, texto);
        });
    },
    estadisticas(estadisticas, texto) {
      console.log(estadisticas.elementos[0]);
      this.resultado = estadisticas.elementos;

      texto = texto.replace (/\r?\n/g," ");
      texto = texto.replace (/[ ]+/g," ");
      texto = texto.replace (/^ /,"");
      texto = texto.replace (/ $/,"");
      var palabras = texto.split(" ").length;
      let resultado = (estadisticas.elementos.length / palabras) * 100;
      let resultadoConDosDecimales = resultado.toFixed(3);
      this.porcentajes = "Porcentaje de ofuscacion = " + resultadoConDosDecimales + "%";
      if(estadisticas.elementos.length > 0){
        this.hayOfuscacion = 1;
      }else{
        this.hayOfuscacion = 0;
      }
      this.ver=4;
    }
  }
}
</script>

<style scoped>
.principal{
  display: flex;
}
.menu {
  position: relative;
  height: 97vh;
  width: 17vw;
  border-style: solid;
  background-color: #333333;
  color: white;
  display: block;
  margin-top: 1.5vh;
  margin-left: 1.5vh;
}

.vboton{
  margin-top: 10vh;
  text-align: center;
  
}

.vbtn:hover{
  background-color: #555555;
  color: white;
  font-weight: bold;
}

.menu .h4 {
  width: 99%;
  margin-top: 10vh;
  height: 5vh;
  border-style: solid;
  border-color: #333333;
  text-align: center;
}

h4{
  margin-top: 8px;
}

.menu .h4:hover {
  color: cyan;
  background-color: #555555;
}

.pie {
  position: absolute;
  bottom: 10px;
}

h5 {
  font-size: 15px;
  margin-left: 1vw;
}
</style>