#include <iostream>
#include <random>

void generateRandomBinarySequence(int length) {
    std::random_device rd; 
    std::mt19937 gen(rd()); 
    std::uniform_int_distribution<> dis(0, 1); 

    std::cout << "Sequence: ";
    for (int i = 0; i < length; ++i) {
        std::cout << dis(gen); 
    }
    std::cout << std::endl; 
}

int main() {
    const int length = 128; 
    generateRandomBinarySequence(length);

    return 0;
}