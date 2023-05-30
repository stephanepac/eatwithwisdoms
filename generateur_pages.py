import csv


fichier=open('commun.txt','r')
commun=fichier.read()
fichier.close()

def pages_indexe(nom_fichier):
  fichier=open('pages.csv','r')
  reader=csv.reader(fichier,delimiter=";")

  for line in reader:
      if nom_fichier in line:
          fichier.close()
          return True
  fichier.close()
  return False

nom_fichier=input("Entrez un nom de fichier qui sera également le nom de la page : ")+".html"
print("le fichier",nom_fichier,"a été créé")

titre_page=input("Entrez maintenant le titre de la page (espaces possibles) : ")

  
nom_image=input("Entrez le nom de l'image de la page : ")
description=input("Entrez la description de la page : ")

if not pages_indexe(nom_fichier):
  fichier=open("pages.csv","a",encoding="utf-8")
  fichier.write("\n"+nom_fichier+";"+nom_image+";"+titre_page+";"+description)
  fichier.close()

fichier = open(nom_fichier, "w", encoding="utf-8")
fichier.write( 

  commun+"""

<h1>Écoute corporelle : Se reconnecter avec son corps pour une meilleure santé</h1>

  <p>Dans notre vie trépidante, il est facile de se déconnecter de notre corps et de perdre le contact avec les signaux qu'il nous envoie. Cependant, l'écoute corporelle est une pratique essentielle pour notre bien-être et notre santé. En prenant le temps d'écouter et de comprendre les besoins de notre corps, nous pouvons prendre des décisions alimentaires plus éclairées et adopter un mode de vie plus équilibré. Dans cet article, nous allons explorer l'importance de l'écoute corporelle et partager des conseils pratiques pour y parvenir.</p>

  <h2>1. Prendre conscience des signaux de faim et de satiété</h2>
  <p>L'un des aspects clés de l'écoute corporelle est la prise de conscience des signaux de faim et de satiété. Apprenez à reconnaître les sensations de faim et d'appétit, ainsi que les signes de satiété. Écoutez votre corps et mangez lorsque vous avez faim, arrêtez-vous lorsque vous vous sentez rassasié, et évitez de manger simplement par habitude ou par ennui.</p>

  <h2>2. Cultiver une relation saine avec la nourriture</h2>
  <p>L'écoute corporelle implique également de cultiver une relation saine avec la nourriture. Au lieu de se concentrer sur les régimes restrictifs ou les calories, apprenez à écouter les besoins réels de votre corps. Soyez conscient de ce qui vous nourrit réellement, tant sur le plan physique que mental. Choisissez des aliments frais et nutritifs, mais n'oubliez pas de vous faire plaisir de temps en temps avec des aliments que vous aimez.</p>

  <h2>3. Pratiquer la pleine conscience lors des repas</h2>
  <p>La pleine conscience est un outil puissant pour développer l'écoute corporelle. Lorsque vous mangez, concentrez-vous pleinement sur le repas. Évitez les distractions telles que la télévision ou le téléphone, et prenez le temps de savourer chaque bouchée. Soyez attentif aux saveurs, aux textures et aux sensations physiques que vous ressentez pendant le repas.</p>

  <h2>4. Être à l'écoute des besoins émotionnels</h2>
  <p>L'écoute corporelle ne se limite pas seulement aux signaux physiques, mais aussi aux besoins émotionnels. Apprenez à reconnaître les émotions qui influencent votre relation avec la nourriture. Êtes-vous en train de manger par ennui, stress, tristesse ou joie ? Prenez conscience de ces émotions et trouvez des moyens plus sains de les gérer, tels que la pratique de la méditation, de l'exercice physique ou la recherche de soutien auprès de vos proches.</p>

  <p>L'écoute corporelle est une compétence précieuse pour une alimentation saine et une meilleure santé globale. En prenant le temps d'écouter et de comprendre les signaux de notre corps, nous pouvons prendre des décisions alimentaires éclairées, adopter une approche plus équilibrée de la nourriture et cultiver une relation saine avec notre corps. Pratiquez régulièrement l'écoute corporelle et observez les bienfaits qu'elle apporte à votre vie.</p>

  <p>N'oubliez pas, votre corps est votre meilleur guide vers une alimentation nourrissante et une vie équilibrée. Écoutez-le avec bienveillance et faites des choix qui vous soutiennent vraiment. Bonne écoute corporelle !</p>

</body>
</html>
"""
)
fichier.close()