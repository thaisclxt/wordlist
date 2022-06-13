from random import randrange
import string


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
        newWord = []

        # Para cada palavra em `keyWord` será gerada uma correspondente
        for keyword in keyWords:

            # UFT
            if keyword.isupper():
                newWord.append(keyword)

            # thais
            elif keyword.isalpha():
                newWord.append(keyword)

            # 2022
            if keyword.isdigit():
                newWord.append(keyword)

            # Segurança e Auditoria de Sistemas / Ciência da Computação
            if " " in keyword:
                for word in keyword.split(" "):
                    if word.istitle():
                        newWord.append(word[0])

        wordList.append("".join(newWord))

    exportWordList(wordList)


if __name__ == '__main__':
    main()
