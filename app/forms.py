from flask_wtf import FlaskForm
from wtforms import BooleanField, RadioField, IntegerField, SubmitField
from wtforms.validators import InputRequired
from wtforms_html5 import AutoAttrMeta
from wtforms.widgets import NumberInput


class FieldsRequiredForm(FlaskForm):
    """Require all fields to have content. This works around the bug that WTForms radio
    fields don't honor the `DataRequired` or `InputRequired` validators.
    """
    class Meta(AutoAttrMeta):
        pass


class DiagnoseForm(FieldsRequiredForm):
    age = IntegerField('Age',
                       widget=NumberInput(min=1, max=140),
                       validators=[InputRequired()])
    gender = RadioField('Label',
                        choices=[(True, 'Male'),
                                 (False, 'Female')],
                        validators=[InputRequired()])
    polyuria = BooleanField('Polyuria')
    polydipsia = BooleanField('Polydipsia')
    sudden_wl = BooleanField('Sudden Weight Loss')
    weakness = BooleanField('Weakness')
    polyphagia = BooleanField('Polyphagia')
    genital_thrush = BooleanField('Genital Thrush')
    visual_blur = BooleanField('Visual Blurring')
    itch = BooleanField('Itching')
    irritability = BooleanField('Irritability')
    delayed_healing = BooleanField('Delayed Healing')
    paresis = BooleanField('Partial Paresis')
    muscle_stiffness = BooleanField('Muscle Stiffness')
    alopecia = BooleanField('Alopecia')
    obesity = BooleanField('Obesity')
    submit = SubmitField('Get result')
