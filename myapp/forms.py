# forms.py

from django import forms
from .models import * 



class ComputerEngineering_1RequestForm(forms.ModelForm):
    class Meta:
        model = ComputerEngineering_1Request
        fields = ['student', 'chair']

    def clean_chair(self):
        selected_chair = self.cleaned_data.get('chair')
        selected_student = self.cleaned_data.get('student')

        # التحقق من عدم اختيار نفس الكرسي من قبل طالب آخر
        existing_request = ComputerEngineering_1Request.objects.filter(chair=selected_chair).exclude(student=selected_student).exists()

        if existing_request:
            raise forms.ValidationError("لا يمكن اختيار نفس الكرسي من قبل طالب آخر!")

        return selected_chair
                 

class ComputerEngineering_2RequestForm(forms.ModelForm):
    class Meta:
        model = ComputerEngineering_2Request
        fields = ['student', 'chair']

    def clean_chair(self):
        selected_chair = self.cleaned_data.get('chair')
        selected_student = self.cleaned_data.get('student')

        # التحقق من عدم اختيار نفس الكرسي من قبل طالب آخر
        existing_request = ComputerEngineering_2Request.objects.filter(chair=selected_chair).exclude(student=selected_student).exists()

        if existing_request:
            raise forms.ValidationError("لا يمكن اختيار نفس الكرسي من قبل طالب آخر!")

        return selected_chair

class ComputerEngineering_3RequestForm(forms.ModelForm):
    class Meta:
        model = ComputerEngineering_3Request
        fields = ['student', 'chair']

    def clean_chair(self):
        selected_chair = self.cleaned_data.get('chair')
        selected_student = self.cleaned_data.get('student')

        # التحقق من عدم اختيار نفس الكرسي من قبل طالب آخر
        existing_request = ComputerEngineering_3Request.objects.filter(chair=selected_chair).exclude(student=selected_student).exists()

        if existing_request:
            raise forms.ValidationError("لا يمكن اختيار نفس الكرسي من قبل طالب آخر!")

        return selected_chair
class ComputerEngineering_32RequestForm(forms.ModelForm):
    class Meta:
        model = ComputerEngineering_32Request
        fields = ['student', 'chair']

    def clean_chair(self):
        selected_chair = self.cleaned_data.get('chair')
        selected_student = self.cleaned_data.get('student')

        # التحقق من عدم اختيار نفس الكرسي من قبل طالب آخر
        existing_request = ComputerEngineering_32Request.objects.filter(chair=selected_chair).exclude(student=selected_student).exists()

        if existing_request:
            raise forms.ValidationError("لا يمكن اختيار نفس الكرسي من قبل طالب آخر!")

        return selected_chair


class ComputerEngineering_4RequestForm(forms.ModelForm):
    class Meta:
        model = ComputerEngineering_4Request
        fields = ['student', 'chair']

    def clean_chair(self):
        selected_chair = self.cleaned_data.get('chair')
        selected_student = self.cleaned_data.get('student')

        # التحقق من عدم اختيار نفس الكرسي من قبل طالب آخر
        existing_request = ComputerEngineering_4Request.objects.filter(chair=selected_chair).exclude(student=selected_student).exists()

        if existing_request:
            raise forms.ValidationError("لا يمكن اختيار نفس الكرسي من قبل طالب آخر!")

        return selected_chair
class ComputerEngineering_42RequestForm(forms.ModelForm):
    class Meta:
        model = ComputerEngineering_42Request
        fields = ['student', 'chair']

    def clean_chair(self):
        selected_chair = self.cleaned_data.get('chair')
        selected_student = self.cleaned_data.get('student')

        # التحقق من عدم اختيار نفس الكرسي من قبل طالب آخر
        existing_request = ComputerEngineering_42Request.objects.filter(chair=selected_chair).exclude(student=selected_student).exists()

        if existing_request:
            raise forms.ValidationError("لا يمكن اختيار نفس الكرسي من قبل طالب آخر!")

        return selected_chair

class Cyber_security_1RequestForm(forms.ModelForm):
    class Meta:
        model = Cyber_security_1Request
        fields = ['student', 'chair']

    def clean_chair(self):
        selected_chair = self.cleaned_data.get('chair')
        selected_student = self.cleaned_data.get('student')

        # التحقق من عدم اختيار نفس الكرسي من قبل طالب آخر
        existing_request = Cyber_security_1Request.objects.filter(chair=selected_chair).exclude(student=selected_student).exists()

        if existing_request:
            raise forms.ValidationError("لا يمكن اختيار نفس الكرسي من قبل طالب آخر!")

        return selected_chair


class ComputerEngineering_11RequestForm(forms.ModelForm):
    class Meta:
        model = ComputerEngineering_11Request
        fields = ['status']
class ComputerEngineering_22RequestForm(forms.ModelForm):
    class Meta:
        model = ComputerEngineering_22Request
        fields = ['status']
class ComputerEngineering_33RequestForm(forms.ModelForm):
    class Meta:
        model = ComputerEngineering_33Request
        fields = ['status']
class ComputerEngineering_44RequestForm(forms.ModelForm):
    class Meta:
        model = ComputerEngineering_44Request
        fields = ['status']
class Cyber_security_11RequestForm(forms.ModelForm):
    class Meta:
        model = Cyber_security_11Request
        fields = ['status']