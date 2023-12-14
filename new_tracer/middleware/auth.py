# from django.utils.deprecation import MiddlewareMixin
# from django.conf import settings
#
# from trade.models import Transaction
# from users.models import userProfile
#
# from datetime import datetime
#
# class AuthMiddleware(MiddlewareMixin):
#     def process_request(self, request):
#         userid = request.session.get('user_id',0)
#         if userid:
#             user_project = userProfile.objects.filter(id=userid).first()
#             request.user = user_project
#
#         _object = Transaction.objects.filter(user_id=userid, status=2).order_by('-id').first()
#         current_datetime = datetime.now()
#         if _object:
#             if _object.end_datetime and _object.end_datedtime < current_datetime:
#                 _object = Transaction.objects.filter(user_id=userid, status=2, price_policy__category=1).first()
#
#             request.price_policy = _object.price_policy
#         request.userid = userid
