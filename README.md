# Django: Página de cadastro de empréstimos :brazil: 

## Conteúdos
  * [Visão Geral](#visão-geral)
  * [Tecnologias Utilizadas](#tecnologias-utilizadas)
  * [Aspectos Técnicos](#aspectos-técnicos)

## Visão Geral
Este aplicativo, desenvolvido com a framework Django, visa ser um modelo básico de site de cadastro de empréstimo. No qual o usuário pode cadastrar sua proposta e o sistema decidirá o resultado da análise. O administrador do sistema também poderá adicionar campos customizados para a proposta, através do Django Admin.


## Tecnologias Utilizadas
[<img target="_blank" src="https://cdn.iconscout.com/icon/free/png-512/django-2-282855.png" width=170>](https://www.djangoproject.com/)
[<img target="_blank" src="https://forthebadge.com/images/badges/made-with-python.svg" width=170>](https://www.python.org/)
[<img target="_blank" src="https://images.g2crowd.com/uploads/product/image/social_landscape/social_landscape_8a31c306355eb532650043bf039d70a7/python-celery.png" width=170>](https://docs.celeryq.dev/en/stable/)
[<img target="_blank" src="https://logosmarcas.net/wp-content/uploads/2021/03/Docker-Emblema.jpg" width=170>](https://www.docker.com/)


## Aspectos Técnicos
-Versão do Python: 3.8.10

-Versão do Django: 4.2.2

-Versão do Docker: 24.0.2

-Super usuário (para logar no admin):
```
Usuário = useradmin

Senha = Mundo098@
```
-Comandos para iniciar o sistema:
```
docker-compose up --build
```

-Links de acesso:
```
Página Principal: http://0.0.0.0:8080/
Django Admin: http://0.0.0.0:8080/admin
```

-Página de cadastro:
Na página de cadastro, todos os campos customizados adicionados pelo administrador serão exibidos para o usuário. 
Quando o mesmo apertar no botão 'Confirmar', a proposta será salva, inicialmente com o campo 'Status' = 'Em Análise'.
Depois de salva, a proposta entrará na tarefa do celery, que rodará uma função para retornar um valor aleatório, dependendo do valor, a proposta será 'Aceita' ou 'Negada'.

-Django Admin:
Para verificar todas as propostas cadastradas, basta ir no modelo 'Propostas'.
Para cadastrar campos customizados para as propostas, acesse o modelo 'Campos Customizados'.
Para visualizar todas as respostas aos campos customizados, acesse o o modelo 'Respostas'.
