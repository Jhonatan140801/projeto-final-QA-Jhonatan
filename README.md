# projeto-final-QA-Jhonatan

1. Apresentação
   
Nome completo: Jhonatn Costa Dias

Curso e semestre: GTI-5NA

Ao longo desta disciplina de Quality Assurance (QA), tive a oportunidade de expandir minha visão sobre qualidade em desenvolvimento de software. Desde os primeiros conceitos teóricos até a prática com ferramentas reais, consegui compreender como os testes se tornam parte essencial de qualquer projeto bem-sucedido. Aprendi não apenas a escrever testes automatizados, mas a enxergar a qualidade como um valor que deve ser cultivado por toda a equipe.

2. O que é Quality Assurance (QA)?
É como um escudo que protege o usuário final de erros e experiências ruins. É o processo que garante que tudo funcione como deveria, não só em termos técnicos, mas também pensando na usabilidade, segurança e desempenho do software. Enxerguei o QA como uma etapa que economiza tempo, reduz custos e aumenta a confiança nos produtos que entregamos.

3. Conceitos Aprendidos Durante o Semestre
Durante o semestre, trabalhei com vários tipos de testes e ferramentas que me mostraram o quão diversa e estratégica é a área de QA:

📌 Qualidade em Software
Entendi que qualidade não é só ausência de bugs, envolve também performance, segurança, acessibilidade e experiência do usuário.

🧪 Tipos de Testes
Unitários: testam partes isoladas do código.

Integração: verificam se diferentes partes do sistema se comunicam corretamente.

Sistema: validam o comportamento do sistema como um todo.

Aceitação: garantem que o sistema atenda às expectativas do cliente.

Regressão: asseguram que novas alterações não quebrem funcionalidades antigas.

Exploratórios: usados para encontrar erros de forma não estruturada, com base na intuição e experiência.

🧠 Planejamento e Estratégia
Aprendi a criar casos de teste bem definidos, com base em critérios de aceitação claros e objetivos.

🛠️ Ferramentas Utilizadas
Python (pytest, unittest, requests) para automação dos testes.

Google Colab para prototipar rapidamente.

GitHub para versionar o código e colaborar.

CI/CD (Integração Contínua): entendi como os testes automatizados se integram no ciclo de entrega contínua de software.

📊 Métricas e Monitoramento
Passei a valorizar a coleta de métricas como cobertura de testes e taxas de falha, que ajudam a identificar pontos de melhoria de forma contínua.

4. Ferramentas e Sites Utilizados
Reqres.in para testar chamadas de API REST

Google Colab = prototipagem online

GitHub = controle de versão e colaboração

Pytest = framework de testes simples e poderoso

Unittest (Python) = testes unitários estruturados

5. Explicação dos Testes Entregues
   
✅ Teste 01 – Validação de Formulários

Ferramenta: pytest

Objetivo: Validar formatos de e-mail e senhas conforme regras de segurança

Resultados esperados:

Aceitar apenas e-mails válidos

Senhas devem ter 8+ caracteres, 1 letra maiúscula e 1 número

Arquivo: https://colab.research.google.com/drive/10MVIeFSA4FkWrdSCXpES2yMC3SW5z0K-?usp=sharing

✅ Teste 02 – Calculadora com Testes Unitários

Ferramenta: unittest

Objetivo: Verificar operações básicas de uma calculadora e tratamento de erros

Resultados esperados:

Operações matemáticas (+, –, *, /) corretas

Erro apropriado para divisão por zero

Arquivo: https://colab.research.google.com/drive/1z_2_Ejg8bVibCEwnPJdo7KdFSrk_3O9B?usp=sharing

✅ Teste 03 – Testes de API com Requests

Ferramentas: requests + unittest

Objetivo: Testar endpoints da API pública ReqRes

Resultados esperados:

GET /users retorna status 200 com dados estruturados

POST /users cria usuários com status 201

Arquivo: https://colab.research.google.com/drive/1Ah4lPRDGCB9qnsfxRHaqmLYBJb5o3zuF?usp=sharing

6. Conclusão Final
O maior aprendizado foi entender o quanto os testes automatizados são poderosos para evitar problemas e economizar tempo no desenvolvimento. Ver a automação funcionando, especialmente com pytest, me mostrou o quanto é possível garantir qualidade com pouco código — especialmente usando recursos como parametrização para testar múltiplos cenários de forma eficiente.

Hoje enxergo a área de QA como fundamental dentro de qualquer time de desenvolvimento. Saio desta disciplina com a certeza de que qualidade não é um estágio final, mas um compromisso constante.


teste_01.py
https://colab.research.google.com/drive/10MVIeFSA4FkWrdSCXpES2yMC3SW5z0K-?usp=sharing



teste_02.py
https://colab.research.google.com/drive/1z_2_Ejg8bVibCEwnPJdo7KdFSrk_3O9B?usp=sharing
=== TESTE MAIS SIMPLES ===
2 + 3 = 5
✅ Teste passou!



teste_03.py

https://colab.research.google.com/drive/1Ah4lPRDGCB9qnsfxRHaqmLYBJb5o3zuF?usp=sharing


=== Testando API Simples ===
Fazendo requisição para: https://reqres.in/api/users/2

Resultado do teste:
Status Code: 401
Tempo de resposta: 0.307535 segundos
❌ Falha! API não respondeu como esperado
