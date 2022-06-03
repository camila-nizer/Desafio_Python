from bs4 import BeautifulSoup
import requests
import os
import zipfile

html = requests.get(" https://www.gov.br/ans/pt-br/assuntos/consumidor/o-que-o-seu-plano-de-saude-deve-cobrir-1/o-que-e-o-rol-de-procedimentos-e-evento-em-saude").content
soup= BeautifulSoup(html,'html.parser')

comclassecallout= soup.find_all("p", class_= "callout")

temanexo=[]
nomearquivos=[]
for p in comclassecallout:
	a= p.find('a')
	texto=a.string
	if texto != None and "Anexo" in texto:
		temanexo.append(a.get('href'))
		nomearquivos.append(texto)

pastaanexos= "C:/anexos/"
if not os.path.exists(pastaanexos):
	os.makedirs(pastaanexos)

def baixar_arquivo(url, endereco, nomearquivo):
    resposta = requests.get(url)
    if resposta.status_code == requests.codes.OK:
        with open(endereco+nomearquivo, 'wb') as novo_arquivo:
                novo_arquivo.write(resposta.content)
        print("Download finalizado. Arquivo salvo em: {}".format(endereco))
    else:
        resposta.raise_for_status()

for indice in range(len(nomearquivos)):
	url=temanexo[indice]
	nomearquivo=nomearquivos[indice]
	baixar_arquivo(url,pastaanexos,nomearquivo)

anexos_zip = zipfile.ZipFile(pastaanexos+"anexoscompress.zip", 'w')
 
for folder, subfolders, files in os.walk(pastaanexos):
 
    for file in files:
        if file.endswith('(.pdf)') or file.endswith('(.xlsx)'):
            anexos_zip.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder,file), pastaanexos), compress_type = zipfile.ZIP_DEFLATED)
 
anexos_zip.close()

