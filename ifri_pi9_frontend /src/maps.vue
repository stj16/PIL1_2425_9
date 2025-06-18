<template>
  <div class="main-container">
    <div class="container">
      <section class="page-section active">
        <div class="card">
          <h2 class="form-title">✚ Publier une demande de covoiturage</h2>

          <form @submit.prevent="submitForm" id="publishForm" class="form">
            <div class="form-group">
              <label class="form-label">Point de Départ</label>
              <div class="input-group">
                <input v-model="formData.departure" type="text" required />
                <button type="button" @click="getCurrentLocation" class="location-btn">
                  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 16 16">
                    <path d="M8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10zm0-7a3 3 0 1 1 0-6 3 3 0 0 1 0 6z"/>
                  </svg>
                  Ma Position
                </button>
              </div>
            </div>

            <div class="form-group">
              <label class="form-label">Point d'Arrivée</label>
              <div class="input-group">
                <input v-model="formData.arrival" type="text" required />
                <button type="button" @click="searchDestination" class="location-btn">
                  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 16 16">
                    <path d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001c.03.04.062.078.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1.007 1.007 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0z"/>
                  </svg>
                  Rechercher
                </button>
              </div>
              <small class="location-note">📍 Cliquez sur la carte ou recherchez une adresse</small>
            </div>

            <div class="map-container">
              <div id="map"></div>
              <div class="map-status" v-show="isMapLoading">
                <div class="loading-spinner"></div>
                <p>Chargement de la carte...</p>
              </div>
            </div>

            <div class="form-row">
              <div class="form-group">
                <label class="form-label">Date et Heure de Départ</label>
                <input v-model="formData.departureTime" type="datetime-local" required />
              </div>
            </div>

            <button type="submit" class="submit-btn"> Publier ma demande</button>
          </form>
        </div>
      </section>
    </div>

    <!-- Modal -->
    <div class="modal" v-show="showModal" @click.self="closeModal">
      <div class="modal-content">
        <span class="close-modal" @click="closeModal">&times;</span>
        <p>{{ modalMessage }}</p>
        <div class="modal-actions">
          <button class="modal-btn confirm" @click="closeModal">OK</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { useRouter } from 'vue-router';

const router = useRouter();
export default {
  name: 'RideForm',
  data() {
    return {
      formData: {
        departure: '',
        arrival: '',
        departureTime: ''
      },
      map: null,
      userMarker: null,
      destinationMarker: null,
      isMapLoading: true,
      showModal: false,
      modalMessage: '',
      defaultLocation: {
        lat: 6.4201,
        lng: 2.3286
      }
    }
  },
  mounted() {
    this.initMap();
  },
  methods: {
    initMap() {
      this.isMapLoading = true;
      
      
      import('leaflet').then(L => {
        this.map = L.map('map').setView([this.defaultLocation.lat, this.defaultLocation.lng], 13);
        
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
          attribution: '© OpenStreetMap contributors'
        }).addTo(this.map);

       
        this.map.on('click', (e) => {
          this.setDestination(e.latlng.lat, e.latlng.lng);
        });

        this.isMapLoading = false;
      }).catch(error => {
        console.error("Erreur de chargement de Leaflet:", error);
        this.isMapLoading = false;
      });
    },
    
    getCurrentLocation() {
      if (!navigator.geolocation) {
        this.showMessage("La géolocalisation n'est pas supportée par votre navigateur");
        return;
      }

      const btn = event.target;
      const originalText = btn.innerHTML;
      btn.innerHTML = '<div class="mini-spinner"></div> Localisation...';
      btn.disabled = true;

      navigator.geolocation.getCurrentPosition(
        position => {
          const { latitude, longitude } = position.coords;
          this.updateUserPosition(latitude, longitude);
          btn.innerHTML = originalText;
          btn.disabled = false;
        },
        error => {
          this.showMessage("Impossible d'obtenir votre position");
          console.error(error);
          btn.innerHTML = originalText;
          btn.disabled = false;
        }
      );
    },
    
    updateUserPosition(lat, lng) {
      import('leaflet').then(L => {
        if (this.userMarker) {
          this.map.removeLayer(this.userMarker);
        }
        
        this.userMarker = L.marker([lat, lng], {
          icon: L.divIcon({
            className: 'user-icon',
            html: '<div style="background:#10B981;color:white;width:36px;height:36px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:16px;border:2px solid white;">📍</div>',
            iconSize: [36, 36]
          })
        }).addTo(this.map);
        
        this.map.setView([lat, lng], 13);
        this.reverseGeocode(lat, lng, 'departure');
      });
    },
    
    setDestination(lat, lng) {
      import('leaflet').then(L => {
        if (this.destinationMarker) {
          this.map.removeLayer(this.destinationMarker);
        }
        
        this.destinationMarker = L.marker([lat, lng], {
          icon: L.divIcon({
            className: 'destination-icon',
            html: '<div style="background:#EF4444;color:white;width:36px;height:36px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:16px;border:2px solid white;">🏁</div>',
            iconSize: [36, 36]
          })
        }).addTo(this.map);
        
        this.reverseGeocode(lat, lng, 'arrival');
      });
    },
    
    searchDestination() {
      if (!this.formData.arrival.trim()) return;
      
      fetch(`https://nominatim.openstreetmap.org/search?format=json&q=${encodeURIComponent(this.formData.arrival)}&limit=1`)
        .then(response => response.json())
        .then(data => {
          if (data && data.length > 0) {
            const result = data[0];
            this.setDestination(result.lat, result.lon);
          } else {
            this.showMessage("Adresse non trouvée");
          }
        })
        .catch(error => {
          console.error("Erreur de géocodage:", error);
          this.showMessage("Erreur de recherche");
        });
    },
    
    reverseGeocode(lat, lng, field) {
      fetch(`https://nominatim.openstreetmap.org/reverse?format=json&lat=${lat}&lon=${lng}&zoom=18&addressdetails=1`)
        .then(response => response.json())
        .then(data => {
          if (data && data.display_name) {
            this.formData[field] = data.display_name;
          } else {
            this.formData[field] = `${lat.toFixed(6)}, ${lng.toFixed(6)}`;
          }
        })
        .catch(error => {
          console.error("Erreur de géocodage inverse:", error);
          this.formData[field] = `${lat.toFixed(6)}, ${lng.toFixed(6)}`;
        });
    },
    
    showMessage(msg) {
      this.modalMessage = msg;
      this.showModal = true;
    },
    
    closeModal() {
      this.showModal = false;
    },
    
    submitForm() {
      console.log("Formulaire soumis:", this.formData);
      
      this.showMessage("Demande publiée avec succès!");
    }
  }
}
</script>

