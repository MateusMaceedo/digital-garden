# Token Bucker - policer-algorithm-single-token-bucket

### Algoritmo de balde de token único

#### Conceitos de Token Bucket
Quando você aplica o policiamento de tráfego ao tráfego de entrada ou saída em uma interface, os limites de taxa e as ações especificadas na configuração do policiador são usados para aplicar um limite na taxa média de taxa de transferência na interface, ao mesmo tempo em que permitem explosões de tráfego de até um número máximo de bytes com base na carga de tráfego geral. Os policiais do Junos OS medem a conformidade do fluxo de tráfego com um limite de taxa de policiamento usando um algoritmo de balde de token. Um algoritmo baseado em um único balde de token permite a explosão de tráfego por curtos períodos, enquanto um algoritmo baseado em baldes de token duplo permite explosões de tráfego mais sustentadas.

#### Algoritmo de balde de token único
Um policial de duas cores de taxa única limita a taxa de transferência de tráfego em uma interface com base em como o tráfego está em conformidade com os valores de limite de taxa especificados na configuração do policial. Da mesma forma, um policial hierárquico limita a taxa de transferência de tráfego em uma interface com base em como os subfluxos de tráfego agregados e premium estão em conformidade com valores agregados e premium de limite de taxa especificados na configuração do policial. Para ambos os tipos de policiador de duas cores, os pacotes em um fluxo de tráfego em conformidade são categorizados como verdes, e os pacotes em um fluxo de tráfego não conforme são categorizados como vermelhos.

O algoritmo do balde de token único mede a conformidade do fluxo de tráfego com um limite de taxa de policiamento de duas cores da seguinte forma:

A taxa de chegada de tokens representa o único limite de largura de banda configurado para o policial. Você pode especificar o limite de largura de banda como um número absoluto de bits por segundo, incluindo a bandwidth-limit bps declaração. Alternativamente, apenas para policiais de duas cores de taxa única, você pode usar a bandwidth-percent percentage declaração para especificar o limite de largura de banda como uma porcentagem da velocidade da porta da interface física ou da taxa de modelagem da interface lógica configurada.

A profundidade do balde de token representa o tamanho de explosão único configurado para o policial. Você especifica o tamanho da explosão, incluindo a burst-size-limit bytes declaração.

Se o balde for preenchido até a capacidade, os tokens que chegam "transbordam" o balde e são perdidos.

Quando o balde contém tokens insuficientes para receber ou transmitir o tráfego na interface, os pacotes podem ser descartados ou então re-marcados com uma classe de encaminhamento mais baixa, um nível mais alto de prioridade de perda de pacotes (PLP) ou ambos.

#### Fundo
Ao projetar um limitador de taxa, certamente se depara com o termo Token Bucket Algorithm. Um algoritmo de token bucket funciona da seguinte forma:

Um token bucket é um contêiner que possui capacidade predefinida. Os tokens são então colocados no balde em determinadas taxas, periódica ou esporadicamente. Quando o balde estiver cheio, nenhum outro token será adicionado. Finalmente, quando o balde está cheio, as solicitações recebidas são descartadas (provavelmente vão para DLQ ou algum tipo de fila para reprocessar essas mensagens) e isso limita o tráfego de entrada em certos limites. Portanto, é um ótimo algoritmo para Rate Limiter.

Aí surge a minha pergunta: O que há de tão especial no TBA? Parece estar simplesmente limitando o número de solicitações até que o bucket ganhe tokens. Isso pode ser feito com array simples?

Antes de explicar isso, acho que vale a pena mencionar brevemente o limitador de taxa, então explicarei o que é o limitador de taxa na seção seguinte. (Se quiser ir direto para o TBA, você pode pular a seção a seguir.)

#### Limitador de taxa
O limitador de taxa em alto nível é um contador para controlar quantas solicitações são enviadas do mesmo usuário, endereço IP, etc. Se o contador for maior que o limite, a solicitação não será permitida.

Onde armazenamos contadores? Usar o banco de dados não é uma boa ideia devido à lentidão do acesso ao disco. O cache na memória é melhor porque é rápido e oferece suporte à estratégia de expiração baseada em tempo. Por exemplo, REDIS será um bom armazenamento na memória e oferece dois comandos: INCR e EXPIRE.

INCR: Aumenta o contador armazenado em 1
EXPIRE: Define um tempo limite para o contador. Se o tempo limite expirar, o contador será excluído automaticamente.

![cluster](/assets/token-bucket/1_HlwDP0ebxbMaYkcKk-H4hg.webp)

#### Referencias
> https://jgam.medium.com/rate-limiter-token-bucket-algorithm-efd86758c8ee
