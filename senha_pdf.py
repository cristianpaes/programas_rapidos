from PyPDF2 import PdfFileWriter, PdfFileReader

def seguranca(arq, senha):
    x = PdfFileWriter()
    pdf = PdfFileReader(arq)
    for pg in range(pdf.numPages):
        x.addPage(pdf.getPage(pg))
    x.encrypt(senha)
    with open(f"Seg_{arq}", "wb") as f:
        x.write(f)
        f.close()
    print(f"Seg_{arq} Criado...")

arq = input('Digite o nome do arquivo na pasta: ')

senha = input('Digite a senha do arquivo: ')

seguranca(arq, senha)

