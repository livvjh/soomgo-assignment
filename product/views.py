from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from config.common.exception_handler import CustomAPIException
from config.common.library_classes import response_serializer, essential_param
from config.common.response_code import STATUS_SUCCESS, \
    MSG_RSP_CATEGORY_DOES_NOT_EXISTS, MSG_RSP_PRODUCT_PRICE_IS_NOT_POSITIVE_NUM, MSG_RSP_PURCHASE_DOES_NOT_EXISTS, \
    MSG_RSP_PRODUCT_DOES_NOT_EXISTS, MSG_RSP_PERMISSION_ERROR
from product.models import Product, Purchase, Category
from product.product_serializers import ProductPostSerializer, PurchaseSerializer, ProductSerializer, \
    PurchasePostSerializer


class ProductAPI(APIView):

    @swagger_auto_schema(tags=['상품목록 API'])
    def get(self, request):
        """
        상품 목록 API

        ---
          # 설명
            - id: 상품 id
            - category: 카테고리
            - name: 상품명
            - price: 가격
            - description: 상품 설명
        """
        purchase_list = Purchase.objects.filter(user=request.user)
        context = {
            'purchase_list': PurchaseSerializer(purchase_list, many=True).data
        }
        return Response(response_serializer(STATUS_SUCCESS, context), status=status.HTTP_200_OK)

    @swagger_auto_schema(tags=['상품등록 API'], request_body=ProductPostSerializer, responses={200: 'Success'})
    def post(self, request):
        """
        상품 등록 API

        ---
          # 설명
            - id: 상품 id
            - parent_category: depth 1 카테고리
            - category: depth 2 카테고리
            - name: 상품명
            - price: 가격
            - description: 상품 설명
            - created_at: 생성 날짜
            - updated_at: 수정 날짜
        """
        category_id = essential_param(request, 'category')
        name = essential_param(request, 'name')
        price = essential_param(request, 'price')
        description = essential_param(request, 'description')

        if not request.user.is_superuser:
            raise CustomAPIException(
                MSG_RSP_PERMISSION_ERROR,
                500
            )

        try:
            Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            raise CustomAPIException(
                MSG_RSP_CATEGORY_DOES_NOT_EXISTS,
                500
            )

        if price < 0:
            raise CustomAPIException(
                MSG_RSP_PRODUCT_PRICE_IS_NOT_POSITIVE_NUM,
                400
            )

        product = Product.objects.create(
            category_id=category_id,
            name=name,
            price=price,
            description=description,
        )

        context = {
            'product': ProductSerializer(product).data
        }

        return Response(response_serializer(STATUS_SUCCESS, context), status=status.HTTP_200_OK)


class PurchaseDetailAPI(APIView):

    @swagger_auto_schema(tags=['상품상세 API'])
    def get(self, request, purchase_id):
        """
        상품 상세 API

        ---
          # 설명
            - product_id : 상품 id
        """
        try:
            purchase = Purchase.objects.get(
                id=purchase_id,
                user=request.user
            )
        except Purchase.DoesNotExist:
            raise CustomAPIException(
                MSG_RSP_PURCHASE_DOES_NOT_EXISTS,
                404
            )

        context = {
            'product': PurchaseSerializer(purchase).data
        }

        return Response(response_serializer(STATUS_SUCCESS, context), status=status.HTTP_200_OK)


class PurchaseAPI(APIView):
    @swagger_auto_schema(tags=['상품구매 API'], request_body=PurchasePostSerializer, responses={200: 'Success'})
    def post(self, request):
        """
        상품 구매 API

        ---
          # 설명
        """
        product_id_set = essential_param(request, 'product_id_set')
        product_bulk_list = []
        for product_id in product_id_set:
            try:
                Product.objects.get(id=product_id)
            except Product.DoesNotExist:
                raise CustomAPIException(
                    MSG_RSP_PRODUCT_DOES_NOT_EXISTS,
                    404
                )
            product_bulk_list.append(
                Purchase(
                    user=request.user,
                    product_id=product_id
                )
            )

        Purchase.objects.bulk_create(product_bulk_list)
        return Response(response_serializer(STATUS_SUCCESS), status=status.HTTP_200_OK)
