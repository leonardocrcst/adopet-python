from rest_framework import serializers
from .models import Adocao
from pet.serializers import PetSerializer # Para retornar os dados do Pet após uma adoção
from pet.models import Pet

class AdocaoSerializer(serializers.ModelSerializer):
  # o campo pet agora não retornará o id do pet, mas os dados daquele pet
  pet = PetSerializer(many=False, read_only=True)

  pet_id = serializers.PrimaryKeyRelatedField(
    many=False, write_only=True, queryset=Pet.objects.all()
  )
  
  class Meta:
    model = Adocao
    fields = ('id', 'value', 'email', 'pet', 'pet_id')
  
  # Isso daqui foi feito para alterar o campo de envio do id de pet para pet_id
  def create(self, validated_data):
    validated_data['pet'] = validated_data.pop('pet_id') # remove o pet_id e retorna seu conteúdo
    return super().create(validated_data)

  # A função de validação dos campos deve começar com validate_ e ter o nome do campo
  # a ser validado. Ela é executada automaticamente no campo mencionado
  def validate_value(self, value):
    if value < 10:
      raise serializers.ValidationError("A doação deve ser maior que 10,00")
    if value > 100:
      raise serializers.ValidationError("Agradecemos mas, por questões de segurança, não aceitamos mais que 100,00 de doação para um pet único.")
    return value