#include <stdio.h>              // Bibliothèque standard pour les entrées/sorties (printf)
#include <stdlib.h>             // Pour atoi(), atol(), exit(), etc.
#include "unif01.h"             // Déclaration de la structure unif01_Gen et fonctions liées aux générateurs
#include "bbattery.h"           // Fonctions des batteries de tests (SmallCrush, Rabbit, etc.)
#include "ufile.h"              // Fonctions pour créer un générateur à partir d’un fichier
#include "swrite.h"             // Permet d'activer/désactiver les impressions standard TestU01

int main(int argc, char *argv[])
{
    // Désactivation des messages de sortie par défaut de TestU01 (swrite)
    swrite_Basic = FALSE;

    // Déclaration du générateur (type générique utilisé par toutes les batteries)
    unif01_Gen *gen;

    // Vérification du nombre d'arguments passés par l'utilisateur
    if (argc != 3) {
        // Message d'aide si les arguments sont incorrects
        printf("Usage : %s <fichier_uint32.txt> <nbuf>\n", argv[0]);
        return 1; // Fin du programme avec code d'erreur
    }

    // Récupération du nom de fichier et du paramètre nbuf à partir des arguments
    char *filename = argv[1];         // Chemin du fichier texte contenant les uint32 (1 par ligne)
    long nbuf = atol(argv[2]);        // Conversion de l'argument string en entier long (nombre de valeurs à lire)

    // Création d'un générateur depuis un fichier binaire, lecture de 'nbuf' entiers 32 bits
    gen = ufile_CreateReadBin(filename, nbuf);

    // Message d'information avant lancement du test
    printf("=== Lancement du test smallcrush avec %ld valeurs ===\n", nbuf);

    // Lancement de la batterie de tests statistiques Rabbit sur le générateur
    bbattery_SmallCrush(gen);

    // Message de fin de test
    printf("=== Test smallcrush terminé ===\n");

    // Libération propre de la mémoire associée au générateur
    unif01_DeleteExternGenBits(gen);

    return 0; // Fin normale du programme
}
