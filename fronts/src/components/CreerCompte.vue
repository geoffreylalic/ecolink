<template>
    <div>
        <div class="newUser">
            <H1>Nouveau membre</H1>
            <form novalidate class="md-layout" @submit.prevent="submit">
                <md-field class="md-block">
                    <label>Username</label>
                    <md-input v-model="form.newUsername" type="text" name="newUsername" required></md-input>
                </md-field>

                <md-field class="md-block">
                    <label>Mail</label>
                    <md-input v-model="form.newMail" type="text" name="newMail" required></md-input>
                </md-field>

                <md-field class="md-block">
                    <label>Numéro de tel.</label>
                    <md-input v-model="form.numTel" type="text" name="numTel" required></md-input>
                </md-field>

                <md-field class="md-block">
                    <label>Password</label>
                    <md-input v-model="form.newPassword" type="password" name="newPassword" required></md-input>
                </md-field>

                <md-field class="md-block">
                    <label for="movie">Vous êtes ?</label>
                    <md-select v-model="form.catégorie" name="catégorie" id="catégorie">
                        <md-option value="entreprise">Entreprise</md-option>
                        <md-option value="particulier">Particulier</md-option>
                    </md-select>
                </md-field>
                <br>
                <md-button class="md-block" type="submit">Créer compte </md-button>
            </form>
            <md-dialog :md-active.sync="showSave" @submit.prevent="closeDialog">
                <md-dialog-title>Bienvenue {{ newUser }} !</md-dialog-title>
                <md-tab>
                    <p>Nous sommes ravis de vous compter dans notre communauté !</p>
                </md-tab>
                <md-dialog-actions>
                    <router-link to="/">
                        <md-button class="md-primary">Super !</md-button>
                    </router-link>
                </md-dialog-actions>
            </md-dialog>
        </div>

        <div class="connect">
            <H1>Déjà membre ?</H1>
            <form novalidate class="md-layout" @submit.prevent="connect">
                <md-field class="md-block">
                    <label>Username</label>
                    <md-input v-model="form.username" type="text" name="username"></md-input>
                </md-field>
                <md-field class="md-block">
                    <label>Password</label>
                    <md-input v-model="form.password" type="password" name="password"></md-input>
                </md-field>
                <br>
                <md-button class="md-block" type="submit">Connexion </md-button>
            </form>

            <md-dialog :md-active.sync="showDialog" @submit.prevent="closeDialog">
                <md-dialog-title>Heureux de vous revoir !</md-dialog-title>
                <md-tab>
                    <p>Vous etes connecté en tant que {{ lastUser }}</p>
                </md-tab>
                <md-dialog-actions>
                    <router-link to="/">
                        <md-button class="md-primary">Super !</md-button>
                    </router-link>
                </md-dialog-actions>
            </md-dialog>
        </div>

    </div>
</template>
<script>
import { numeric } from 'vuelidate/lib/validators'

export default {
    name: 'LoginProfile',
    props: {
        msg: String,
        newPassword: String,
        numTel: numeric,
        catégorie: String,
        username: String,
        password: String,
    },
    data: () => ({
        form: {
            newUsername: null,
            newMail: null,
            numTel: null,
            newPassword: null,
            catégorie: null,
            username: null,
            password: null,
            showDialog: false,
            showSave: false
        },
        userSaved: false,
        lastUser: null,
        newUser: null

    }),
    methods: {
        connect() {
            console.log(this.form.username)
            this.saveUser()
        },
        submit() {
            console.log(this.form.newUsername)
            this.connectUser()
        },
        saveUser() {
            this.lastUser = `${this.form.username}`
            this.userSaved = true
            this.showDialog = true
            this.clearForm()
        },
        connectUser(){
            this.newUser = `${this.form.newUsername}`
            this.userSaved = true
            this.showSave = true
            this.clearForm()
        },
        clearForm() {
            this.form.newUsername = null
            this.form.numTel = null
            this.form.newPassword = null
            this.form.catégorie = null
            this.form.username = null
            this.form.password = null
        },
        closeDialog() {
            this.showDialog = false
        }
    }

}
</script>
<style>
.newUser {
    padding-top: 2%;
    padding-bottom: 3%;
    width: 100%;
    max-width: 500px;
    margin: 0 auto;
    background-color: white;
    border-radius: 10px;
}

.connect {
    padding-top: 2%;
    padding-bottom: 3%;
    width: 100%;
    max-width: 500px;
    margin: 0 auto;
    background-color: white;
    border-radius: 10px;
}

.md-block {
    width: 60%;
    margin: auto;
}

a {
    color: #42b983;
}
</style>
