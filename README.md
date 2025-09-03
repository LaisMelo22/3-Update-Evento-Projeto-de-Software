
# Terceiro Update: Sistema de Gerenciamento de Eventos / Event Management System

Este projeto é um sistema completo de gerenciamento de eventos desenvolvido em Python, utilizando **programação orientada a objetos** para organizar e controlar todos os aspectos de um evento.

This project is a comprehensive event management system developed in Python, using **object-oriented programming** to organize and control all aspects of an event.

---

## Funcionalidades / Features

### Gerenciamento de Eventos / Event Management

* Criação e cancelamento de eventos / Create and cancel events
* Listagem de todos os eventos cadastrados / List all registered events
* Criação de pesquisas de satisfação / Create satisfaction surveys
* Coleta e visualização de feedbacks dos participantes / Collect and view participant feedback

### Gerenciamento de Pessoas / People Management

* **Participantes:** Cadastro com geração automática de ingresso, listagem e exclusão / Participants: Registration with automatic ticket generation, listing, and deletion
* **Palestrantes:** Cadastro completo com informações biográficas, tópico da palestra e horário / Speakers: Complete registration with biographical information, presentation topic, and schedule

### Gerenciamento de Fornecedores / Vendor Management

* Cadastro de fornecedores com serviços oferecidos / Vendor registration with services offered
* Controle de status dos fornecedores (Pendente, Confirmado, etc.) / Vendor status control (Pending, Confirmed, etc.)
* Atualização de status dos serviços / Service status updates

### Gestão Financeira / Financial Management

* Definição de orçamento para o evento / Budget definition for events
* Registro de despesas com descrição, valor e data / Expense recording with description, amount, and date
* Controle de saldo e visualização das finanças do evento / Balance control and event financial overview

### Pesquisas e Feedbacks / Surveys and Feedback

* Criação de pesquisas personalizadas com múltiplas perguntas / Creation of customized surveys with multiple questions
* Coleta de feedbacks vinculados aos participantes através do número do ingresso / Feedback collection linked to participants through ticket numbers
* Visualização de todos os feedbacks recebidos / View all received feedback

---

## Estrutura do Projeto / Project Structure

### Classes Principais / Main Classes

* **Pessoa (Classe Abstrata):** Classe base para Participante e Palestrante / Base class for Participant and Speaker
* **Participante:** Representa os participantes do evento com ingresso único / Represents event participants with unique tickets
* **Speaker:** Representa os palestrantes com informações detalhadas / Represents speakers with detailed information
* **Fornecedor:** Gerencia os fornecedores de serviços para o evento / Manages service vendors for events
* **Despesa:** Controla as despesas financeiras do evento / Controls event financial expenses
* **Survey:** Gerencia as pesquisas de satisfação / Manages satisfaction surveys
* **Feedback:** Armazena os feedbacks dos participantes / Stores participant feedback
* **Evento:** Classe principal que gerencia todos os aspectos de um evento / Main class that manages all aspects of an event
* **SistemaEventos:** Sistema principal que coordena múltiplos eventos / Main system that coordinates multiple events

---

## Como Executar / How to Run

### Português

1. Certifique-se de ter **Python 3.x** instalado em seu sistema.
2. Faça o download ou clone este repositório:

   ```bash
   git clone <URL_DO_SEU_REPOSITORIO>
   ```
3. Navegue até a pasta do projeto:

   ```bash
   cd nome_da_pasta
   ```
4. Execute o script principal:

   ```bash
   python sistema_eventos.py
   ```

   > Substitua `sistema_eventos.py` pelo nome do arquivo Python principal do projeto.
5. Utilize o **menu interativo** para navegar pelas opções do sistema e gerenciar eventos, participantes, palestrantes, fornecedores, finanças e pesquisas.

### English

1. Make sure you have **Python 3.x** installed on your system.
2. Download or clone this repository:

   ```bash
   git clone <YOUR_REPOSITORY_URL>
   ```
3. Navigate to the project folder:

   ```bash
   cd folder_name
   ```
4. Run the main script:

   ```bash
   python sistema_eventos.py
   ```

   > Replace `sistema_eventos.py` with the name of the main Python file.
5. Use the **interactive menu** to navigate through system options and manage events, participants, speakers, vendors, finances, and surveys.

---

## Requisitos / Requirements

* Python 3.x
* Módulo **random** (já incluído na biblioteca padrão do Python) / Random module (included in Python standard library)

---

## Exemplos de Uso / Usage Examples

* Criar um evento com nome e data / Create an event with name and date
* Adicionar participantes com nome e email (o sistema gera ingresso automaticamente) / Add participants with name and email (system generates tickets automatically)
* Cadastrar palestrantes com biografia, tópico e horário da palestra / Register speakers with biography, topic, and presentation time
* Controlar fornecedores e seus status / Manage vendors and their statuses
* Definir orçamento e registrar despesas / Set budget and record expenses
* Criar pesquisas e coletar feedbacks dos participantes / Create surveys and collect participant feedback

---

## Características Técnicas / Technical Characteristics

* Programação orientada a objetos com herança e classes abstratas / Object-oriented programming with inheritance and abstract classes
* Gerenciamento de múltiplos eventos simultaneamente / Management of multiple simultaneous events
* Interface de linha de comando (CLI) intuitiva / Intuitive command-line interface (CLI)
* Validações de entrada de dados / Input data validation
* Geração automática de números de ingresso únicos / Automatic generation of unique ticket numbers
* Controle financeiro completo com cálculo automático de saldo / Complete financial control with automatic balance calculation

