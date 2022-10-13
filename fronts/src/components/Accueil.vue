<template>

<div>

  <div>
    <h2 class="slogan">Trouvez votre <span>ecolink</span> pour une meilleure planète</h2>
    </div>
    <div class="recherche">
        
        <h2 style="margin-bottom: 5%; margin-left: 20%; text-align: left;">Que recherchez vous ?</h2>
        <div>
            <md-radio v-model="radio" value="Offres">Offres</md-radio>
            <md-radio v-model="radio" value="Demandes" class="md-primary">Demandes</md-radio>
        </div>
        <md-field>
            <label>{{ radio }}</label>
            <md-input @input="chercherRestaurants" type="texte" v-model="nomRechercher"></md-input>
        </md-field>

        <md-button class="md-raised md-primary">Rechercher</md-button>

        <md-table v-model="restaurantsRecherche" v-show="show">
          <md-table-row slot="md-table-row" slot-scope="{ item }" v-on:click="$router.push('/RestaurantDetails/' + item._id)">
            <md-table-cell>{{ item.name }}</md-table-cell>
            <md-table-cell>{{ item.cuisine }}</md-table-cell>
            <md-table-cell><i class="el-icon-star-on" v-for="note in item.grades[0].score" :key="note"></i></md-table-cell>
            <md-table-cell><img src="../assets/heart-icon.png" alt="LIKED" width="10px" v-if="isFavoris(item._id)"></md-table-cell>
          </md-table-row>
        </md-table>

        <p v-show="noResult">Aucun résultat</p>
      </div>

      <div id="categorie">
        <md-card md-with-hover>
          <md-ripple>
            <md-card-header>
              <div class="md-title">Metal</div>
            </md-card-header>

            <md-card-content>
              <img src="../assets/metal_ball.png" class="categorieIcon" alt="Metal">
            </md-card-content>
          </md-ripple>
        </md-card>

        <md-card md-with-hover>
          <md-ripple>
            <md-card-header>
              <div class="md-title">Carton</div>
            </md-card-header>

            <md-card-content>
              <img src="../assets/cardboard_ball.png" class="categorieIcon" alt="Carton">
            </md-card-content>
          </md-ripple>
        </md-card>

        <md-card md-with-hover>
          <md-ripple>
            <md-card-header>
              <div class="md-title">Plastique</div>
            </md-card-header>

            <md-card-content>
              <img src="../assets/plastic_ball.png" class="categorieIcon" alt="Plastique">
            </md-card-content>
          </md-ripple>
        </md-card>

        <md-card md-with-hover>
          <md-ripple>
            <md-card-header>
              <div class="md-title">Bois</div>
            </md-card-header>

            <md-card-content>
              <img src="../assets/wood_ball.png" class="categorieIcon" alt="Bois">
            </md-card-content>
          </md-ripple>
        </md-card>

        <md-card md-with-hover>
          <md-ripple>
            <md-card-header>
              <div class="md-title">Verre</div>
            </md-card-header>

            <md-card-content>
              <img src="../assets/glass_ball.png" class="categorieIcon" alt="Verre">
            </md-card-content>
          </md-ripple>
        </md-card>
      </div>

      <div class="derniereAnnonce">
        <h3>Les dernières annonces</h3>

        <!--FAIRE LISTE DERNIERE ANNONCE POSTER-->

        
      </div>
      
</div>

    
     </template>
    <script>
    
    export default {
      name: 'AccueilComponent',
      data: () => ({
      radio: 'Offres'
    }),
      props: {
        msg: String
      }
    }
    </script>
    
    <style scoped>
    
    h3 {
      margin: 40px 0 0;
    }
    ul {
      list-style-type: none;
      padding: 0;
    }
    li {
      display: inline-block;
      margin: 0 10px;
    }
    a {
      color: #42b983;
    }


    .md-field {
        width: 60%;
        margin: auto;
    }

    .recherche {
        padding-top: 4%;
        padding-bottom: 4%;
        margin: 2%;
        margin-left: 15%;
        margin-right: 15%;
        background-color: white;
        border-radius: 10px;
    }

    .categorie {
      width: 100%;
      margin-bottom: 4%;
    }

    .categorieIcon {
      width: 50px;
      height: 50px;
    }

    .md-card {
        width: 15%;
        margin: 4px;
        display: inline-block;
        vertical-align: top;
        border-radius: 20px;
    }

    .slogan {
      font-size: 2em;
      font-weight: 150;
    }

    .slogan span {
      color: #42b983;
      font-family: 'DM Serif Display', sans-serif;
    }
    
    </style>
    