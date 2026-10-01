"""1 - Implemente uma classe Residencia que contenha diversos cômodos, representados por objetos da classe
Comodo. Cada cômodo deve possuir um nome (como sala, cozinha, banheiro) e uma área em metros
quadrados. Os objetos da classe Comodo devem ser criados exclusivamente dentro da classe Residencia, caracterizando
uma relação de composição. Eles não devem ser acessados ou modificados diretamente fora da Residencia.
A classe Residencia deve possuir um método para calcular a área total da residência, somando as áreas de
todos os seus cômodos. Crie um programa com menu interativo no console que permita ao usuário criar uma
Residencia, adicionar cômodos, visualizar os cômodos existentes, calcular e exibir a área total da Residencia, e
encerrar o programa.

Avaliação 2

Neidiman Raposo
"""
#Relação de Composição
#A classe Comodo representa cada cômodo que fará parte de uma residência
class Comodo:
    #O método construtor recebe o nome e a área de cada cômodo
    def __init__(self, nome, area): #__ Duplo underscore têm significado especial para a linguagem Python
        #Armazena o nome recebido no objeto
        self.__nome = nome
        #Armazena a área em metros quadrados recebida no objeto
        self.__area = area

    #Métodos para acessar os dados do cômodo
    #Retorna o nome do cômodo
    def get_nome(self):
        return self.__nome

    #Retorna a área do cômodo
    def get_area(self):
        return self.__area

#A classe Residencia é responsável por armazenar e controlar seus cômodos
class Residencia:
    #Método construtor da classe Residencia
    def __init__(self):
        #A lista de cômodos pertence à residência
        self.__comodos = []

    #O objeto Comodo é criado dentro da classe Residencia
    #Recebe o nome e a área necessários para criar um novo cômodo
    def adicionar_comodo(self, nome, area):
        #Cria um novo objeto da classe Comodo dentro da própria Residencia
        novo_comodo = Comodo(nome, area)
        #Adiciona o novo cômodo à lista de cômodos da residência
        self.__comodos.append(novo_comodo)
        #Informa ao usuário que a operação foi realizada
        print("\nCômodo adicionado com sucesso!")

    #Exibe os cômodos sem permitir acesso direto à lista
    def visualizar_comodos(self):
        #Verifica se ainda não existem cômodos cadastrados
        if len(self.__comodos) == 0:
            print("\nNenhum cômodo cadastrado.")
        else:
            #Exibe o título antes da relação de cômodos
            print("\n Cômodos da Residência Raposo's")

            #Percorre todos os objetos Comodo armazenados na residência
            for comodo in self.__comodos:
                #Utiliza os métodos da classe Comodo para acessar seus dados
                print(f"Nome: {comodo.get_nome()}")
                print(f"Área: {comodo.get_area():.2f} m²")
                print("----------------------------")

    #Soma a área de todos os cômodos
    def calcular_area_total(self):
        #A variável começa em zero e receberá a soma das áreas
        area_total = 0

        #Percorre todos os cômodos existentes na residência
        for comodo in self.__comodos:
            #Obtém a área de cada cômodo e acrescenta ao total
            area_total += comodo.get_area()

        #Retorna para quem chamou o método o resultado da soma
        return area_total

#Função principal responsável pela execução e pelo menu do programa
def main():
    #Cria o objeto que representa a residência
    residencia = Residencia()

    #Mantém o menu em execução até que o usuário escolha encerrar
    while True:
        #Exibe as opções disponíveis no menu
        print("\nResidência Raposo's")
        print("1 - Adicionar Cômodo")
        print("2 - Visualizar Cômodos")
        print("3 - Calcular Área Total")
        print("4 - Encerrar o Programa")

        #Recebe a opção escolhida pelo usuário
        opcao = input("Escolha uma opção: ")

        #Opção responsável pelo cadastro de um novo cômodo
        if opcao == "1":
            #Solicita o nome do cômodo
            nome = input("\nDigite o nome do cômodo: ")

            #O try permite tratar possíveis erros na digitação da área
            try:
                #Converte a área digitada para um número decimal
                area = float(input("Digite a área do cômodo em m²: "))

                #Só permite cadastrar uma área maior que zero
                if area > 0:
                    #Envia o nome e a área para a Residencia criar o Comodo
                    residencia.adicionar_comodo(nome, area)
                else:
                    #Informa que valores iguais ou menores que zero não são aceitos
                    print("\nA área deve ser maior que zero.")

            #Captura o erro caso o usuário não digite um número válido
            except ValueError:
                print("\nDigite um valor numérico válido para a área.")

        #Opção responsável por mostrar os cômodos já cadastrados
        elif opcao == "2":
            residencia.visualizar_comodos()

        #Opção responsável por calcular e mostrar a soma das áreas
        elif opcao == "3":
            #Recebe o valor retornado pelo método calcular_area_total
            area_total = residencia.calcular_area_total()
            #Exibe a área total com duas casas decimais
            print(f"\nÁrea total da residência: {area_total:.2f} m²")

        #Opção responsável por finalizar o programa
        elif opcao == "4":
            print("\nPrograma Encerrado.")
            #Interrompe o laço while e encerra o menu
            break

        #É executado caso o usuário digite uma opção inexistente
        else:
            print("\nOpção Inválida.")

#Verifica se este arquivo está sendo executado diretamente
#Evita que a função main seja executada automaticamente caso o arquivo seja importado
if __name__ == "__main__":
    main()