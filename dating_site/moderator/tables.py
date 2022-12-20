import django_tables2 as tables
from  users.models import Profile
from  dating.models import Reports

class ProfileTable(tables.Table):
    class Meta:
        model = Profile
        
class ReportTable(tables.Table):
    report_from = tables.Column()
    report_against =tables.Column()
    reason =tables.Column()




