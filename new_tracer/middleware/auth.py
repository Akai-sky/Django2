from django.utils.deprecation import MiddlewareMixin
from django.conf import settings
from django.contrib.auth import get_user_model

from trade.models import Transaction
from users.models import userProfile
from project.models import Project, ProjectUser

from datetime import datetime

User = get_user_model()


class Tracer(object):

    def __init__(self):
        self.user = None
        self.price_policy = None
        self.project = None


#
class AuthMiddleware(MiddlewareMixin):
    # def process_request(self,request):
    #     request.tracer = Tracer()
    #
    #     user_id = request.session.get('user_id',0)
    #     print("session.userid:",user_id)
    #     user_object = User.objects.filter(id=user_id)
    #     request.tracer.user = user_object

    #     def process_request(self, request):
    #         userid = request.session.get('user_id',0)
    #         if userid:
    #             user_project = userProfile.objects.filter(id=userid).first()
    #             request.user = user_project

    #         _object = Transaction.objects.filter(user_id=userid, status=2).order_by('-id').first()
    #         current_datetime = datetime.now()
    #         if _object:
    #             if _object.end_datetime and _object.end_datedtime < current_datetime:
    #                 _object = Transaction.objects.filter(user_id=userid, status=2, price_policy__category=1).first()

    #             request.price_policy = _object.price_policy
    #         request.userid = userid

    def process_view(self, request, view, *args, **kwargs):
        if not request.path_info.startswith('/manage/'):
            return

        project_id = args[1].get('project_id')
        project_object = Project.objects.filter(creator=request.user, id=project_id).first()
        if project_object:
            request.project = project_object
            return
        project_user_object = ProjectUser.objects.filter(user=request.user, project_id=project_id).first()
        if project_user_object:
            request.project = project_user_object
            return
