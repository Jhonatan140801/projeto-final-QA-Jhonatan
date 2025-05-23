print("=== TESTE MAIS SIMPLES ===")

def somar(a, b):
    """Função simples para teste"""
    return a + b

# Teste manual sem framework
resultado = somar(2, 3)
print(f"2 + 3 = {resultado}")

if resultado == 5:
    print("✅ Teste passou!")
else:
    print("❌ Teste falhou!")
