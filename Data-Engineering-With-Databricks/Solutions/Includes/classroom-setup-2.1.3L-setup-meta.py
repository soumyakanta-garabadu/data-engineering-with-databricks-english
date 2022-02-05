# Databricks notebook source
# MAGIC %run ./_databricks-academy-helper $lesson="2.1.3L"

# COMMAND ----------

# MAGIC %run ./_utility-methods

# COMMAND ----------

DA.cleanup()
DA.init(create_db=False)
install_dtavod_datasets()
print()
copy_source_dataset(f"{DA.working_dir_prefix}/source/dtavod/weather", f"{DA.paths.working_dir}/weather", "parquet", "weather")
DA.conclude_setup()

