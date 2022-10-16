<template>

 <div class="md-layout md-gutter" style="margin-top:5%">
    
    <div class="md-layout-item md-size-50" style="margin-left:10% ">
   <img src="./pexels1.jpg" style="border-radius:30px;border: solid;height:90%">
    </div>
    
    <div class="md-layout-item md-size-25" style="margin-right:15% ">

        <div style="margin-bottom:10%;border-radius:10px;box-shadow: 2px 2px 2px 2px grey ;" >
            <h2 style="color:black;">Contactez le vendeur</h2>
            <h2 style="color:black;">Adecco</h2>
            <md-button class="md-raised md-primary" style="width:80%;margin-top:6%">{{myObject.email}}</md-button> <br>
            <md-button class="md-raised md-primary" style="width:80%">{{myObject.phone_number}}</md-button> <br>
           
        </div>

    </div>

    <div class="md-layout-item md-size-85">
            <h1 style="text-align: left;margin-left: 12.5%;color:black;" >{{myObject.name}}</h1> 
            <p style="text-align: left;margin-left: 12.5%;color:black;">{{myObject.location}}</p> 
            <h1 style="text-align: left;margin-left: 12.5%;color:black;">{{myObject.price}} €</h1> <br>
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
    <h1 style="text-align: left;margin-left: 12.5%;color:black;" >Critères : </h1> 
           <div class="md-layout-item md-size-35">
            <p style="margin-left: 2.5%;color:black;">Matiere  : {{myObject.category}}</p> 
          </div>
    <div class="md-layout-item md-size-25">
              <p style="margin-left: 29.5%;color:black;">Type : {{myObject.type}} </p> 
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
//import publicationServices from '@/services/publicationServices';

export default {
  name: 'AnnonceComponent',
  props: {
    msg: String
  },

  data: function () {
    return {
      teste: 'hello teste',
      publications: [],
      
      myObject: {
      name: 'Nom annonce : ',
      description: 'Jane Doe',
      category: 'Matiere',
      location: 'la ville',
      type: 'type',
      photos: '../pexels1.jpg',
      price: '2016',
      quantity: '2016-04-10',
      email: 'myObject.email',
      phone_number: '09 90 00 23 11'
    }
        };
  },

  mounted() {
    console.log("params id", this.$route.params.id)
  //  publicationServices.getDetailPublication(this.$route.params.id).then((r)=> console.log(r))
    
  },
}
</script>