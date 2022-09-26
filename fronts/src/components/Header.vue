<template>
   <div>  

<section class="menu">

  <md-menu md-size="small">
      <md-button md-menu-trigger>Deposer une annonce</md-button>
    </md-menu>


    <md-menu md-size="big">
     <md-button md-menu-trigger>A propos de nous</md-button>
    </md-menu>

    <md-menu md-size="huge">
      <md-button md-menu-trigger>Login</md-button>
    </md-menu>

    <md-menu md-size="auto">
      <md-button md-menu-trigger>S'inscrire</md-button>
    </md-menu>
</section>

   <div class="stp" >
    <section class="titre">
    <p class="style" >Ecolink</p>
    <md-field class="text-center">
      <label>nom de l'annonce</label>
      <md-input></md-input>
    </md-field>

      <md-button class="md-raised md-accent">Deposer une annonce</md-button>

    </section>
   </div>
 

 </div>

 </template>
<script>

export default {
  name: 'HelloWorld',
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

.stp{
width: 100%;
 height: 500px;
  background-attachment: fixed;
   background-image: url('./pexels1.jpg');
   background-size: 100% 100%;
    background-repeat: no-repeat;
    background-position:  cover ;
    overflow: hidden;
}


.ajouter{
  justify-content: center ;
}

.md-field {
    
   border: white ;
  border-radius:30px;
  background: white;
  }

.md-input{
  
}

.menu{
  margin-left:59%;
}



.titre{
margin-top: 10%;
font-size:3em;
color:white;

}

.style{
text-align: center;
font-family : Comic Sans MS, Comic Sans, cursive;
}



</style>
