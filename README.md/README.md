# Reposirório de desafios - Módulo 2

## Desafio 1

### Construção de algoritmo que consiga ler dados de url referentes ao user, repositório e release.

#### Define a função **dividir()**, para splitar a url.
```
def dividir():  ##define a funcao dividir, para splitar a url
    url_repo = "https://github.com/barrozo1/repo/releases/tag/teste-v1"
    divid = url_repo.split('/')
    return divid
```

#### Define a função **mostrar()**, que chama a função **dividir()** para pegar apenas o que importa.
```
def mostrar():  ##chama a funcao dividir() para pegar apenas o que importa
    user = dividir()[3]
    repo = dividir()[4]
    release = dividir()[7]
    return user, repo, release
```

#### Define a função **main()** do código.
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