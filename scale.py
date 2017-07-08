import boto3
import ConfigParser
import time

from libs.utils import cloudwatch_connection
from libs.cloudwatch import RDS
from libs.terraform import Terraform

def scale():
    config_file = ConfigParser.ConfigParser()
    config_file.read("scale.cfg")
    CF_GENERAL = dict(config_file.items('general'))

    cw_con = cloudwatch_connection(CF_GENERAL['aws_profile'], CF_GENERAL['aws_region'])
    tf = Terraform(CF_GENERAL['terraform_project'])

    try:
        n_nodes = tf.get_n_nodes(CF_GENERAL['aurora_tf_file'])
    except Exception, e:
        raise e

    while True:
        cpu_dp = RDS(cw_con).get_rds_cluster_metric(CF_GENERAL['aurora_cluster'], "WRITER", "CPUUtilization")
        if cpu_dp['Average'] > CF_GENERAL['max_cpu'] and n_nodes < CF_GENERAL['max_nodes']:
            print "increase cluster"
            # set aurora_nodes(-1)
        elif cpu_dp['Average'] < CF_GENERAL['min_cpu'] and n_nodes > CF_GENERAL['min_nodes']:
            print "reduce cluster"
            # set_aurora_nodes(-1)
        else:
            print "nothing to do"

        time.sleep(10)

if __name__ == "__main__":
    scale()

# change_n_of_nodes (n):
    # git pull
    # read the var
    # replace the var
    # terraform plan
    # terraform apply
    # git push
