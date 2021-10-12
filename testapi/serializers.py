from rest_framework import serializers
from .models import Student
def age_validations(value): 
        if value <=18  or value >=35:
            raise serializers.ValidationError("invalid age")
        

        
        
        
class StudentSerializer(serializers.HyperlinkedModelSerializer):
    name=serializers.CharField()
    address=serializers.CharField()
    age=serializers.IntegerField(validators=[age_validations])
    class Meta:
        model = Student
        fields = ['url','name','age','address']
   
        # fields='__all__'
        # include='url'
    
    # ------------field level validations -------  
    # def validate_age(self, value):
    #     if value <=18 or value>=30 :
    #         raise  serializers.ValidationError("invalid age")
    #     return value
    
     # ------------object level validations -------  
     
    # def validate(self,data):
    #     address=data.get('address')
    #     if address.lower()!='pabna':
    #         raise serializers.ValidationError("address must be pabna")
    #     return data
    

  
    