<template>

<div>
    <div class="recherche">
        <h2 style="margin-bottom: 5%; margin-left: 20%; text-align: left;">Que recherchez vous ?</h2>
        <md-field>
          <label>Restaurants</label>
            <md-input @input="chercherRestaurants" type="texte" v-model="nomRechercher"></md-input>
          </md-field>

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
</div>

    
     </template>
    <script>
    
    export default {
      name: 'AccueilComponent',
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
    padding-top: 8%;
    padding-bottom: 8%;
    margin: 2%;
    margin-left: 15%;
    margin-right: 15%;
    background-color: white;
    border-radius: 10px;
}

.top3 {
  margin-bottom: 4%;
}

.top3 .md-card {
    width: 25%;
    margin: 4px;
    display: inline-block;
    vertical-align: top;
    border-radius: 20px;
}
    
    </style>
    