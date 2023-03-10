#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
using namespace std;

string ReadFile(string fileName){
    string tempString;
    string text = "";
    ifstream inputFile(fileName, ios::in);
    while(!inputFile.eof()){
        inputFile >> tempString;
        text += tempString;
    }
    inputFile.close();
    cout << "The text read from file: " << text << endl << endl;
    return text;
}

vector<string> ArrangeColForCiphertext(string ciphertext){
    vector<string> colArrangeCiphertext;
    string singleColForCiphertext;
    for(int i = 0; i < 7; i++){
        singleColForCiphertext = "";
        for(int j = 0; j < 9; j++)
            singleColForCiphertext += ciphertext[i*9+j];
        colArrangeCiphertext.push_back(singleColForCiphertext);
    }
    cout << "The ciphertext every column:" << endl;
    for(int i = 0; i < colArrangeCiphertext.size(); i++)
        cout << "col " << (i+1) << ": " << colArrangeCiphertext[i] << endl;
    cout << endl;
    return colArrangeCiphertext;
}

void FindPlaintext(vector<string> colArrangeCiphertext){
    int colNumber[7] = {0, 1, 2, 3, 4, 5, 6};
    string plaintext;
    do{
        plaintext = "";
        for(int i = 0; i < 9; i++)
            for(int j = 0; j < 7; j++)
                plaintext += colArrangeCiphertext[colNumber[j]][i];
        if((plaintext.find("CARRY") != string::npos) && (plaintext.find("CAN") != string::npos) && (plaintext.find("INTELLIGENCE") != string::npos))
            cout << "Answer: " << plaintext << endl;
    }while(next_permutation(colNumber, colNumber+7));
}

void Decrypt(string ciphertext){
    vector<string> colArrangeCiphertext;
    colArrangeCiphertext = ArrangeColForCiphertext(ciphertext);
    FindPlaintext(colArrangeCiphertext);
}

void CalculateEveryAlphabetFrequency(string message){
    double totalWordCount = message.length();
    double alphabetFrequency[26] = {0};
    char alphabet[26] =
    {
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
        'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
        'U', 'V', 'W', 'X', 'Y', 'Z'
    };
    for(int i = 0; i < totalWordCount; i++){
        for(int j = 0; j < 26; j++){
            if(message[i] == alphabet[j]){
                alphabetFrequency[j]++;
                break;
            }
        }
    }

    double tempValue = 0;
    for(int i = 0; i < 26; i++)
        tempValue += (alphabetFrequency[i] * (alphabetFrequency[i] - 1));
    double IC = (tempValue / (totalWordCount * (totalWordCount - 1)));
    cout << "Answer: IC = " << IC << endl << endl;
}

int main(){
    cout << "2." << endl;
    string fileName = "ciphertext_2.txt";
    string ciphertext = ReadFile(fileName);
    Decrypt(ciphertext);
    cout << "----------------------------------------------------------------------------" << endl;

    cout << endl << "3." << endl;
    string fileNameArray[4] = {"message_3_1.txt", "message_3_2.txt", "message_3_3.txt", "message_3_4.txt"};
    for(int i = 0; i < (sizeof(fileNameArray) / sizeof(string)); i++){
        cout << "Message " << (i+1) << endl;
        string message = ReadFile(fileNameArray[i]);
        CalculateEveryAlphabetFrequency(message);
    }
    cout << "----------------------------------------------------------------------------" << endl;

    cout << endl << "4." << endl;
    fileName = "ciphertext_4.txt";
    ciphertext = ReadFile(fileName);
    CalculateEveryAlphabetFrequency(ciphertext);

    return 0;
}
