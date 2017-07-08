import boto3

def cloudwatch_connection(profile, region):
    if profile:
        session = boto3.Session(profile_name=profile)
    con = session.client('cloudwatch', region_name=region)
    return con
