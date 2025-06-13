<template>
  <div class="home-page">
    <!-- Barre de navigation -->
    <nav class="navbar">
      <div class="logo">
        <i class="fas fa-car"></i>
        <span>IFRI Covoiturage</span>
      </div>
      <div class="nav-buttons" @submit.prevent="Connexion">
        <router-link to="/connexion"><button class="btn-login"  type="submit">Connexion</button></router-link>
        <button class="btn-register" type="submit">S'inscrire</button>
      </div>
    </nav>

    <!-- Hero Section -->
    <section class="hero">
      <div class="hero-content">
        <h1>
          <i class="fas fa-car"></i> IFRI Covoiturage
        </h1>
        <p class="tagline">Voyagez malin, économisez ensemble !</p>
        
      </div>
      <div class="hero-image">
        <img src="">
      </div>
    </section>

    <!-- Avantages -->
    <section class="benefits">
      <h2>Pourquoi choisir IFRI Covoiturage ?</h2>
      <div class="benefits-grid">
        <div class="benefit-card">
          <i class="fas fa-wallet"></i>
          <h3>Économique</h3>
          <p>Partagez les frais de voyage et réduisez vos dépenses jusqu'à 75%.</p>
        </div>
        <div class="benefit-card">
          <i class="fas fa-leaf"></i>
          <h3>Écologique</h3>
          <p>Moins de voitures sur la route, c'est moins de pollution pour notre planète.</p>
        </div>
        <div class="benefit-card">
          <i class="fas fa-users"></i>
          <h3>Communautaire</h3>
          <p>Rencontrez des personnes partageant le même trajet que vous.</p>
        </div>
        <div class="benefit-card">
          <i class="fas fa-shield-alt"></i>
          <h3>Sécurisé</h3>
          <p>Profils vérifiés et système de notation pour voyager en toute confiance.</p>
        </div>
      </div>
    </section>

    <!-- Trajets populaires -->
    <section class="popular-routes">
      <h2>Trajets populaires</h2>
      <div class="routes-grid">
        <div class="route-card">
          <div class="route-info">
            <h3>Cotonou → Calavi</h3>
            <p><i class="fas fa-clock"></i> 6h30 - <i class="fas fa-calendar-alt"></i> Départ quotidien</p>
            <p><i class="fas fa-user-friends"></i> 3 places disponibles</p>
          </div>
          <div class="route-price">
            <span>800 FCFA</span>
            <button class="btn-book">Réserver</button>
          </div>
        </div>
        <div class="route-card">
          <div class="route-info">
            <h3>Calavi →  Ouidah</h3>
            <p><i class="fas fa-clock"></i> 4h15 - <i class="fas fa-calendar-alt"></i> Départ quotidien</p>
            <p><i class="fas fa-user-friends"></i> 2 places disponibles</p>
          </div>
          <div class="route-price">
            <span>4 500 FCFA</span>
            <button class="btn-book">Réserver</button>
          </div>
        </div>
        <div class="route-card">
          <div class="route-info">
            <h3>Arconville → Calavi</h3>
            <p><i class="fas fa-clock"></i> 19h - <i class="fas fa-calendar-alt"></i> Départ demain</p>
            <p><i class="fas fa-user-friends"></i> 4 places disponibles</p>
          </div>
          <div class="route-price">
            <span>450 FCFA</span>
            <button class="btn-book">Réserver</button>
          </div>
        </div>
      </div>
    </section>

    <!-- Témoignages -->
    <section class="testimonials">
      <marquee behavior="" direction=""><h2 style="font-weight: bolder;">Ce que nos utilisateurs disent :</h2></marquee>
      <div class="testimonial-grid">
        <div class="testimonial-card">
          <div class="testimonial-text">
            <p>"IFRI Covoiturage m'a permis de réduire mes frais de transport tout en faisant des rencontres intéressantes 💑."</p>
          </div>
          <div class="testimonial-author">
            <img src="https://randomuser.me/api/portraits/women/44.jpg" alt="Aminata">
            <span>Bénita A.</span>
          </div>
        </div>
        <div class="testimonial-card">
          <div class="testimonial-text">
            <p>"Simple, efficace et économique😁. Je l'utilise tous les jours pour aller au cours👌."</p>
          </div>
          <div class="testimonial-author">
            <img src="https://randomuser.me/api/portraits/men/32.jpg" alt="Jean">
            <span>Gaby D.</span>
          </div>
        </div>
      </div>
    </section>

    <!-- Footer -->
    <footer class="site-footer">
      <div class="footer-content">
        <div class="footer-section about">
          <h3 style="text-decoration: underline;">IFRI Covoiturage</h3>
          <p>La solution intelligente pour vos déplacements en Côte d'Ivoire.</p>
          <div class="socials" style="margin-left: 7rem;">
            <a href="#"><i class="fab fa-facebook-f"></i></a>
            <a href="#"><i class="fab fa-twitter"></i></a>
            <a href="#"><i class="fab fa-instagram"></i></a>
            <a href="#"><i class="fab fa-linkedin-in"></i></a>
          </div>
        </div>
        <div class="footer-section links">
          <h3 style="text-decoration: underline;">Liens rapides</h3>
          <ul>
            <li><a href="#">Accueil</a></li>
            <li><a href="#">Trajets</a></li>
            <li><a href="#">Comment ça marche</a></li>
            <li><a href="#">Tarifs</a></li>
            <li><a href="#">Contact</a></li>
          </ul>
        </div>
        <div class="footer-section contact">
          <h3 style="margin-left: -12rem; text-decoration: underline;">Contactez-nous </h3>
          <p><i class="fas fa-map-marker-alt"></i> Calavi, Cotonou</p>
          <p><i class="fas fa-phone"></i> +225 XX XX XX XX</p>
          <p><i class="fas fa-envelope"></i> contact@ifricovoiturage.ci</p>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; 2025 IFRI Covoiturage. Tous droits réservés.</p>
      </div>
    </footer>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router';

