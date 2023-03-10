import math
def CalculateAlphabetFrequency(group, ciphertext, keyLength, alphabetFrequency):
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
                "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                "U", "V", "W", "X", "Y", "Z"]
    for enChar in range(group, len(ciphertext), keyLength):
        for perAlphabet in range(len(alphabet)):
            if ciphertext[enChar] == alphabet[perAlphabet]:
                alphabetFrequency[perAlphabet] += 1
                break
    return alphabetFrequency

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
            alphabetFrequency = CalculateAlphabetFrequency(group, ciphertext, keyLength, alphabetFrequency)
            totalWordCount = sum(alphabetFrequency)        
            temp = 0
            for perAlphabet in range(len(alphabet)):
                temp += (alphabetFrequency[perAlphabet] * (alphabetFrequency[perAlphabet] - 1))
            groupIC.append(temp / (totalWordCount * (totalWordCount - 1)))        
        IC.append(sum(groupIC) / len(groupIC))
    print("Answer:", IC.index(max(IC)) + 1)
    return IC.index(max(IC)) + 1

def RemoveSpaceAndEnter(ciphertext):
    ciphertext = ciphertext.replace(" ", "").replace("\n", "")
    return ciphertext

def FindKey(keyLength, ciphertext):
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
                "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                "U", "V", "W", "X", "Y", "Z"]
    pAlphaFreqProb = [0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015, 0.06094, 0.06966, 0.00153,
                      0.00772, 0.04025, 0.02406, 0.06749, 0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056,
                      0.02758, 0.00978, 0.02360, 0.00150, 0.01974, 0.00074]
    key = ""
    for group in range(keyLength):
        alphabetFrequency = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                             0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                             0, 0, 0, 0, 0, 0]
        cAlphaFreqProb = []
        alphabetFrequency = CalculateAlphabetFrequency(group, ciphertext, keyLength, alphabetFrequency)
        totalWordCount = sum(alphabetFrequency)
        for perAlphabet in range(len(alphabet)):
            cAlphaFreqProb.append(alphabetFrequency[perAlphabet] / totalWordCount)
        x = []
        for shift in range(26):
            temp = 0
            for perAlphabet in range(len(alphabet)):
                temp += (((cAlphaFreqProb[(perAlphabet + shift) % 26] - pAlphaFreqProb[perAlphabet]) ** 2) / pAlphaFreqProb[perAlphabet])
            x.append(math.sqrt(temp))
        key += alphabet[x.index(min(x))]
    print("Answer:", key)
    return key

def ConvertTextToNumber(text):
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
                "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                "U", "V", "W", "X", "Y", "Z"]
    textNum = []
    for char in text:
        for alphaNum in range(len(alphabet)):
            if char == alphabet[alphaNum]:
                textNum.append(alphaNum)
                break
    return textNum

def BreakCiphertext(key, ciphertext, keyLength):    
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
                "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                "U", "V", "W", "X", "Y", "Z"]
    keyNum = ConvertTextToNumber(key)
    ciphertextNum = ConvertTextToNumber(ciphertext)
    plaintextNum = []
    keyCount = 0
    for enCharNum in ciphertextNum:
        temp = enCharNum - keyNum[keyCount]
        if temp < 0:
            temp += 26
        plaintextNum.append(temp)
        keyCount += 1
        if keyCount == keyLength:
            keyCount = 0
    plaintext = ""
    for deCharNum in plaintextNum:
        plaintext += alphabet[deCharNum]
    return plaintext

for message in range(1, 3):
    encryptedMessage = input("Enter the encrypted message: ")
    print()
    print("Message", message, end = "")
    print(":")
    print("1.Determine the keyword length of these two encrypted messages using I.C.")
    encryptedMessage = RemoveSpaceAndEnter(encryptedMessage)
    answerKeyLength = FindKeyLength(encryptedMessage)
    print("2.Then solve the encryption keyword letters.")
    answerKey = FindKey(answerKeyLength, encryptedMessage)
    print("3.Finally, break this ciphertext and recover the plaintext.")
    answerPlaintext = BreakCiphertext(answerKey, encryptedMessage, answerKeyLength)
    print("Answer: The answer in 311552022_msg", end = "")
    print(message, end = "")
    print(".txt")
    fileName = "311552022_msg" + str(message) + ".txt"
    with open(fileName, 'w') as fileObject:
        fileObject.write(answerPlaintext)
    print()

