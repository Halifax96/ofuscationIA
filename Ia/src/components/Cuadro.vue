<template>
    <div class="cuadro">
        <v-textarea 
            no-resize 
            outlined 
            bg-color="#00ffff" 
            color="black" 
            label="Introduzca el texto" 
            height="675" 
            mt="15" 
            class="texto mt-15" 
            id="escritura"
        >

        </v-textarea>
    </div>
</template>

<script>
import { VTextarea } from 'vuetify/lib';
export default {
    name: "CuadroTexto",
    components: {
        VTextarea,
    },
    methods:{
        getText () {
            var texto = document.getElementById("escritura").value;
            this.$emit("envia", texto);
            document.getElementById("escritura").value = "";
        }
    }
}
</script>

<style scoped>
.cuadro {
    position: relative;
    width: 80vw;
    margin-left: 20;
    height: 97vh;
    margin-top: 1.5vh;
    background-color: #322458;
}

.texto {
    position: absolute;
    width: 95%;
    margin-left: 2.5%;
    height: 94%;
    margin-top: 1.5%;
    resize: none;
    background-color: #ffffff;
}
</style>