import cortex

cx_aws = cortex.client("aws")

api_spec = {
    "name": "nyc-taxi-eta",
    "kind": "RealtimeAPI",
    "predictor": {
        "type": "python",
        "path": "predictor.py"
    }
}

cx_aws.deploy(api_spec, project_dir=".")
