# Testes de Software

Este repositório contém um projeto simples de um sistema de cálculo de salário, desenvolvido como parte de um estudo sobre Testes de Software. O objetivo principal deste projeto é demonstrar a aplicação de testes de nível de unidade utilizando a técnica de caixa preta, baseada em especificação.

## Requisitos de Negócio

Os requisitos de negócio para o software podem ser encontrados no arquivo `requisitos.pdf`. Este documento descreve as regras de negócio do sistema, que incluem:

- Cálculo do salário base com base no tempo de contrato.
- Cálculo da comissão com base no valor total das vendas do funcionário.

## Estrutura do Projeto

O projeto está organizado da seguinte forma:

- `requisitos.pdf`: Documento que descreve as regras de negócio do sistema.
- `src/`: Pasta que contém o código-fonte do sistema.
  - `vendedor.py`: Módulo contendo a implementação das funcionalidades relacionadas aos vendedores.
- `tests/`: Pasta que contém os testes de unidade do sistema.
  - `test_calcular_salario_base.py`: Arquivo de teste para a função de cálculo do salário base.
  - `test_calcular_comissao.py`: Arquivo de teste para a função de cálculo da comissão.

## Testes de Unidade

Os testes de unidade são aplicados para validar as funções `calcular_salario_base` e `calcular_comissao`. Essas funções são cruciais para o funcionamento do sistema e, portanto, são alvo de testes automatizados.

### Técnica de Caixa Preta

Os testes são baseados na técnica de caixa preta, onde os testes são projetados com base nas especificações do software, sem considerar sua implementação interna. Isso ajuda a garantir que o software funcione conforme esperado, independentemente de como ele é implementado.

### Especificações de Teste

Os testes são projetados com base nas seguintes especificações:

- Particionamento em Classes de Equivalência: As entradas são divididas em classes de equivalência, onde cada classe representa um conjunto de entradas que devem produzir resultados semelhantes. Isso ajuda a garantir uma cobertura abrangente dos cenários de teste.
- Análise de Valor Limite: Os testes incluem valores nos limites das classes de equivalência, bem como valores que estão fora desses limites, para garantir que o software lide corretamente com esses casos extremos.

## Automação dos Testes com GitHub Actions

Este projeto utiliza o GitHub Actions para automatizar a execução dos testes de unidade sempre que um novo código é enviado (push) para a branch main. Essa automação faz parte das práticas de Integração Contínua (CI), garantindo que todos os testes sejam executados automaticamente e que qualquer erro ou falha seja identificado imediatamente antes de mais alterações serem introduzidas no código base.

## Importância dos Testes

Os testes em um software são essenciais para garantir sua qualidade e confiabilidade. Eles ajudam a identificar e corrigir erros de forma precoce no ciclo de desenvolvimento, reduzindo o custo e o risco de falhas no software em produção. Além disso, os testes fornecem uma documentação viva do comportamento esperado do software, facilitando a manutenção e evolução do sistema ao longo do tempo.
