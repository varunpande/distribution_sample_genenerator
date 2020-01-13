from django.http import HttpResponse
from django.template import loader
from ..src import SimulateDist

def samplesGen(request,distribution_type):
    number_of_sample = request.POST.get('no_of_samples')
    if distribution_type == 'bernoulli':
        params = list([request.POST.get('p_param')])
    elif distribution_type == 'binomial':
        params = list([request.POST.get('n_param'),request.POST.get('p_param')])
    elif distribution_type == 'geometric':
        params = list([request.POST.get('p_param')])
    elif distribution_type == 'neg-binomial':
        params = list([request.POST.get('k_param'),request.POST.get('p_param')])
    elif distribution_type == 'poisson':
        params = list([request.POST.get('lambda_param')])
    elif distribution_type == 'arb-discrete':
        params = list([request.POST.get('arb_p_param')])
    elif distribution_type == 'uniform':
        params = list([request.POST.get('a_param'),request.POST.get('b_param')])
    elif distribution_type == 'exponential':
        params = list([request.POST.get('lambda_param')])
    elif distribution_type == 'gamma':
        params = list([request.POST.get('a_param'),request.POST.get('lambda_param')])
    elif distribution_type == 'normal':
        params = list([request.POST.get('mu_param'),request.POST.get('s_param')])
    template = loader.get_template('samples_display.html')
    res = SimulateDist.distProgram(number_of_sample,distribution_type,params)
    context = {
        'samples' : res
        }
    return HttpResponse(template.render(context))
