import{ createRouter, createWebHistory } from 'vue-router';
import Acceuil from '../acceuil.vue';
import Connexion from '../connexion.vue';
import Maps from '../maps.vue';
import Welcome from '../Welcome.vue';



const routes = [
    {path:'/', component: Acceuil},
    {path:'/acceuil', component: Acceuil},
    {path:'/connexion', component: Connexion},
    {path:'/maps', component: Maps},
    {path:'/welcome', component: Welcome},
    
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});
export default router;

