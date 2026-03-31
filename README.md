# LeitorPDF

Script em Python para extrair termos únicos de um PDF a partir de um prefixo.

## Requisitos

- Python 3.8+ (recomendado)
- pacotes:
  - PyMuPDF (`pip install PyMuPDF`)
  - pandas (`pip install pandas`)

## Uso

1. Copie `main.py` e execute:

```bash
python main.py
```

2. Informe o prefixo a buscar (ex: `BRINQ_`).
3. Informe o caminho do arquivo PDF (ex: `exemplo.pdf`).
4. Informe se deseja gerar `resultados.xlsx` (s/n).

O script grava:

- `resultados.txt` com cada termo único por linha
- opcionalmente `resultados.xlsx` com tantos resultados quanto houver

## Comportamento de erro

- Se o PDF não puder ser aberto, o script pede outro caminho até conseguir abrir o arquivo.

## Exemplo

1. prefixo: `BRINQ_`
2. caminho: `.\documento.pdf`
3. gerar Excel: `s`

## Estrutura de saída

- `resultados.txt`
- `resultados.xlsx` (se solicitado)
