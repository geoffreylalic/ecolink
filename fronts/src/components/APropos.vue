<template>

    <div class="md-layout">
        <div class="md-layout-item apropos">
            <h1>À propos</h1>
            <p>Les entreprises produisent des déchets qui polluent notre planète et ne sont pas réutilisés. Lors d’une production, chaque entreprise gaspille énormément de matières premières, seulement la moitié des matières premières sont recyclées. La plupart sont généralement jetés à la déchetterie, ainsi les entreprises dépensent de l’argent pour jeter leur surplus</p>
        </div>

        <div class="md-layout-item apropos">
            <h1>Notre équipe</h1>
            <img width="200" src="../assets/equipe.jpg">
            <p class="description">Wajdi GAIECH, Paul BUREL, Rémy NGUYEN, Ayoub BENALLAL, Geoffrey LALIC</p>
            <p></p>
        </div>
    </div>  
  
   </template>
  <script>
  
  export default {
    name: 'APropos',
    props: {
      msg: String
    }
  }
  </script>
  
  <!-- Add "scoped" attribute to limit CSS to this component only -->
  <style scoped>
  
  .apropos {
      margin-top: 5em;
      margin-left: 2.5em;
      margin-right: 2.5em;
      margin-bottom: 1em;
      padding: 4%;
      background-color: white;
      border-radius: 10px;
      align-items: center;
  }

  .description{
    font-size: 1em;
    font-style: italic;
  }

  </style>
  