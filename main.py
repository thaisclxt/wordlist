from random import randrange


# Exemplo: thais
def getAlpha(keyWord):
    value = randrange(3)

    if keyWord.isalpha() and not keyWord.isupper():
        if value == 0:
            return keyWord

        elif value == 1:
            return keyWord[:len(keyWord) // 2]

        elif value == 2:
            return keyWord[len(keyWord) // 2:]

    return ''


# Exemplo: UFT
def getUpper(keyWord):
    if keyWord.isupper():
        return keyWord
    return ''


# Exemplo: 2022
def getNumber(keyWord):
    value = randrange(2)

    if keyWord.isdigit():
        if value == 0:
            return keyWord

        elif value == 1:
            return keyWord[len(keyWord) // 2:]

    return ''


# Exemplo: Segurança e Auditoria de Sistemas / Ciência da Computação
def getTitle(keyWord):
    newWord = []
    value = randrange(3)

    if " " in keyWord:
        for word in keyWord.split(" "):
            if word.istitle():
                newWord.append(word[0])

        if value == 0:
            return ''.join(newWord)

        elif value == 1:
            return '.'.join(newWord)

        elif value == 2:
            return '-'.join(newWord)

    return ''


# Lê cada linha do arquivo `wordList.txt` e as retorna
def getKeyWords():
    file = open("keyWords.txt", "r")
    keyWords = file.read().split("\n")

    file.close

    return keyWords


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
        value = randrange(3)
        newWord = []

        # Para cada palavra em `keyWord` será gerada uma correspondente
        for keyword in keyWords:
            newWord.append(getAlpha(keyword))
            newWord.append(getUpper(keyword))
            newWord.append(getNumber(keyword))
            newWord.append(getTitle(keyword))

        # Verifica se o tamanho X da palavra é menor que 8, se for acrescenta 9 - X números
        if len(newWord) < 8:
            for _ in range(9 - len(newWord)):
                newWord.append(str(randrange(10)))

        if value == 0:
            pass

        elif value == 1:
            newWord.reverse()

        elif value == 2:
            newWord.sort()

        wordList.append("".join(newWord))

    exportWordList(wordList)


if __name__ == '__main__':
    main()
