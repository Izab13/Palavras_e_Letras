texto = """Oh, Sereia Serenata
Eu fiquei sabendo que cê gosta de pirata
Que contraditório cê tá dentro desse navio
No fim da viagem te deixam morrer na praia...
Ela cantou pra marinheiro ouvir
Lá da pedra, do alto, em direção ao Sol
E pra ser convidada à festa,
Só bastou sorrir
"""

def limpar_texto(texto):
     
  texto_limpo = texto.replace(",", "").replace(".", "").replace(":", "").replace("?", "").replace("!", "")
  texto_limpo = texto_limpo.replace("\n", " ")
  texto_limpo = texto_limpo.lower()

  return texto_limpo

def converter_para_lista(texto_string):

  palavras = texto_string.split(" ")

  while palavras.count(" ") > 0:
    palavras.remove(" ")

  return palavras

def gerar_frequencias(elementos):

  lista_elementos = []
  lista_frequencias = []

  for elemento in elementos:  

    if elemento in lista_elementos:

      indice = lista_elementos.index(elemento)
      lista_frequencias[indice] += 1

    else:    
      lista_elementos.append(elemento)
      lista_frequencias.append(1)  

  return [lista_elementos, lista_frequencias]

def mostrar_maiores_frequencias(lista_elementos, lista_frequencias, texto):

  for i in range(0, 5):

    indice = mostrar_maior_frequencia(lista_elementos, lista_frequencias, texto)
    lista_elementos.pop(indice)
    lista_frequencias.pop(indice)

def mostrar_maior_frequencia(lista_elementos, lista_frequencias, texto):

  indice = 0
  maior_frequencia = 0
  elemento_maior_frequencia = ""
  indice_maior_frequencia = 0

  for elemento in lista_elementos:

    if lista_frequencias[indice] > maior_frequencia:

      maior_frequencia = lista_frequencias[indice]
      elemento_maior_frequencia = elemento
      indice_maior_frequencia = indice

    indice += 1  

  print(f"A {texto} '{elemento_maior_frequencia}' apareceu {maior_frequencia} vezes")

  return indice_maior_frequencia

def mostrar_quantidade_total_palavras(palavras):

  qtd_palavras = len(palavras)
  print(f"A quantidade total de palavras é {qtd_palavras}")

def mostrar_quantidade_total_linhas(texto):

  qtd_linhas = texto.count('\n')
  print(f"A quantidade total de linhas é {qtd_linhas}")

def mostrar_maior_palavra(palavras):  

  tamanho_maior_palavra = 0
  maior_palavra = ""

  for palavra in palavras:

    tamanho_palavra = len(palavra)

    if tamanho_palavra > tamanho_maior_palavra:

      tamanho_maior_palavra = tamanho_palavra
      maior_palavra = palavra

  print(f"A maior palavra é {maior_palavra}")

texto_limpo = limpar_texto(texto)
palavras = converter_para_lista(texto_limpo)
palavras_frequencias = gerar_frequencias(palavras)

mostrar_maiores_frequencias(palavras_frequencias[0], palavras_frequencias[1], "palavra")

palavras_frequencias = gerar_frequencias(texto)

mostrar_maiores_frequencias(palavras_frequencias[0], palavras_frequencias[1], "letra")

mostrar_quantidade_total_palavras(palavras)
mostrar_quantidade_total_linhas(texto)
mostrar_maior_palavra(palavras)