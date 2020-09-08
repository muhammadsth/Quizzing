from django import forms


class CourseForm(forms.Form):
    type_choices = [
        ("1", "middle school"),
        ("2", "high school"),
        ("3", "college"),
        ("4", "bootcamp"),
        ("5", "other"),
    ]
    institution_type = forms.ChoiceField(required=True, label='Type of the Institution', choices =type_choices)
    institution_name = forms.CharField(label='Name of the Institution')
    subject = forms.CharField(label='Course Subject')
    code = forms.CharField(label='Course Code')
    name = forms.CharField(label='Course Name')
