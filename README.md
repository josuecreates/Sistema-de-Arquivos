# Sistema-de-Arquivos
# Simulador de Sistema de Arquivos

Este projeto é um simulador de sistema de arquivos em Python, que utiliza a biblioteca **PyQt5** para criar uma interface gráfica interativa. O simulador permite a criação, leitura e exclusão de arquivos, gerenciando a memória de forma eficiente e visualizando o estado do disco.

## Sumário

- [Funcionalidades](#funcionalidades)
- [Arquitetura do Projeto](#arquitetura-do-projeto)
- [Requisitos](#requisitos)
- [Instalação](#instalação)
- [Uso](#uso)
- [Estrutura do Código](#estrutura-do-código)
- [Exemplo de Uso](#exemplo-de-uso)
- [Contribuições](#contribuições)
- [Licença](#licença)
- [Contato](#contato)

## Funcionalidades

- **Criar Arquivo**: Permite criar novos arquivos, armazenando seu conteúdo em blocos de memória.
- **Ler Arquivo**: Lê o conteúdo de arquivos existentes e o exibe em uma caixa de mensagem.
- **Excluir Arquivo**: Remove arquivos do sistema de arquivos e libera os blocos de memória.
- **Estado do Disco**: Exibe o estado atual da memória, mostrando quais blocos estão ocupados e quais estão livres.
- **Gerenciamento de Memória**: Monitora a alocação e liberação de blocos de memória, garantindo a eficiência do uso.

## Arquitetura do Projeto

O projeto é estruturado da seguinte forma:

- **Interface Gráfica**: Desenvolvida com PyQt5, permitindo interações do usuário.
- **Módulo de Lógica**: Contém a implementação do sistema de arquivos e gerenciamento de memória.
- **Estruturas de Dados**:
  - `Block`: Representa cada bloco na memória, contendo um caractere e um ponteiro para o próximo bloco.
  - `File`: Representa um arquivo, com nome, tamanho e índice do bloco inicial na memória.
  - `FileSystem`: Implementa a lógica do sistema de arquivos, incluindo operações de criar, ler e excluir arquivos.

## Requisitos

- **Python**: Versão 3.x
- **PyQt5**: Biblioteca para interface gráfica

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://seu-repositorio.git
   cd seu-repositorio
