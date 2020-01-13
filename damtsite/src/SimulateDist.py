#!/usr/bin/python
#################################################################################
# Varunkumar Pande 1001722538                                                   #
# Monte Carlo Simulation Assignment                                             #
# Generating samples for various distributions.                                 #
#################################################################################
import sys
import random
import math

def distProgram(param1,param2,param3):
    #storing the input from cmdline
    number_of_samples = int(param1)
    type_of_distribution = param2
    parameters = []
    i = 0
    #################################################################################
    # For changing the seed value change code here:                                 #
    #################################################################################
    #seed value for random number generator
    seed_for_random_gen = 0.7948
    #seeding the random number generator
    random.seed(seed_for_random_gen)

    while i < len(param3):
        parameters.append(float(param3[i]))
        i = i + 1

    # bernoulli <p>
    if type_of_distribution == "bernoulli":
        p = parameters[0] #parameter of bernoulli
        values = []
        looper = 0
        while looper < number_of_samples:
            if random.uniform(0,1) < p :
                values.append(1)
            else:
                values.append(0)
            looper = looper + 1
        sum_of_samples = sum(values)
        sample_mean = sum_of_samples/number_of_samples
        square_of_sum_of_xi = 0
        for i in values:
            square_of_sum_of_xi += i * i
        sample_variance = ( square_of_sum_of_xi - (number_of_samples * sample_mean * sample_mean) ) / ( number_of_samples - 1 )
        population_mean = p
        population_variance = p * ( 1 - p)

    # binomial <n> <p>
    elif type_of_distribution == "binomial":
        n = int(parameters[0]) #parameter of binomial
        p = parameters[1] #parameter of binomial
        values = []
        looper = 0
        while looper < number_of_samples:
            pass_case_count = 0
            for i in range(n):
                if random.uniform(0,1) < p:
                    pass_case_count += 1 
            values.append(pass_case_count)
            looper += 1
        sum_of_samples = sum(values)
        sample_mean = sum_of_samples/number_of_samples
        square_of_sum_of_xi = 0
        for i in values:
            square_of_sum_of_xi += i * i
        sample_variance = ( square_of_sum_of_xi - (number_of_samples * sample_mean * sample_mean) ) / ( number_of_samples - 1 )
        population_mean = n * p
        population_variance = n * p * ( 1 - p)    

    # geometric <p>
    elif type_of_distribution == "geometric":
        p = parameters[0] #parameter of geometric
        values = []
        for i in range(number_of_samples):   #default value of X = 1 for atleast 1 success
            values.append(1)
        looper = 0
        while looper < number_of_samples:
            while random.uniform(0,1) > p:
                values[looper] += 1
            looper += 1
        sum_of_samples = sum(values)
        sample_mean = sum_of_samples/number_of_samples
        square_of_sum_of_xi = 0
        for i in values:
            square_of_sum_of_xi += i * i
        sample_variance = ( square_of_sum_of_xi - (number_of_samples * sample_mean * sample_mean) ) / ( number_of_samples - 1 )
        population_mean = 1/p
        population_variance = (1 - p)/(p**2)  

    # neg-binomial <k> <p>
    elif type_of_distribution == "neg-binomial":
        k = int(parameters[0]) #parameter of neg-binomial
        p = parameters[1] #parameter of neg-binomial
        values = []
        looper = 0
        while looper < number_of_samples:
            geometric_sample_counter = 0
            geometric_sample = []
            for i in range(k):   #default value of X = 1 for atleast 1 success
                geometric_sample.append(1)
            while geometric_sample_counter < k:
                while random.uniform(0,1) > p:
                    geometric_sample[geometric_sample_counter] += 1
                geometric_sample_counter += 1
            values.append(sum(geometric_sample))
            looper += 1
        sum_of_samples = sum(values)
        sample_mean = sum_of_samples/number_of_samples
        square_of_sum_of_xi = 0
        for i in values:
            square_of_sum_of_xi += i * i
        sample_variance = ( square_of_sum_of_xi - (number_of_samples * sample_mean * sample_mean) ) / ( number_of_samples - 1 )
        population_mean = k/p
        population_variance = (k * (1 - p))/(p*p)

    # poisson <λ>
    elif type_of_distribution == "poisson":
        lambda_poisson = parameters[0] #parameter of poisson
        values = []
        looper = 0
        while looper < number_of_samples:
            i = 0
            uniform_random_number = random.uniform(0,1)
            cdf = math.exp(-lambda_poisson) #initial value of cdf F(0).
            while uniform_random_number >= cdf:
                cdf += math.exp(-lambda_poisson) * (lambda_poisson**i) / math.factorial(i)
                i += 1
            values.append(i)
            looper += 1
        sum_of_samples = sum(values)
        sample_mean = sum_of_samples/number_of_samples
        square_of_sum_of_xi = 0
        for i in values:
            square_of_sum_of_xi += i * i
        sample_variance = ( square_of_sum_of_xi - (number_of_samples * sample_mean * sample_mean) ) / ( number_of_samples - 1 )
        population_mean = lambda_poisson
        population_variance = lambda_poisson

    # arb-discrete <p0> <p1> <p2> … <pn>
    elif type_of_distribution == "arb-discrete":
        arb_dist_parameters = parameters[:]#parameter of arb-discrete distribution.
        subinterval_ai = [list(range(len(arb_dist_parameters))),list(range(len(arb_dist_parameters)))]
        for i in range(len(arb_dist_parameters)):
            adder = 0.0
            for j in range(i):
                adder += arb_dist_parameters[j]
            subinterval_ai[0][i] = adder
            subinterval_ai[1][i] = adder + arb_dist_parameters[i]
        values = []
        looper = 0
        while looper < number_of_samples:
            uniform_random_number = random.uniform(0,1)
            for i in range(len(arb_dist_parameters)):
                if (uniform_random_number >= subinterval_ai[0][i]  and uniform_random_number < subinterval_ai[1][i]):
                    break
            values.append(i)
            looper += 1
        sum_of_samples = sum(values)
        sample_mean = sum_of_samples/number_of_samples
        square_of_sum_of_xi = 0
        for i in values:
            square_of_sum_of_xi += i * i
        sample_variance = ( square_of_sum_of_xi - (number_of_samples * sample_mean * sample_mean) ) / ( number_of_samples - 1 )
        population_mean = 0
        for k in range(len(parameters)):
            population_mean += k * parameters[k]  
        square_of_sum_of_xi2_Px = 0
        for i in range(len(parameters)):
            square_of_sum_of_xi2_Px += i * i * parameters[i]
        population_variance = square_of_sum_of_xi2_Px - population_mean * population_mean

    # uniform <a> <b>
    elif type_of_distribution == "uniform":
        a = parameters[0] #parameter of uniform
        b = parameters[1] #parameter of uniform
        values = []
        looper = 0
        while looper < number_of_samples:
            u1 = random.uniform(0,1) #creating a standard uniform random number.
            values.append(a + (b-a) * u1 ) #unstandardizing uniform random variable
            looper += 1
        sum_of_samples = sum(values)
        sample_mean = sum_of_samples/number_of_samples
        square_of_sum_of_xi = 0
        for i in values:
            square_of_sum_of_xi += i * i
        sample_variance = ( square_of_sum_of_xi - (number_of_samples * sample_mean * sample_mean) ) / ( number_of_samples - 1 )
        population_mean = (a + b)/2
        population_variance = ((b-a)**2)/12

    # exponential <λ>
    elif type_of_distribution == "exponential":
        lambda_exp = parameters[0] #parameter of exponential
        values = []
        looper = 0
        while looper < number_of_samples:
            exponential_sample = -((1/lambda_exp)*math.log(random.uniform(0,1)))
            values.append(exponential_sample)
            looper += 1
        sum_of_samples = sum(values)
        sample_mean = sum_of_samples/number_of_samples
        square_of_sum_of_xi = 0
        for i in values:
            square_of_sum_of_xi += i * i
        sample_variance = ( square_of_sum_of_xi - (number_of_samples * sample_mean * sample_mean) ) / ( number_of_samples - 1 )
        population_mean = 1/lambda_exp
        population_variance = 1/(lambda_exp**2)

    # gamma <α> <λ>
    elif type_of_distribution == "gamma":
        alpha_gamma = int(parameters[0]) #parameter of gamma
        lambda_gamma = parameters[1] #parameter of gamma
        values = []
        looper = 0
        while looper < number_of_samples:
            exponential_sample_counter = 0
            gamma_sample = 0
            while exponential_sample_counter < alpha_gamma:
                gamma_sample += -((1/lambda_gamma)*math.log(random.uniform(0,1)))
                exponential_sample_counter += 1
            values.append(gamma_sample)
            looper += 1
        sum_of_samples = sum(values)
        sample_mean = sum_of_samples/number_of_samples
        square_of_sum_of_xi = 0
        for i in values:
            square_of_sum_of_xi += i * i
        sample_variance = ( square_of_sum_of_xi - (number_of_samples * sample_mean * sample_mean) ) / ( number_of_samples - 1 )
        population_mean = alpha_gamma/lambda_gamma
        population_variance = alpha_gamma/(lambda_gamma**2)

    # normal <μ> <σ>
    elif type_of_distribution == "normal":
        mu = parameters[0] #parameter of normal
        sigma = parameters[1] #parameter of normal
        values = []
        looper = 0
        while looper < number_of_samples:
            u1 = random.uniform(0,1)
            u2 = random.uniform(0,1)
            zstd1 = (math.sqrt(-2 * math.log(u1))) * math.cos( 2 * math.pi * u2)
            values.append(mu + zstd1 * sigma) #unstandardizing normal random variable
            looper += 1
        sum_of_samples = sum(values)
        sample_mean = sum_of_samples/number_of_samples
        square_of_sum_of_xi = 0
        for i in values:
            square_of_sum_of_xi += i * i
        sample_variance = ( square_of_sum_of_xi - (number_of_samples * sample_mean * sample_mean) ) / ( number_of_samples - 1 )
        population_mean = mu
        population_variance = sigma * sigma

    # printing the output:
    output = {"Values":values,"Sample_Mean":"{:0.12f}".format(sample_mean).rstrip("0"),"Sample_Variance":"{:0.12f}".format(sample_variance).rstrip("0"),"Population_Mean":"{:0.12f}".format(population_mean).rstrip("0"),"Population_Variance":"{:0.12f}".format(population_variance).rstrip("0")}
    return output
