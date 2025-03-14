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
