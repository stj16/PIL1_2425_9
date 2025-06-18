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
          <label for="nom">Nom</label>
          <input type="text" id="nom" v-model="form.nom" required />
        </div>

        <div class="form-group">
          <label for="prenom">Prénom</label>
          <input type="text" id="prenom" v-model="form.prenom" required />
        </div>

        <div class="form-group">
          <label for="email">Email</label>
          <input type="email" id="email" v-model="form.email" required />
        </div>

        <div class="form-group">
          <label for="phone_number">Téléphone</label>
          <input type="tel" id="phone_number" v-model="form.phone_number" />
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
            <input type="text" id="vehicleName" v-model="form.vehicleName" />
          </div>
          <div class="form-group">
            <label for="serialNumber">Numéro de série</label>
            <input type="text" id="serialNumber" v-model="form.serialNumber" />
          </div>
          <div class="form-group">
            <label for="brand">Marque de voiture</label>
            <input type="text" id="brand" v-model="form.brand" />
          </div>
          <div class="form-group">
            <label for="color">Couleur</label>
            <input type="text" id="color" v-model="form.color" />
          </div>
          <div class="form-group">
            <label for="plateNumber">Numéro d'immatriculation</label>
            <input type="text" id="plateNumber" v-model="form.plateNumber" />
          </div>
        </div>

        <button type="submit" :disabled="loading">
          {{ loading ? 'Enregistrement...' : 'Enregistrer' }}
        </button>
        
        <p v-if="message" :class="{ success: success, error: !success }">{{ message }}</p>
      </form>
    </div>
  </body>
</template>

<script>
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";
import { getUserProfile, updateUserProfile, uploadFile } from "@/api";

const router = useRouter();

export default {
  name: "EditProfil",
  data() {
    return {
      form: {
        nom: "",
        prenom: "",
        email: "",
        phone_number: "",
        role: "",
        vehicleName: "",
        serialNumber: "",
        brand: "",
        color: "",
        plateNumber: "",
      },
      profilePic: null,
      profilePicUrl: "",
      loading: false,
      message: "",
      success: false
    };
  },
  async mounted() {
    try {
      const response = await getUserProfile();
      const userData = response.data;
      
      this.form = {
        nom: userData.nom || "",
        prenom: userData.prenom || "",
        email: userData.email || "",
        phone_number: userData.phone_number || "",
        role: userData.role || "",
        vehicleName: userData.vehicleName || "",
        serialNumber: userData.serialNumber || "",
        brand: userData.brand || "",
        color: userData.color || "",
        plateNumber: userData.plateNumber || "",
      };
      
      if (userData.photo) {
        this.profilePicUrl = userData.photo;
      }
    } catch (error) {
      console.error('Erreur chargement profil:', error);
      this.message = "Erreur lors du chargement du profil";
      this.success = false;
    }
  },
  methods: {
    onFileChange(e) {
      const file = e.target.files[0];
      if (file) {
        this.profilePic = file;
        this.profilePicUrl = URL.createObjectURL(file);
      }
    },
    async submitForm() {
      this.loading = true;
      this.message = "";
      
      try {
        // Upload de la photo si elle a été modifiée
        if (this.profilePic) {
          const uploadResponse = await uploadFile(this.profilePic, 'photo');
          this.form.photo = uploadResponse.data.url;
        }
        
        // Mise à jour du profil
        await updateUserProfile(this.form);
        
        this.message = "Profil mis à jour avec succès !";
        this.success = true;
        
        // Redirection vers le profil après 2 secondes
        setTimeout(() => {
          router.push('/profil');
        }, 2000);
        
      } catch (error) {
        console.error('Erreur mise à jour profil:', error);
        this.message = error.response?.data?.detail || "Erreur lors de la mise à jour du profil";
        this.success = false;
      } finally {
        this.loading = false;
      }
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