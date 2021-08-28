alunos = []
print("1 - Cadastrar aluno\n2 - Remover aluno\n3 - Listar aluno\n4 - Encerrar programa\n")
opcao = int(input("Digite o numero da operação desejada: "))
print()
while opcao != 4:
    if opcao == 1:
        alunos.append(input("Digite o nome do aluno a ser cadastrado: "))
    elif opcao == 2:
        nome = input("Digite o nome do aluno a ser excluido da face da terra: ")
        print()
        try:
            alunos.remove(nome)
        except:
            print("Aluno não encontrado, tente novamente :(")
    elif opcao == 3:
        for aluno in alunos:
            print(f"_{aluno}_")
    else:
        print("Opção não disponivel, tente novamente :(")
    print("\n1 - Cadastrar aluno\n2 - Remover aluno\n3 - Listar aluno\n4 - Encerrar programa\n")
    opcao = int(input("Digite o numero da operação desejada: "))
    print()

