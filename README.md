# Sobre o projeto
O foco do projeto é recuperar dados do Spotify, limpá-los e salvá-los em um banco de dados para futura análise.

# Design
Para esse projeto, iremos utilizar Apache Airflow para automatizar o processo de ETL e executá-lo diariamente. O banco de dados a ser utilizado será o PostgreSQL. Inicialmente salvando os dados em arquivos json.

# Requisitos
- Python
- Json
- Spotipy
- Pyyaml
- Apache Airflow

Para esse projeto, é necessário registrar seu app no Spotify, assim você receberá as chaves de configuração para acesasr os dados. Siga os passos a seguir para criar seu app: [spotify authorization docs](https://developer.spotify.com/documentation/general/guides/authorization/app-settings/)  
Após receber suas chaves de acesso, crie um arquivo de configuração chamado **config.yml**, como no exemplo abaixo. Troque os XXXX pelas suas respectivas chaves de acesso:  

```yaml
spotify_keys:
  CLIENT_ID: "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
  CLIENT_SECRET: "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
```

# Próximos passos
- Limpar os dados e pegar apenas aqueles que nos interessam
- Modelar o banco para receber os dados
- Salvar os dados do Spotify no banco
- Criar o pipeline de dados com o Airflow, configurando para rodar todos os dias, uma vez por dia