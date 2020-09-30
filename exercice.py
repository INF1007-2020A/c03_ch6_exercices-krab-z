#Écrire un programme qui vérifie sur une liste contient des doublons, c’est-à-dire si la liste ne contient que des éléments uniques.
#Écrire un programme qui calcule la moyenne des notes rentrées dans un dictionnaire ayant pour clés le nom des étudiants. Par la suite, le programme doit retourner le nom de l’étudiant ayant la meilleure note, dans la même structure de données.
#À partir d’une phrase donnée par l’utilisateur, écrire un programme qui construit et affiche l’histogramme de cette phrase. Par la suite, afficher toutes les lettres qui sont utilisées plus de 5 fois dans la phrase, en ordre décroissant d’utilisation (le plus fréquent en premier).
#Écrire un programme qui permet de sauvegarder les ingrédients nécessaires à plusieurs recettes, dans une seule structure de données. Par la suite, écrire un programme qui affiche les ingrédients d’une recette, en vérifiant au préalable si cette recette est dans notre livre de recettes.


def order(values: list = None) -> bool:
  liste=[]
  while len(liste)<10 :
    liste.append(int(input("Entrer les valeurs :")))
  if liste==sorted(liste) :
    print("Ordonnée")
  else:
    print("Désordonnée")
  return False


def anagrams(words: list = None) -> bool:
  mot1=['A', 'L', 'E', 'V', 'I', 'N']
  mot2=['N','I', 'V', 'E', 'L', 'A']
  if sorted(mot1)==sorted(mot2):
    print("Ce sont des annagrammes")
  else :
    print("Ce ne sont pas des annagrammes")
  return False


def contains_doubles(items: list) -> bool:
  for i in range(0,len(list)):
    if list[i]==list[i+1]:
      print("La liste contient des doublons")
      i=+1
    else :
      print("Aucun doublon")
      break
    return False


def best_grades(student_grades: dict) -> dict:
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
    return {}


def histogram(sentence: str) -> tuple:
    # TODO: Créer l'histogramme a l'aide d'un dictionnaire
    #       Afficher l'histogramme et les lettres les plus fréquentes
    #       Retourner l'histogramme et le tableau de lettres
    phrase='Bonjour, je m\'appelle Benjamin et je suis votre enseignant.'
    phrase_set=set(phrase)
    resultat={}
    for lettre in phrase_set:
      resultat[lettre] = phrase.count(lettre)
    print(resultat)
    return {}, []


def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingrédients et enregistrer dans une structure de données 
    pass


def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    pass


def main() -> None:
    print(f"On essaie d'ordonner les valeurs...")
    order()

    print(f"On vérifie les anagrammes...")
    anagrams()

    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    name, result = best_grades(grades)
    print(f"{name} a la meilleure moyenne: {result}")
    
    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == '__main__':
    main()
