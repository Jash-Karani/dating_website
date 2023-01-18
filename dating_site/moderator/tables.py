import django_tables2 as tables
from  users.models import Profile
from  dating.models import Reports

class ProfileTable(tables.Table):
    class Meta:
        model = Profile
        orderable = False
        
class ReportTable(tables.Table):
    report_id = tables.Column()
    report_from = tables.Column()
    report_against =tables.Column()
    reason =tables.Column()
    ignore = tables.TemplateColumn(template_name='./ignore.html')
    delete_user = tables.TemplateColumn(template_name='./delete_user.html')



    class Meta:         
        orderable = False
