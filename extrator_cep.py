import re #Regular Expression -- RegEx

endereco = "aklsmas malkdm ask maslkd masl  88032005"
padrao = re.compile("[0-9][0-9][0-9][0-9][0-9][-]?[0-9][0-9][0-9]") # define o padão de cep
busca = padrao.search(endereco) # retira no o cep do endereco
if busca:
    cep = busca.group()
    print(cep)