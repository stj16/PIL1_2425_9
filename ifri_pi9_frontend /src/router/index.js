import{ createRouter, createWebHistory } from "vue-router";

const routes = [
    {
        path: '/',
        redirect: '/acceuil'
    },
    {
        path: '/acceuil',
        name: 'acceuil',
        component: () => import('../acceuil.vue')
    },
    {
        path: '/connexion',
        name: 'connexion',
        component: () => import('../connexion.vue')
    },
    {
        path: '/welcome',
        name: 'welcome',
        component: () => import('../Welcome.vue')
    },
    {
        path: '/offre_demende',
        name: 'offre_demende',
        component: () => import('../offre_demende.vue')
    },
    {
        path: '/messagerie',
        name: 'messagerie',
        component: () => import('../messagerie.vue')
    },
    {
        path: '/profil',
        name: 'profil',
        component: () => import('../profil.vue')
    },
    {
        path: '/editprofil',
        name: 'editprofil',
        component: () => import('../editprofil.vue')
    },
    {
        path: '/notifications',
        name: 'notifications',
        component: () => import('../notifications.vue')
    },
    {
        path: '/motdepasseoublier',
        name: 'motdepasseoublier',
        component: () => import('../motdepasseoublier.vue')
    },
    {
        path: '/renitialisation',
        name: 'renitialisation',
        component: () => import('../renitialisation.vue')
    },
    {
        path: '/about',
        name: 'about',
        component: () => import('../about.vue')
    },
    {
        path: '/deconnexion',
        name: 'deconnexion',
        component: () => import('../deconnexion.vue')
    },
    {
        path: '/parametre',
        name: 'parametre',
        component: () => import('../parametre.vue')
    },
    {
        path: '/authentification',
        name: 'authentification',
        component: () => import('../authentification.vue')
    },
    {
        path: '/pwd',
        name: 'pwd',
        component: () => import('../pwd.vue')
    },
    {
        path: '/help',
        name: 'help',
        component: () => import('../help.vue')
    },
    {
        path: '/maps',
        name: 'maps',
        component: () => import('../maps.vue')
    }
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;

