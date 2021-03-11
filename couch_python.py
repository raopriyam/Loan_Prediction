from couchbase.cluster import Cluster, ClusterOptions
from couchbase_core.cluster import PasswordAuthenticator
from couchbase.cluster import QueryOptions
import dataclasses
from dataclasses import dataclass
import json
import pandas as pd

cluster = Cluster('couchbase://localhost:8091', ClusterOptions(
  PasswordAuthenticator('Admin', 'Admin123')))
cb = cluster.bucket('training_data')
cb_coll = cb.default_collection()

# @dataclass
# class Dataset_train:
#     ApplicantIncome: int
#     CoapplicantIncome: int
#     Credit_History: int
#     Dependents: int
#     Education: str
#     Gender: str
#     LoanAmount: int
#     Loan_Amount_Term: int
#     Loan_ID: str
#     Loan_Status: str
#     Married: str
#     Property_Area: str
#     Self_Employed: str

def download_document(v):
  try:
    result = cb_coll.get(v)
    print(result.content_as[str])
    json_doc = json.loads(result.content_as[str])
    return json_doc
  except Exception as e:
    print(e)

df_id = pd.read_csv('loan_id.csv')
# out_file = open("output.json", "w") 
for i in df_id['Loan_ID']:
  d1 = download_document(i)
  # json.dump(d1,out_file)

# We are able to extract data but are unable to convert it into json files.




