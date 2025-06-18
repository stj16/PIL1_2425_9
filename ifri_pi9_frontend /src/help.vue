<template>
    <div class="help-page">
        <h1>Aide - GO-IFRI</h1>
        <section>
            <h2>Trouver des offres de covoiturage</h2>
            <ul>
                <li>Utilisez la barre de recherche pour trouver des trajets disponibles selon votre destination et date.</li>
                <li>Filtrez les résultats selon vos préférences (prix, heure, conducteur, etc.).</li>
                <li>Cliquez sur une offre pour voir les détails et contacter le conducteur.</li>
            </ul>
        </section>

        <section>
            <h2>Proposer une offre de covoiturage</h2>
            <ul>
                <li>Accédez à la section "Proposer une offre".</li>
                <li>Remplissez les informations du trajet (départ, arrivée, date, nombre de places, prix, etc.).</li>
                <li>Publiez votre offre pour la rendre visible aux autres utilisateurs.</li>
            </ul>
        </section>

        <section>
            <h2>Gérer votre profil</h2>
            <ul>
                <li>Accédez à votre profil via le menu utilisateur.</li>
                <li>Modifiez vos informations personnelles et vos préférences.</li>
                <li>Ajoutez une photo de profil pour plus de confiance.</li>
            </ul>
        </section>

        <section>
            <h2>Envoyer et recevoir des messages</h2>
            <ul>
                <li>Utilisez la messagerie intégrée pour communiquer avec les conducteurs ou passagers.</li>
                <li>Consultez vos messages dans la section "Messages".</li>
                <li>Répondez rapidement pour organiser votre covoiturage.</li>
            </ul>
        </section>

        <section>
            <h2>Autres possibilités</h2>
            <ul>
                <li>Consultez l’historique de vos trajets.</li>
                <li>Laissez des avis sur les conducteurs ou passagers.</li>
                <li>Recevez des notifications pour les nouvelles offres ou messages.</li>
            </ul>
        </section>
    </div>
</template>

<script setup>

</script>

<style scoped>
.help-page {
    max-width: 800px;
    margin: 2rem auto;
    padding: 2rem;
    background: #f9f9f9;
    border-radius: 12px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.05);
}
h1 {
    color: #2c3e50;
    margin-bottom: 1.5rem;
}
section {
    margin-bottom: 2rem;
}
h2 {
    color: #2980b9;
    margin-bottom: 0.5rem;
}
ul {
    padding-left: 1.5rem;
}
li {
    margin-bottom: 0.5rem;
}
</style>