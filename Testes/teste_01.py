import requests

# Teste mais básico possível - sem usar unittest ou pytest
def testar_api():
    print("\n=== Testando API Simples ===")
    
    url = "https://reqres.in/api/users/2"
    
    print(f"Fazendo requisição para: {url}")
    resposta = requests.get(url)
    
    print("\nResultado do teste:")
    print(f"Status Code: {resposta.status_code}")
    print(f"Tempo de resposta: {resposta.elapsed.total_seconds()} segundos")
    
    if resposta.status_code == 200:
        print("✅ Sucesso! API respondeu corretamente")
        dados = resposta.json()
        print(f"Usuário encontrado: {dados['data']['first_name']} {dados['data']['last_name']}")
    else:
        print("❌ Falha! API não respondeu como esperado")

# Executa o teste diretamente
if __name__ == "__main__":
    testar_api()
