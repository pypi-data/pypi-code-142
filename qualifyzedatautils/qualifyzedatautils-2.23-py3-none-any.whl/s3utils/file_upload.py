
from ..connections.dwh_awsservicer import initialize_dwhservicer_credentials, establish_dwhservicer_session
from io import StringIO

#aws_dwhsession = establish_dwhservicer_session()
#print(99999992222222222)

def df_tos3csvfile(dfoject):

    session = establish_dwhservicer_session()

    s3_res = session.resource('s3')
    csv_buffer = StringIO()
    dfoject.to_csv(csv_buffer)
    bucket_name = 'qualifyze-redshift-staging'
    s3_object_name = 'df4.csv'
    s3_res.Object(bucket_name, s3_object_name).put(Body=csv_buffer.getvalue())

    return 12345
