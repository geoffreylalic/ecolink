<template>
  <div id="app">

    <div class="md-layout md-gutter">
      <div class="md-layout-item">
        <router-link to="/">
          <h1 class="md-title titre">ecolink</h1>
        </router-link>
      </div>
      <div class="md-layout-item">
        <router-link to="/deposerannonce">
          <md-button class="md-raised md-primary">Déposer une annonce</md-button>
        </router-link>
        <router-link to="/annonces">
          <md-button class="md-raised md-primary">Lister les annonces</md-button>
        </router-link>
          <router-link to="/annonce">
          <md-button class="md-raised md-primary">Annonce</md-button>
        </router-link>
      </div>
      <div class="md-layout-item">
        <md-button class="md-accent">Favoris</md-button>
        <router-link to="/apropos">
          <md-button class="">À propos</md-button>
        </router-link>
        <router-link to="/creercompte">
          <md-button class="">Se connecter</md-button>
        </router-link>
      </div>
  </div>  

  <router-view></router-view> 

    <footer>
      ecolink
    </footer>
  </div>
</template>

<script>
export default {
  name: 'App',
  components: {
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

.titre {
  color: #41a963;
  text-decoration: none;
  font-family: 'DM Serif Display', sans-serif;
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

button.md-primary {
  background-color: #41a963!important;
}

button.md-primary:hover{
  background-color: #448aff!important;
}

footer {
  margin-top: 5%;
  font-family: 'DM Serif Display', sans-serif;
  color: #41a963;
}

@import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display&display=swap');
</style>
