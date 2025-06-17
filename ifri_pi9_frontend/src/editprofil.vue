<template>
  <body>
    <div class="edit-profile">
      <h2>Éditer le profil</h2>
      <form @submit.prevent="submitForm">
        <div class="profile-picture">
          <label for="profilePic">Photo de profil</label>
          <input type="file" id="profilePic" accept="image/*" @change="onFileChange" />
          <img v-if="profilePicUrl" :src="profilePicUrl" alt="Photo de profil" class="preview" />
        </div>

        <div class="form-group">
          <label for="name">Nom</label>
          <input type="text" id="name" v-model="form.name" required />
        </div>

        <div class="form-group">
          <label for="email">Email</label>
          <input type="email" id="email" v-model="form.email" required />
        </div>

        <div class="form-group">
          <label>Rôle</label>
          <select v-model="form.role" required>
            <option disabled value="">Sélectionnez un rôle</option>
            <option value="conducteur">Conducteur</option>
            <option value="passager">Passager</option>
          </select>
        </div>

        <div v-if="form.role === 'conducteur'" class="driver-fields">
          <div class="form-group">
            <label for="vehicleName">Nom du véhicule</label>
            <input type="text" id="vehicleName" v-model="form.vehicleName" required />
          </div>
          <div class="form-group">
            <label for="serialNumber">Numéro de série</label>
            <input type="text" id="serialNumber" v-model="form.serialNumber" required />
          </div>
          <div class="form-group">
            <label for="brand">Marque de voiture</label>
            <input type="text" id="brand" v-model="form.brand" required />
          </div>
          <div class="form-group">
            <label for="color">Couleur</label>
            <input type="text" id="color" v-model="form.color" required />
          </div>
          <div class="form-group">
            <label for="plateNumber">Numéro d'immatriculation</label>
            <input type="text" id="plateNumber" v-model="form.plateNumber" required />
          </div>
        </div>

        <router-link to="/profil"><button type="submit">Enregistrer</button></router-link>
      </form>
    </div>
  </body>
</template>

<script>
import { ref } from "vue";
import { useRouter } from "vue-router";
const router = useRouter();
export default {
  name: "EditProfil",
  data() {
    return {
      form: {
        name: "",
        email: "",
        role: "",
        vehicleName: "",
        serialNumber: "",
        brand: "",
        color: "",
        plateNumber: "",
      },
      profilePic: null,
      profilePicUrl: "",
    };
  },
  methods: {
    onFileChange(e) {
      const file = e.target.files[0];
      if (file) {
        this.profilePic = file;
        this.profilePicUrl = URL.createObjectURL(file);
      }
    },
    submitForm() {
      if (
        this.form.role === "conducteur" &&
        (!this.form.vehicleName ||
          !this.form.serialNumber ||
          !this.form.brand ||
          !this.form.color ||
          !this.form.plateNumber)
      ) {
        alert("Veuillez remplir tous les champs du conducteur.");
        return;
      }
      alert("Profil mis à jour !");
    },
  },
};
</script>

<style scoped>
body {
  padding-top: 5rem;
  background: linear-gradient(180deg, #0a1a2e, #1a3a5a);
  min-height: 100vh;
  margin: 0;
}
.edit-profile {
  max-width: 500px;
  margin: 2rem auto;
  padding: 2rem;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 20px;
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.15);
  box-sizing: border-box;
}
.profile-picture {
  margin-bottom: 1rem;
}
.profile-picture .preview {
  display: block;
  margin-top: 0.5rem;
  width: 100px;
  height: 100px;
  object-fit: cover;
  border-radius: 50%;
  border: 2px solid #eee;
}
.form-group {
  margin-bottom: 1rem;
}
label {
  display: block;
  margin-bottom: 0.3rem;
  font-weight: 500;
  color: orangered;
}
input, select {
  width: 100%;
  padding: 0.5rem;
  border-radius: 4px;
  border: 1px solid #ccc;
  box-sizing: border-box;
}
button {
  background: #1877f2;
  color: #fff;
  border: none;
  padding: 0.7rem 1.5rem;
  border-radius: 4px;
  cursor: pointer;
  font-size: 1rem;
}
button:hover {
  background: #145db2;
}
.driver-fields {
  background: rgba(255, 255, 255, 0.1);
  padding: 1rem;
  border-radius: 6px;
  margin-bottom: 1rem;
  border: 1px solid rgba(255, 255, 255, 0.1);
}
h2 {
  text-align: center;
  color: blue;
  font-size: 2.5rem;
}

/* Responsivité */
@media (max-width: 600px) {
  .edit-profile {
    max-width: 98vw;
    padding: 1rem;
    margin: 1rem auto;
    border-radius: 12px;
  }
  h2 {
    font-size: 1.5rem;
  }
  .profile-picture .preview {
    width: 70px;
    height: 70px;
  }
  button {
    width: 100%;
    padding: 0.7rem 0;
    font-size: 1rem;
  }
  .driver-fields {
    padding: 0.5rem;
  }
  input, select {
    font-size: 1rem;
    padding: 0.4rem;
  }
}
</style>