# 📌 Semáforos | Sistemas Operacionais
<p>
Crie um objeto chamado Geladeira que é capaz de suportar no máximo 10 litros de leite. Posteriormente, deve-se criar uma Thread denominada BebeLeite, que dorme por um tempo aleatório e quando acorda bebe 1 litro de leite. 
Além disso, deve-se criar mais 3 Threads (Pai, Mae e Tio) que monitoram a geladeira e compram a quantidade de leite que falta para a geladeira. Nesse contexto, ocorrerá um desafio que irá ilustrar que a "região crítica" não foi bem tratada, e que gera um problema neste ponto.
</p>

<h1>  👥Equipe: <br></h1>
<uL> 
	<li>Paulo Queiroz de Carvalho <br></li>
	<li>Rita Kassiane Santos  <br></li>
</ul>

<h1><strong>Como o problema foi resolvido</strong></h1>
<p>
No programa solicitado o problema gerado esta relacionado ao momento em que as Threads Pai, Mãe e/ou Tio, compram mais leite do que cabe na geladeira. 

Nesse contexto, usamos sicronização avançanda com semáforo, o qual pode ser usado para limitar o acesso aos recursos compartilhados com capacidade limitada. 

Primeiro, definimos um objeto semáforo - chamado de geladaObj - o qual terá a função de controlar o recurso. Todo objeto semáforo possui:
1. Um parâmetro padrão count o qual representa o número de Threads permitidos para acessar simultaneamente.
2. Um método acquire( ) o qual decrementa o valor de count em 1.
3. Um método release( ) o qual incrementa o valor de count em 1. 
Nesse contexto, esse valor é 1. 

O método definido como monitora( ) será responsável por implementar a lógica que verifica a quantidade de leite que a geladeira possui e invocará o método adicionarLeite( ) na condição em que esse valor seja menor do que 10 L. Aqui o controle de acesso será adicionado, visto que a cada chamada dessa função, deve-se permitir apenas uma invocação de adicionarLeite( ) para que não ocorra a possibilidade de se adicionar mais leite que permitido. Para isso, inicialmente chama-se o método acquire( ), e a cada loop invoca-se realease( ) para liberar.

Essa função será instanciada por 3 diferentes Threads as quais representarão Pai, Mãe e Tio e posteriormente são inicializada através do métodos start( ).
</p>
 
