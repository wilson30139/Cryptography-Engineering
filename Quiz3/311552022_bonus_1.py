import hashlib
hashValue = ["5f4dcc3b5aa765d61d8327deb882cf99", "5a105e8b9d40e1329780d62ea2265d8a"]
commonPasswordList = [
          "12345",     "123456",   "123456789",   "picture1",        "test1",  "password",    "qwerty", "12345678",     "111111",        "zinch",
         "123123", "g_czechout",        "asdf", "1234567890",        "senha",   "1234567", "qwerty123",   "000000",  "Aa123456.",       "abc123",
           "1234",  "password1",       "11111",   "iloveyou",     "aaron431", "qwertyiop",  "dubsmash",   "123321",       "test",     "qqww1122",
    "password123",   "princess",         "123", "1q2w3e4r5t",       "omgpop",  "sunshine",    "123321",   "654321", "BvtTest123",       "666666",
      "987654321",     "ashley",  "qwer123456",      "00000",      "123456a",   "a123456",    "qwe123",   "monkey",   "asdfghkl",      "7777777",
       "livetest",   "1qaz2wsx",       "55555",     "soccer",      "unknown",   "zxcvbnm",   "charlie",   "121212",     "asdasd",    "chatbooks",
         "family",   "20100728",     "michael",  "123123123",       "dragon",  "football", "jacket025", "baseball",      "evite", "q1w2e3r4t5y6",
         "nicole",    "jessica",      "159753",     "purple",       "shadow",    "hannah", "chocolate",  "5201314",     "123654",       "deniel",
         "maggie",    "pokemon", "Bangbang123",     "aaaaaa", "jobandtalent",  "myspace1",  "88888888",   "tigger",    "default",       "summer",
     "ohmnamah23",    "fitness",   "147258369",     "bailey",         "zing",    "102030",  "computer",   "buster",  "butterfly",     "jennifer"]
for perHashValue in hashValue:
    print("Hash Value:", perHashValue)
    for commonPassword in commonPasswordList:
        guess = hashlib.md5(commonPassword.encode('utf-8')).hexdigest()
        if guess.upper() == perHashValue or guess.lower() == perHashValue:
            print("Password found:", commonPassword)
            print()
            break
