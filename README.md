🛠️ Deployment & Implementation Guide
This guide outlines the end-to-end setup of the Secure RAG Orchestrator, from infrastructure provisioning to Zero-Trust IAM configuration and API Gateway integration.
1. Core Infrastructure Provisioning
Deploy the following base resources into a single Resource Group for unified management:
Storage & Data: Create an Azure Storage Account (datastorageaccount) and a container (datastoragecontainer). Upload your source documents (PDF, Word) here.
Security: Create an Azure Key Vault (azure-ai-keyvault) for secret management.
Observability: Deploy Application Insights to enable end-to-end tracing.
2. Microsoft Foundry Setup
The AI backbone is built on the Microsoft Foundry ecosystem:
Foundry Resource: Deploy the Microsoft Foundry resource (azure-ai-foundry).
AI Hub: Create an Azure AI Hub (azure-ai-hub).
Connect the Foundry resource, Key Vault, and App Insights created in Step 1.
Enable System Assigned Identity.
Project: Create an Azure AI Hub Project (azure-ai-hub-project) linked to your Hub.
Model Deployment: Via the Foundry Portal, deploy:
Chat Completion: gpt-4o (or preferred model).
Embeddings: text-embedding-ada-002 for vectorization.
3. Knowledge Base (RAG) Configuration
Integrate your private data using Azure AI Search:
Service: Deploy Azure AI Search (azure-ai-search).
Ingestion: Use the Import Data wizard to connect the Storage Account to the AI Hub Project.
Optimization: Enable Semantic Ranker and set an indexing schedule to ensure data freshness.
🔐 4. Identity & Access Management (IAM)
Crucial: This project follows the Principle of Least Privilege (PoLP) using System-Assigned Managed Identities.
Source Component	Target Resource	Role Assignment
User Account	Resource Group	Azure AI Inference Deployment Operator
User Account	AI Search Service	Search Index Data Reader/Contributor
AI Hub	Resource Group	Azure AI Administrator
AI Search Identity	Storage Account	Storage Blob Data Reader
AI Search Identity	Foundry Resource	Cognitive Services OpenAI User
Project Identity	Project Resource	Azure AI Administrator
5. Prompt Flow Orchestration
Connections: In the Foundry Management Center, add Azure AI Search as a connection (using Entra ID Auth).
Custom Connection: Create AzureAISearchConn with variables: AZURE_SEARCH_ENDPOINT, AZURE_SEARCH_INDEX, and AZURE_SEARCH_KEY.
Flow Deployment:
Upload the source code from this repository to Prompt Flow.
Test the DAG logic to ensure the "Groundedness" guardrails are functioning.
Deploy as a Machine Learning Online Endpoint.
6. API Management (APIM) Security Layer
To secure the inference endpoint for public consumption, we front it with Azure API Management:
Instance: Deploy azure-ai-apim with System Identity enabled.
API Integration: Create a new HTTP API pointing to your Prompt Flow Inference URL (*.inference.ml.azure.com).
Governance IAM:
Assign azure-ai-apim the role of AzureML Data Scientist across the Foundry, Hub, and Project resources.
Assign Azure Machine Learning Workspace Connection Secrets Reader to allow APIM to resolve backend keys.
Policies: Implement the inbound processing rules (Rate Limiting, Caching) as defined in the /policies folder of this repo.
