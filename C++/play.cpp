#include <iostream>
#include <math.h>

int main(int argc, char const *argv[]) {
        std::cout << ceilf(log10(12))<< '\n';
        return 0;
}

// int main(int argc, char const *argv[]) {
//         srand(time(NULL));
//         int count = 100;
//         float sum = 0;
//         for (size_t i = 0; i < count; i++) {
//                 int r = int(static_cast <float> (rand())*100.0f/ static_cast <float> (RAND_MAX));
//                 std::cout << r << '\n';
//                 sum += r;
//         }
//         std::cout << "sum "<<sum << '\n';
//         return 0;
// }
