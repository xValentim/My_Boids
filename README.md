# Boids
Neste projeto, estou fazendo um estudo dos Boids (Craig Reynolds, 1982) e como isso pode ser aplicado na natureza, em movimentos de pássaros, cardumes e etc.

### Alinhamento
Os boids são influenciados pelos seus vizinhos de modo que o vetor velocidade tende a se alinhar com a média dos vetores dos vizinhos (dentro do raio de percepção).

### Coesão
Os boids são influenciados pelos seus vizinhos de modo que existirá uma força que atua no elemento com sentido apontado para a média do vetor posição de seus vizinhos (dentro do raio de percepção).

### Separação
Os boids são influenciados pelos seus vizinhos de modo que existirá uma força que atua no elemento no sentido oposto ao da média do vetor posição dos seus vizinhos (dentro do raio de percepção).

## Como usar?
Inicie o arquivo main.py e pressione P para adicionar os boids e O para eliminar.

## Problema na implementação
Note que na simulação os boids estão fazendo uma trajetória no formato de vórtex em seus grupos. Ainda não consegui achar o erro de implementação.
