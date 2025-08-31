import random
from abc import ABC, abstractmethod


# Clase Abstrata --> SuperClass
class Pessoa(ABC):
    def __init__(self, nome, email):
        self._nome = nome
        self._email = email

    @property
    def nome(self):
        return self._nome

    @property
    def email(self):
        return self._email

    @abstractmethod
    def exibir_info(self):
        """Cada subclasse deve implementar sua própria forma de exibir informações"""
        pass


# Participante -- Herança --> Pessoa
class Participante(Pessoa):
    def __init__(self, nome, email):
        super().__init__(nome, email)
        self._ingresso = self._gerar_ingresso()

    def _gerar_ingresso(self):
        return f"ING{random.randint(1000, 9999)}"

    @property
    def ingresso(self):
        return self._ingresso

    def exibir_info(self):
        return f"Participante: {self.nome} ({self.email}) | Ingresso: {self.ingresso}"


# Palestrante -- Herança -> Pessoa
class Speaker(Pessoa):
    def __init__(self, nome, bio, email, topico, horario):
        super().__init__(nome, email)
        self.bio = bio
        self.topico = topico
        self.horario = horario

    def exibir_info(self):
        return f"Palestrante: {self.nome} | Tópico: '{self.topico}' às {self.horario} ({self.email})"


# Despesa
class Despesa:
    def __init__(self, descricao, valor, data):
        self.descricao = descricao
        self.valor = float(valor)
        self.data = data


# Pesquisa
class Survey:
    def __init__(self, titulo, perguntas):
        self.titulo = titulo
        self.perguntas = perguntas


# Feedback
class Feedback:
    def __init__(self, ingresso, respostas):
        self.ingresso = ingresso
        self.respostas = respostas


# Fornecedores
class Fornecedor:
    def __init__(self, nome, servico, contato=None):
        self.nome = nome
        self.servico = servico
        self.contato = contato
        self._status = "Pendente"

    @property
    def status(self):
        return self._status

    def atualizar_status(self, novo_status):
        self._status = novo_status
        print(f"Status de '{self.nome}' atualizado para {self._status}.")


# Evento
class Evento:
    def __init__(self, nome, data):
        self.nome = nome
        self.data = data
        self.participantes = {}
        self.fornecedores = []
        self._budget = 0.0
        self.expenses = []
        self.surveys = []
        self.feedbacks = []
        self.speakers = []

    # Participantes
    def adicionar_participante(self, participante: Participante):
        self.participantes[participante.ingresso] = participante

    def listar_participantes(self):
        if not self.participantes:
            print("Nenhum participante cadastrado.")
            return
        print(f"\nParticipantes de '{self.nome}':")
        for p in self.participantes.values():
            print("-", p.exibir_info())

    def excluir_participante(self, ingresso):
        if ingresso in self.participantes:
            nome = self.participantes[ingresso].nome
            del self.participantes[ingresso]
            print(f"Participante '{nome}' removido.")
        else:
            print("Ingresso não encontrado.")

    # Palestrantes
    def adicionar_speaker(self, sp: Speaker):
        self.speakers.append(sp)
        print(f"Palestrante '{sp.nome}' adicionado.")

    def listar_speakers(self):
        if not self.speakers:
            print("Nenhum palestrante cadastrado.")
            return
        print(f"\nPalestrantes de '{self.nome}':")
        for sp in self.speakers:
            print("-", sp.exibir_info())

    def remover_speaker(self, índice):
        try:
            rem = self.speakers.pop(índice)
            print(f"Palestrante '{rem.nome}' removido.")
        except IndexError:
            print("Índice inválido.")

    # Fornecedores
    def adicionar_fornecedor(self, fornecedor):
        self.fornecedores.append(fornecedor)

    def listar_fornecedores(self):
        if not self.fornecedores:
            print("Nenhum fornecedor cadastrado.")
            return
        print(f"\nFornecedores de '{self.nome}':")
        for i, f in enumerate(self.fornecedores):
            print(f"{i}. {f.nome} | Serviço: {f.servico} | Status: {f.status}")

    def atualizar_fornecedor(self, índice, status):
        try:
            self.fornecedores[índice].atualizar_status(status)
        except IndexError:
            print("Índice inválido.")

    # Finanças 
    def definir_orcamento(self, valor):
        self._budget = float(valor)
        print(f"Orçamento definido: R${self._budget:.2f}")

    def registrar_despesa(self, descricao, valor, data):
        d = Despesa(descricao, valor, data)
        self.expenses.append(d)
        print(f"Despesa '{descricao}' de R${valor:.2f} em {data} registrada.")

    def ver_financas(self):
        total = sum(d.valor for d in self.expenses)
        saldo = self._budget - total
        print(f"Orçamento: R${self._budget:.2f}")
        print(f"Total gasto: R${total:.2f}")
        print(f"Saldo: R${saldo:.2f}")

    # Pesquisas e Feedback
    def criar_survey(self, titulo, perguntas):
        survey = Survey(titulo, perguntas)
        self.surveys.append(survey)
        print(f"Survey '{titulo}' criada.")

    def coletar_feedback(self, ingresso):
        if ingresso not in self.participantes:
            print("Ingresso não encontrado.")
            return
        if not self.surveys:
            print("Nenhuma pesquisa disponível.")
            return
        survey = self.surveys[-1]
        respostas = {}
        print(f"Survey: {survey.titulo}")
        for p in survey.perguntas:
            respostas[p] = input(f"{p} ")
        fb = Feedback(ingresso, respostas)
        self.feedbacks.append(fb)
        print("Feedback registrado.")

    def listar_feedbacks(self):
        if not self.feedbacks:
            print("Nenhum feedback registrado.")
            return
        print(f"\nFeedbacks de '{self.nome}':")
        for fb in self.feedbacks:
            print(f"Ingresso: {fb.ingresso}")
            for p, r in fb.respostas.items():
                print(f"- {p}: {r}")


