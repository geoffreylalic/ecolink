<template>
    <div class="container">
        <h1>Les annonces</h1>
        <md-card md-with-hover v-for="(item, index) in publications" :key="index">
            <md-ripple>
                <md-card-media>
                    <img v-if='item.photos !== null' :src="item.photos" alt="publicationImage">
                    <img v-else src='../assets/default-image.png' alt="publicationImage">
                </md-card-media>
                <div class="card-container">
                    <md-card-header>
                        <div class="md-title">{{item.name}}</div>
                        <!-- <div class="md-subhead">{{item.description}}</div> -->
                    </md-card-header>
                    <md-card-content>
                        <div>{{item.price}} €</div>
                        <div>{{item.quantity}} restant(s)</div>
                        <div>{{item.location}}</div>
                        <md-chip class="md-primary">{{item.category}}</md-chip>
                    </md-card-content>
                </div>


            </md-ripple>
        </md-card>
    </div>
</template>
  
<script>
import publicationServices from '../services/publicationServices.js'
export default {
    name: 'ListingAnnonces',
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
        console.log("hello",)
        publicationServices.getPublications().then(data => {
            console.log(data)
            this.publications = data
            console.log("this.publications", this.publications)
        })

    }
}

</script>
  
  <!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.container {
    display: flex;
    flex-direction: column;
    align-items: center;
}

.md-card {
    width: 500px;
    height: 200px;
    margin: 2%;
    margin-left: 15%;
    margin-right: 15%;
    background-color: white;
    border-radius: 10px;
    text-align: center;
}

.md-card .md-ripple {
    display: flex;
}

.md-card .md-card-header {
    padding-left: 5%;
}

.card-container {
    padding-left: 5%;
    width: 100%;
}

.md-card-media img {
    height: 200px;
    width: auto;
    object-fit: contain;
    align-items: flex-start;
    padding-left: 40px;
}
</style>
  