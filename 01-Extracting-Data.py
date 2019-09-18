# Databricks notebook source
# MAGIC %md
# MAGIC ![x](https://zdnet4.cbsistatic.com/hub/i/r/2017/12/17/e9b8f576-8c65-4308-93fa-55ee47cdd7ef/resize/370xauto/30f614c5879a8589a22e57b3108195f3/databricks-logo.png)

# COMMAND ----------

# MAGIC %md
# MAGIC &copy; 2019 Databricks, Inc. All rights reserved.<br/>

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC # Getting access to our data
# MAGIC 
# MAGIC ### Databricks File System - DBFS
# MAGIC Databricks File System (DBFS) is a distributed file system installed on Azure Databricks clusters. Files in DBFS persist to Azure Blob storage, so you won’t lose data even after you terminate a cluster.
# MAGIC 
# MAGIC You can access files in DBFS using the Databricks CLI, DBFS API, Databricks Utilities, Spark APIs, and local file APIs.
# MAGIC 
# MAGIC On your local computer you access DBFS using the Databricks CLI or DBFS API. In a Spark cluster you access DBFS using Databricks Utilities, Spark APIs, or local file APIs.
# MAGIC 
# MAGIC DBFS allows you to mount containers so that you can seamlessly access data without requiring credentials.
# MAGIC 
# MAGIC **Databricks Mount Points:**
# MAGIC - Connect to our Azure Storage Account - https://docs.azuredatabricks.net/spark/latest/data-sources/azure/azure-storage.html
# MAGIC - Connect to our Azure Data Lake - https://docs.azuredatabricks.net/spark/latest/data-sources/azure/azure-datalake.html

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC ### Cluster Setup
# MAGIC 
# MAGIC Please ensure you have a cluster with the following configuration:
# MAGIC 
# MAGIC Cluster Mode: Standard  
# MAGIC Databricks Runtime: 5.4+ ML  
# MAGIC NO autoscaling  
# MAGIC Standard VMs (DS3 v2)  
# MAGIC 1 worker node

# COMMAND ----------

# MAGIC %md
# MAGIC **IMPORTANT** If you are using a shared workspace, please be careful whenever writing files or creating tables. These will be shared across your instance, so please add a prefix/suffix to your tables/file names on write, and, whenever reading, make sure you propagate the changes.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Fetch Titanic Data

# COMMAND ----------

# MAGIC %sh
# MAGIC # Pull CSV file from url
# MAGIC wget -nc https://raw.githubusercontent.com/bensadeghi/Databricks-DataScience-Titanic/master/data/titanic.csv

# COMMAND ----------

# MAGIC %md
# MAGIC ### DB Utils
# MAGIC Set of tools to manage file-system activities

# COMMAND ----------

dbutils.fs.help()

# COMMAND ----------

# Create a new directory within DBFS
dbutils.fs.mkdirs('titanic_data')

# Copy data from Spark driver to DBFS
dbutils.fs.cp('file:/databricks/driver/titanic.csv', 'dbfs:/titanic_data/titanic.csv')

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC We can use **%fs** to issue filesystem commands such as **ls** to browse through our folder

# COMMAND ----------

# MAGIC %fs ls /titanic_data

# COMMAND ----------

# MAGIC %md 
# MAGIC 
# MAGIC ### Reading the Training File
# MAGIC 
# MAGIC **Technical Accomplishments:**
# MAGIC - Read data from CSV using PySpark
# MAGIC - Read data from CSV using SQL
# MAGIC - Switching languages

# COMMAND ----------

# MAGIC %md
# MAGIC We can use **&percnt;head ...** to view the first few lines of the file.

# COMMAND ----------

# MAGIC %fs head /titanic_data/titanic.csv

# COMMAND ----------

# MAGIC %md
# MAGIC Let's start with the bare minimum by specifying that the file we want to read is delimited and the location of the file:
# MAGIC The default delimiter for `spark.read.csv( )` is comma but we can change by specifying the option delimiter parameter.
# MAGIC 
# MAGIC For the purpose of the workshop, we will be reading samples of the files, as to not spend too many resources from our Azure Pass. If you're using your own, bigger clusters, feel free to use the full data files (just remove _sample_ from the name).

# COMMAND ----------

csvFile = "/titanic_data/titanic.csv"

titanicDF = (spark.read           # The DataFrameReader
   .option("header", "true")       # Use first line of all files as header
   .option("inferSchema", "true")  # Automatically infer data types
   .csv(csvFile)                   # Creates a DataFrame from CSV after reading in the file
   .cache()                        # Persist the data in memory
)

# COMMAND ----------

display(titanicDF)

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC Alternatively, we can accomplish the same results using SQL

# COMMAND ----------

