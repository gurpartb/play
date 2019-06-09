#include <iostream>

void print_blank_space(int spaces){
        for (size_t i = 0; i < spaces; i++) {
                std::cout << " ";
        }
}

int main(int argc, char const *argv[]) {
        int rows;
        int cols;
        std::cin >> rows;
        std::cin >> cols;
        int M[cols][rows];
        int max;
        for (size_t i = 0; i < rows; i++) {
                for (size_t j = 0; j < cols; j++) {
                        int val;
                        std::cin >> val;
                        if(i==0 && j ==0) {
                                max = abs(val);
                        } else if(max<abs(val)) {
                                max = abs(val);
                        }
                        M[i][j]=val;
                }
        }
        int minspace = floorf(max);
        std::cout << "min space "<< minspace << '\n';
        for (size_t i = 0; i < rows; i++) {
                for (size_t j = 0; j < cols; j++) {
                        int val;
                        val = M[i][j];
                        std::cout << val;
                        print_blank_space(1);
                }
                std::cout<< '\n';
        }        std::cout << "hello world" << '\n';
        return 0;
}
