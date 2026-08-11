# Fixture de teste

Este diretório existe de propósito sem `index.html`. Ele testa a checagem 2
de `tools/check_portal.py`: um diretório sem índice devolve 404 no GitHub
Pages, ao contrário de um `SimpleHTTPRequestHandler` comum, que listaria os
arquivos. Ver `tests/test_check_portal.py`.
