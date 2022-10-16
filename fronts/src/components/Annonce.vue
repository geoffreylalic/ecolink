<template>

  <div class="md-layout md-gutter" style="margin-top:5%">

    <div class="md-layout-item md-size-50" style="margin-left:10% ">
      <img :src="image" style="border-radius:30px;border: solid;height:90%">
      
    </div>

    <div class="md-layout-item md-size-25" style="margin-right:15% ">

      <div style="margin-bottom:10%;border-radius:10px;box-shadow: 2px 2px 2px 2px grey ;">
        <h2 style="color:black;">Contactez le vendeur</h2>
        <!-- <h2 style="color:black;">Admin</h2> -->
        <md-button class="md-raised md-primary" style="width:80%;margin-top:6%">{{email}}</md-button> <br>
        <md-button class="md-raised md-primary" style="width:80%">{{phone_number}}</md-button> <br>

      </div>

    </div>

    <div class="md-layout-item md-size-85">
      <h1 style="text-align: left;margin-left: 12.5%;color:black;">{{name}}</h1>
      <p style="text-align: left;margin-left: 12.5%;color:black;">{{location}}</p>
      <h1 style="text-align: left;margin-left: 12.5%;color:black;">{{price}} €</h1> 
      <h1 style="text-align: left;margin-left: 12.5%;color:black;">{{quantity}} restant(s)</h1><br>
    </div>

    <div id="trait_dessus" style="
    margin-left: 11.5%;
    border-top: 1px solid grey;
    width : 700px "> </div>

    <div id="trait_dessus" style="
    margin-left: 11.5%;
    border-top: 1px solid grey;
    width : 700px;margin-top:5% "> </div>




    <div class="md-layout-item md-size-85" style="color:black">
      <h1 style="text-align: left;margin-left: 12.5%;color:black;">Critères : </h1>
      <div class="md-layout-item md-size-35">
        <p style="margin-left: 2.5%;color:black;">Matiere : {{category}}</p>
      </div>
      <div class="md-layout-item md-size-25">
        <p style="margin-left: 29.5%;color:black;">Type : {{type==='supply'? 'Offre': 'Demande'}} </p>
      </div>
    </div>


    <div id="trait_dessus" style="
    margin-left: 11.5%;
    border-top: 1px solid grey;
    width : 700px "> </div>

    <div class="md-layout-item md-size-100" style="color:black">
      <h1 style="text-align: left;margin-left: 10.5%;color:black;">Description</h1>
      <p style="text-align: left;margin-left: 10.5%;color:black; margin-right:33%">{{description}}
      </p>
    </div>




    <div id="trait_dessus" style="
    margin-left: 11.5%;
    border-top: 1px solid grey;
    width : 700px;margin-top:5% "> </div>


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
      name: null,
      description: null,
      category: null,
      location: null,
      type: null,
      photos: null,
      price: null,
      quantity: null,
      email: null,
      phone_number: null,
      image: null
    };
  },

  mounted() {
    console.log("params id", this.$route.params.id)
    publicationServices.getDetailPublication(this.$route.params.id).then((r) => {
      this.name = r.name
      this.description = r.description
      this.category = r.category
      this.location = r.location
      this.type = r.type
      this.photos = r.photos
      this.price = r.price
      this.quantity = r.quantity
      this.email = r.email
      this.phone_number = r.phone_number
      this.image = r.photos
    })

  },
}
</script>