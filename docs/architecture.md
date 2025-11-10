# Azure Data Pipeline Architecture

This pipeline demonstrates ingestion, transformation, and visualization using:
- Azure Data Factory for orchestration
- Azure Databricks (PySpark) for transformation
- Azure SQL Database for storage
- Power BI for visualization

## Workflow
1. Upload raw CSV data into Azure Blob Storage  
2. Azure Data Factory triggers a Databricks notebook/job  
3. Databricks cleans & transforms the data  
4. Transformed data is loaded into Azure SQL / Synapse  
5. Power BI connects to Azure SQL for dashboards
