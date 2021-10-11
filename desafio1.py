##construindo algoritmo para ler, splitar e salvar string


def dividir():  ##define a funcao dividir, para splitar a url
    url_repo = "https://github.com/barrozo1/repo/releases/tag/teste-v1"
    divid = url_repo.split('/')
    return divid


def mostrar():  ##chama a funcao dividir() para pegar apenas o que importa
    user = dividir()[3]
    repo = dividir()[4]
    release = dividir()[7]
    return user, repo, release


def main():
    print("USUÁRIO:", mostrar()[0])
    print("REPOSITÓRIO:", mostrar()[1])
    print("RELEASE:", mostrar()[2])

    file = open('../../Desafio 1/desafio.txt', 'w+')
    file.write(mostrar()[0])
    file.write('\n')
    file.write(mostrar()[1])
    file.write('\n')
    file.write(mostrar()[2])
    file.close()


if __name__ == '__main__':
    main()