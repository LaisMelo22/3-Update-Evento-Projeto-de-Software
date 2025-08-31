# Terceiro Update: Sistema de Gerenciamento de Eventos

Este projeto é um sistema completo de gerenciamento de eventos desenvolvido em Python, utilizando programação orientada a objetos para organizar e controlar todos os aspectos de um evento.
Funcionalidades
Gerenciamento de Eventos

    Criação e cancelamento de eventos

    Listagem de todos os eventos cadastrados

    Criação de pesquisas de satisfação

    Coleta e visualização de feedbacks dos participantes

Gerenciamento de Pessoas

    Participantes: Cadastro com geração automática de ingresso, listagem e exclusão

    Palestrantes: Cadastro completo com informações biográficas, tópico da palestra e horário

Gerenciamento de Fornecedores

    Cadastro de fornecedores com serviços oferecidos

    Controle de status dos fornecedores (Pendente, Confirmado, etc.)

    Atualização de status dos serviços

Gestão Financeira

    Definição de orçamento para o evento

    Registro de despesas com descrição, valor e data

    Controle de saldo e visualização das finanças do evento

Pesquisas e Feedbacks

    Criação de pesquisas personalizadas com múltiplas perguntas

    Coleta de feedbacks vinculados aos participantes através do número do ingresso

    Visualização de todos os feedbacks recebidos

Estrutura do Projeto
Classes Principais

    Pessoa (Classe Abstrata): Classe base para Participante e Palestrante

    Participante: Representa os participantes do evento com ingresso único

    Speaker: Representa os palestrantes com informações detalhadas

    Fornecedor: Gerencia os fornecedores de serviços para o evento

    Despesa: Controla as despesas financeiras do evento

    Survey: Gerencia as pesquisas de satisfação

    Feedback: Armazena os feedbacks dos participantes

    Evento: Classe principal que gerencia todos os aspectos de um evento

    SistemaEventos: Sistema principal que coordena múltiplos eventos

Como Utilizar

    Execute o script Python

    Utilize o menu interativo para navegar pelas opções:

        Gerenciar Eventos

        Gerenciar Participantes

        Gerenciar Palestrantes

        Gerenciar Fornecedores

        Gerenciar Finanças

    Siga as instruções do sistema para adicionar, listar ou modificar informações

Requisitos

    Python 3.x

    Módulo random (já incluído na biblioteca padrão do Python)

Exemplos de Uso

    Criar um evento com nome e data

    Adicionar participantes com nome e email (o sistema gera ingresso automaticamente)

    Cadastrar palestrantes com biografia, tópico e horário da palestra

    Controlar fornecedores e seus status

    Definir orçamento e registrar despesas

    Criar pesquisas e coletar feedbacks dos participantes

Características Técnicas

    Programação orientada a objetos com herança e classes abstratas

    Gerenciamento de múltiplos eventos simultaneamente

    Interface de linha de comando (CLI) intuitiva

    Validações de entrada de dados

    Geração automática de números de ingresso únicos

    Controle financeiro completo com cálculo automático de saldo