const router = useRouter();
function Connexion(){
  router.push({name: 'login'})
}

</script>

<style scoped>
/* Import Font Awesome */
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css');

/* Styles de base */
.home-page {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  color: white;
  background: linear-gradient(135deg, #0a1a2e, #1a3a5a,rgb(2, 81, 2),rgb(137, 62, 1)80%);
  min-height: 100vh;
  margin-left: 0;
  margin-right: 0;
}

/* Navbar */
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 5%;
  background-color: rgba(10, 26, 46, 0.9);
  position: sticky;
  top: 0;
  z-index: 100;
}

.logo {
  display: flex;
  align-items: center;
  font-size: 1.5rem;
  font-weight: bold;
}

.logo i {
  margin-right: 10px;
  color: #4fc3f7;
}

.nav-buttons button {
  padding: 0.5rem 1.5rem;
  margin-left: 1rem;
  border-radius: 20px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
}

.btn-login {
  background: transparent;
  border: 2px solid #fff;
  color: #4fc3f7;
}

.btn-login:hover {
  background: #4fc3f7;
  color: #0a1a2e;
}

.btn-register {
  background: transparent;
  border: 4px dashed #4fc3f7;
  color: red;

}

.btn-register:hover {
  background: #3fb3e7;
  border-color: #3fb3e7;
}

/* Hero Section */
.hero {
  display: flex;
  align-items: center;
  padding: 3rem 5%;
  min-height: 70vh;
}

.hero-content {
  flex: 1;
  padding-right: 3rem;
}

.hero-image {
  flex: 1;
}

.hero-image img {
  width: 100%;
  border-radius: 10px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
}

.hero h1 {
  font-size: 3rem;
  margin-bottom: 1rem;
}

.hero h1 i {
  color: #4fc3f7;
}

.tagline {
  font-size: 1.5rem;
  margin-bottom: 2rem;
  color: #a1c4fd;
}

.search-box {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
  margin-bottom: 2rem;
}

.search-box input {
  flex: 1;
  min-width: 200px;
  padding: 0.8rem 1rem;
  border-radius: 5px;
  border: none;
  background-color: rgba(255, 255, 255, 0.9);
  color: #0a1a2e;
}

.btn-search {
  background: #4fc3f7;
  color: #0a1a2e;
  border: none;
  padding: 0.8rem 2rem;
  border-radius: 5px;
  font-weight: bold;
  cursor: pointer;
  transition: background 0.3s ease;
}

.btn-search:hover {
  background: #3fb3e7;
}

