import string


# Lê cada linha do arquivo `wordList.txt` e as retorna
def getKeyWords():
    file = open("keyWords.txt", "r")
    keyWords = file.read().split("\n")

    file.close

    return keyWords


# Gera uma nova palavra a partir de `word`
def getNewWord(keyWord):
    newWord = []

    # Verifica se `keyWord` é uma frase
    if " " in keyWord:
        for word in keyWord.split(" "):
            pass
    else:
        for character in keyWord:
            pass

    return "".join(newWord)


# Acessa ou cria um arquivo chamado `wordList.txt`, se já não existir, e escreve as palavras geradas
def exportWordList(wordList):
    file = open("wordList.txt", "w+")

    for word in wordList:
        file.write(word)
        file.write('\n')

    file.close


def main():
    wordList = []
    keyWords = getKeyWords()

    for _ in range(int(input("Quantas palavras você deseja gerar? "))):

        # Para cada palavra em `keyWord` será gerada uma correspondente
        for word in keyWords:
            wordList.append(getNewWord(word))

    exportWordList(wordList)


if __name__ == '__main__':
    main()
