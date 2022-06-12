from random import randrange


# Lê as palavras do arquivo `wordList.txt` e as retorna
def getKeyWords():
    file = open("keyWords.txt", "r")
    keyWords = file.read().split("\n")

    file.close

    return keyWords


# Gera novas palavras a partir do arquivo `wordList.txt` e as retorna
def generateWords():
    wordList = []
    keyWords = getKeyWords()

    for _ in range(int(input("Quantas palavras você deseja gerar? "))):
        newWord = []
        for word in keyWords:

            # Adiciona duas letras randomicamente de cada palavra
            newWord.append(word.upper()[randrange(len(word))])
            newWord.append(word.upper()[randrange(len(word))])

        # Adiciona dois números randomicamente ao final da palavra
        newWord.append(str(randrange(10)))
        newWord.append(str(randrange(10)))

        # Adiciona a nova palavra em `wordList`
        wordList.append("".join(newWord))

    return wordList


# Acessa ou cria um arquivo chamado `wordList.txt`, se já não existir, e escreve as palavras geradas
def exportWordList():
    file = open("wordList.txt", "w+")

    wordList = generateWords()

    for word in wordList:
        file.write(word)
        file.write('\n')

    file.close


def main():
    exportWordList()


if __name__ == '__main__':
    main()