'''
Message 1:
ZQQTK PQUWD PGMWD BQTXY LFQWL SHAJB UCIPV KUQEJ RBAAC LRSIZ ZCRWT LDFMT PGYXF ISOSE ASZXN PHTAY HHIIR ADDIJ LBFO
E VKUWW VFFLV TCEXG HFFXF ZVGXF BFQEI ZOSEZ UGFGF UJUGK PCZWZ UQQJI VAFLV CSDCX YOPYR SQTEI HQFII VTAYI LRGGR AWAR
N LAGWK JCZXZ UIMPC FTAVX LHMRU LAMRT PDMXV VIDWV SJQWW YCYOE VKXIU NSBVV CWAYJ SMMGH BWDIU DSYYJ AGQXR ZWP
IF SRZSK PCZWR URQQS YOOIW YSELF USEEE KOEAV SSMVE DSYYJ APQHR PZKYE SSMVE PBSWF TSFLZ UUILZ JVUXY HGOSJ AIERF ZAMP
C SONSL YOZHR ULUIK FHAET XIUVV HBPXY PGPMW MWOYC AMMXK HQTIJ PHEIC MAAVV JZAWV SMFSR UOSIZ UKTMT ODDSX YSEW
Y HGSEZ USPEJ AFARX HGOIE KSZGP VJQVG YSVYU PQQEE KWZAY PQTTV YGARJ HBPXY PBSWR YSPEP IMPEP MWZHZ UUFLV PFDIR SZQ
ZV SWZPZ LIAJK OSUVT VBHIE AWARR SJMPL LHTIJ HAQTI PBOMG SSEAY PQTLR CSEAV WHMAR FHDEU PHUSE HZMFL ZSEEE KKTMT O
ODID HYURX YOBMU OOHST HAARX AVQVV CSZYV ZCRWZ USOYI PGFWR UREXI PDBME NHTIK OWZXR DRDCM LWXJI VAMXK YOOXZ C
SEYG LFEXZ AWARJ HFQAF YYURX HGMGK PJQPP PBXMK LFMXL YSMWZ UGAGZ LHKXY LQDIU BZUXP VTARV DFUXV YCDXY LDMVK POX
MK FCREE VHTII MWZHJ HGBSN LFRYC HHAYT OGFSE LOZHR ZKTSC LGAQV HQTEJ AWEID LBFME AVQLV HZFLP ZQQTK PQUWD VTMXV
TDQVR ASOPR ZGAJR UHMKF UWEXJ HGFLV KFQED ZCRGF UGQVM HHUWD VFFLV PABSJ AIDIJ VTBPL YOXMJ AGURV JIDIJ PBFLV JVGVT
OVUWK VFKEE KHDEU PHUSE DVQXY LFAJR UQUIE ACDGF TDMVR AWHIC FFQGV UHFMD LGMVV ZINNV JHQHK VJQVP KWRJV YSZXY
HBPPZ UURVF THTEK DVUGY AVQME KIXKV UQQSI JFQHL SWFCF MTAVD LFMKV ZQAYC KOXPF DAQVV ZHMXV TSZXJ HFQNV HZAYJ SM
IEK JVQHR URFLV TCFMM LGAJK OSIVZ ASDJF YAMWZ TDAVK HBFEE PBSVV KWQRK PBFLV HBMPP ZWESW OWELZ ZHAVP HGFLV MOO
XJ OSDIT VFPWG YCNES PZUXP PGMTF DSDJL SOZHK YCGFC LGAQV ASEXR URUXZ ZPKXY PGFVF BPXIJ VAQWK HBPEI KHTEK HZMVX LD
AVK PCZSW OWEXF YWOEC LJUHV UQQMJ ZWRXV KQARJ PGFIE JMUWE VZQWJ WSDXZ UOOMF BGMRU LLMGK PBSME PHEHV TOZHJ
PBNVZ LTFSN YWFIR OWEXF YMIID BGFOE VKYSI LHTEE TSDIW HQFWY BAMRE HHGVV CWQAV KIZHV YOZME KIOXZ VBAJV EHQRU LRQ
BG LFUIE JSUWK OSNIJ AVQPG ACFLV JFUXZ JWEQF MVGQR UVUWK VFKLZ ZHAVZ JOXGY HFMGK LFEGR UCZPP ISQWK PAMXV KPKXY L
GFEE KODHN OWOLY BAMRV EDQVZ LBOIN OSFLV YOOXL HZAVK YOPMK PCZEI FVMWW BFZMJ OSPXF MCDQT VFDIT AJUIN ZCRME K
WHMU BOXWN LAGWK YSSEI KHTID HGRSI TWZKG HFFWF MOSVV HHILF SSIID BGFQV HGGVV AVQQS FHTIZ YFQPR AWARK VHTID HGE
SW ISURX ZPKAY VAFLV FODIJ BFDSL URQHR URURT VBFID WZMXZ UUFLV PBOMU LBFWZ UHTIZ YZUZV ZCDGF URUXZ VBILZ JVFVR KW
FMF UVMWY HBPIU KCIRK VIEAV TIEXI HHTII JCZWZ KSDXY LUQRV YOXFV HFURX VTFLV DVAPV UODVR AWHIK OOZXY LFQWG LQFMM
LDDSS HPUPZ AMAJZ AGPIK HWXW

Message 2:
IVIKDKDQMJGLPWLZGMPFBJIIDBBYSLJDXFGBIWWEHAPHEYSGNCCYOOTSTZABCOBV RTAZEYWVWWAZAIDGAZ
PETHPVBPWOBVJXGFMDOBCGPFKXKSZZAIGCJRPETACJHUTHPVHKJHPZHFPMEVZEQS BYOMHSDVFTASFGZTC
OBZCGHFMDOBCWVNVBRVKRGXDBMKFBTGBVGMPTBVFMTGBLBMXZWESHGCBYSKDTBYS FWOARQHCJQEQBC
UIDCNCHWWGNEDWIHPTKQCZGDKIGDENHPZGIGWVTWIASBFHATQIJSBCDWZBMPGQKK THTQIGMEFMJSGISLK
CFTHPVFXLSZVHAGSMGCLHWJCSXMDTRBTIWWEGHUHPVGXRZCJWHCCZZBVPFKVFTIW WECYIVQJUXCHTVAT
CWVRBHJHPFILTCNYWLUOBYSKHAIEGBDBBYSKTKIJHATSFGZTCOBZCGIVIKVXLOAZ BAXRQEUYDFITFBBSWIHA
PHPVKTHAIUOGSHPRHMWSGNWLWSLKCTKCQUOGPGGCIFDFBYOMWSPRRLDAMUWLTOAV KAXQPTONHSLYWL
HSOISZPHQFBBRCCCRMWWVBCYCCWKVXGOLVENPHMJCEJHQFBLIVMJSMWSVYOWICJV GBUHMUOGSPICOGR
SLRUTXBAKSTRVWKVXG
'''
