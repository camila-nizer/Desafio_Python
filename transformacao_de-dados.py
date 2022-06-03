import tabula
import zipfile
import os

#Conversão do arquivo de .pdf para .csv
tabula.convert_into("C:/anexos/Anexo I - Lista completa de procedimentos (.pdf)", "C:/anexos/Anexo I - Lista completa de procedimentos.csv", output_format="csv", pages="all")
print("Arquivo convertido para .csv")

#Substituição do texto "OD" para "Seg. Odontológica" e "AMB" para "Seg. Ambulatorial"
text = open("C:/anexos/Anexo I - Lista completa de procedimentos.csv", "r") 
text = ''.join([i for i in text]) #feito para unir todas as linhas do arquivo em uma string 
text = text.replace("OD","Seg. Odontológica")
text = text.replace("AMB","Seg. Ambulatorial")
x = open("C:/anexos/Anexo I - Lista completa de procedimentos.csv","w") 
x.writelines(text) 
x.close()

print("Alterações realizadas com sucesso.")


# Zipar o csv num arquivo "Teste_{seu_nome}.zip".
pastaanexos= "C:/anexos/"

anexo_i_lista_zip = zipfile.ZipFile(pastaanexos+"Teste_Camila_Nizer.zip", 'w')
 
for folder, subfolders, files in os.walk(pastaanexos):
 
    for file in files:
        if file.endswith('.csv'):
            anexo_i_lista_zip.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder,file), pastaanexos), compress_type = zipfile.ZIP_DEFLATED)
 
anexo_i_lista_zip.close()
print("Arquivo zip ok")

