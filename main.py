import fitz # PyMuPDF
import pandas as pd
import re

def extrair_termos_unicos(caminho_pdf, prefixo):
    # Tentando abrir o arquivo com o fitz
    while True:
        try:
            doc = fitz.open(caminho_pdf)
            break
        except Exception as e:
            print(f"Erro ao abrir o arquivo PDF: {e}")
            caminho_pdf = input("Caminho inválido ou erro no arquivo. Digite outro caminho para tentar novamente: ")

    # Padrão de busca para o prefixo definido seguido de qualquer caractere que não seja espaço
    padrao = re.compile(rf"{prefixo}\S*")

    # Usar o SET para garantir que não haja duplicidades
    termos_encontrados = set()

    for pagina in doc:
        # Pega todo texto da pagina atual
        texto = pagina.get_text("text")

        # Encontra todos os temos que correspondem ao prefixo definido na pagina atual
        achados = padrao.findall(texto)

        # Adiciona os termos com metodo update para garantir que não haja duplicidades
        termos_encontrados.update(achados)

    doc.close()

    # Convertendo o SET para um lista ordenada usando o SORTED
    return sorted(list(termos_encontrados))

# Pegando os inputs para deixar bem flexivel
prefixo = input("Digite o prefixo para buscar no PDF (ex: 'EX_MUITO_'): ")
caminho_pdf = input("Digite o caminho do arquivo PDF (ex: 'documento.pdf'): ")


lista_final = extrair_termos_unicos(caminho_pdf, prefixo)
print(f"Total de itens únicos encontrados: {len(lista_final)}")

with open('resultados.txt', 'w', encoding='utf-8') as resultados_txt:
    for item in lista_final:
        resultados_txt.write(f"{item}\n")
        print(f" -> {item}")

listar_excel = input("Deseja listar os resultados em um arquivo Excel? (s/n): ").strip().lower() == 's'

if listar_excel:
    df = pd.DataFrame(lista_final)
    df.to_excel('resultados.xlsx', index = False, header = False)
    print("Resultados também foram salvos em 'resultados.xlsx'")

print("Processo concluído.")
# Fim do codigo.