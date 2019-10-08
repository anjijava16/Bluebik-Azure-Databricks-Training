# Instruction - Databricks Airlift Data Engineering Workshop

**Disclaimer**: The views and opinions expressed in this article are those of the author's and do not necessarily reflect the official policy or position of current or previous employer, organization, committee, other group or individual. Analysis performed within this article is based on limited dated open source information. Assumptions made within the analysis are not reflective of the position of any previous or current employer.

**Copyright**: Copyright (c) Microsoft Corporation

**Instructor**: Kyle Akepanidtaworn, Cloud Solution Architect (Advanced Analytics & Artificial Intelligence)

## Requirements

1. Azure subscription. You will need a valid and active Azure account to complete the quickstarts. If you do not have one, you can sign up for a [free trial](https://azure.microsoft.com/en-us/free/).

   - The Microsoft Azure subscription must be pay-as-you-go or MSDN. 

   - Trial subscriptions will not work. You will run into issues with Azure resource quota limits. 

   - Subscriptions with access limited to a single resource group will not work. You will need the ability to deploy multiple resource groups.

2. Azure Storage Account. You will need an Azure Storage Account to contain all of your Azure Storage data objects: blobs, files, queues, tables, and disks. The storage account provides a unique namespace for your Azure Storage data that is accessible from anywhere in the world over HTTP or HTTPS. Data in your Azure storage account is durable and highly available, secure, and massively scalable. To learn how to create an Azure storage account, see [Create a storage account](https://docs.microsoft.com/en-us/azure/storage/common/storage-quickstart-create-account?tabs=azure-portal).

3. Azure Databricks. You will need an Azure Databricks to bring teams together in an interactive workspace. From data gathering to model creation, use Databricks Notebooks to unify the process and instantly deploy to production. Launch your new Spark environment with a single click. Integrate effortlessly with a wide variety of data stores and services such as Azure SQL Data Warehouse, Azure Cosmos DB, Azure Data Lake Store, Azure Blob storage, and Azure Event Hub. Add advanced artificial intelligence (AI) capabilities instantly and share your insights through rich integration with PowerBI. Please set the following configuration:
   1. **Workspace Name** - Enter a unique name as indicated by a green checkmark.
   2. **Subscription** - Select the subscription you are using for this hands-on lab.
   3. **Location** - Select a region close to you.
   4. **Resource Group** - Select Create new and enter a unique name, such as "hands-on-databricks".
   5. **Pricing Tier** - Select the pricing tier that is suitable to your needs.
      1. __Standard__ - Apache Spark, Secure with Azure Active Directory
      2. __Premium__ - Apache Spark, Secure with Azure Active Directory + Role-Based Access Control
      3. __Trial__ - Premium + 14 Days Free DBUs.
   6. **Deploy Azure Databricks Workspace to Your Virtual Networks** - Select "No" for the purpose of this workshop. However, if there is a strong requirement with regards to the security, you may want to consider this option.

## Data Engineering Notebooks

**Lab Duration**: 1.5 hour

Databricks notebooks covering data engineering and data science workloads (Microsoft Airlift Agenda). Here's our training plan:

* Reading Data Basics
  * Apache Spark is an open source cluster computing framework for fast real-time large-scale data processing. Since its inception in 2009 at UC Berkeley’s AMPLab, Spark has seen major growth.
  * Spark revolves around the concept of a resilient distributed dataset (RDD), which is a fault-tolerant collection of elements that can be operated on in parallel. There are two ways to create RDDs: parallelizing an existing collection in your driver program, or referencing a dataset in an external storage system, such as a shared filesystem, HDFS, HBase, or any data source offering a Hadoop InputFormat.
  * **Databricks File System (DBFS)** is a layer over Azure's blob store. Files in DBFS persist to the blob store, so data is not lost even after clusters are terminated.
  * **Parquet** is a column-based storage format for Hadoop.
  * A Databricks archive is a JAR file with extra metadata and has the extension .dbc.
* Transformations & Actions
  * A DataFrame is the most common Structured API and simply represents a table of data with rows and columns. The list of columns and the types in those columns the schema. A simple analogy would be a spreadsheet with named columns.
* Integration with Azure Data Services
* Azure Event Hub
* Azure SQL Data Warehouse
* Azure Cosmos DB
* Delta Lakes
  * Delta Lake is an open source storage layer that brings reliability to data lakes. Delta Lake provides ACID transactions, scalable metadata handling, and unifies streaming and batch data processing. Delta Lake runs on top of your existing data lake and is fully compatible with Apache Spark APIs. Delta Lake on Databricks allows you to configure Delta Lake based on your workload patterns and provides optimized layouts and indexes for fast interactive queries.
  * **UPSERT** - Literally means "UPdate" and "inSERT". It means to atomically either insert a row, or, if the row already exists, UPDATE the row.
  * **APPEND** - Add on to the end of the dataframe. 
* Batch Jobs
* Streaming Jobs
* Optimization