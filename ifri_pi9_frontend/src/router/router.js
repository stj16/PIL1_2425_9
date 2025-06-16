import{ createRouter, createWebHistory } from 'vue-router';
import Acceuil from '../acceuil.vue';
import Connexion from '../connexion.vue';



const routes = [
    {path:'/', component: Acceuil},
    {path:'/acceuil', component: Acceuil},
    {path:'/connexion', component: Connexion},
    
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});
export default router;

