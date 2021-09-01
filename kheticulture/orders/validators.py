from rest_framework import serializers

from .models import Order, OrderItem
from tractor.models import Tractor

class UniqueUpdateValidator(object):
    instance = None
    initial_data = {}

    def set_context(self, serializer):

        self.initial_data = getattr(serializer, 'initial_data', None)

    def __call__(self, attrs):
        """
        We will override this method to ensure the order details is unique for
        order and quantity, in the current request context.
        """
        unique_store = []
        for data in self.initial_data:
            to_validate = (data.get('tractor'), data.get('tractor_type'))
            if to_validate in unique_store:
                raise serializers.ValidationError({
                    'order': (
                        u'Already added a tractor of this type, '
                        u'consider using quantity'
                    )
                })
            unique_store.append(to_validate)


class UniqueUpdateDBValidator(object):
    instance = None
    initial_data = {}

    def set_context(self, serializer):
        # Determine the existing instance, if this is an update operation.
        self.instance = getattr(serializer, 'instance', None)
        self.initial_data = getattr(serializer, 'initial_data', None)

    def __call__(self, attrs):
        """
        Validate we are not updating a order detail that matches another
        order detail from the same order, in that case we should update
        the quantity from the original order detail.
        """
        data = self.initial_data
        qs = OrderItem.objects.filter(
            order=self.instance.order,
            tractor=data.get('tractor'),
            tractor_type=data.get('tractor_type')
        ).exclude(id=self.instance.id).exists()

        if qs:
            raise serializers.ValidationError({
                'order': (
                    u'Looks like this order already has this '
                    u'tractor'
                )
            })


class UniqueUpdateStatusValidator(object):
    instance = None
    status_not_permitted = [
        Order.OUT_FOR_DELIVERY,
        Order.DELIVERED
    ]

    def set_context(self, serializer):
        """
        Code from rest_framework/validators
        """
        # Determine the existing instance, if this is an update operation.
        self.instance = getattr(serializer, 'instance', None)

    def __call__(self, attrs):
        """
        Validate we are not updating a order detail that matches another
        order detail from the same order, in that case we should update
        the quantity from the original order detail.
        """
        order = self.instance.order
        if order.status in self.status_not_permited:
            raise serializers.ValidationError({
                (
                    u'This order is `{status}` and cannot be '
                    u'updated at this moment'
                ).format(
                    status=order.get_status_display()
                )
            })