# Chat_UDP

<b>Introdução</b>

Este Projeto tem como propósito desenvolver um Sistema de Chat completamente descentralizado. 

Tal escolha foi motivada pelo risco em que uma arquitetura com um servidor central possui: caso o servidor fique indisponível, todas as outras estações caem. 

Seguem abaixo uma figura que ilustra a arquitetura do Sistema. Observem que não há um servidor central:

<b>Regras de Negócio</b>

ID | Descrição
------ | -----------------------------------------------------------------------
RN-01 | Todos os usuários possuem acesso a todas as mensagens da Sala.
RN-02 | As informações das conversas deverão ser sigilosas, a fim de evitar que outras pessoas que não sejam participantes possam visualizar as informações.

<b>Requisitos Funcionais</b>

ID | Descrição
------ | -----------------------------------------------------------------------
RQF01 | O Sistema deverá permitir que o Usuário mantenha as configurações do Chat UDP, preenchendo os seguintes dados: <br><br>– Nome do Usuário <br>– Nome da Sala <br>– Senha da Sala <br><br>O Sistema deverá preencher automaticamente a seguinte informação: <br><br>– ID do Usuário <br>– IP do Usuário <br>– ID da Sala <br><br>O Sistema deverá apresentar uma Sala, contendo os seguintes dados: <br><br>– Nome da Sala <br>– Nome do Usuário <br>– Campo onde ficarão as mensagens enviadas e recebidas <br>– Campo onde ficará a lista de participantes <br>– Campo onde o Usuário escreverá sua mensagem para ser enviada <br>– Botão “Enviar”
RQF02 | O Sistema deverá enviar a Mensagem de Presença para todos os outros participantes na sala. Além disso, o Sistema deverá receber a mensagem de Presença de todos os outros participantes. Tal mensagem deverá conter os seguintes dados: <br><br>– Nome do Usuário <br>– Data Hora <br>– Tipo (PRESENÇA) <br><br>Cada participante será considerado “online” , caso o Sistema receba sua Mensagem de Presença. Caso contrário, será considerado “offline”. <br><br>Dessa forma, o Sistema deverá apresentar ao Usuário a lista de participantes da Sala, contendo os seguintes dados: <br><br>– Nome do Participante
RQF03 | O Sistema deverá permitir que o Usuário envie mensagens para todos os usuários na mesma sala, preenchendo os seguintes dados: <br>Texto da Mensagem <br>Mensagem de Referência (OPCIONAL) <br><br>O Sistema deverá preencher automaticamente as seguintes informações: <br><br>– Número da Mensagem <br>– Data Hora do envio da Mensagem <br>– Nome do Usuário <br>– Tipo (MENSAGEM TEXTO) <br><br>O Sistema deverá apresentar ao Usuário as seguintes informações: <br><br>– Texto da Mensagem <br>– Mensagem de Referência (se for o caso) <br>– Número da Mensagem <br>– Data Hora do envio da Mensagem <br>– Data Hora de Recebimento de cada participante (atualizado automaticamente, assim que receber a mensagem do tipo RECIBO do referido participante) <br>– Data Hora de Lido de cada participante (atualizado automaticamente assim que receber a mensagem do tipo LEITURA do referido participante) <br>– Status de envio (não enviada ou enviada)
RQF04 | O Sistema deverá receber todas as mensagens de todos os participantes da Sala. As mensagens recebidas conterão as seguintes informações: <br><br>– Número da Mensagem <br>– Participante que enviou a Mensagem (Origem) <br>– Data Hora da Mensagem <br>– Texto <br>– Mensagem de Referência (se for o caso)
RQF05 | O Sistema deverá permitir que o Usuário LISTE todas as mensagens enviadas que ainda faltam ciência de algum dos participantes.

<b>Requisitos Não-Funcionais</b> 

ID | Descrição
------ | -----------------------------------------------------------------------
RQNF01 | O Sistema deve ter uma interface Web compatível para uso em desktop.
RQNF02 | O Sistema deve ser desenvolvido utilizando a linguagem Python.
RQNF03 | O Sistema deve persistir localmente todas as configurações e mensagens, a fim de, quando faltar energia, os dados não sejam perdidos.
RQNF04 | Todas as mensagens deverão ser enviados criptografados.
RQNF05 | As comunicações deverão ser por UDP.
RQNF06 | O Sistema deverá ser completamente descentralizado, utilizando a arquitetura de Rede Malha.

<b>Identificação de Casos de Uso</b>

ID | Descrição
------ | -----------------------------------------------------------------------
RQF01 | UCS01 - Manter Configurações
RQF02 | UCS02 - Enviar Mensagem de  Presença <br>UCS03 - Receber Mensagem de Presença
RQF03 | UCS04 - Enviar Mensagem <br>UCS11 - Referenciar Mensagem <br>UCS08 - Receber Mensagem Recibo <br>UCS09 - Receber Mensagem Lido
RQF04 | UCS05 - Receber Mensagem <br>UCS06 - Enviar Mensagem Recibo <br>UCS07 - Enviar Mensagem Lido
RQF05 | UCS11 - Listar Mensagens Enviadas Pendentes

<b>Diagrama de Casos de Uso</b> <br>
![usecase diagram0chatupd](https://user-images.githubusercontent.com/6242328/36845085-46a639a8-1d4d-11e8-9b71-5d6dc5d435bb.png)

<b>Diagrama de Atividades</b> <br>
![activity diagram0chatudp](https://user-images.githubusercontent.com/6242328/36845060-262ed37e-1d4d-11e8-9fb6-8796b00c7283.png)

<b>Diagrama de Classes</b> <br>
![chatudp_classdiagram](https://user-images.githubusercontent.com/6242328/36845031-fa579196-1d4c-11e8-8cd3-cba62a42c84d.png)

Sinta-se a vontade para contribuir como quiser ;)

















