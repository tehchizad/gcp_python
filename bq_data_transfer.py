# Modified version of the python example for "scheduled query"
# https://cloud.google.com/bigquery/docs/scheduling-queries#setting_up_a_scheduled_query
#
# Current cli user must be authenticated and have the propper authrorization to BQDT

from google.cloud import bigquery_datatransfer

client = bigquery_datatransfer.DataTransferServiceClient()

# TODO: Replace variables before attempting
project = ''
source_dataset_id = ''
destination_dataset_id = ''
display_name = 'Python Data Transfer final'

parent = f"projects/{project}"

transfer_config = bigquery_datatransfer.TransferConfig(
    destination_dataset_id=destination_dataset_id,
    display_name=display_name,
    data_source_id="cross_region_copy",
    params={
        "source_dataset_id": source_dataset_id,
        "source_project_id": project,
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
