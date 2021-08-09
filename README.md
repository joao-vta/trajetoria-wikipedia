# Descrição
<img src="https://github.com/joao-vta/trajetoria-wikipedia/blob/main/imgs/wikipedia-logo.jpg" align="right"
     alt="Size Limit logo by Anton Lovchikov" width="200" height="140">
**[Trajetoria Wikipedia]** é um site que descobre a trajetória mais curta entre duas páginas da wikipédia em português. Ele faz uso de dados pré processados para executar um algoritmo de BFS nas páginas da wikipédia.  
A Lógica é executadada em um servidor AWS, e o código está dispónivel na pasta "endpoint".

# Motivo
O site ajuda procura ajduar na composição e competição do jogo **["WikiRacing"]**.

# Fonte dos dados
A wikipédia disponibiliza um **[datadump]** da maioria dos dados para uso livre. São omitidos arquivos de mídia como fotos e áudios. 

# Inspiração  
O projeto **["six degrees of wikipédia"]** de Jacob Wenger faz algo similar e foi de grande inspiração, porém fez uso de infraestrutura e investimento que esse projeto não possui, portanto utilizou meios diferentes para atacar o problema. Além disso, Ele é limitado a wikipédia em inglês.

[Trajetoria Wikipedia]: https://joao-vta.github.io/trajetoria-wikipedia/index.html
["six degrees of wikipédia"]: https://github.com/jwngr/sdow
["WikiRacing"]: https://en.wikipedia.org/wiki/Wikiracing
[datadump]: https://dumps.wikimedia.org/ptwiki/
