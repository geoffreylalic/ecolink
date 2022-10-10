
  <template>
  <div >
    <form
      novalidate
      class="md-layout"
      @submit.prevent="validateUser"
    >
      <md-card   class="md-layout-item md-size-50 md-small-size-100 centrer ">
        <md-card-header>
          <div class="md-title">Deposer une annonce</div>
        </md-card-header>

        <md-card-content>
          <div class="md-layout md-gutter">
            <div class="md-layout-item md-small-size-100">
              <md-field :class="getValidationClass('firstName')">
                <label for="first-name">titre de l'annonce</label>
                <md-input
                  name="first-name"
                  id="first-name"
                  autocomplete="given-name"
                  v-model="form.firstName"
                  :disabled="sending"
                />
                <span class="md-error" v-if="!$v.form.firstName.required"
                  >Titre de l'annonce requis</span
                >
                <span class="md-error" v-else-if="!$v.form.firstName.minlength"
                  >Invalid first name</span
                >
              </md-field>
            </div>

            <div class="md-layout-item md-small-size-100">
              <md-field :class="getValidationClass('lastName')">
                <label for="last-name">Location</label>
                <md-input
                  name="last-name"
                  id="last-name"
                  autocomplete="street-address"
                  v-model="form.lastName"
                  :disabled="sending"
                />
                <span class="md-error" v-if="!$v.form.lastName.required"
                  >The last name is required</span
                >
                <span class="md-error" v-else-if="!$v.form.lastName.minlength"
                  >Invalid last name</span
                >
              </md-field>
            </div>
          </div>

          <div class="md-layout md-gutter">
            <div class="md-layout-item md-small-size-100">
              <md-field :class="getValidationClass('gender')">
                <label for="category">categorie</label>
                <md-select
                  name="category"
                  id="category"
                  v-model="form.gender"
                  md-dense
                  :disabled="sending"
                >
                  <md-option></md-option>
                  <md-option value="M">Metaux</md-option>
                  <md-option value="C">Carton</md-option>
                  <md-option value="P">Plastique</md-option>
                  <md-option value="B">Bois</md-option>
                  <md-option value="V">Verre</md-option>
                  <md-option value="F">Autres</md-option>
                </md-select>
                <span class="md-error">The gender is required</span>
              </md-field>
            </div>

            <div class="md-layout-item md-small-size-100">
              <md-field :class="getValidationClass('age')">
                <label for="age">price</label>
                <md-input
                  type="number"
                  id="price"
                  name="price"
                  v-model="form.age"
                  :disabled="sending"
                />
                <span class="md-error" v-if="!$v.form.age.required">The price is required</span>
                <span class="md-error" v-else-if="!$v.form.age.maxlength">Invalid price</span>
              </md-field>
            </div>

            <div class="md-layout-item md-small-size-100">
              <md-field :class="getValidationClass('quantite')">
                <label for="quantite">quantite</label>
                <md-input
                  type="number"
                  id="quantite"
                  name="quantite"
                  autocomplete="quantite"
                  v-model="form.quantite"
                  :disabled="sending"
                />
                <span class="md-error" v-if="!$v.form.quantite.required"
                  >The quantite is required</span
                >
                <span class="md-error" v-else-if="!$v.form.quantite.maxlength"
                  >Invalid quantite</span
                >
              </md-field>
            </div>
          </div>

          <md-field>
            <label>Only images</label>
            <md-file v-model="single" accept="image/*" />
          </md-field>

          <md-field>
            <label>Description</label>
            <md-textarea v-model="textarea"></md-textarea>
          </md-field>
        </md-card-content>

        <md-progress-bar md-mode="indeterminate" v-if="sending" />

        <md-card-actions>
          <md-button type="submit" class="md-primary" :disabled="sending"
            >Create user</md-button
          >
        </md-card-actions>
      </md-card>

      <md-snackbar :md-active.sync="userSaved"
        >The user {{ lastUser }} was saved with success!</md-snackbar
      >
    </form>
  </div>
</template>
  




 

<script>
/*
 "name": "pub name",
        "description": "desc teste",
        "category": "teste",
        "location": "France",
        "type": "demand",
        "photos": null,
        "limit_date": "2022-09-30",
        "price": "14.00",
        "quantity": 1
*/

import { validationMixin } from "vuelidate";
import {
  required,
  email,
  minLength,
  maxLength,
} from "vuelidate/lib/validators";

export default {
  name: "FormValidation",
  mixins: [validationMixin],
  data: () => ({
    form: {
      firstName: null,
      lastName: null,
      gender: null,
      age: null,
      quantite:null,
      email: null,
    },
    userSaved: false,
    sending: false,
    lastUser: null,
  }),
  validations: {
    form: {
      firstName: {
        required,
        minLength: minLength(3),
      },
      lastName: {
        required,
        minLength: minLength(3),
      },
      age: {
        required,
        maxLength: maxLength(3),
      },
       quantite: {
        required,
        maxLength: maxLength(3),
      },
      gender: {
        required,
      },
      email: {
        required,
        email,
      },
    },
  },
  methods: {
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
      this.form.firstName = null;
      this.form.lastName = null;
      this.form.age = null;
      this.form.quantite=null;
      this.form.gender = null;
      this.form.email = null;
    },
    saveUser() {
      this.sending = true;

      // Instead of this timeout, here you can call your API
      window.setTimeout(() => {
        this.lastUser = `${this.form.firstName} ${this.form.lastName}`;
        this.userSaved = true;
        this.sending = false;
        this.clearForm();
      }, 1500);
    },
    validateUser() {
      this.$v.$touch();

      if (!this.$v.$invalid) {
        this.saveUser();
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