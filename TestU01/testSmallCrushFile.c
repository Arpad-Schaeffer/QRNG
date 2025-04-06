#include "gdef.h"
#include "bbattery.h"
#include "swrite.h"

int main() 
{
    swrite_Basic = FALSE;
    bbattery_SmallCrushFile("binary_converted.txt");
    return 0;
}
