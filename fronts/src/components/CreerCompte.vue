<template>
    <div>
        <div class="form">
            <form novalidate class="md-layout" @submit.prevent="submit">
                <md-field class="md-block">
                    <label>Username</label>
                    <md-input v-model="username" type="text" name="username" required></md-input>
                </md-field>
                <md-field class="md-block">
                    <label>Numéro de tel.</label>
                    <md-input v-model="username" type="text" name="username" required></md-input>
                </md-field>
                <md-field class="md-block">
                    <label>Password</label>
                    <md-input v-model="password" type="password" name="password" required></md-input>
                </md-field>
                <md-field class="md-block">
                    <label for="movie">Vous êtes ?</label>
                    <md-select v-model="catégorie" name="catégorie" id="catégorie">
                        <md-option value="entreprise">Entreprise</md-option>
                        <md-option value="particulier">Particulier</md-option>
                    </md-select>
                </md-field>
                <br>
                <md-button class="md-block" type="submit">Login</md-button>
            </form>
        </div>
    </div>
</template>
<script>

export default {
  name: 'LoginProfile',
  props: {
    msg: String
  }
}
</script>
<style>
.form {
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
