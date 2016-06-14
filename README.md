# requirements-allocation
Esse projeto está sendo desenvolvido como produto do Trabalho de Graduação da aluna Priscila dos Santos Araújo
para o curso de Bacharelado em Sistemas de Informação na Universidade Federal Rural de Pernambuco.

**Aluna:** Priscila dos Santos Araújo

**Orientador:** Gabriel Alves

**Coorientadora:** Suzana Sampaio

**Trabalho:** Um ambiente para verificação de Requisitos de Software com Alocação Automatizada ([link](https://www.overleaf.com/read/dthyfqtzqgms))

O objeto principal deste projeto é a implementação de um algoritmo de alocação automatizada, utilizando algoritmos genétivos, com o intuito de alocar requisitos de software a analistas, para que a revisão de software em equipes distribuídas seja facilitada.

## Algoritmo de Alocação 

Problemas clássicos de otimização combinatória pertencentes à classe NP-hard são discutidos vastamente na literatura. Problemas NP-hard são aqueles onde determinar uma solução ótima para o problema, em um período de tempo aceitável, não é uma tarefa simples. A utilização de métodos exatos para solucionar problemas deste tipo chegam a consumir tempos de ordem exponencial. Consequentemente, torna-se impraticável a utilização de algoritmos determinísticos para resolução de problemas desta classe. Desta forma, é preciso recorrer a técnicas não-determinísticas na tentativa de se obter uma boa solução, próxima a uma solução ótima.

## Algoritmos Genéticos

Algoritmos Genéticos, uma das classes de algoritmos evolucionários mais conhecidas, são baseados em uma população de cromossomos, permitindo mutações aleatórias e operadores de cruzamento. Os operadores de cruzamento são um modo de rearranjar informações englobadas nos cromossomos dos pais, trazendo filhos que tornam-se novos pontos no espaço de busca.

## O que esse algoritmo será capaz de realizar?

Partindo de duas entradas:
* lista de requisitos de software previamente analisados por um analista de requisitos
* lista de analistas de requisitos 

Será possível alocar os requisitos a analistas baseando-se em critérios como: complexidade do requisito, categoria do requisito, disponibilidade do analista, experiência do analista e competência do analista na categoria.
