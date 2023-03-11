# Quiz 3
### Quiz 3重點如下:
- 根據IC值，決定鑰匙的長度
- 解出鑰匙內容
- 透過密文和鑰匙，解出明文
---
## **程式說明**
### **這次用哪些函數**
- RemoveSpaceAndEnter(ciphertext)
- FindKeyLength(ciphertext)
- CalculateAlphabetFrequency(group, ciphertext, keyLength, alphabetFrequency)
- FindKey(keyLength, ciphertext)
- BreakCiphertext(key, ciphertext, keyLength)
- ConvertTextToNumber(text)
### **RemoveSpaceAndEnter(ciphertext)**
把空白或含有\n符號去掉

### **FindKeyLength(ciphertext)**
簡單來說，就是根據給的密文解出鑰匙長度。
```
def FindKeyLength(ciphertext):
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
                "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                "U", "V", "W", "X", "Y", "Z"]
    IC = []
    for keyLength in range(1, 7):    
        groupIC = []
        for group in range(keyLength):  
            alphabetFrequency = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                 0, 0, 0, 0, 0, 0]
	    #取得每個英文單字在該keyLength的該Group出現的頻率
            alphabetFrequency = CalculateAlphabetFrequency(group, ciphertext, keyLength, alphabetFrequency)
	    #取得該keyLength的該Group中總字數
            totalWordCount = sum(alphabetFrequency)        
            temp = 0
	    #套入IC公式，取得該keyLength該Group的IC值
            for perAlphabet in range(len(alphabet)):
                temp += (alphabetFrequency[perAlphabet] * (alphabetFrequency[perAlphabet] - 1))
            groupIC.append(temp / (totalWordCount * (totalWordCount - 1)))   
	#平均該Group所有的IC值
        IC.append(sum(groupIC) / len(groupIC))
    print("Answer:", IC.index(max(IC)) + 1)
    #取得所有KeyLength的IC值最高的，也就是取得該密文的鑰匙的長度
    return IC.index(max(IC)) + 1
```
### **CalculateAlphabetFrequency(group, ciphertext, keyLength, alphabetFrequency)**
計算該keyLength該Group的每個單字出現頻率
### **FindKey(keyLength, ciphertext)**
```
def FindKey(keyLength, ciphertext):
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
                "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                "U", "V", "W", "X", "Y", "Z"]
    #明文每英文單字出現頻率所佔的機率，統計出來
    pAlphaFreqProb = [0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015, 0.06094, 0.06966, 0.00153,
                      0.00772, 0.04025, 0.02406, 0.06749, 0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056,
                      0.02758, 0.00978, 0.02360, 0.00150, 0.01974, 0.00074]
    key = ""
    for group in range(keyLength):
        alphabetFrequency = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                             0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                             0, 0, 0, 0, 0, 0]
        cAlphaFreqProb = []
	#取得該密文每英文單字出現頻率
        alphabetFrequency = CalculateAlphabetFrequency(group, ciphertext, keyLength, alphabetFrequency)
        totalWordCount = sum(alphabetFrequency)
	#計算該密文每英文單字出現頻率所佔的機率
        for perAlphabet in range(len(alphabet)):
            cAlphaFreqProb.append(alphabetFrequency[perAlphabet] / totalWordCount)
        x = []
	#代入公式取得26種x值
        for shift in range(26):
            temp = 0
            for perAlphabet in range(len(alphabet)):
                temp += (((cAlphaFreqProb[(perAlphabet + shift) % 26] - pAlphaFreqProb[perAlphabet]) ** 2) / pAlphaFreqProb[perAlphabet])
            x.append(math.sqrt(temp))
	#取值最小，該字母為key中某個group的內容
        key += alphabet[x.index(min(x))]
    print("Answer:", key)
    return key
```
### **BreakCiphertext(key, ciphertext, keyLength)**
```
def BreakCiphertext(key, ciphertext, keyLength):
	#把密文和鑰匙由英文轉成數字，用到ConvertTextToNumber函數
	#透過密文(轉成數字後)和鑰匙(轉成數字後)把明文解出來
```
### **ConvertTextToNumber(text)**
把字母轉成數字

---
### **Motivation**
解密文有各式各樣的方式，想體驗一下解密文的奧妙之處。
### **Build Status**
目前Quiz 3已完成，沒有任何的Bug和Error。
### **Code Style**
- 若變數的命名中含有多個英文單字，第一個單字全部為小寫，後面其他的單字第一個字母為大寫，其他為小寫，例如encryptedMessage、answerKeyLength...等。
- 若函數的命名中含有多個英文單字，所有英文單字的第一個字母為大寫，其他為小寫，而且第一個英文單字為動詞，因為我認為函數通常在整個程式碼中代表的是做一件事情，例如RemoveSpaceAndEnter、FindKeyLength...等。
- 一個函數只負責做一件事情。
- 程式碼盡可能簡單且易懂。
- 命名變數名稱時，我基本上都會把整個英文單字命名出來，這樣，其他人再看我的程式碼時，才可以透過變數的命名知道我撰寫的程式碼再做什麼，例如answerKey、answerPlaintext...等。
- 除非變數名稱太長時，我才會縮減變數名稱，例如ciphertextAlphabetFrequencyProbability這個太長，我就會把它縮減成cAlphaFreqProb。
### **Screenshots**
![](https://i.imgur.com/hMAzBPs.png)

根據IC值，決定鑰匙的長度

![](https://i.imgur.com/2MfW2z6.png)

解出鑰匙內容

![](https://i.imgur.com/QGHOHGg.png)

透過密文和鑰匙，解出明文

### **Tech/Framework used**
目前沒有用什麼Framework。
### **Source Code**
兩個py檔就是了。
### **Installation**
裝Anaconda，在Anaconda Navigator建立一個環境，使用Jupyter Notebook就好。
### **Tests Results**
不提供。
### **How to Use?**
複製程式碼，貼到你所用的軟體，就可以執行了。
### **Contribute**
無。
### **Credits**
無。