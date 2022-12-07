from flask import render_template, redirect, url_for
from webapp.antimonyTools import *
from webapp.forms import addReaction, submit, reset, upload, SBML
from webapp import app
import os

currentK = 0

@app.route('/')
def home():
    resetFiles()
    return redirect(url_for('build'))

@app.route('/build', methods=['GET', 'POST'])
def build():
    global currentK
    form = addReaction()
    form2 = submit()
    form3 = reset()
    form4 = upload()
    form5 = SBML()
    if form.validate() and form.submit.data:
        reactants = form.reactNames.data
        reactantIC = form.startingReactConcs.data
        fixed_reactants = form.fixedReactConc.data
        products = form.productNames.data
        productIC = form.startingProductConcs.data
        fixed_products = form.fixedProductConc.data
        rxn_constants = str(form.reactionConstant.data)
        reversibility = form.reversible.data
        dict = init(reactants, fixed_reactants,reactantIC,products,fixed_products,productIC,rxn_constants,reversibility)
        currentK, kList = reactionAntimony(dict,currentK)
        f,g,h = conditionsAntimony(dict, kList)
        return redirect(url_for('build'))
    if form2.validate() and form2.submit2.data:
        runSim()
        return redirect(url_for('results'))
    if form3.validate() and form3.submit3.data:
        currentK = 0
        resetFiles()
        if (os.path.exists("webapp/static/output.jpg")):
            os.remove("webapp/static/output.jpg")
        runSim()
    if form4.validate() and form4.submit4.data:
        form4.model.data.save('webapp/static/antimony1.txt')
        loadModel()
        return redirect(url_for('results'))
    if form5.validate() and form5.submit5.data:
        loadSBML(form5.model.data)
        return redirect(url_for('results'))
        
        
    return render_template('buildSystem.html', title='Build Reactions', form=form, form2 = form2, form3 = form3, form4 = form4, form5 = form5)

@app.route('/results')
def results():

    return render_template('results.html', title="Results")