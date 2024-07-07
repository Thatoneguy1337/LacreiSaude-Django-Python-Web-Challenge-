# LacreiSaude-Django-Python-Web-Challenge-

Este é um projeto de desafio feito em Django-Python, feito utilizando Django-RestFramework, utilizando testes unitários e PostgresSQl como nosso banco de dados relacional, afim de demonstrar as minhas habilidades como dev backend para a LacreiSaude, este projeto contém 11 endpoints funcionais e foi feito no intuito de que o usuário consigar agendar um tratamento médico com uma pessoa profissional cadastrada em nosso banco de dados do projeto.

Esta aplicação roda na porta: http://127.0.0.1:8000/


# Endpoints
  

| HTTP Method | Description            | Endpoint                            | Authentication Required |
| ----------- | ---------------------- | ----------------------------------  | ----------------------- |
| POST        | Register professional  | `api/professionals/`                | No Authentication       |
| PATCH       | Update professional    | `api/professionals/:id/`            | No Authentication       |             
| GET         | List All professionals | `api/professionals/all/`            | No Authentication       |
| GET         | Get professional       | `api/professionals/:id/`            | No Authetication        |
| DELETE      | Delete professional    | `api/professionals/:id/`            | No Authentication       |
| POST        | Create Schedules       | `api/schedules/`                    | No Authentication       |
| GET         | List all schedules     | `api/schedules/all/`                | No Authentication       |
| GET         | Retrieve schedules     | `api/schedules/:id/`                | No Authentication       |
| PATCH       | Update schedules       | `api/schedules/:id`                 | No Authentication       |
| GET         | Get schedules          | `api/schedules/:id`                 | No Authentication       |
| GET         | Get schedules          | `api/schedules/?professional_id=2`  | No Authentication       |

# Instalando Dependências

```bash

# Crie um ambiente virtual
python -m venv venv
source venv/bin/activate  # Para Linux/macOS
venv\Scripts\activate  # Para Windows

# Instale as dependências 
pip install -r requirements.txt

# Aplique as migrações
python manage.py makemigrations
python manage.py migrate

# Rodando o servidor
python manage.py runserver

# Rodando o teste
python manage.py test

```

## Testando as Rotas


<h2 align ='center'>Cadastrando Profissionais</h2>

Nesta rota é possível que o profissional seja cadastrado no banco de dados

```json
{
	 "fullname":"Roberta Peres",
	 "profession":"Medical Doctor",
	 "address": "Rua Itajubara, 145",
	 "contact": "9999-9999"
}
```

`POST api/professionals/ - FORMATO DA RESPOSTA - STATUS 201`

```json
{
	"id": 1,
	"fullname": "Roberta Peres",
	"profession": "Medical Doctor",
	"address": "Rua Itajubara, 145",
	"contact": "9999-9999",
	"socialname": null
}
```

<h2 align ='center'>Listando Profissionais</h2>

Nesta rota é possível buscar todos os profissionais cadastrados

NO BODY

`GET api/professionals/all/ - FORMATO DA RESPOSTA - STATUS 200`

```json
{
	"id": 1,
	"fullname": "Roberta Peres",
	"profession": "Medical Doctor",
	"address": "Rua Itajubara, 145",
	"contact": "9999-9999",
	"socialname": null
},
{
		"id": 2,
		"fullname": "John Doe",
		"profession": "Dentist",
		"address": "Rua Itajubara, 145",
		"contact": "9999-9999",
		"socialname": "AL"
},
{
		"id": 3,
		"fullname": "Jane Doe",
		"profession": "Nutritionist",
		"address": "Rua Itajubara, 145",
		"contact": "9999-9999",
		"socialname": "JD"
}

```

<h2 align ='center'>Editando Profissionais</h2>

Nesta rota é possível atualizar dados de um profissional cadastrado

```json
    {
     
	"socialname": "RP"     
      }
```

`PATCH api/professionals/:id/ - FORMATO DA RESPOSTA - STATUS 200`

```json
{
	"id": 1,
	"fullname": "Roberta Peres",
	"profession": "Medical Doctor",
	"address": "Rua Itajubara, 145",
	"contact": "9999-9999",
	"socialname": "RP"
}

```

<h2 align ='center'>Procurando Profissional</h2>

Nesta rota é possível procurar dados de um profissional cadastrado

NO BODY

`GET api/professionals/:id/ - FORMATO DA RESPOSTA - STATUS 200`

NO RETURN

<h2 align ='center'>Deletando Profissional</h2>

Nesta rota é possível procurar deletar um profissional cadastrado

NO BODY

`DELETE api/professionals/:id/ - FORMATO DA RESPOSTA - STATUS 200`

NO RETURN

<h2 align ='center'>Agendando uma consulta</h2>

Nesta rota é possível agendar uma consulta com um profissional cadastrado

NO BODY

`DELETE api/professionals/:id/ - FORMATO DA RESPOSTA - STATUS 200`

NO RETURN



 





  






