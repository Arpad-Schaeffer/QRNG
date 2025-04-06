#include <stdio.h>
#include <stdlib.h>
#include "unif01.h"
#include "bbattery.h"

int main(int argc, char *argv[]) {
    if (argc != 3) {
        printf("Usage : %s <fichier_uint32.txt>\n", argv[0]);
        return 1;
    }

    char *filename = argv[1];
    int n = atol(argv[2]);
    printf("=== Lancement du test Rabbit sur le fichier : %s ===\n", filename);

    bbattery_RabbitFile(filename , n);  // RabbitFile lit directement un fichier texte d'uint32

    printf("=== Test Rabbit terminé ===\n");
    return 0;
}
