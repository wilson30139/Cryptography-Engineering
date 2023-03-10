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
    for(int i = 0; i < 5; i++){
        singleColForCiphertext = "";
        for(int j = 0; j < 6; j++)
            singleColForCiphertext += ciphertext[i*6+j];
        colArrangeCiphertext.push_back(singleColForCiphertext);
    }
    for(int i = 5; i < 9; i++){
        singleColForCiphertext = "";
        for(int j = 0; j < 6; j++){
            if(j != 5)
                singleColForCiphertext += ciphertext[i*6+j-i+5];
            else
                singleColForCiphertext += "X";
        }
        colArrangeCiphertext.push_back(singleColForCiphertext);
    }


    cout << "The ciphertext every column:" << endl;
    for(int i = 0; i < colArrangeCiphertext.size(); i++)
        cout << "col " << (i+1) << ": " << colArrangeCiphertext[i] << endl;
    cout << endl;
    return colArrangeCiphertext;
}

void FindPlaintext(vector<string> colArrangeCiphertext){
    int colNumber[9] = {0, 1, 2, 3, 4, 5, 6, 7, 8};
    string plaintext;
    do{
        plaintext = "";
        for(int i = 0; i < 6; i++)
            for(int j = 0; j < 9; j++)
                plaintext += colArrangeCiphertext[colNumber[j]][i];
        if((plaintext.find("LOOK") != string::npos) && (plaintext.find("ANSWER") != string::npos) && (plaintext.find("NUMBER") != string::npos))
            cout << "Answer: " << plaintext << endl;
    }while(next_permutation(colNumber, colNumber+9));
}

void Decrypt(string ciphertext){
    vector<string> colArrangeCiphertext;
    colArrangeCiphertext = ArrangeColForCiphertext(ciphertext);
    FindPlaintext(colArrangeCiphertext);
}

int main(){
    string fileName = "ciphertext_bonus.txt";
    string ciphertext = ReadFile(fileName);
    Decrypt(ciphertext);

    return 0;
}
