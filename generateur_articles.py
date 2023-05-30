import csv

fichier=open("commun.txt","r")
commun=fichier.read()
fichier.close()

pages=""
fichier=open("pages.csv","r")
reader=csv.reader(fichier,delimiter=";")  
for ligne in reader:
    pages+=f"""
    <div class="card centrer" style="width: 18rem;float:left;">
  <img src="{ligne[1]}" class="card-img-top" alt="...">
  <div class="card-body">
    <h5 class="card-title">{ligne[2]}</h5>
    <p class="card-text">{ligne[3]}</p>
    <a href="{ligne[0]}" class="btn btn-primary">Bien se nourrir</a>
  </div>
</div>
    """

fichier = open("articles.html", "w")
fichier.write( 
f"""
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ENjdO4Dr2bkBIFxQpeoTz1HIcje39Wm4jDKdf19U8gI4ddQ3GYNS7NTKfAdVQSZe" crossorigin="anonymous"></script>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KK94CHFLLe+nY2dmCWGMq91rCGa5gtU4mk92HdvYe+M/SXH301p5ILy+dN9+nJOZ" crossorigin="anonymous">
    <title>Eatwithwisdom Articles</title>

    {commun}
    {pages}
</body>
</html>
"""
)
fichier.close()