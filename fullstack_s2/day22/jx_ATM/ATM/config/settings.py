#__author:  "Jing Xu"
#date:  2018/1/24

import os
import logging

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASE = {
	"engine" : "file_storage",
	"name" : "accounts",
	"path" : "%s/database" % BASE_DIR
}

LOG_LEVEL = logging.WARNING
LOG_TYPES = {
	"transaction" : "transactions.log",
	"access" : "access.log",
}

TRANSACTION_TYPE = {
    'repay':{'action':'plus', 'interest':0},
    'withdraw':{'action':'minus', 'interest':0.05},
    'transfer':{'action':'minus', 'interest':0.05},
    'consume':{'action':'minus', 'interest':0},

}