#include <iostream>
#include <random>

/*
 * Generates a random binary sequence of a given length and outputs it to the console
 * @param length (int): The length of the generated binary sequence
 */
void generateRandomBinarySequence(int length){
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> dis(0, 1);

    std::cout << "Sequence: ";
    for (int i = 0; i < length; ++i)
    {
        std::cout << dis(gen);
    }
    std::cout << std::endl;
}

int main(){
    const int length = 128;
    generateRandomBinarySequence(length);

    return 0;
}