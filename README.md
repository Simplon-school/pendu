# pendu

1. Choisir un mot dans une liste
2. Initialiser une variable qui contiendra les lettres devinées correctement
3. Liste des erreurs trouvées
4. Préparer une fonction qui génère un masque (“m_t à d_vin_r”) à partir du mot à deviner, et des lettres déjà devinées. Lettres aléatoirement cachées.
5. Niveaux: facile=1 lettre cachée,moyen=2 lettres cachées,difficile=3 lettres cachées
6. Demander une lettre(input=char?) qu’on compare avec les lettres du mot à deviner : On l’ajoute à la liste des lettres devinées, ou(if ou else) on retire une chance.(compteur:-1)
7. Si le masque est “complet”, il est == au mot à deviner. La partie est gagnée.
8. Tant que le mot n’est pas deviné, et qu’il reste des chances, continuer
10. Si lettre déjà essayée,afficher”la lettre a déjà été utilisée”
