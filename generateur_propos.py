fichier=open("commun.txt","r")
commun=fichier.read()
fichier.close()

fichier = open("a_propos.html", "w", encoding="utf-8")
fichier.write( 

  commun+"""
  <section class="section">
  <div class="container">
    <h2>À propos de EatWithWisdom</h2>
    <p>EatWithWisdom est un blog dédié à l'alimentation intuitive et à la promotion d'une relation saine avec la nourriture.</p>
    <p>Nous croyons en l'idée de manger en écoutant nos signaux internes et en accordant une attention particulière à nos besoins physiques et émotionnels. Notre objectif est d'aider les gens à développer une conscience de leur corps, à abandonner les régimes restrictifs et à cultiver une alimentation équilibrée basée sur l'écoute de leurs propres sensations alimentaires.</p>
    <p>Sur ce blog, vous trouverez des articles informatifs, des conseils pratiques, des recettes savoureuses et des témoignages inspirants de personnes qui ont adopté l'alimentation intuitive dans leur vie quotidienne.</p>
    <p>Rejoignez-nous dans ce voyage vers une relation saine et épanouissante avec la nourriture.</p>
    
    <h2>À propos de l'auteur</h2>
    <p>Je m'appelle Jeanne et je suis passionnée par la nutrition et le bien-être. En tant que défenseur de l'alimentation intuitive, j'ai personnellement découvert les bienfaits de cette approche et je souhaite partager mes connaissances et mon expérience avec vous.</p>
    <p>Mon objectif est de vous fournir des informations précieuses et des ressources pratiques pour vous aider à explorer l'alimentation intuitive, à comprendre les concepts clés et à mettre en pratique ces principes dans votre vie quotidienne.</p>
    <p>Je suis convaincue que chacun de nous possède la sagesse interne nécessaire pour prendre des décisions alimentaires éclairées et trouver un équilibre qui nous convient. Je suis ravie de vous accompagner dans votre voyage vers une relation plus consciente avec la nourriture.</p>
  </div>
</section>

  </body>
</html>
"""
)
fichier.close()