# Gerenciamento
class SistemaEventos:
    def __init__(self):
        self.eventos = {}

    def selecionar_evento(self):
        if not self.eventos:
            print("Nenhum evento cadastrado.")
            return None
        print("\nEventos disponíveis:")
        for i, (n, e) in enumerate(self.eventos.items()):
            print(f"{i}. {n} (Data: {e.data})")
        try:
            idx = int(input("Selecione o evento: "))
            return list(self.eventos.keys())[idx]
        except (ValueError, IndexError):
            print("Seleção inválida.")
            return None

    # Menu
    def menu(self):
        while True:
            print("\n====== MENU PRINCIPAL ======")
            print("1. Gerenciar Evento")
            print("2. Gerenciar Participantes")
            print("3. Gerenciar Palestrantes")
            print("4. Gerenciar Fornecedores")
            print("5. Gerenciar Finanças")
            print("0. Sair")
            opc = input("Opção: ")
            if   opc == '1': self.gerenciar_evento()
            elif opc == '2': self.gerenciar_participante()
            elif opc == '3': self.gerenciar_speakers()
            elif opc == '4': self.gerenciar_fornecedores()
            elif opc == '5': self.gerenciar_financas()
            elif opc == '0':
                print("Encerrando...")
                break
            else:
                print("Inválido.")

    # Evento(s)
    def gerenciar_evento(self):
        while True:
            print("\n--- GERENCIAR EVENTO ---")
            print("1. Criar evento")
            print("2. Cancelar evento")
            print("3. Listar eventos")
            print("4. Criar pesquisa de satisfação")
            print("5. Coletar feedback")
            print("6. Listar feedbacks")
            print("0. Voltar")
            op = input("Opção: ")
            if   op == '1': self.criar_evento()
            elif op == '2': self.cancelar_evento()
            elif op == '3': self.listar_eventos()
            elif op == '4': self.criar_survey_evento()
            elif op == '5': self.coletar_feedback_evento()
            elif op == '6': self.listar_feedbacks_evento()
            elif op == '0': break
            else: print("Inválido.")

    def criar_evento(self):
        nome = input("Nome: ")
        if nome in self.eventos:
            print("Já existe.")
            return
        data = input("Data (dd/mm/aaaa): ")
        self.eventos[nome] = Evento(nome, data)
        print(f"'{nome}' criado.")

    def cancelar_evento(self):
        select = self.selecionar_evento()
        if select:
            del self.eventos[select]
            print(f"'{select}' cancelado.")

    def listar_eventos(self):
        if not self.eventos:
            print("Nenhum cadastrado.")
            return
        for e in self.eventos.values():
            print(f"- {e.nome} ({e.data})")

    def criar_survey_evento(self):
        sel = self.selecionar_evento()
        if not sel: return
        perguntas = []
        titulo = input("Título da pesquisa: ")
        print("Digite perguntas (vazio para encerrar):")
        while True:
            p = input("> ")
            if not p: break
            perguntas.append(p)
        self.eventos[sel].criar_survey(titulo, perguntas)

    def coletar_feedback_evento(self):
        sel = self.selecionar_evento()
        if not sel: return
        ingresso = input("Ingresso: ")
        self.eventos[sel].coletar_feedback(ingresso)

    def listar_feedbacks_evento(self):
        sel = self.selecionar_evento()
        if not sel: return
        self.eventos[sel].listar_feedbacks()

    # Participantes
    def gerenciar_participante(self):
        while True:
            print("\n--- GERENCIAR PARTICIPANTE ---")
            print("1. Adicionar participante")
            print("2. Listar participantes")
            print("3. Excluir participante")
            print("0. Voltar")
            op = input("Opção: ")
            if   op == '1': self.adicionar_participante_evento()
            elif op == '2': self.listar_participantes_evento()
            elif op == '3': self.excluir_participante_evento()
            elif op == '0': break
            else: print("Inválido.")

    def adicionar_participante_evento(self):
        sel = self.selecionar_evento()
        if not sel: return
        n = input("Nome: "); e = input("Email: ")
        p = Participante(n, e)
        self.eventos[sel].adicionar_participante(p)
        print(f"Ingresso: {p.ingresso}")

    def listar_participantes_evento(self):
        sel = self.selecionar_evento()
        if not sel: return
        self.eventos[sel].listar_participantes()

    def excluir_participante_evento(self):
        sel = self.selecionar_evento()
        if not sel: return
        i = input("Ingresso: ")
        self.eventos[sel].excluir_participante(i)

    # Palestrantes 
    def gerenciar_speakers(self):
        while True:
            print("\n--- GERENCIAR PALESTRANTES ---")
            print("1. Adicionar palestrante")
            print("2. Listar palestrantes")
            print("3. Remover palestrante")
            print("0. Voltar")
            op = input("Opção: ")
            if   op == '1': self.adicionar_speaker_evento()
            elif op == '2': self.listar_speakers_evento()
            elif op == '3': self.remover_speaker_evento()
            elif op == '0': break
            else: print("Inválido.")

    def adicionar_speaker_evento(self):
        sel = self.selecionar_evento()
        if not sel: return
        n = input("Nome: "); bio = input("Bio: ")
        email = input("Email: "); top = input("Tópico: ")
        hr = input("Horário: ")
        sp = Speaker(n, bio, email, top, hr)
        self.eventos[sel].adicionar_speaker(sp)

    def listar_speakers_evento(self):
        sel = self.selecionar_evento()
        if not sel: return
        self.eventos[sel].listar_speakers()

    def remover_speaker_evento(self):
        sel = self.selecionar_evento()
        if not sel: return
        idx = int(input("Índice do palestrante: "))
        self.eventos[sel].remover_speaker(idx)

    # Fornecedores
    def gerenciar_fornecedores(self):
        while True:
            print("\n--- GERENCIAR FORNECEDORES ---")
            print("1. Adicionar fornecedor")
            print("2. Listar fornecedores")
            print("3. Atualizar status de fornecedor")
            print("0. Voltar")
            op = input("Opção: ")
            if   op == '1': self.adicionar_fornecedor_evento()
            elif op == '2': self.listar_fornecedores_evento()
            elif op == '3': self.atualizar_status_fornecedor_evento()
            elif op == '0': break
            else: print("Inválido.")

    def adicionar_fornecedor_evento(self):
        sel = self.selecionar_evento()
        if not sel: return
        n = input("Nome: "); s = input("Serviço: ")
        c = input("Contato (opcional): ") or None
        f = Fornecedor(n, s, c)
        self.eventos[sel].adicionar_fornecedor(f)

    def listar_fornecedores_evento(self):
        sel = self.selecionar_evento()
        if not sel: return
        self.eventos[sel].listar_fornecedores()

    def atualizar_status_fornecedor_evento(self):
        sel = self.selecionar_evento()
        if not sel: return
        idx = int(input("Índice do fornecedor: "))
        st = input("Novo status: ")
        self.eventos[sel].atualizar_fornecedor(idx, st)

    # Orçamento/Finanças 
    def gerenciar_financas(self):
        while True:
            print("\n--- GERENCIAR FINANÇAS ---")
            print("1. Definir orçamento")
            print("2. Registrar despesa")
            print("3. Ver finanças")
            print("0. Voltar")
            op = input("Opção: ")
            if   op == '1': self.definir_orcamento_evento()
            elif op == '2': self.registrar_despesa_evento()
            elif op == '3': self.ver_financas_evento()
            elif op == '0': break
            else: print("Inválido.")

    def definir_orcamento_evento(self):
        sel = self.selecionar_evento()
        if not sel: return
        val = input("Valor orçamento: R$")
        self.eventos[sel].definir_orcamento(val)

    def registrar_despesa_evento(self):
        sel = self.selecionar_evento()
        if not sel: return
        d = input("Descrição: ")
        v = float(input("Valor: R$"))
        dt = input("Data: ")
        self.eventos[sel].registrar_despesa(d, v, dt)

    def ver_financas_evento(self):
        sel = self.selecionar_evento()
        if not sel: return
        self.eventos[sel].ver_financas()
# Menu
if __name__ == "__main__":
    SistemaEventos().menu()
