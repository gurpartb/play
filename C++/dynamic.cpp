#include <iostream>
#include <set>

bool* W_i;

bool dict(std::string S, int a, int b){
        std::string s = S.substr(a,b);
        std::string as = "and";
        std::cout <<s<< '\n';
        if(std::strcmp(s,as)) {
                std::cout << "inside for loop" << '\n';
                return true;
        }
        return true;
}

bool W(int i, std::string S){
        // std::cout <<i<< " " << '\n';
        // if(i <= 0) {
        //         return false;
        // }
        // for (size_t j = i-1; j > 0; j--) {
        //         W_i[j] = W(j, S)&&dict(S,j+1, i);
        // }
        // return W_i[i];
        W_i[i-1] = dict(S, 0,i);
        return dict(S, 0,i);
}

int main(int argc, char const *argv[]) {
        const int count = 3;
        bool w1 = new bool[12];
        W_i = &w1;
        std::string S = "and";
        W(count, S);
        for (size_t i = 0; i < count; i++) {
                std::cout << W_i[i]<<" ";
        }
        std::cout << '\n';
        return 0;
}
