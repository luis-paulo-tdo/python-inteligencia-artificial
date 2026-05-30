def obter_consolidacao(resenhas):
    qtd_positivas = 0
    qtd_negativas = 0
    qtd_neutras = 0
    lista_comentarios = []

    for resenha in resenhas:
        if resenha['avaliacao'] == 'Positiva':
            qtd_positivas += 1
        elif resenha['avaliacao'] == 'Negativa':
            qtd_negativas += 1
        else:
            qtd_neutras += 1

        lista_comentarios.append(str(resenha))

    comentarios = "#####".join(lista_comentarios)

    return comentarios, qtd_positivas, qtd_negativas, qtd_neutras