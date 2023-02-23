from ninja import Router, Schema
from django.http.request import HttpRequest
from django.utils import timezone
from django.db import transaction
from endpoints.error import FriendlyException

from models.models import ArticleModel, StockModel, TradeModel, UserModel

router = Router()


class DemoRequest(Schema):
    create_user: str
    test_abort: bool


@router.post("/")
@transaction.atomic
def demo_post(request: HttpRequest, data: DemoRequest) -> str:
    # Should create AAPL stock and qwerty article in admin interface before running
    article = ArticleModel.objects.get(article_id="qwerty")
    user = UserModel.create_typed(
        username=data.create_user, password="xxxxx", balance=0.)
    apple = StockModel.objects.get(ticker="AAPL")
    # should use django.utils.timezone.now instead of datetime.now, to ensure time is in UTC
    TradeModel.create_typed(user=user, stock=apple, units=10, total_cost=2, time=timezone.now(),
                            text_evidence="here", article_evidence=[article])
    if data.test_abort:
        raise FriendlyException(
            "Something went wrong! The @transaction.atomic decorator means all above changes will be rolled back.")
    return "Success!"
