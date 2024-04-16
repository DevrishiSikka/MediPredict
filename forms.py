from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class ParkinsonsForm(FlaskForm):
    fo_hz = FloatField('MDVP:Fo(Hz)', validators=[DataRequired(), NumberRange(min=0.0)])
    fhi_hz = FloatField('MDVP:Fhi(Hz)', validators=[DataRequired(), NumberRange(min=0.0)])
    flo_hz = FloatField('MDVP:Flo(Hz)', validators=[DataRequired(), NumberRange(min=0.0)])
    jitter_percent = FloatField('MDVP:Jitter(%)', validators=[DataRequired(), NumberRange(min=0.0)])
    jitter_abs = FloatField('MDVP:Jitter(Abs)', validators=[DataRequired(), NumberRange(min=0.0)])
    rap = FloatField('MDVP:RAP', validators=[DataRequired(), NumberRange(min=0.0)])
    ppq = FloatField('MDVP:PPQ', validators=[DataRequired(), NumberRange(min=0.0)])
    ddp = FloatField('Jitter:DDP', validators=[DataRequired(), NumberRange(min=0.0)])
    shimmer = FloatField('MDVP:Shimmer', validators=[DataRequired(), NumberRange(min=0.0)])
    shimmer_db = FloatField('MDVP:Shimmer(dB)', validators=[DataRequired(), NumberRange(min=0.0)])
    apq3 = FloatField('Shimmer:APQ3', validators=[DataRequired(), NumberRange(min=0.0)])
    apq5 = FloatField('Shimmer:APQ5', validators=[DataRequired(), NumberRange(min=0.0)])
    apq = FloatField('MDVP:APQ', validators=[DataRequired(), NumberRange(min=0.0)])
    dda = FloatField('Shimmer:DDA', validators=[DataRequired(), NumberRange(min=0.0)])
    nhr = FloatField('NHR', validators=[DataRequired(), NumberRange(min=0.0)])
    hnr = FloatField('HNR', validators=[DataRequired(), NumberRange(min=0.0)])
    rpde = FloatField('RPDE', validators=[DataRequired(), NumberRange(min=0.0)])
    dfa = FloatField('DFA', validators=[DataRequired(), NumberRange(min=0.0)])
    spread1 = FloatField('spread1', validators=[DataRequired(), NumberRange(min=0.0)])
    spread2 = FloatField('spread2', validators=[DataRequired(), NumberRange(min=0.0)])
    d2 = FloatField('D2', validators=[DataRequired(), NumberRange(min=0.0)])
    ppe = FloatField('PPE', validators=[DataRequired(), NumberRange(min=0.0)])
    submit = SubmitField('Submit')