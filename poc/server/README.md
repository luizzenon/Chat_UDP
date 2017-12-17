# [PoC] server.py

## Instalando

### Criar o virtualenv

```sh
virtualenv --python=python3 .venv
```

### Ativar o virtualenv

```sh
source .venv/bin/activate
```

### Instalar o twisted

```sh
pip install twisted
```

## Usando o script

### Executar o servidor (em uma aba)

```sh
python server.py -n node-1
```

### Ler o log (em outra aba)

```sh
tail -f node-1.log
```

### Enviar mensagem (em outra aba)

```sh
echo -n "hello" | nc -4u -q1 localhost 9999
```