# MAGIC %sql
# MAGIC 
# MAGIC DROP TABLE IF EXISTS titanic; 
# MAGIC CREATE TABLE titanic
# MAGIC USING CSV
# MAGIC OPTIONS (path "/titanic_data/titanic.csv", header "true", inferSchema "true")

# COMMAND ----------

# MAGIC %sql
# MAGIC 
# MAGIC SELECT * FROM titanic LIMIT 10

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC This time we are going to read the same file.
# MAGIC 
# MAGIC The difference here is that we are going to define the schema beforehand to avoid the execution of any extra jobs.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Inferred Schema

# COMMAND ----------

# What is the current schema inferred?

titanicDF.printSchema()

# COMMAND ----------

# MAGIC %md
# MAGIC <h3>Data Dictionary</h3>
# MAGIC <table style="width: 100%;">
# MAGIC <tbody>
# MAGIC <tr><th><b>Variable</b></th><th><b>Definition</b></th><th><b>Key</b></th></tr>
# MAGIC <tr>
# MAGIC <td>survival</td>
# MAGIC <td>Survival</td>
# MAGIC <td>0 = No, 1 = Yes</td>
# MAGIC </tr>
# MAGIC <tr>
# MAGIC <td>pclass</td>
# MAGIC <td>Ticket class</td>
# MAGIC <td>1 = 1st, 2 = 2nd, 3 = 3rd</td>
# MAGIC </tr>
# MAGIC <tr>
# MAGIC <td>sex</td>
# MAGIC <td>Sex</td>
# MAGIC <td></td>
# MAGIC </tr>
# MAGIC <tr>
# MAGIC <td>Age</td>
# MAGIC <td>Age in years</td>
# MAGIC <td></td>
# MAGIC </tr>
# MAGIC <tr>
# MAGIC <td>sibsp</td>
# MAGIC <td># of siblings / spouses aboard the Titanic</td>
# MAGIC <td></td>
# MAGIC </tr>
# MAGIC <tr>
# MAGIC <td>parch</td>
# MAGIC <td># of parents / children aboard the Titanic</td>
# MAGIC <td></td>
# MAGIC </tr>
# MAGIC <tr>
# MAGIC <td>ticket</td>
# MAGIC <td>Ticket number</td>
# MAGIC <td></td>
# MAGIC </tr>
# MAGIC <tr>
# MAGIC <td>fare</td>
# MAGIC <td>Passenger fare</td>
# MAGIC <td></td>
# MAGIC </tr>
# MAGIC <tr>
# MAGIC <td>cabin</td>
# MAGIC <td>Cabin number</td>
# MAGIC <td></td>
# MAGIC </tr>
# MAGIC <tr>
# MAGIC <td>embarked</td>
# MAGIC <td>Port of Embarkation</td>
# MAGIC <td>C = Cherbourg, Q = Queenstown, S = Southampton</td>
# MAGIC </tr>
# MAGIC </tbody>
# MAGIC </table>
# MAGIC 
# MAGIC <h3>Variable Notes</h3>
# MAGIC <p><b>pclass</b>: A proxy for socio-economic status (SES)<br> 1st = Upper<br> 2nd = Middle<br> 3rd = Lower<br><br> <b>age</b>: Age is fractional if less than 1. If the age is estimated, is it in the form of xx.5<br><br> <b>sibsp</b>: The dataset defines family relations in this way...<br> Sibling = brother, sister, stepbrother, stepsister<br> Spouse = husband, wife (mistresses and fiancés were ignored)<br><br> <b>parch</b>: The dataset defines family relations in this way...<br> Parent = mother, father<br> Child = daughter, son, stepdaughter, stepson<br> Some children travelled only with a nanny, therefore parch=0 for them.</p>

# COMMAND ----------

# MAGIC %md
# MAGIC ### Summary of Data

# COMMAND ----------

display(titanicDF.describe())

# COMMAND ----------

# MAGIC %md
# MAGIC ### Simple Exploratory Analysis

# COMMAND ----------

# How many people survived?

display(titanicDF.groupBy('Survived').count())

# COMMAND ----------

# MAGIC %md 
# MAGIC To know the particulars about survivors we have to explore more of the data.
# MAGIC The survival rate can be determined by different features of the dataset such as Sex, Port of Embarcation, Age; few to be mentioned.

# COMMAND ----------

## Checking survival rate using feature Sex 

display(titanicDF.groupBy('Survived', 'Sex').count())

# COMMAND ----------

# MAGIC %md
# MAGIC Although the number of males are more than females on ship, the female survivors are twice the number of males saved

# COMMAND ----------

## Checking survival rate using feature Passanger Class 

display(titanicDF.groupBy('Survived', 'Pclass').count())

# COMMAND ----------

# MAGIC %md
# MAGIC ## Next Step
# MAGIC 
# MAGIC [Cleaning Data]($./02-Cleaning-Data)

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2019 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="http://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="http://help.databricks.com/">Support</a>