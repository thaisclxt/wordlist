from random import randrange
import string


# Retorna um número
def getNumber(word):
    number = []

    # Verifica se tem algum número em `word` e se tiver, o adiciona a lista
    for digit in string.digits:
        if digit in word:
            number.append(digit)

    # Adiciona um número aleatório se não tiver número na lista
    if not number:
        number.append(str(randrange(10)))

    return "".join(number)


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
            newWord.append(getNumber(word))
    else:
        for character in keyWord:
            newWord.append(getNumber(character))
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
        newWord = []

        # Para cada palavra em `keyWord` será gerada uma correspondente
        for word in keyWords:
            newWord.append(getNewWord(word))

        wordList.append("".join(newWord))

    exportWordList(wordList)


if __name__ == '__main__':
    main()
