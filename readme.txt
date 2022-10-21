Autômato Finito Determinístico (AFD)
Descrição
Implemente um algoritmo que simule um AFD. A entrada consiste da especificação de um AFD e
de um conjunto de palavras. A saída consiste de uma lista indicando ‘S’ caso o AFD reconheça a
palavra em questão e ‘N’ caso contrário. Veja o slide ‘Algoritmo para simular AFDs’ página 26 (32)
do conjunto de slides capitulo2.pdf.

Você deve redigir um relatório técnico usando Jupyter a ser hospedado no Github. O relatório deve
conter pelo menos os seguintes tópicos: como projetou o algoritmo, quais as estruturas de dados,
como sua implementação para reconhecimento possui complexidade O(|w|), onde |w| é o tamanho
da palavra de entrada. O link para o Github contendo o código e relatório no formato Jupyter deve
ser enviado para: rlopes@ufrb.edu.br

Observação:
• Leitura e escrita na entrada/saída padrão.
• Qualquer divergência na saída com relação ao formato especificado implicará em nota zero.
• A implementação não pode fazer uso de recursão.


Entrada
Na primeira linha, há uma lista de estados. Na segunda linha, há uma lista contendo os símbolos do
alfabeto. Na terceira linha, há o número total n de transições. Para cada uma das n linhas seguintes,
há uma tripla <o,c,d> onde ‘o’ é o estado de origem, ‘c’ é o caractere e ‘d’ é o estado de destino. Em
seguida, há o estado inicial. Na próxima linha, há uma lista de estados finais. Por fim, há uma lista
de palavras de teste a ser reconhecida. Os itens da lista serão separados por espaço em branco.

Obs: O AFD de entrada não é necessariamente completo, ou seja, transições para o estado de erro
podem não estar representadas.

Saída
Seu programa deve imprimir para cada palavra de teste ‘S’ se o AFD reconhece a palavra ou ‘N’
caso contrário.

Exemplos
Entrada                Saída
0 1                      S
a b                      N
3                        S    
0 a 1                    S
1 a 1                    N
1 b 1
0
1
a b aba abb b