<style>
:root {
  --primary: #10B981;
  --primary-dark: #0E9F6E;
  --secondary: #3B82F6;
  --text-light: #6B7280;
  --border: #E5E7EB;
}

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  background: linear-gradient(180deg, #0a1a2e, #1a3a5a);
  color: var(--text-dark);
  line-height: 1.6;
}

.main-container {
  max-width: 800px;
  margin: 40px auto;
  padding: 0 20px;
}

.container {
  border-radius: 12px;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.05);
   background-color: rgba(241, 235, 235, 0.089);
  backdrop-filter: blur(12px);
}

.card {
  padding: 30px;
}

.form-title {
  text-align: center;
  margin-bottom: 30px;
  font-size: 28px;
  color: var(--primary);
  position: relative;
  padding-bottom: 15px;
}

.form-title:after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 100px;
  height: 4px;
  background: linear-gradient(45deg, var(--primary), var(--secondary));
  border-radius: 2px;
}

.form {
  display: flex;
  flex-direction: column;
  gap: 25px;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.form-label {
  font-weight: 600;
  color: var(--text-dark);
  font-size: 16px;
}

.input-group {
  display: flex;
  gap: 12px;
}

.input-group input {
  flex: 1;
}

input, select, textarea {
  padding: 14px;
  border: 1px solid var(--border);
  border-radius: 8px;
  font-size: 16px;
  transition: all 0.3s;
  width: 100%;
}

input:focus, select:focus, textarea:focus {
  border-color: var(--primary);
  outline: none;
  box-shadow: 0 0 0 3px rgba(16, 185, 129, 0.2);
}

.location-note {
  color: var(--text-light);
  font-size: 14px;
  margin-top: 5px;
  display: flex;
  align-items: center;
  gap: 5px;
}

.map-container {
  position: relative;
  height: 320px;
  border-radius: 10px;
  overflow: hidden;
  margin: 20px 0;
  border: 1px solid var(--border);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
}

#map {
  height: 100%;
  width: 100%;
  z-index: 1;
}

.map-status {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(255, 255, 255, 0.95);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  z-index: 10;
  font-size: 18px;
  color: var(--text-dark);
  font-weight: 500;
  gap: 15px;
}

.loading-spinner {
  border: 4px solid rgba(0, 0, 0, 0.1);
  border-radius: 50%;
  border-top: 4px solid var(--primary);
  width: 50px;
  height: 50px;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.location-btn {
  display: flex;
  align-items: center;
  padding: 0 20px;
  background-color: var(--primary);
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.3s;
  font-weight: 600;
  font-size: 15px;
  white-space: nowrap;
  height: 50px;
}

.location-btn:hover {
  background-color: var(--primary-dark);
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(16, 185, 129, 0.3);
}

.submit-btn {
  padding: 16px;
  background: linear-gradient(45deg, blue, var(--secondary));
  color: white;
  border: none;
  border-radius: 8px;
  font-weight: 600;
  font-size: 18px;
  cursor: pointer;
  transition: all 0.3s;
  margin-top: 15px;
  box-shadow: 0 4px 15px rgba(16, 185, 129, 0.3);
}

.submit-btn:hover {
  transform: translateY(-3px);
  box-shadow: 0 6px 20px rgba(16, 185, 129, 0.4);
}

.modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.7);
  z-index: 1000;
  display: flex;
  align-items: center;
  justify-content: center;
}

.modal-content {
  background: white;
  border-radius: 12px;
  width: 90%;
  max-width: 500px;
  padding: 30px;
  position: relative;
}

.close-modal {
  position: absolute;
  top: 15px;
  right: 20px;
  font-size: 28px;
  color: var(--text-light);
  cursor: pointer;
}

.modal-actions {
  display: flex;
  justify-content: center;
  margin-top: 20px;
}

.modal-btn {
  padding: 12px 30px;
  border: none;
  border-radius: 8px;
  font-weight: 600;
  font-size: 16px;
  cursor: pointer;
}

.modal-btn.confirm {
  background-color: var(--primary);
  color: white;
}
</style>