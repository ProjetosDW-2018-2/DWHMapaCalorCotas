# DWHMapaCalor

### Programa de Pós-Graduação PPGIA - Mestrado - Projeto Data Warehouse - 2018.2.
> (Python + Django + MySQL + Pentaho)

### Índice
* [1) Objetivos
* [2) Instalação / configuração de ambiente
* [3) Consultas e resultados
* [4) Equipe

### Objetivos

- [X] Aplicar os conceitos e ferramentas utilizados durante a disciplina em uma base de dados abertos sobre Cotas na Educação Superior;
- [X] Apresentar os dados através de um mapa de calor;

### Instalação e configuração de ambiente

* 1.1) Instalar o Anaconda
- [x] [Anaconda](https://www.anaconda.com/download/)
* 1.1.1) Após a instalação, verificar se o Anaconda foi corretamente instalado através do terminal, ou cmd, usando o do comando:

```
$ conda --version
```
* 1.2) Instalar o PyCharm Community
- [x] [PyCharm](https://www.jetbrains.com/pycharm/download)

* 1.3) Instalar os Packages abaixo através do PyCharm:
- [x] Django 2.1.4
- [x] Folium 0.7.0
- [x] MySqlClient 1.3.14

* 1.4) Mudar os dados de conexão do banco de dados no arquivo settings.py:
- [x] 'NAME': 'xxxxxx',
- [x] 'USER': 'xxxxxx',
- [x] 'PASSWORD': 'xxxxxx',
- [x] 'HOST': 'xxxxxx',
- [x] 'PORT': 'xxxxxx',

* 1.5) Após executar o projeto, seguir os passos abaixo:
- [x] Acessar o endereço "http://127.0.0.1:8081/filtro_mapa/"
- [x] Escolher os filtros e clicar em exibir
- [x] Aguardar a exibição da mensagem "Mapa Gerado com Sucesso!"
- [x] Abrir o arquivo DWHMapaCalor\MapaCalor\mapa.html

### Equipe
- [Leonardo Farias](https://github.com/leoroberto)<br>
- [Wendell Soares](https://github.com/wendellsoares)<br>
- [Bonny Kathy](https://github.com/bonnykathy)<br>
- [Thiago Martins](https://github.com/tmartiiins)<br>
