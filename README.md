# Appinio test ai backend app
This project is using:
- Python
- Langchain for text preparation, summarization and openai api handling
- Openai for using their api
- Flask for Rest API decorators & serving requests
- Gunicorn for scaling & multi-threads serving
- SQLAlchemy + Postgresql for ORM/CRUD

##### All environment variables
```
OPENAI_API_KEY=sk-**** # your api key here
OPENAI_MODEL_NAME=gpt-3.5-turbo-1106 # gpt-4-turbo-preview
POSTGRESQL_URL=postgresql://user:password@host:port/db # ?sslmode=require for production
CORS_ALLOWED_ORIGIN=http://localhost:5173
```

##### For development:
To run it, do the following:
- `copy .env.example into .env and fill env variables`
- `pipenv shell` <-- redo this on .env file changes
- `pipenv install`
- `./start.sh`
- `restart ./start.sh on code change to apply changes`

##### For production:
To test production build, run this from the main project folder where Pipfile is located:
- `docker build . --tag registry.digitalocean.com/appinio/backend`
- `docker run --name appinio_backend --env-file .env --rm -it -p 5000:5000 registry.digitalocean.com/appinio/backend`

##### Testing server
```
# Remove "| jq" part at the end, if you don't have "jq" utility
# To create summary
curl -sS -X POST http://127.0.0.1:5000/summary -H "Content-Type: application/json" -d "{\"content\":\"Perform summary on this text.\"}" | jq
# To get created summary
curl -sS -X GET http://127.0.0.1:5000/summary | jq
```

##### For deployment:
```
DOCKER_USERNAME=Digicalocean_username_here
DOCKER_PASSWORD=Digicalocean_api_token_here
docker login registry.digitalocean.com -u="${DOCKER_USERNAME}" -p="${DOCKER_PASSWORD}"
docker push registry.digitalocean.com/appinio/backend
```

##### TODO
- `Integrate map reduce summarization technique`
- `Integrate refine summarization technique`
- `Integrate LLamaIndex for tree summarization and others built-in methods`
- `Implement summarization evaluation for metrics, to see improvements changes`
- `Improve LLM summarization with GPT-4, different techniques, like Chain of Thought, Tree of Thoughts, Graph of Thoughts.`
- `Fine-tune LLM for a specific areas, implement semantical router for MoE (Mixture of Experts), to route specific domain requests to a fine-tuned expert LLM`
- `Tune Prompts and LLM settings`
- `Integrate RAG with indexed openly available marketing material and best practices`
- `Integrate Graph Knowledge with Neo4j database to boost RAG feature, based on openly available marketing relationships and historical data`
- `Authentication & Authorization via signed JWT and its claims, use RBAC if required`
- `OpenAPI specification definition & integration with Flask`
- `Docs generation based on OpenAPI spec`
- `Docs hosting/serving with testing calls`
- `Kubernetes cluster deployment & configuration`
- `Helm chart for Kubernetes deployment, using above docker image`
- `L7 Load Balancer and service/ingress configuration to work with backend docker image`
- `Git repository && CI/CD configuration for building & deployment into kubernetes`
- `Kafka cluster deployment & integration for improved generation & load handling with queues`
- `Websockets for LLM generation delivery in live mode or when it's finished if queued in Kafka`
- `LLM generation streaming via Websockets`
- `DB cluster for scaling`
