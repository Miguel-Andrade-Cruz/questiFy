# questiFy: questões a pronta entrega
## O que é e porque o questiFy?
Pensado para professores, o questiFy foi desenvolvido para que consigam mais tempo para desenvolver suas aulas da melhor maneira possível, focando no criativo e atrativo para os alunos. Utilizando da API do gemini, o web app consegue através dos dados indicados (matéria e conteúdo) gerar questões com o gabarito para utilizar em suas avaliações¹, economizando tempo para ser utilizado em preprarar conteúdos para as aulas.
>1: Com a devida revisão para alterações se necessário.
 


## Referência

|Código| Função |
|--|--|
| `insertKey(key: str)` | Insere a chave de API |
|`chooseModel(mdodel_name, generation_config, safety_settings)` | Define modelo e configurações necessárias para o mesmo (contém valores padrão)
| `prepareFile(path)-> genai class` | Prepara arquivo para ser tratado pelo gemini |
| `sendSimplePrompt(message, attach = False)`-> response | Envia um comando ao gemini e retorna a resposta, sem considerar histórico |
| `chatSession(prompt) -> response` | Envia um comando ao gemini e retorna uma resposta, considerando o histórico de conversa |
