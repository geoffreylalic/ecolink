<template>

  <div>

    <div>
      <h2 class="slogan">Trouvez votre <span>ecolink</span> pour une meilleure planète</h2>
    </div>
    <div class="recherche">

      <h2 style="margin-bottom: 5%; margin-left: 20%; text-align: left;">Que recherchez vous ?</h2>
      <div>
        <md-radio v-model="type" value="supply">Offres</md-radio>
        <md-radio v-model="type" value="demand" class="md-primary">Demandes</md-radio>
      </div>
      <md-field>
        <label>{{ type === 'supply' ? 'Offres': 'Demandes' }}</label>
        <md-input type="texte" v-model="name"></md-input>
      </md-field>

      <md-button class="md-raised md-primary" @click="handleResearch">Rechercher</md-button>

      <!-- Uncomment if needed -->
      <!-- <md-table>
          <md-table-row slot="md-table-row" slot-scope="{ item }" v-on:click="$router.push('/RestaurantDetails/' + item._id)">
            <md-table-cell>{{ item.name }}</md-table-cell>
            <md-table-cell>{{ item.cuisine }}</md-table-cell>
            <md-table-cell><i class="el-icon-star-on" v-for="note in item.grades[0].score" :key="note"></i></md-table-cell>
            <md-table-cell><img src="../assets/heart-icon.png" alt="LIKED" width="10px" v-if="isFavoris(item._id)"></md-table-cell>
          </md-table-row>
        </md-table> -->

      <p>Aucun résultat</p>
    </div>

    <div id="categorie">
      <span @click="handleChoiceCategory('Métal')">
        <md-card md-with-hover>
          <md-ripple>
            <md-card-header>
              <div class="md-title">Métal</div>
            </md-card-header>

            <md-card-content>
              <img src="../assets/metal_ball.png" class="categorieIcon" alt="Metal">
            </md-card-content>
          </md-ripple>
        </md-card>
      </span>

      <span @click="handleChoiceCategory('Carton')">
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
      </span>

      <span @click="handleChoiceCategory('Plastique')">
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
      </span>

      <span @click="handleChoiceCategory('Bois')">
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
      </span>

      <span @click="handleChoiceCategory('Verre')">
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
      </span>

      <span v-if="category" @click="handleChoiceCategory('')">
        <md-card md-with-hover>
          <md-ripple>
            <md-card-header>
              <div class="md-title">Annuler</div>
            </md-card-header>

            <md-card-content>
              <img src="../assets/cancel_logo.png" class="categorieIcon" alt="Verre">
            </md-card-content>
          </md-ripple>
        </md-card>
      </span>
    </div>

    <div class="derniereAnnonce">
      <h3>Les dernières annonces</h3>
      <ListingAnnonces :filterName="name" :filterCategory="category" :filterType="type" :key="keyUpdate">
      </ListingAnnonces>

    </div>

  </div>


</template>
<script>
import ListingAnnonces from './ListingAnnonces.vue';

export default {
  name: "AccueilComponent",
  data: () => ({
    // filtering the research
    name: null,
    category: null,
    type: 'supply',
    keyUpdate: 0,
  }),
  props: {
    msg: String
  },
  components: { ListingAnnonces },
  methods: {
    handleResearch: function () {
      console.log("ici", this.name, this.type)
      this.keyUpdate++
    },
    handleChoiceCategory: function (selectedCategory) {
      this.category = selectedCategory
      console.log("catégory", selectedCategory)
      this.keyUpdate++
    }
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
    