import covid19_inference as cov19
import pymc3 as pm

def analyze_country(country, date_data_begin, date_data_end, prior_rate_0 = 0.4):

	#Gets data
	df_cases = cov19.get_jhu_cdr(country, None)
	new_cases = df['confirmed'].diff()[1:]

	mobility = cov19.get_mobility_reports_apple(country,['transit'])

	if date_data_end > mobility.index.max():
		ValueError('date_data_end later than {}'.format(str(mobility.index.max())))

	lambda_0 = mobility[date_data_begin:date_data_end]*prior_rate_0

	model = cov19.model_with_continuous_changepoints(stuff)

	trace = pm.sample(model=model, init='advi', tune=500, draws=3000)

	return trace, model