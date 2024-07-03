# contador-sincrono-backend
 
# Para acessar é necessario rodar o ambiente virtual

.env/script/activate

# E então rodar o servidor com

uvicorn --reload asyncviews.asgi:application

# então ir para o local host com /sync ou /async

exemplo: http://127.0.0.1:8000/async/

# se for async vai carregar a página instantanemente juntamente com a contagem
# se for sync vai terminar a contagem para carregar a página
