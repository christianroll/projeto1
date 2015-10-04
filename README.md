# Redes de Computadores: Projeto 1 - Servidor de Consultas Linux

Professor [Cesar Marcondes](https://github.com/cmarcond) - [DC UFSCar](http://www.dc.ufscar.br/)


## Descrição do projeto

Descrição completa em [Projeto_01-description.pdf](docs/Projeto_01-description.pdf)

Esta aplicação permite consultar a saída de determinados comandos (`ps`, `df`,
`finger` e `uptime`) em diferentes máquinas da rede através de uma interface
web.

A aplicação é formada pelas seguintes partes:

- `webserver.py`: programa CGI acoplado ao servidor web. Também é o backend;
- `index.html`: interface web. Redireciona para webserver.py;
- `daemon.py`: programa que executa comandos localmente e retorna as saídas.


## Requerimentos

*   [Apache HTTP Server](https://httpd.apache.org/)
*   [Python 2.7](https://www.python.org/)
*   [Mako Templates for Python](http://www.makotemplates.org/)
*   [Unidecode](https://pypi.python.org/pypi/Unidecode)


### Apache no OS X

Descomente as seguintes linhas em `/etc/apache2/httpd.conf`:

    LoadModule authz_core_module libexec/apache2/mod_authz_core.so
    LoadModule authz_host_module libexec/apache2/mod_authz_host.so
    LoadModule rewrite_module libexec/apache2/mod_rewrite.so
    LoadModule cgi_module libexec/apache2/mod_cgi.so


Reinicie o Apache com `sudo apachectl restart`


### Ubuntu
    $ sudo apt-get install python-pip python-dev build-essential 
    $ sudo pip install --upgrade pip 
    $ pip install netifaces mako unidecode


## Alunos

*   [Christian Rollmann (414514)](https://github.com/christianroll)
*   [Isaac Mitsuaki Saito (344320)](https://github.com/zacmks)
*   [Julio Batista Silva (351202)](https://github.com/jbsilva)
*   [Marcelo Fernandes Tedeschi (414450)](https://github.com/marcelotedeschi)
