# pendu

Choisir un mot dans une liste
Initialiser une variable qui contiendra les lettres devinées correctement
Liste des erreurs trouvées
Préparer une fonction qui génère un masque (“m_t à d_vin_r”) à partir du mot à deviner, et des lettres déjà devinées. Lettres aléatoirement cachées.
Niveaux: facile=1 lettre cachée,moyen=2 lettres cachées,difficile=3 lettres cachées
Demander une lettre(input=char?) qu’on compare avec les lettres du mot à deviner : On l’ajoute à la liste des lettres devinées, ou(if ou else) on retire une chance.(compteur:-1)
Si le masque est “complet”, il est == au mot à deviner. La partie est gagnée.
Tant que le mot n’est pas deviné, et qu’il reste des chances, continuer
Si lettre déjà essayée,afficher”la lettre a déjà été utilisée”
