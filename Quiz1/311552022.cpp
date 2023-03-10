#include <iostream>
#include <fstream>
using namespace std;
int main()
{
    string tempString;
    string ciphertext = "";
    ifstream inputFile("ciphertext.txt", ios::in);
    while(!inputFile.eof())
    {
        inputFile >> tempString;
        ciphertext += tempString;
    }
    inputFile.close();

    int alphabetFrequency[26] = {0};
    char alphabet[26] =
    {
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
        'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
        'U', 'V', 'W', 'X', 'Y', 'Z'
    };
    for(int i = 0; i < ciphertext.length(); i++){
        for(int j = 0; j < (sizeof(alphabet) / sizeof(char)); j++){
            if(ciphertext[i] == alphabet[j]){
                alphabetFrequency[j]++;
                break;
            }
        }
    }

    cout << "Ciphertext's letter frequency count:" << endl;
    for(int i = 0; i < (sizeof(alphabet) / sizeof(char)); i++)
        cout << alphabet[i] << ": " << alphabetFrequency[i] << endl;
    return 0;
}
