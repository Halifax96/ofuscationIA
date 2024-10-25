<template>
    <div class="archivo">
        <v-main>
            <v-container fill-height>
                <v-row justify="center">
                    <v-col cols="auto">
                        <v-card width="80vw" height="330" raised>
                            <v-card-title style="font-weight:bold; font-size:30px;">Texto original</v-card-title>
                            <br>
                            <v-textarea no-resize readonly outlined color="black" height="20.3vh"
                                :value="texto"></v-textarea>
                        </v-card>
                    </v-col>
                </v-row>
                <v-row>
                    <v-col cols="auto">
                        <v-card height="54vh"  width="80vw" raised>
                            <v-card-title style="font-weight:bold; font-size:30px;">Resultados de la prueba 😎</v-card-title>
                            <v-card class="resultado"> 
                                <table v-show="ver==1">
                                    <header>
                                        <tr> <th>Palabra ofuscada</th> <th>Tipo de ofuscación</th></tr>
                                    </header>
                                    <body>
                                        <tr v-for="(linea, index) in resultados" :index="index" :key="index">
                                            <td>{{ linea.palabra }}</td>
                                            <td>{{ linea.ofuscacion }}</td>
                                        </tr>
                                    </body>
                                </table>
                                <p v-show="ver==0" style="font-weight:bold; font-size: 30px; margin-left: 10vw;">No se ha encontrado ofuscación</p>
                            </v-card>  
                        </v-card>
                    </v-col>
                </v-row>
                <v-row>
                    <v-col cols="auto">
                        <v-card width="80vw" raised>
                            <v-card-title style="font-weight:bold; font-size:30px;">{{ ofuscacion }}</v-card-title>
                        </v-card>
                    </v-col>
                </v-row>
            </v-container>
        </v-main>
    </div>
</template>

<script>
import { /*VBtn,*/ VContainer, VCard, VCardTitle, VCol, VRow, VMain } from 'vuetify/lib';
export default {
    name: "EstadisticasVue",
    components: {
        VContainer,
        VRow,
        VCol,
        VCard,
        VCardTitle,
        VMain,
        //VBtn,
    },
    data: () => ({
        itemsPerPage: 5,
        headers: [
            {
                title: 'Palabra ofuscada',
                align: 'start',
                sortable: true,
                key: 'palabra',
            },
            { title: 'Tipo de ofuscacion', key: 'ofuscacion', align: 'end' }
        ],
      
    }),
    props: {
        texto: {
            type: String,
        },
        resultados: {
            type: []
        },
        ofuscacion: {
            type: String,
        },

        ver: {
            type: Number,
        },
    },

    methods: {
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

tr{
    width: 70vw;
}

th, td{
    border-style: solid;
    border-width: 1px;
    width: 35vw;
    text-align: center;
    border-spacing: 0px;
    background-color: #dddddd;
    padding-top: 7px;
    padding-bottom: 7px;
    font-size: 25px;
}

th {
    background-color: #aaffff;
}

table{
    margin-left: 1vw;
    width: 65vw;
    border-collapse: collapse;
}

.resultado{
    overflow-y: scroll;
    height: 45vh;
}
</style>