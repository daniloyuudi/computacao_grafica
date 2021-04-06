agenda = {
	"Benedita Sophia Souza": "(21) 2840-6476",
	"Isabela Louise Adriana Ribeiro": "(61) 2933-1950",
	"Bento Fábio Oliveira": "(48) 3796-5140"
}

print("=== AGENDA ===")


continuar = True

while continuar:
	print("\n[1] Incluir um novo contato")
	print("[2] Consultar um contato individual")
	print("[3] Alterar um contato")
	print("[4] Excluir um contato")
	print("[5] Mostrar agenda completa")
	print("[6] Sair da agenda\n")

	opcao = input("Opção> ")

	if opcao == "1":
		nome = input("Digite o nome> ")
		telefone = input("Digite o telefone> ")
		agenda[nome] = telefone
	elif opcao == "2":
		nome = input("Digite o nome> ")
		print("O telefone é ", agenda[nome])
	elif opcao == "3":
		nome = input("Digite o nome> ")
		telefone = input("Digite o telefone> ")
		agenda[nome] = telefone
	elif opcao == "4":
		nome = input("Digite o nome> ")
		del agenda[nome]
	elif opcao == "5":
		for key in agenda:
			print("\nNome: ", key)
			print("Telefone: ", agenda[key])
	elif opcao == "6":
		continuar = False

