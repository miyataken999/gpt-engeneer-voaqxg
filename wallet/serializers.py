from rest_framework import serializers
from .models import Wallet

class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ['brand_name', 'model_number', 'purchase_date', 'purchase_price', 'purchase_place', 'accessory', 'precious_metal_purity', 'precious_metal_weight']