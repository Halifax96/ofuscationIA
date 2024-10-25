<template>
    <div class="archivo">
        <v-main>
            <v-container fill-height>
                <v-row justify="center">
                    <v-col cols="auto">
                        <v-card width="600" height="270" raised>
                            <v-card-title>Carga de datos desde url</v-card-title>
                            <br>
                            <v-card-text>
                                <v-text-field label="Introduzca url" outlined v-model="enlace">
                                </v-text-field>
                            </v-card-text>
                            <v-card-actions>
                                <v-spacer></v-spacer>
                                <v-btn right @click="importar">Cargar</v-btn>
                            </v-card-actions>
                        </v-card>
                    </v-col>
                    <v-col cols="auto">
                        <v-card class="urlArchivo" raised>
                            <v-card-title>Contenido:</v-card-title>
                            <v-textarea no-resize readonly outlined color="black" height="45.3vh" :value="texto"/>
                        </v-card>
                    </v-col>
                </v-row>
            </v-container>
        </v-main>
    </div>
</template>

<script>
import { VTextField, VContainer, VCard, VCardTitle, VCardText, VCol, VRow, VMain } from 'vuetify/lib';
import { VCardActions, VSpacer, VBtn } from 'vuetify/lib';
import axios from "axios";
export default {
    name: "CuadroTexto",
    components: {
        VTextField,
        VContainer,
        VRow,
        VCol,
        VCard,
        VCardTitle,
        VCardText,
        VMain,
        VCardActions,
        VSpacer,
        VBtn,
    },
    data:() => ({
        enlace: null, // <- initialize the v-model prop
        texto: null,
        prueba: JSON,
    }),
    methods: {
        importar() {
            if(this.enlace==null) alert("Introduzca el enlace primero");
            else{
                axios.get("http://127.0.0.1:8000/admin/",{
                    params:{
                        "url": this.enlace,
                    }
                }
                ).then(response => {
                    this.texto = response.data.texto;
                }) 
            }
        },
        getText () {
            this.$emit("envia", this.texto);
            this.texto = "";
            this.enlace = null;
        }
    }
}
</script>

<style scoped>
.archivo {
    position: relative;
    width: 80vw;
    margin-left: 20;
    height: 97vh;
    margin-top: 1.5vh;
    background-color: #322458;
}

.texto{
    overflow-y: scroll;
}
</style>