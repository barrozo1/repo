# Reposirório de desafios - Módulo 2

## Desafio 1

### Construção de algoritmo que consiga ler dados de url referentes ao user, repositório e release.

#### Define a função __pega_url()__, fazendo conexão com a latest releases
```
def pega_url():
    url_repo = requests.get('https://github.com/barrozo1/repo/releases/latest')
    return url_repo
```

#### Define a função __dividir()__, para splitar a url.
```
def dividir():  ##define a funcao dividir, para splitar a url
    divid = pega_url().url.split('/')
    return divid
```

#### Define a função __mostrar()__, chamando a função __dividir()__ para pegar apenas o que importa.
```
def mostrar():  ##chama a funcao dividir() para pegar apenas o que importa
    user = dividir()[3]
    repo = dividir()[4]
    release = dividir()[7]
    return user, repo, release
```

#### Define a função __main()__ do código.
```
def main():
    print("USUÁRIO:", mostrar()[0])
    print("REPOSITÓRIO:", mostrar()[1])
    print("RELEASE:", mostrar()[2])

    file = open('desafio.txt', 'w+')
    file.write(mostrar()[0])
    file.write('\n')
    file.write(mostrar()[1])
    file.write('\n')
    file.write(mostrar()[2])
    file.close()

if __name__ == '__main__':
    main()
```


## Desafio 2

### Adição do código dentro do conceito de Orientação a objetos.

#### Define o construtor da classe __git()__ com seus atributos e métodos, seguindo o mesmo padrão do desafio 1, porém em OO.
```
from Desafios.repo.desafio1 import mostrar, dividir, pega_url
import requests

class git:
    def __init__(self, dividir, mostrar, printar_salvar, pega_url):
        self.pega_url = pega_url
        self.dividir = dividir
        self.mostrar = mostrar
        self.printar_salvar = printar_salvar


    def pega_url(self):
        url_repo = requests.get('https://github.com/barrozo1/repo/releases/latest')
        return url_repo

    def dividir(self):  ##define a funcao dividir, para splitar a url
        divid = pega_url().url.split('/')
        return divid

    def mostrar(self):  ##chama a funcao dividir() para pegar apenas o que importa
        user = dividir()[3]
        repo = dividir()[4]
        release = dividir()[7]
        return user, repo, release

    def printar_salvar(self):
        print("USUÁRIO:", mostrar()[0])
        print("REPOSITÓRIO:", mostrar()[1])
        print("RELEASE:", mostrar()[2])
        file = open('desafio.txt', 'w+')
        file.write(mostrar()[0])
        file.write('\n')
        file.write(mostrar()[1])
        file.write('\n')
        file.write(mostrar()[2])
        file.close()


if __name__ == '__main__':
    git.dividir(self=git)
    git.mostrar(self=git)
    git.printar_salvar(self=git)
```