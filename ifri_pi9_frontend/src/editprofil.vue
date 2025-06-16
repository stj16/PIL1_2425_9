<template>
  <div class="profile-editor-overlay">
    <div class="profile-editor">
      <h2>Modifier le profil</h2>
      
      <form @submit.prevent="handleSubmit">
         <div class="form-group">
          <label>photo</label>
          <input type="file"  required >
          
        </div>
        <div class="form-group">
          <label>Nom complet</label>
          <input type="text" v-model="formData.name" required>
        </div>
        
        <div class="form-group">
          <label>Bio</label>
          <textarea v-model="formData.bio" rows="3"></textarea>
        </div>
        
        <div class="form-group">
          <label>Email</label>
          <input type="email" v-model="formData.email" required>
        </div>
        
        <div class="form-group">
          <label>Téléphone</label>
          <input type="tel" v-model="formData.phone">
        </div>
        
        <div class="form-group">
          <label>Localisation</label>
          <input type="text" v-model="formData.location">
        </div>
        
        <div class="form-actions">
          <button type="button" class="cancel-btn" @click="$emit('cancel')">Annuler</button>
          <button type="submit" class="save-btn">Enregistrer</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const props = defineProps({
  user: {
    type: Object,
    required: true
  }
})

const emit = defineEmits(['save', 'cancel'])

const formData = ref({
  name: '',
  bio: '',
  email: '',
  phone: '',
  location: ''
})

onMounted(() => {
  formData.value = { ...props.user }
})

const handleSubmit = () => {
  emit('save', formData.value)
}
</script>

<style scoped>
.profile-editor-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
}

.profile-editor {
  background-color: white;
  border-radius: 10px;
  padding: 2rem;
  width: 100%;
  max-width: 500px;
  max-height: 90vh;
  overflow-y: auto;
}

.dark-theme .profile-editor {
  background-color: #2d2d2d;
}

.profile-editor h2 {
  margin-top: 0;
  margin-bottom: 1.5rem;
  text-align: center;
}

.form-group {
  margin-bottom: 1.5rem;
}

.form-group label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: 500;
}

.form-group input,
.form-group textarea {
  width: 100%;
  padding: 0.75rem;
  border: 1px solid #ddd;
  border-radius: 5px;
  font-family: inherit;
}

.dark-theme .form-group input,
.dark-theme .form-group textarea {
  background-color: #3d3d3d;
  border-color: #555;
  color: #f0f0f0;
}

.form-actions {
  display: flex;
  justify-content: flex-end;
  gap: 1rem;
  margin-top: 2rem;
}

.cancel-btn {
  background-color: #f5f5f5;
  color: #333;
  border: none;
  padding: 0.75rem 1.5rem;
  border-radius: 5px;
  cursor: pointer;
  font-weight: 500;
}

.dark-theme .cancel-btn {
  background-color: #4d4d4d;
  color: #f0f0f0;
}

.save-btn {
  background-color: #4a6bff;
  color: white;
  border: none;
  padding: 0.75rem 1.5rem;
  border-radius: 5px;
  cursor: pointer;
  font-weight: 500;
}
</style>