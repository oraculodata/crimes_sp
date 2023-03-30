import pandas as pd
import config as cfg
import aux as func
from google.cloud import bigquery
from google.oauth2 import service_account

path_write = 'files'
crime_name = func.fix_name(cfg.ssp['crime'])
filename=f"{path_write}/{crime_name}_{cfg.ssp['mes'].lower()}_{cfg.ssp['ano']}.csv"

def main():
    try:
        df = pd.read_csv(filename, sep='\t', encoding='utf-16le', engine='python')

        # Change text to Timestamp, Date and Time
        fields_ts = ['BO_INICIADO', 'BO_EMITIDO', 'DATAELABORACAO']

        for item in fields_ts:
            df[item] = func.fix_ts(df[item])

        fields_dt = ['DATAOCORRENCIA', 'DATACOMUNICACAO']

        for item in fields_dt:
            df[item] = func.fix_dt(df[item])

        df['HORAOCORRENCIA'] = df['HORAOCORRENCIA'].apply(func.fix_tm)

        # Convert text to numeric
        df['LATITUDE'] = df['LATITUDE'].str.replace(',', '.').astype(float)
        df['LONGITUDE'] = df['LONGITUDE'].str.replace(',', '.').astype(float)

        # BQ Loading...
        credentials = service_account.Credentials.from_service_account_file(
            cfg.bq["key_path"],
            scopes=["https://www.googleapis.com/auth/cloud-platform"],
        )
        table_target = f"{cfg.bq['dataset']}.{crime_name}"

        client = bigquery.Client(credentials=credentials, project=credentials.project_id,)
        job_config = bigquery.LoadJobConfig(
            write_disposition="WRITE_TRUNCATE",
        )
        job = client.load_table_from_dataframe(
            df, table_target, job_config=job_config
        )
        job.result()

        table = client.get_table(table_target)
        print(
            "Loaded {} rows and {} columns to {}".format(
                table.num_rows, len(table.schema), table_target
            )
        )
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()
