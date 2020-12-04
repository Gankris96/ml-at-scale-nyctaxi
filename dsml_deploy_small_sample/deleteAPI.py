import cortex

cx_aws = cortex.client("aws")
cx_aws.delete_api("nyc-taxi-eta")

