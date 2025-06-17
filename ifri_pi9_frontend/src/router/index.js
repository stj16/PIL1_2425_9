import{ createRouter, createWebHistory } from "vue-router";
const routes = [
    {
        path:'',
        redirect:{ name: 'acceuil'},
        children: [
            {
                path:'acceuil',
                name: 'acceuil',
                component: () => import ('../acceuil.vue'),

            },
        ],
    },
    {
        path:'',
        redirect:{ name: 'connexion'},
        children: [
            {
                path:'connexion',
                name: 'connexion',
                component: () => import ('../connexion.vue'),

            },
        ],
        
    },

    {
        path:'',
        redirect:{ name: 'profil'},
        children: [
            {
                path:'profil',
                name: 'profil',
                component: () => import ('../profil.vue'),

            },
        ],
        
    },
    {
        path:'',
        redirect:{ name: 'editprofil'},
        children: [
            {
                path:'editprofil',
                name: 'editprofil',
                component: () => import ('../editprofil.vue'),

            },
        ],
        
    },
    {
        path:'',
        redirect:{ name: 'notifications'},
        children: [
            {
                path:'notifications',
                name: 'notifications',
                component: () => import ('../notifications.vue'),

            },
        ],
        
    },
    {
        path:'',
        redirect:{ name: 'motdepasseoublier'},
        children: [
            {
                path:'motdepasseoublier',
                name: 'motdepasseoublier',
                component: () => import ('../motdepasseoublier.vue'),

            },
        ],
        
    },
    {
        path:'',
        redirect:{ name: 'offre_demende'},
        children: [
            {
                path:'offre_demende',
                name: 'offre_demende',
                component: () => import ('../offre_demende.vue'),

            },
        ],
        
    },
    {
        path:'',
        redirect:{ name: 'messagerie'},
        children: [
            {
                path:'messagerie',
                name: 'messagerie',
                component: () => import ('../messagerie.vue'),

            },
        ],
        
    },
    {
        path:'',
        redirect:{ name: 'renitialisation'},
        children: [
            {
                path:'renitialisation',
                name: 'renitialisation',
                component: () => import ('../renitialisation.vue'),

            },
        ],
        
    },
    {
        path:'',
        redirect:{ name: 'about'},
        children: [
            {
                path:'about',
                name: 'about',
                component: () => import ('../about.vue'),

            },
        ],
        
    },
    {
        path:'',
        redirect:{ name: 'deconnexion'},
        children: [
            {
                path:'deconnexion',
                name: 'deconnexion',
                component: () => import ('../deconnexion.vue'),

            },
        ],
        
    },
    {
        path:'',
        redirect:{ name: 'parametre'},
        children: [
            {
                path:'parametre',
                name: 'parametre',
                component: () => import ('../parametre.vue'),

            },
        ],
        
    },
    {
        path:'',
        redirect:{ name: 'Welcome'},
        children: [
            {
                path:'Welcome',
                name: 'Welcome',
                component: () => import ('../Welcome.vue'),

            },
        ],
        
    },
    {
        path:'',
        redirect:{ name: 'authentification'},
        children: [
            {
                path:'authentification',
                name: 'authentification',
                component: () => import ('../authentification.vue'),

            },
        ],
        
    },
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});
export default router;

