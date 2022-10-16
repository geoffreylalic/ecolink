
<template>
  <div>
    <form novalidate class="md-layout" @submit.prevent="validateUser">
      <md-card class="md-layout-item md-size-50 md-small-size-100 centrer ">
        <md-card-header>
          <div class="md-title">Déposer une annonce</div>
        </md-card-header>
        <md-card-content>
          <div class="md-layout md-gutter">
            <div class="md-layout-item md-small-size-100">
              <md-field :class="getValidationClass('pubName')">
                <label for="first-name">Titre de l'annonce</label>
                <md-input name="pubName" id="pub-name" autocomplete="given-name" v-model="form.pubName"
                  :disabled="sending" />
                <span class="md-error" v-if="!$v.form.pubName.required">Titre de l'annonce requis</span>
                <span class="md-error" v-else-if="!$v.form.pubName.minlength">Le titre de l'annonce est invalid</span>
              </md-field>
            </div>

            <div class="md-layout-item md-small-size-100">
              <md-field :class="getValidationClass('location')">
                <label for="location">Localisation</label>
                <md-input name="location" id="location" autocomplete="street-address" v-model="form.location"
                  :disabled="sending" />
                <span class="md-error" v-if="!$v.form.location.required">Localisation requise</span>
                <span class="md-error" v-else-if="!$v.form.location.minlength">La localisation est invalide</span>
              </md-field>
            </div>
          </div>

          <div class="md-layout md-gutter">
            <div class="md-layout-item md-small-size-100">
              <md-field :class="getValidationClass('category')">
                <label for="category">Categorie</label>
                <md-select name="category" id="category" v-model="form.category" md-dense :disabled="sending">
                  <md-option value="Métal">Métal</md-option>
                  <md-option value="Carton">Carton</md-option>
                  <md-option value="Plastique">Plastique</md-option>
                  <md-option value="Bois">Bois</md-option>
                  <md-option value="Verre">Verre</md-option>
                </md-select>
                <span class="md-error">La catégorie est requise</span>
              </md-field>
            </div>

            <div class="md-layout-item md-small-size-100">
              <md-field :class="getValidationClass('type')">
                <label for="type">Type</label>
                <md-select name="type" id="type" v-model="form.type" md-dense :disabled="sending">
                  <md-option value="supply">Offre</md-option>
                  <md-option value="demand">Demande</md-option>
                </md-select>
                <span class="md-error">Le type est requis</span>
              </md-field>
            </div>

            <div class="md-layout-item md-small-size-100">
              <md-field :class="getValidationClass('type')">
                <label for="isPro">Professionel ou particulier</label>
                <md-select name="isPro" id="isPro" v-model="form.isPro" md-dense :disabled="sending">
                  <md-option value=true>Professionel</md-option>
                  <md-option value=false>Particulier</md-option>
                </md-select>
                <span class="md-error">Le type est requis</span>
              </md-field>
            </div>


            <div class="md-layout-item md-small-size-100">
              <md-field :class="getValidationClass('price')">
                <label for="price">Prix à l'unité</label>
                <md-input type="number" id="price" name="price" v-model="form.price" :disabled="sending" />
                <span class="md-error" v-if="!$v.form.price.required">Le prix est requis</span>
                <span class="md-error" v-else-if="!$v.form.price.maxlength">Invalid price</span>
              </md-field>
            </div>

            <div class="md-layout-item md-small-size-100">
              <md-field :class="getValidationClass('quantite')">
                <label for="quantite">Quantité</label>
                <md-input type="number" id="quantite" name="quantite" autocomplete="quantite" v-model="form.quantite"
                  :disabled="sending" />
                <span class="md-error" v-if="!$v.form.quantite.required">La quantité est requise</span>
                <span class="md-error" v-else-if="!$v.form.quantite.maxlength">Invalid quantite</span>
              </md-field>
            </div>
          </div>

          <md-field>
            <label>Choisir une image</label>
            <md-file accept="image/*" @input="handleSelectedFiles" />
          </md-field>

          <md-field>
            <label>Description</label>
            <md-textarea v-model="form.description"></md-textarea>
          </md-field>
        </md-card-content>

        <md-progress-bar md-mode="indeterminate" v-if="sending" />

        <md-card-actions>
          <md-button type="submit" class="md-raised md-primary" :disabled="sending">Créer une annonce</md-button>
        </md-card-actions>
      </md-card>

      <!-- <md-snackbar :md-active.sync="userSaved">The user {{ lastUser }} was saved with success!</md-snackbar> -->
    </form>
    <md-snackbar :md-position="center" :md-active.sync="showSnackbar" md-persistent>
      <span>Votre annonce a été publiée.</span>
    </md-snackbar>
  </div>
</template>
  
<script>

import publicationServices from "@/services/publicationServices";
import { validationMixin } from "vuelidate";
import {
  required,
  minLength,
  maxLength,
} from "vuelidate/lib/validators";

export default {
  name: "FormValidation",
  mixins: [validationMixin],
  data: () => ({
    position: 'center',
    showSnackbar : false,
    form: {
      pubName: null,
      location: null,
      category: null,
      type: null,
      price: null,
      quantite: null,
      image: null,
      description: null,
      isPro: null,
    },
    sending: false,
  }),
  validations: {
    form: {
      pubName: {
        required,
        minLength: minLength(3),
      },
      location: {
        required,
        minLength: minLength(3),
      },
      price: {
        required,
        maxLength: maxLength(3),
      },
      quantite: {
        required,
        maxLength: maxLength(3),
      },
      category: {
        required,
      },
    },
  },
  methods: {
    handleSelectedFiles(event) {
      let file = event.currentTarget.files[0]

      this.form.image = file
      console.log('fom file', this.form.image)
    },

    getValidationClass(fieldName) {
      const field = this.$v.form[fieldName];

      if (field) {
        return {
          "md-invalid": field.$invalid && field.$dirty,
        };
      }
    },
    clearForm() {
      this.$v.$reset();
      this.form.image = "";
      this.form.pubName = null;
      this.form.location = null;
      this.form.price = null;
      this.form.quantite = null;
      this.form.category = null;
      this.form.type = null;
      this.form.isPro = null;
      this.form.description = null
    },
    savePublication() {
      this.sending = true;
      let formData = new FormData()
      formData.append('name', this.form.pubName)
      formData.append('description', this.form.description)
      formData.append('category', this.form.category)
      formData.append('location', this.form.location)
      formData.append('type', this.form.type)
      if (this.form.image !== null) {
        formData.append('photos', this.form.image, this.form.image.name)
      }
      formData.append('quantity', this.form.quantite)
      formData.append('price', this.form.price)
      formData.append('is_pro', this.form.isPro)
      publicationServices.createPublication(formData).then(() => {
        this.showSnackbar = true
        this.sending = false
      })
      this.clearForm()
    },

    validateUser() {
      this.$v.$touch();

      if (!this.$v.$invalid) {
        this.savePublication();
      }
    },
  },
};
</script>

<style>
#depose {
  color: red;
}

.md-progress-bar {
  top: 0;
  right: 0;
  left: 0;
}

.centrer {
  margin-left: auto;
  margin-right: auto;
}
</style>