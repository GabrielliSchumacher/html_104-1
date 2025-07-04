#lista vazia criada para receber valores 
# lista para receber 5 valores

carrinho=[]
for i in range(5):
  produto=str(input("Digite o nome do produto:"))
  carrinho.append(produto)
  
print(f"Os valores que estão no carrinho de compras da lista de compras são {carrinho}")

