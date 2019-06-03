import json

def extract_json_score(s=None):
	''' s - str in format JSON;  return max_score (int), user_score (float)'''
	if not s:
		return None
	score = json.loads(s)
	max_score = int( list(score.keys())[0] )
	user_score = float( list(score.keys())[0] )
	return max_score, user_score

def place_json_score(max_score=None, user_score=None):
	'''get max_score and user_score ; return json.dumps {"max": user}'''
	if max_score is None or user_score is None:
		return None
	return json.dumps( {max_score: user_score} )

def extract_score(s=None):
	'''s - str; return user_score (float) and max_score (int)'''
	if not s:
		return None
	scores = s.split('/')
	return float(scores[0]), int(scores[1]) # user's, max

def place_score(user_score=None, max_score=None):
	'''get user_score and max_score; return str in format "user/max" '''
	if user_score is None or max_score is None:
		return None
	return '{}/{}'.format(user_score, max_score)

def list_from_dict_values(listdict, *args):
	newd = {}
	for key in args:
		l = [ item.get(key, None) for item in listdict ]
		if l:
			newd[key] = l

	return newd

# def calculate_score_s
#
# def calculate_score_m
#
# def calculate_score_o
#
# def calculate_score_a

def group_values_by_keys(ld=None, *args):
	'''
	:ld: list of dict in format [{key1: val, key2: val}, {key1: val, key2}, ... ]
	or single dict
	:args: - any keys that will try found in ld
	return dict if format {key1: [...], key2: [...], ...}
	as return values in the dict can be a single value or list of values
	()

	'''
	if not ld:
		return None
	newd = {}
	if type(ld) is list:
		for key in args:
			if key in ld[0]:
				l = [ item.get(key, None) for item in ld ]
				if l: newd[key] = l
	elif type(ld) is dict:
		for key in args:
			if key in ld:
				newd[key] = ld[key]
	else:
		return None
	return newd