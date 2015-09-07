# Redes de Computadores: Projeto 1 - Servidor de Consultas Linux

Professor [Cesar Marcondes](https://github.com/cmarcond) - [DC UFSCar](http://www.dc.ufscar.br/)


## Descrição do projeto

Esta aplicação permite consultar a saída de determinados comandos (`ps`, `df`,
`finger` e `uptime`) em diferentes máquinas da rede através de uma interface
web.

A aplicação é formada pelas seguintes partes:

- `webserver.py`: programa CGI acoplado ao servidor web;
- `index.html`: interface web;
- `backend.py`: programa que gerencia o backend;
- `daemon.py`: programa que executa comandos localmente e retorna as saídas.


## Alunos

*   [Christian Rollmann (414514)](https://github.com/christianroll)
*   [Isaac Mitsuaki Saito (344320)](https://github.com/isaito)
*   [Julio Batista Silva (351202)](https://github.com/jbsilva)
*   [Marcelo Fernandes Tedeschi (414450)](https://github.com/marcelotedeschi)
