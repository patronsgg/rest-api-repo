from data import db_session
from data.jobs import Jobs

db_session.global_init('mars_db.sqlite')
session = db_session.create_session()

job_1 = Jobs()
job_1.team_leader = 1
job_1.job = 'deployment of residential modules 1 and 2'
job_1.work_size = 15
job_1.collaborators = '2, 3'
job_1.is_finished = False
session.add(job_1)

job_2 = Jobs()
job_2.team_leader = 2
job_2.job = 'installing equipment'
job_2.work_size = 7
job_2.collaborators = "1"
job_2.is_finished = False
session.add(job_2)

session.commit()