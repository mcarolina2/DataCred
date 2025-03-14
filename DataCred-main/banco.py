class Cliente:
    def __init__(self, nome, faturamento, score_credito):
        self.nome = nome
        self.faturamento = faturamento  # Usando os setters corretamente
        self.score_credito = score_credito  # Usando os setters corretamente

    @property
    def faturamento(self):
        return self._faturamento

    @faturamento.setter
    def faturamento(self, valor):
        if valor < 0:
            raise ValueError("O faturamento não pode ser negativo.")
        self._faturamento = valor

    @property
    def score_credito(self):
        return self._score_credito

    @score_credito.setter
    def score_credito(self, valor):
        if not (0 <= valor <= 1000):
            raise ValueError("O score de crédito deve estar entre 0 e 1000.")
        self._score_credito = valor

    # Comparação de clientes pelo score de crédito
    def __gt__(self, outro):
        if not isinstance(outro, Cliente):
            raise TypeError("A comparação deve ser feita entre objetos da classe Cliente.")
        return self.score_credito > outro.score_credito

    # Método para exibir os dados do cliente
    def exibir_dados(self):
        print(f"Cliente: {self.nome}")
        print(f"Faturamento: R${self.faturamento:,.2f}")
        print(f"Score de Crédito: {self.score_credito}")
        print("-" * 30)  # Apenas para separar visualmente


class Cliente_pf(Cliente): # herança > cliente_pf herda os atributos de cliente + o cpf
    def __init__(self, nome, faturamento, score_credito,cpf):
        super().__init__(nome, faturamento, score_credito)
        self.cpf = self.validar_cpf(cpf)  # Validação do CPF

    def validar_cpf(self, cpf):
        if not (cpf.isdigit() and len(cpf) == 11):
            raise ValueError("CPF inválido. Deve conter 11 dígitos numéricos.")
        return cpf

    def exibir_dados(self):
        super().exibir_dados()
        print(f"CPF: {self.cpf}")
        print("-" * 30)

class Cliente_pj(Cliente):  # herança > cliente_pj herda os atributos de cliente + o cnpj
    def __init__(self, nome, faturamento, score_credito,cnpj):
        super().__init__(nome, faturamento, score_credito)
        self.cnpj = self.validar_cnpj(cnpj)  # Validação do CNPJ

    def validar_cnpj(self, cnpj):
        if not (cnpj.isdigit() and len(cnpj) == 14):
            raise ValueError("CNPJ inválido. Deve conter 14 dígitos numéricos.")
        return cnpj

    def exibir_dados(self):
        super().exibir_dados()
        print(f"CNPJ: {self.cnpj}")
        print("-" * 30)
        
class Banco:
    def __init__(self, nome , taxa_juros,limite_credito):
        self.nome = nome
        self.taxa_juros = taxa_juros
        self.limite_credito = limite_credito
        self.clientes = [] #o banco contém clientes

    def adicionar_cliente(self, cliente):
        if not isinstance(cliente, Cliente):
            raise TypeError("O cliente deve ser uma instância da classe Cliente.")
        self.clientes.append(cliente)


    def calcular_juros(self, cliente):
        #taxa de juros vai depender do score do cliente
        if cliente.score_credito > 750:
            juros = self.taxa_juros * 0.8  # red de 20% para scores altos
        elif cliente.score_credito < 500:
            juros = self.taxa_juros * 1.2  # aumento de 20% para scores baixos
        else:
            juros = self.taxa_juros  # mantem o padrao

        return max(juros, 0)  # evita taxa negativa

    def exibir_clientes(self):
        #lista todos os clientes do banco
        print(f"\nClientes do {self.nome}:")
        for cliente in self.clientes:
            cliente.exibir_dados()

    def avaliar_credito(self, cliente): #avalia se o cliente pode obter credito c base no score
        if cliente.score_credito >= 700:
            return f"{cliente.nome} pode obter crédito até R${self.limite_credito:,.2f}."
        else:
            return f"{cliente.nome} não tem score suficiente para obter crédito."