<template>
    <div>
        <h1>Nos annonces</h1>
        <md-card md-with-hover v-for="(item, index) in publications" :key="index">
            <md-ripple>
                <md-card-header>
                    <div class="md-title">{{item.name}}</div>
                    <!-- <div class="md-subhead">{{item.description}}</div> -->
                </md-card-header>

                <md-card-content>
                    {{item.description}}
                </md-card-content>

                <md-card-actions>
                    <md-button>Action</md-button>
                    <md-button>Action</md-button>
                </md-card-actions>
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

</style>
  