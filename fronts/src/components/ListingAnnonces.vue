<template>
    <!-- <div class="md-layout">
        <div class="md-layout-item"></div>
        <div class="md-layout-item"></div>
        <div class="md-layout-item"></div>
    </div> -->
    <div class="container md-layout md-alignment-center">
        <md-card md-with-hover v-for="(item, index) in publications" :key="index">
            <div class="md-layout-item" v-on:click="handleClickPub(item.id)">
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
                            <md-chip>{{item.category}}</md-chip>
                            <md-chip class="md-primary">{{item.type == 'supply' ? 'Offre' : 'Demande'}}</md-chip>
                        </md-card-content>
                    </div>
                </md-ripple>
            </div>
        </md-card>
    </div>
</template>
  
<script>
import publicationServices from '../services/publicationServices.js'
export default {
    name: 'ListingAnnonces',
    props: {
        msg: String,
        filterName: String, // nom de l'annonce
        filterCategory: String, // Metaux ....
        filterType: String // offre et demande 
    },

    data: function () {
        return {
            teste: 'hello teste',
            publications: []
        };
    },

    mounted() {
        console.log("-- listing filter name", this.filterName)
        console.log("-- listing filter type", this.filterType)
        console.log("-- listing filter category", this.filterCategory)
        let type = this.filterType == undefined ? "" : this.filterType
        let category = this.filterCategory == undefined ? "" : this.filterCategory
        let name = this.filterName == undefined ? "" : this.filterName
        publicationServices.getPublications(name, category, type).then(data => {
            this.publications = data
        })

    },

    methods: {
        handleClickPub: function (id) {
            this.$router.push({ name: 'Annonce', params: { id: id } })
        }
    }
}

</script>
  
  <!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.container {
    margin-left: auto;
    margin-right: auto;
    text-align: center;
    align-items: center;
    align-self: center;
}

.md-card {
    width: 600px;
    height: 225px;
    margin: 2%;
    /* margin-left: 15%;
    margin-right: 15%; */
    background-color: white;
    border-radius: 10px;
    text-align: left;
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
  