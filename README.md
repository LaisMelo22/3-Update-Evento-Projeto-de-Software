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
------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Update: Event Management System

This project is a comprehensive event management system developed in Python, using object-oriented programming to organize and control all aspects of an event.
Features
Event Management

    Create and cancel events

    List all registered events

    Create satisfaction surveys

    Collect and view participant feedback

People Management

    Participants: Registration with automatic ticket generation, listing, and deletion

    Speakers: Complete registration with biographical information, presentation topic, and schedule

Vendor Management

    Vendor registration with services offered

    Vendor status control (Pending, Confirmed, etc.)

    Service status updates

Financial Management

    Budget definition for events

    Expense recording with description, amount, and date

    Balance control and event financial overview

Surveys and Feedback

    Creation of customized surveys with multiple questions

    Feedback collection linked to participants through ticket numbers

    View all received feedback

Project Structure
Main Classes

    Pessoa (Abstract Class): Base class for Participant and Speaker

    Participante: Represents event participants with unique tickets

    Speaker: Represents speakers with detailed information

    Fornecedor: Manages service vendors for events

    Despesa: Controls event financial expenses

    Survey: Manages satisfaction surveys

    Feedback: Stores participant feedback

    Evento: Main class that manages all aspects of an event

    SistemaEventos: Main system that coordinates multiple events

How to Use

    Execute the Python script

    Use the interactive menu to navigate through options:

        Manage Events

        Manage Participants

        Manage Speakers

        Manage Vendors

        Manage Finances

    Follow system instructions to add, list, or modify information

Requirements

    Python 3.x

    Random module (already included in Python standard library)

Usage Examples

    Create an event with name and date

    Add participants with name and email (system generates tickets automatically)

    Register speakers with biography, topic, and presentation time

    Manage vendors and their statuses

    Set budget and record expenses

    Create surveys and collect participant feedback

Technical Characteristics

    Object-oriented programming with inheritance and abstract classes

    Management of multiple simultaneous events

    Intuitive command-line interface (CLI)

    Input data validation

    Automatic generation of unique ticket numbers

    Complete financial control with automatic balance calculation
