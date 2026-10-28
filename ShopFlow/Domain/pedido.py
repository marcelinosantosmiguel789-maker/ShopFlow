class pedido:
    def __init__(self, id, usuario_id, data_criacao, status, valor_total):
        self.id = id
        self.usuario_id = usuario_id
        self.data_criacao = data_criacao
        self.status = status
        self.valor_total = valor_total