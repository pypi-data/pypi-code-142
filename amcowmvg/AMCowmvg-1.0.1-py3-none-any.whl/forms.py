from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import *
from wtforms.validators import *

class addReaction(FlaskForm):
    reactNames = StringField('Reactant Names:', validators=[DataRequired()])
    startingReactConcs = StringField('Starting Reactant Concentrations:', validators=[DataRequired()])
    fixedReactConc = StringField('Fixed Reactant Names:', validators=[DataRequired()])
    productNames = StringField('Product Names:', validators=[DataRequired()])
    startingProductConcs = StringField('Starting Product Concentrations:', validators=[DataRequired()])
    fixedProductConc = StringField('Fixed Product Names:', validators=[DataRequired()])
    #reactionConstant = FloatField('Reaction Constant:', validators=[DataRequired()])
    reactionConstant = StringField('Reaction Constant:', validators=[DataRequired()])
    reversible = BooleanField('Reversible')

    submit = SubmitField('Add Reaction')

class submit(FlaskForm):
    submit2 = SubmitField('Run Simulation')

class reset(FlaskForm):
    submit3 = SubmitField('Reset Model')

class upload(FlaskForm):
    model = FileField('Upload an Antimony Text File', validators=[FileAllowed(['txt']), DataRequired()])
    submit4 = SubmitField('Finish Model Upload')

class SBML(FlaskForm):
    model = StringField('SBML File Link')
    submit5 = SubmitField('Submit SBML File')