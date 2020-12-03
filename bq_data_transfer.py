from google.cloud import bigquery_datatransfer

client = bigquery_datatransfer.DataTransferServiceClient()

parent = f"projects/PROJECT_ID"

transfer_config = bigquery_datatransfer.TransferConfig(
    destination_dataset_id='DESTINATION_DATASET',
    display_name='Python Data Transfer',
    data_source_id="cross_region_copy",
    params={
        "source_dataset_id": "SOURCE_DATASET",
        "source_project_id": "PROJECT_ID",
        "overwrite_destination_table": "true"
    },
)

response = client.create_transfer_config(
    request={
        "parent": parent,
        "transfer_config": transfer_config,
        # "authorization_code": authorization_code,
    }
)

print("Transfer Created:'{}'".format(response.name))
