<p align="center">
  <img src="./assets/images/python.png" width="300" alt="Python" /></a>
</p>

## Projeto CRUD Python - Backend
```bash
Backend em python usando mysql, flask e .env exemplificando o uso com postman

```

## Gerando aa tabela
```bash
CREATE TABLE `tb_produto` (
	`id` INT(11) NOT NULL AUTO_INCREMENT,
	`codigo` INT(11) NOT NULL,
	`produto` VARCHAR(100) NOT NULL COLLATE 'utf8mb4_general_ci',
	PRIMARY KEY (`id`) USING BTREE
)
COLLATE='utf8mb4_general_ci'
ENGINE=InnoDB
;
    
```

## Bibliotecas necessárias
## comandos iniciais para instalação do projeto
pip install mysql-connector-python
pip install flask
pip install python-dotenv

## gerando requirements
pip freeze > requirements.txt

## instalando via requirements
pip install -r requirements.txt

## executando
python back_prod.py

## Video Demo
<a href="https://youtu.be/i8g8NAyTvd8" target="_blank">Clique Aqui</a>

## suporte
```bash
WhatsApp: (85) 9 9150-8104
Mail: geraldo@gpsoft.com.br
```
