<template>

  <div class="md-layout md-gutter">
      <div class="md-layout-item">
        <router-link to="/">
          <h1 class="md-title titre">EcoLink</h1>
        </router-link>
      </div>
      <div class="md-layout-item"></div>
      <div class="md-layout-item">
        <md-button class="md-accent">Favoris</md-button>
        <md-button class="">À propos</md-button>
        <md-button class="">Se conecter</md-button>
      </div>
  </div>  

 </template>
<script>

export default {
  name: 'HeaderComponent',
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

.titre {
  color: black;
  text-decoration: none;
  font-family: 'agraham', sans-serif;
}

.card .md-card {
    width: 20%;
    margin: 4px;
    display: inline-block;
    vertical-align: top;
    border-radius: 20px;
}

.card .md-title {
  font-size: small;
}

footer {
  margin-top: 5%;
  font-family: 'agraham', sans-serif;
}

@import url('http://fonts.cdnfonts.com/css/agraham');

</style>
