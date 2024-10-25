<template>
    <div class="archivo">
        <v-main>
            <v-container fill-height>
                <v-row justify="center">
                    <v-col cols="auto">
                        <v-card width="600" height="270" raised>
                            <v-card-title>Carga de datos desde archivo</v-card-title>
                            <br>
                            <v-card-text>
                                <v-file-input accept=".txt" label="Subir archivo .txt" outlined v-model="archivo">
                                </v-file-input>
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
                            <v-textarea no-resize readonly outlined color="black" height="45.3vh" class="texto" :value="texto" id="archivo"/>
                        </v-card>
                    </v-col>
                </v-row>
            </v-container>
        </v-main>
    </div>
</template>

<script>
import { VFileInput, VContainer, VCard, VCardTitle, VCardText, VCol, VRow, VMain } from 'vuetify/lib';
import { VCardActions, VSpacer, VBtn } from 'vuetify/lib';
export default {
    name: "CuadroTexto",
    components: {
        VFileInput,
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
        archivo: null, 
        texto: "",
    }),
    methods: {
        importar() {      
            if (!this.archivo) { this.texto = "No hay archivo seleccionado" }
            var reader = new FileReader();
            reader.readAsText(this.archivo);
            reader.onload = () => {
                this.texto = reader.result;
            }
        },
        getText(txt) {
            txt = this.texto;
            this.$emit("envia", txt);
            this.texto = "";
            this.archivo = null;
        },
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
</style>