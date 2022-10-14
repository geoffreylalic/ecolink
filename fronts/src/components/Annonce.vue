<template>
  <div>
    <div class="md-layout">
      <div class="md-layout-item" style="border: solid;margin-left: 7.5%;">
        <img class="image" src="./pexels1.jpg" alt="">
      </div>
      <div class="md-layout-item" style=" margin-left: 7.5%; margin-right: 2%;border: solid; ">
        <h1>Contactez le vendeur</h1>
        <h2 style="margin-bottom:30%">Nom Entreprise</h2>
        <md-button class="md-raised md-primary" style="width:50%">Acheter</md-button> <br>
        <md-button class="md-raised md-primary" style="width:50%">Message</md-button>
      </div>
    </div>

    <div class="info">
      <h1 style="text-align: left;">Nom annonce : </h1> <br>
      <h2 style="text-align: left;">Prix </h2> <br>
    </div>

    <div class="description">
      <h1 style="text-align: left;">Description : </h1> <br>
      <p style="text-align: left;">Piano d'étude Yamaha (voir numéro de série sur les photos). T
        rès peu servi et désaccordé. A prendre sur place au 1ere étage
        sans ascenseur. Urgent car si il ne se vend pas vite il sera vidé
        et converti en bar.</p>

    </div>


  </div>
</template>

     
<script>
import publicationServices from '@/services/publicationServices';


export default {
  name: 'AnnonceComponent',
  props: {
    msg: String
  },

  data: function () {
    return {
      teste: 'hello teste',
      publications: []
    };
  },

  mounted() {
    console.log("params id", this.$route.params.id)
    publicationServices.getDetailPublication(this.$route.params.id).then((r)=> console.log(r))
  },
}
</script>
    
   