<template>
  <div id="app">

    <div class="md-layout md-gutter">
      <div class="md-layout-item">
        <router-link to="/">
          <h1 class="md-title titre">ecolink</h1>
        </router-link>
        <router-link to="/DeposerAnnonce">
          <md-button class="md-raised md-primary">Déposer une annonce</md-button>
        </router-link>
      </div>
      <div class="md-layout-item"></div>
      <div class="md-layout-item">
        <md-button class="md-accent">Favoris</md-button>
        <md-button class="">À propos</md-button>
        <md-button class="">Se conecter</md-button>
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
  color: black;
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

footer {
  margin-top: 5%;
  font-family: 'DM Serif Display', sans-serif;
}

@import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display&display=swap');
</style>
