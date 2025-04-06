#include "gdef.h"
#include "bbattery.h"
#include "swrite.h"

int main() 
{
    swrite_Basic = FALSE;
    bbattery_RabbitFile("binary_converted.txt",100000);
    return 0;
}
