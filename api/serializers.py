from rest_framework import serializers
from api.models import Incident,Cve_number,Target,Description




class DescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Description
        fields = ['id','name']



class CVESerializer(serializers.ModelSerializer):
    class Meta:
        model = Cve_number
        fields = ['id','cve']


class TargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = ['id','name']



class IncidentSerializer(serializers.ModelSerializer):

    time_creation = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S",read_only=True)
    description = DescriptionSerializer(read_only=True)
    cve_number = CVESerializer(many=True,read_only=True)
    object = TargetSerializer(read_only=True)
    description_id = serializers.PrimaryKeyRelatedField(queryset=Description.objects.all(), source='description',write_only=True)
    target_id = serializers.PrimaryKeyRelatedField(queryset=Target.objects.all(), source='object',write_only=True)
    cve_number_ids = serializers.PrimaryKeyRelatedField(many=True, queryset=Cve_number.objects.all(),write_only=True)
    class Meta:
        model = Incident
        fields = ['id','name','description','cve_number','object','time_creation','cve_number_ids','target_id','description_id']
    
    @staticmethod
    def _create_cves(instance,cves):
        if cves:
            instance.cve_number.set(cves)

    def create(self, validated_data):
        cves = validated_data.pop("cve_number_ids", None)
        incident = Incident.objects.create(**validated_data)
        self._create_cves(incident,cves)

        return incident
    
    def update(self,instance, validated_data):
        cves = validated_data.pop("cve_number_ids", None)
        self._create_cves(instance,cves)
        return instance