/* Benefits Section */
.benefits {
  padding: 4rem 5%;
  text-align: center;
}

.benefits h2 {
  font-size: 2rem;
  margin-bottom: 3rem;
}

.benefits-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 2rem;
}

.benefit-card {
  background: rgba(255, 255, 255, 0.1);
  padding: 2rem;
  border-radius: 10px;
  transition: transform 0.3s ease;
}

.benefit-card:hover {
  transform: translateY(-10px);
}

.benefit-card i {
  font-size: 2.5rem;
  color: #4fc3f7;
  margin-bottom: 1rem;
}

.benefit-card h3 {
  margin: 1rem 0;
  font-size: 1.3rem;
}

/* Popular Routes */
.popular-routes {
  padding: 4rem 5%;
}

.popular-routes h2 {
  text-align: center;
  font-size: 2rem;
  margin-bottom: 3rem;
}

.routes-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1.5rem;
}

.route-card {
  background: rgba(255, 255, 255, 0.1);
  border-radius: 10px;
  padding: 1.5rem;
  display: flex;
  justify-content: space-between;
  transition: transform 0.3s ease;
}

.route-card:hover {
  transform: translateY(-5px);
}

.route-info h3 {
  margin-bottom: 0.5rem;
}

.route-info p {
  margin: 0.5rem 0;
  color: #a1c4fd;
  font-size: 0.9rem;
}

.route-info i {
  margin-right: 5px;
  color: #4fc3f7;
}

.route-price {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  justify-content: space-between;
}

.route-price span {
  font-size: 1.3rem;
  font-weight: bold;
  color: #4fc3f7;
}

.btn-book {
  background: #4fc3f7;
  color: #0a1a2e;
  border: none;
  padding: 0.5rem 1.5rem;
  border-radius: 20px;
  font-weight: bold;
  cursor: pointer;
  transition: background 0.3s ease;
}

.btn-book:hover {
  background: #3fb3e7;
}

/* Testimonials */
.testimonials {
  padding: 4rem 5%;
}

.testimonials h2 {
  text-align: center;
  font-size: 2rem;
  margin-bottom: 3rem;
}

.testimonial-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
}

.testimonial-card {
  background: rgba(255, 255, 255, 0.1);
  border-radius: 10px;
  padding: 2rem;
}

.testimonial-text {
  font-style: italic;
  margin-bottom: 1.5rem;
}

.testimonial-author {
  display: flex;
  align-items: center;
}

.testimonial-author img {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  margin-right: 1rem;
  object-fit: cover;
}

/* Footer */
.site-footer {
  background: rgb(0, 0, 0);
  color: rgb(252, 252, 252);
  padding: 3rem 0 0;
  margin-top: 3rem;
}

.footer-content {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 2rem;
  padding: 0 5%;
}

.footer-section {
  margin-bottom: 2rem;
}

.footer-section h3 {
  margin-bottom: 1.5rem;
  color: #4fc3f7;
}

.footer-section.about p {
  margin-bottom: 1rem;
}

.socials {
  display: flex;
  gap: 1rem;
}

.socials a {
  color: white;
  font-size: 1.2rem;
  transition: color 0.3s ease;
}

.socials a:hover {
  color: #4fc3f7;
}

.footer-section.links ul {
  list-style: none;
}

.footer-section.links li {
  margin-bottom: 0.8rem;
}

.footer-section.links a {
  color: white;
  text-decoration: none;
  transition: color 0.3s ease;
}

.footer-section.links a:hover {
  color: #4fc3f7;
}

.footer-section.contact p {
  display: flex;
  align-items: center;
  margin-bottom: 0.8rem;
}

.footer-section.contact i {
  margin-right: 10px;
  color: #4fc3f7;
}

.footer-bottom {
  text-align: center;
  padding: 1.5rem;
  background: #2a1f1f;
  margin-top: 2rem;
}

/* Responsive */
@media (max-width: 768px) {
  .hero {
    flex-direction: column;
    text-align: center;
  }
  
  .hero-content {
    padding-right: 0;
    margin-bottom: 2rem;
  }
  
  .search-box {
    justify-content: center;
  }
  
  .navbar {
    flex-direction: column;
    padding: 1rem;
  }
  
  .nav-buttons {
    margin-top: 1rem;
  }
}
</style>
