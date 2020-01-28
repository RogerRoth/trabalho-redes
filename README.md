# Trabalho de Redes

Este trabalho tem como objetivo o desenvolvimento de um sistema utilizando a arquitetura Cliente-Servidor utilizando API Sockets TCP na linguagem Python. Através de uma interface terminal, a implementação consiste em estabelecer uma comunicação, entre servidor e inúmeros clientes, possibilitando a troca de mensagens, no formato pergunta-responde. Ou seja, o cliente faz uma pergunta e o server responde, seguindo sempre este sentido, o servidor nunca pergunta ao cliente. Caso o comando esteja fora do padrão pré-definido, o servidor ignora a mensagem e informa o erro.

# Objetivo
O intuito do trabalho é desenvolver uma implementação da comunicação entre Cliente-Servidor utilizando API sockets TCP, os requisitos do cliente são: 
- Implementar o envio das mensagens citadas no trabalho conforme a descrito no tópico Comandos aceitos pelo servidor; 
- Tratar retorno do servidor; 
- Exibir os resultados. 
- Enquanto os requisitos do servidor são: 
- Aguardar o recebimento de mensagens; 
- Utilizar a porta 8899 para comunicação; 
- Receber e tratar mensagens; 
- Enviar mensagens de retorno; 
- Atender mais de um cliente simultaneamente.

# Comandos aceitos pelo servidor
- **/quem**     (Retorna o nome do servidor)
- **/data**     (Retorna a data do sistema do Server)
- **/ip**       (Retorna o IP do servidor)
- **/mac**      (Retorna o MAC address do servidor)
- **/sys**      (Retorna a descrição do S.O. do servidor)
- **/dev**      (Retorna o nome do grupo)
- **/info**     (Retorna mensagens gerais do sistema)
- **/dolar**    (Retorna a cotação do dólar)
- **/trends**   (Retorna os "trend topics" do Twitter)
