<template>
<div>
    <div class="md-layout">
    <div class="md-layout-item" style="border: solid;margin-left: 7.5%;">
        {{photos}}
    </div>
    <div class="md-layout-item" style=" margin-left: 7.5%; margin-right: 2%;border: solid; " >
        <h1>Contactez le vendeur</h1>
        <h2 style="margin-bottom:30%">Nom Entreprise</h2>
        <md-button class="md-raised md-primary" style="width:50%">{{email}}</md-button> <br>
        <md-button class="md-raised md-primary" style="width:50%">{{phone_number}}</md-button> <br>
         <md-button class="md-raised md-primary" style="width:50%">Acheter</md-button> <br>
          <md-button class="md-raised md-primary" style="width:50%">Message</md-button>
    </div>
    </div>

      <div class="info">
            <h1 style="text-align: left;margin-left: 7.5%;">Nom annonce : {{name}}</h1> 
            <h1 style="text-align: left;margin-left: 7.5%;">{{location}}</h1> 
            <br>
            <h2 style="text-align: left;margin-left: 7.5%;">Prix : {{price}}</h2> <br>
    </div>
  <div id="trait_dessus" style="
    margin-left: 7.5%;
    border-top: 1px solid #000;
    width : 700px; "> </div>

    <div class="criteres">
            <h1 style="text-align: left;margin-left: 7.5%;">Criteres </h1> <br>
            <h2 style="text-align: left;margin-left: 7.5%;">Matière : {{category}} </h2> <br>
                        <h2 style="text-align: left;margin-left: 7.5%;">type : {{type}} </h2> <br>

    </div>

    <div id="trait_dessus" style="
    margin-left: 7.5%;
    border-top: 1px solid #000;
    width : 700px; "> </div>


    <div class="description">
                <h1 style="text-align: left;margin-left: 7.5%;">Description :  </h1> <br>
                <p style="text-align: left;margin-left: 7.5%;"> Quantité : {{quantity}}</p> <br>
                <p style="text-align: left;margin-left: 7.5%;">{{desc}}</p>
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
    
   