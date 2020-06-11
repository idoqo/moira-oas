SPEC_FILE = swagger.yml
CLIENTS_DIR = ~/lab/gsoc/moira/clients

merge-spec:
	swagger-cli bundle main.yml -o $(SPEC_FILE) -t yaml
generate-py:
	openapi-generator generate -g python -i $(SPEC_FILE) -o $(CLIENTS_DIR)/python
generate-go:
	openapi-generator generate -g go -i $(SPEC_FILE) -o $(CLIENTS_DIR)/go
generate-ts:
	openapi-generator generate -g typescript-node -i $(SPEC_FILE) -o $(CLIENTS_DIR)/ts-node
generate-cs:
	openapi-generator generate -g csharp -i $(SPEC_FILE) -o $(CLIENTS_DIR)/csharp