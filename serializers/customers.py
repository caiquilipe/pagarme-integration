from django.contrib.auth.password_validation import validate_password

from rest_framework import serializers

from ..models import CustomerUser


class CustomersSerializer(serializers.Serializer):
    id = serializers.CharField(required=False)
    name = serializers.CharField(required=True)
    email = serializers.CharField(required=False)


class CustomerInsertSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    email = serializers.CharField(required=False)


class UserGetOrCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128,
        validators=[validate_password],
        write_only=True,
    )
    confirm_password = serializers.CharField(max_length=128, write_only=True)

    def to_representation(self, instance: CustomerUser):
        """
        Change data representation

        Args:
            instance (User): user model
        """
        data = super().to_representation(instance)
        data["cpf"] = instance.masked_cpf()
        data["email"] = instance.masked_email()
        # data["phone"] = instance.masked_phone()
        return data

    def validate(self, attrs):
        if not attrs.get("confirm_password") == attrs.get("password"):
            raise serializers.ValidationError(
                detail={
                    "password": "Senhas devem ser iguais",
                    "confirm_password": "Senhas devem ser iguais",
                }
            )
        del attrs["confirm_password"]
        if CustomerUser.objects.filter(username=attrs["cpf"]).exists():
            raise serializers.ValidationError(
                detail={
                    "cpf": "Usuário com este CPF já cadastrado.",
                }
            )
        attrs["username"] = attrs["cpf"]
        return super().validate(attrs)

    class Meta:
        model = CustomerUser
        fields = [
            "id",
            "password",
            "confirm_password",
            "first_name",
            "last_name",
            "cpf",
            "email",
            "phone",
            "birth_date",
            "is_active",
        ]
        extra_kwargs = {"is_active": {"read_only": True}}


class CustomerInsertModelSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source="get_full_name")

    class Meta:
        model = CustomerUser
        fields = ["name", "email"]
